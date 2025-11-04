// Renderização Markdown estilo GitHub para elementos com a classe .markdown-body ou [data-markdown]
(function(){
  if (typeof window === 'undefined') return;
  const md = window.markdownit({
    html: false,
    linkify: true,
    typographer: true,
    breaks: true
  });

  function renderMarkdownIn(el){
    const blocks = el.querySelectorAll('[data-markdown], .markdown-body[data-md]');
    blocks.forEach(node => {
      const raw = node.textContent || '';
      const clean = DOMPurify.sanitize(md.render(raw));
      node.classList.add('markdown-body');
      node.innerHTML = clean;
    });
  }

  document.addEventListener('DOMContentLoaded', function(){
    renderMarkdownIn(document);
  });

  // Expor utilitário global para re-render após atualizações dinâmicas
  window.renderMarkdownIn = renderMarkdownIn;
})();
