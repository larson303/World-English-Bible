/**
 * World English Bible - Navigation JavaScript
 */

(function() {
  'use strict';

  // Sidebar toggle functionality
  function initSidebar() {
    const menuToggle = document.querySelector('.menu-toggle');
    const sidebar = document.querySelector('.sidebar');
    const overlay = document.querySelector('.sidebar-overlay');
    const closeBtn = document.querySelector('.sidebar-close');

    if (!menuToggle || !sidebar) return;

    function openSidebar() {
      sidebar.classList.add('open');
      if (overlay) overlay.classList.add('show');
      document.body.style.overflow = 'hidden';
    }

    function closeSidebar() {
      sidebar.classList.remove('open');
      if (overlay) overlay.classList.remove('show');
      document.body.style.overflow = '';
    }

    menuToggle.addEventListener('click', openSidebar);

    if (closeBtn) {
      closeBtn.addEventListener('click', closeSidebar);
    }

    if (overlay) {
      overlay.addEventListener('click', closeSidebar);
    }

    // Close sidebar on escape key
    document.addEventListener('keydown', function(e) {
      if (e.key === 'Escape' && sidebar.classList.contains('open')) {
        closeSidebar();
      }
    });

    // Mark current book as active in sidebar
    const currentPath = window.location.pathname;
    const sidebarLinks = sidebar.querySelectorAll('a');
    sidebarLinks.forEach(function(link) {
      if (currentPath.includes(link.getAttribute('href'))) {
        link.classList.add('active');
        // Open the parent details element
        const details = link.closest('details');
        if (details) {
          details.setAttribute('open', '');
        }
      }
    });
  }

  // Chapter dropdown functionality
  function initChapterDropdown() {
    const chapterSelect = document.querySelector('.chapter-nav select');
    if (!chapterSelect) return;

    chapterSelect.addEventListener('change', function() {
      const selectedValue = this.value;
      if (selectedValue) {
        window.location.href = selectedValue;
      }
    });
  }

  // Keyboard navigation
  function initKeyboardNav() {
    document.addEventListener('keydown', function(e) {
      // Don't trigger if user is typing in an input
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

      const prevLink = document.querySelector('.prev-next a[title="Previous"]');
      const nextLink = document.querySelector('.prev-next a[title="Next"]');

      if (e.key === 'ArrowLeft' && prevLink && !prevLink.classList.contains('disabled')) {
        window.location.href = prevLink.href;
      } else if (e.key === 'ArrowRight' && nextLink && !nextLink.classList.contains('disabled')) {
        window.location.href = nextLink.href;
      }
    });
  }

  // Initialize on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  function init() {
    initSidebar();
    initChapterDropdown();
    initKeyboardNav();
  }
})();
