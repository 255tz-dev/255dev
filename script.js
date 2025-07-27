/*
 * Interactive behaviours for 234TZ Landing Page
 *
 * Handles mobile navigation toggling and simple client‑side form submission
 * responses. When a form is submitted, a friendly message is displayed
 * without sending data to a server. This keeps the demonstration
 * functional while allowing integration with a real backend later.
 */
document.addEventListener('DOMContentLoaded', () => {
  // Mobile navigation toggle
  const menuToggle = document.getElementById('menu-toggle');
  const navbar = document.getElementById('navbar');
  if (menuToggle && navbar) {
    menuToggle.addEventListener('click', () => {
      navbar.classList.toggle('open');
    });
  }

  // Form response element
  const responseEl = document.getElementById('form-response');

  // Callback form handling
  const callbackForm = document.getElementById('callback-form');
  if (callbackForm) {
    callbackForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nameInput = document.getElementById('callback-name');
      const name = nameInput.value.trim() || 'there';
      responseEl.textContent = `Thanks, ${name}! Our team will call you back shortly.`;
      callbackForm.reset();
      // Collapse the menu on form submit (useful for mobile when using nav links)
      if (navbar.classList.contains('open')) {
        navbar.classList.remove('open');
      }
    });
  }

  // Inquiry form handling
  const inquiryForm = document.getElementById('inquiry-form');
  if (inquiryForm) {
    inquiryForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const nameInput = document.getElementById('inquiry-name');
      const name = nameInput.value.trim() || 'there';
      responseEl.textContent = `Thanks, ${name}! We've received your inquiry and will get back to you soon.`;
      inquiryForm.reset();
      if (navbar.classList.contains('open')) {
        navbar.classList.remove('open');
      }
    });
  }
});