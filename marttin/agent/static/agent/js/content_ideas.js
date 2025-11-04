(function(){
  const $ = (sel, root=document) => root.querySelector(sel);
  const $$ = (sel, root=document) => Array.from(root.querySelectorAll(sel));

  function getUrls() {
    const root = $('#contentIdeasPage');
    return {
      api: root?.dataset.apiUrl,
      dashboard: root?.dataset.dashboardUrl,
      csrf: getCsrf()
    };
  }

  function getCsrf() {
    // Tenta obter do cookie; fallback via meta ou input oculto do template
    const match = document.cookie.match(/csrftoken=([^;]+)/);
    return match ? match[1] : '';
  }

  function setLoading(isLoading) {
    const loading = $('#resultsLoading');
    const empty = $('#resultsEmpty');
    const container = $('#resultsContainer');
    if (isLoading) {
      loading?.setAttribute('aria-hidden', 'false');
      loading?.classList.add('show');
      empty && (empty.style.display = 'none');
      container && (container.innerHTML = '');
    } else {
      loading?.setAttribute('aria-hidden', 'true');
      loading?.classList.remove('show');
    }
  }

  function renderIdeas(ideas, meta) {
    const container = $('#resultsContainer');
    if (!container) return;
    let html = '';
    ideas.forEach((idea, idx) => {
      html += `
        <div class="result-card">
          <div class="result-title"><i class="bi bi-lightbulb"></i> Ideia ${idx + 1}</div>
          <div class="result-content"><p>${idea}</p></div>
        </div>
      `;
    });
    if (meta?.content_type || meta?.platform) {
      html += `
        <div class="result-card">
          <div class="result-title"><i class="bi bi-info-circle"></i> Detalhes</div>
          <div class="result-content">
            ${meta.content_type ? `<p><strong>Tipo:</strong> ${labelContentType(meta.content_type)}</p>` : ''}
            ${meta.platform ? `<p><strong>Plataforma:</strong> ${labelPlatform(meta.platform)}</p>` : ''}
            <p><strong>Gerado em:</strong> ${new Date().toLocaleString('pt-BR')}</p>
          </div>
        </div>
      `;
    }
    container.innerHTML = html;
  }

  function labelContentType(type){
    const map = { social_media:'Posts para Redes Sociais', blog_posts:'Artigos para Blog', email_campaigns:'Campanhas de Email', ad_copy:'Textos para Anúncios', video_scripts:'Roteiros para Vídeos', product_descriptions:'Descrições de Produtos' };
    return map[type] || type;
  }
  function labelPlatform(p){
    const map = { instagram:'Instagram', facebook:'Facebook', linkedin:'LinkedIn', twitter:'Twitter/X', tiktok:'TikTok', youtube:'YouTube', website:'Website', email:'Email' };
    return map[p] || p;
  }

  async function loadInsights() {
    try {
      const { dashboard } = getUrls();
      const res = await fetch(dashboard, { method: 'GET' });
      const json = await res.json();
      const list = $('#ciInsights');
      if (!list) return;
      list.innerHTML = '';
      const insights = json?.data?.insights || [];
      if (!insights.length) {
        list.innerHTML = '<div class="insight-item muted">Sem insights no momento.</div>';
        return;
      }
      insights.forEach(it => {
        const icon = it.icon || 'lightbulb';
        list.innerHTML += `
          <div class="insight-item">
            <i class="bi bi-${icon}"></i>
            <div>
              <strong>${it.title || 'Insight'}</strong>
              <div class="text">${it.text || ''}</div>
            </div>
          </div>
        `;
      });
    } catch (e) {
      const list = $('#ciInsights');
      if (list) list.innerHTML = '<div class="insight-item muted">Falha ao carregar insights.</div>';
    }
  }

  function wireTemplates() {
    $$('.qt-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        const t = btn.dataset.type; const p = btn.dataset.platform; const tone = btn.dataset.tone;
        $('#content_type').value = t || '';
        $('#platform').value = p || '';
        $('#tone').value = tone || '';
        $('.ci-form')?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        setTimeout(() => $('#business_description')?.focus(), 300);
      });
    });
  }

  function formToData(form) {
    const fd = new FormData(form);
    return {
      business_description: fd.get('business_description'),
      content_type: fd.get('content_type'),
      platform: fd.get('platform'),
      target_audience: fd.get('target_audience'),
      tone: fd.get('tone'),
      keywords: fd.get('keywords'),
      quantity: fd.get('quantity')
    };
  }

  async function onSubmit(e){
    e.preventDefault();
    const form = e.currentTarget;
    const btn = $('#generateBtn');
    const { api, csrf } = getUrls();
    if (!api) return;

    // estados
    $('#resultsEmpty').style.display = 'none';
    setLoading(true);
    btn.disabled = true; btn.innerHTML = '<i class="bi bi-arrow-repeat"></i> Gerando...';

    try {
      const payload = formToData(form);
      const res = await fetch(api, {
        method: 'POST', headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf }, body: JSON.stringify(payload)
      });
      const json = await res.json();
      setLoading(false);
      if (json?.success) {
        renderIdeas(json.ideas || [], json);
      } else {
        $('#resultsContainer').innerHTML = '<div class="result-card"><div class="result-title"><i class="bi bi-exclamation-triangle"></i> Erro</div><div class="result-content">'+(json?.error || 'Erro ao gerar ideias')+'</div></div>';
      }
    } catch (err) {
      setLoading(false);
      $('#resultsContainer').innerHTML = '<div class="result-card"><div class="result-title"><i class="bi bi-wifi-off"></i> Conexão</div><div class="result-content">Erro de conexão. Tente novamente.</div></div>';
    } finally {
      btn.disabled = false; btn.innerHTML = '<i class="bi bi-lightbulb"></i> Gerar Ideias';
    }
  }

  document.addEventListener('DOMContentLoaded', function(){
    const form = $('#contentForm');
    if (form) form.addEventListener('submit', onSubmit);
    wireTemplates();
    loadInsights();
  });
})();