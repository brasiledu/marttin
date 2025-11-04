// Sidebar/topbar (dedicado)
(function(){
  const $ = (s, c=document)=>c.querySelector(s);
  const $$ = (s, c=document)=>Array.from(c.querySelectorAll(s));

  // Toggle sidebar collapse
  const toggleBtn = $('#toggleSidebar');
  const sidebar = $('#sidebar');
  const layout = $('#dashboardLayout');

  // Restore persisted state
  const persisted = localStorage.getItem('sidebar:collapsed') === 'true';
  if (sidebar && layout && persisted) {
    sidebar.classList.add('collapsed');
    layout.classList.add('collapsed');
  }

  if (toggleBtn && sidebar && layout) {
    toggleBtn.addEventListener('click', () => {
      const collapsed = sidebar.classList.toggle('collapsed');
      layout.classList.toggle('collapsed');
      localStorage.setItem('sidebar:collapsed', String(collapsed));
    });
  }

  // Profile dropdown
  const profile = $('#profileMenu');
  const dropdown = $('#profileDropdown');
  if (profile && dropdown) {
    const btn = profile.querySelector('.profile-btn');
    btn.addEventListener('click', () => {
      dropdown.style.display = dropdown.style.display === 'flex' ? 'none' : 'flex';
    });
    document.addEventListener('click', (e) => {
      if (!profile.contains(e.target)) dropdown.style.display = 'none';
    });
  }

  // Upload modal
  const uploadLink = $('#uploadDadosLink');
  const uploadModal = $('#uploadModal');
  if (uploadLink && uploadModal){
    uploadLink.addEventListener('click', (e)=>{ e.preventDefault(); uploadModal.classList.add('show'); });
    $$('[data-close-modal]').forEach(b=>b.addEventListener('click',()=>uploadModal.classList.remove('show')));
    uploadModal.addEventListener('click',(e)=>{ if(e.target===uploadModal) uploadModal.classList.remove('show'); });
  }
})();
