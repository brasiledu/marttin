// Dashboard data via API
(function(){
  const $ = (sel, ctx=document) => ctx.querySelector(sel);
  const formatBRL = (n)=> new Intl.NumberFormat('pt-BR',{style:'currency',currency:'BRL'}).format(n);

  async function loadData(){
    try{
      const res = await fetch('/api/dashboard-data/');
      const json = await res.json();
      if(!json.success) throw new Error(json.error||'Erro desconhecido');
      const d = json.data;

      // KPIs
      if ($('#kpiFaturamento')) $('#kpiFaturamento').textContent = formatBRL(d.kpis.faturamento_mes || 0);
      if ($('#kpiNovosClientes')) $('#kpiNovosClientes').textContent = d.kpis.novos_clientes ?? 0;
      if ($('#kpiCAC')) $('#kpiCAC').textContent = formatBRL(d.kpis.cac || 0);

      // Charts
      if (window.Chart && $('#cashflowChart')){
        new Chart($('#cashflowChart'),{
          type:'line',
          data:{
            labels:d.cashflow.labels||[],
            datasets:[
              {label:'Entradas',data:d.cashflow.entradas||[],borderColor:'#22c55e',backgroundColor:'rgba(34,197,94,.15)',tension:.35,fill:true},
              {label:'Saídas',data:d.cashflow.saidas||[],borderColor:'#ef4444',backgroundColor:'rgba(239,68,68,.12)',tension:.35,fill:true}
            ]
          },
          options:{plugins:{legend:{labels:{color:'#e5e7eb'}}},scales:{x:{ticks:{color:'#94a3b8'},grid:{color:'rgba(255,255,255,.06)'}},y:{ticks:{color:'#94a3b8'},grid:{color:'rgba(255,255,255,.06)'}}}}
        });
      }
      if (window.Chart && $('#channelChart')){
        new Chart($('#channelChart'),{
          type:'doughnut',
          data:{labels:d.channels.labels||[],datasets:[{data:d.channels.values||[],backgroundColor:['#60a5fa','#f59e0b','#22c55e','#a78bfa','#f97316','#10b981'],borderWidth:0}]},
          options:{plugins:{legend:{labels:{color:'#e5e7eb'}}}}
        });
      }

      // Tabela
      const tbody = $('#latestSalesBody');
      if (tbody){
        tbody.innerHTML = '';
        (d.latest_sales||[]).forEach((r)=>{
          const tr = document.createElement('tr');
          tr.innerHTML = `
            <td>${r.id}</td>
            <td>${(r.data||'').split('T')[0].split('-').reverse().join('/')}</td>
            <td>${r.cliente}</td>
            <td>${r.canal}</td>
            <td>${formatBRL(r.valor||0)}</td>
            <td><span class="status ${r.status==='Pago'?'ok':'pending'}">${r.status}</span></td>`;
          tbody.appendChild(tr);
        });
      }

      // Insights
      const insights = $('#insightsContainer');
      if (insights){
        insights.innerHTML = '';
        (d.insights||[]).forEach(i=>{
          const div = document.createElement('div');
          div.className = 'insight';
          const iconMap = { 'lightbulb':'bi-lightbulb', 'graph-up':'bi-graph-up', 'cash':'bi-cash-coin' };
          div.innerHTML = `<i class="bi ${iconMap[i.icon]||'bi-lightbulb'}"></i><div><strong>${i.title}</strong><p>${i.text}</p></div>`;
          insights.appendChild(div);
        });
      }
    }catch(e){
      console.error('Dashboard load error', e);
    }
  }

  // Init
  document.addEventListener('DOMContentLoaded', loadData);
})();

// Dashboard interactions and placeholder data (somente widgets desta página)
(function(){
  const $ = (sel, ctx=document) => ctx.querySelector(sel);

  // Upload form hook
  const uploadModal = $('#uploadModal');
  const uploadForm = $('#uploadForm');
  if (uploadForm && uploadModal){
    uploadForm.addEventListener('submit', async (e)=>{
      e.preventDefault();
      const file = $('#dataFile').files[0];
      if(!file){ return notify('Selecione um arquivo CSV/XLS/XLSX.', 'error'); }
      notify('Upload enviado. Integração com backend será ligada.', 'success');
      uploadModal.classList.remove('show');
    });
  }

  // Notifications helper
  function notify(message, type='info'){
    const div = document.createElement('div');
    div.className = `dash-toast ${type}`;
    div.textContent = message;
    Object.assign(div.style, {
      position:'fixed',right:'16px',top:'16px',background:'rgba(15,23,42,.98)',
      color:'#e5e7eb',border:'1px solid rgba(255,255,255,.12)',borderRadius:'10px',padding:'10px 12px',zIndex:1000
    });
    document.body.appendChild(div);
    setTimeout(()=>div.remove(), 3500);
  }
})();
