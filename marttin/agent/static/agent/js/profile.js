// JS da página de Perfil
// - Submete o form oculto de apagar conta ao clicar no botão
// - Espaço para validações rápidas de UX

(function() {
  const deleteBtn = document.getElementById('btnDeleteAccount');
  const deleteForm = document.getElementById('deleteAccountForm');

  if (deleteBtn && deleteForm) {
    deleteBtn.addEventListener('click', function() {
      if (confirm('Tem certeza que deseja apagar sua conta e todos os dados? Esta ação não pode ser desfeita.')) {
        deleteForm.submit();
      }
    });
  }

  const profileForm = document.getElementById('profileForm');
  if (profileForm) {
    profileForm.addEventListener('submit', function() {
      // Evitar múltiplos envios
      const submitBtn = profileForm.querySelector('button[type="submit"]');
      if (submitBtn) {
        submitBtn.setAttribute('disabled', 'disabled');
        submitBtn.innerHTML = '<i class="bi bi-hourglass-split"></i> Salvando...';
      }
    });
  }
})();
