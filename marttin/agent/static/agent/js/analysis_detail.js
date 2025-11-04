(function(){
  const buttons = document.querySelectorAll('.tab-btn');
  const panels = document.querySelectorAll('.tab-panel');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      // Remove active de todos os botões e painéis
      buttons.forEach(b => b.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));
      
      // Ativa o botão clicado
      btn.classList.add('active');
      
      // Ativa o painel correspondente
      const tabId = btn.dataset.tab;
      const panel = document.getElementById(tabId);
      if (panel) {
        panel.classList.add('active');
      }
    });
  });
})();
