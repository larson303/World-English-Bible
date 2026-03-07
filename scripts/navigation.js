/**
 * World English Bible - Navigation JavaScript
 */

(function() {
  'use strict';

  // Apply saved theme immediately to prevent flash of unstyled content
  var savedTheme = localStorage.getItem('web-bible-theme') || 'default';
  if (savedTheme !== 'default') {
    document.documentElement.setAttribute('data-theme', savedTheme);
  }

  // Sidebar toggle functionality
  function initSidebar() {
    var menuToggle = document.querySelector('.menu-toggle');
    var sidebar = document.querySelector('.sidebar');
    var overlay = document.querySelector('.sidebar-overlay');
    var closeBtn = document.querySelector('.sidebar-close');

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
    var currentPath = window.location.pathname;
    var sidebarLinks = sidebar.querySelectorAll('a');
    sidebarLinks.forEach(function(link) {
      if (currentPath.includes(link.getAttribute('href'))) {
        link.classList.add('active');
        // Open the parent details element
        var details = link.closest('details');
        if (details) {
          details.setAttribute('open', '');
        }
      }
    });
  }

  // Chapter dropdown functionality
  function initChapterDropdown() {
    var chapterSelect = document.querySelector('.chapter-nav select');
    if (!chapterSelect) return;

    chapterSelect.addEventListener('change', function() {
      var selectedValue = this.value;
      if (selectedValue) {
        window.location.href = selectedValue;
      }
    });
  }

  // Keyboard navigation
  function initKeyboardNav() {
    document.addEventListener('keydown', function(e) {
      // Don't trigger if user is typing in an input
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') return;

      var prevLink = document.querySelector('.prev-next a[title="Previous"]');
      var nextLink = document.querySelector('.prev-next a[title="Next"]');

      if (e.key === 'ArrowLeft' && prevLink && !prevLink.classList.contains('disabled')) {
        window.location.href = prevLink.href;
      } else if (e.key === 'ArrowRight' && nextLink && !nextLink.classList.contains('disabled')) {
        window.location.href = nextLink.href;
      }
    });
  }

  // Theme switcher
  function initThemeSwitcher() {
    var topNav = document.querySelector('.top-nav');
    if (!topNav) return;

    // Create nav-controls container
    var navControls = document.createElement('div');
    navControls.className = 'nav-controls';

    // Create theme switcher
    var themeSwitcher = document.createElement('div');
    themeSwitcher.className = 'theme-switcher';

    var themeSelect = document.createElement('select');
    themeSelect.setAttribute('aria-label', 'Select theme');

    var themes = [
      { value: 'default', label: 'Light' },
      { value: 'dark', label: 'Night' },
      { value: 'sepia', label: 'Sepia' },
      { value: 'olive', label: 'Olive' }
    ];

    themes.forEach(function(theme) {
      var option = document.createElement('option');
      option.value = theme.value;
      option.textContent = theme.label;
      if (theme.value === savedTheme) {
        option.selected = true;
      }
      themeSelect.appendChild(option);
    });

    themeSelect.addEventListener('change', function() {
      var theme = this.value;
      if (theme === 'default') {
        document.documentElement.removeAttribute('data-theme');
      } else {
        document.documentElement.setAttribute('data-theme', theme);
      }
      localStorage.setItem('web-bible-theme', theme);
    });

    themeSwitcher.appendChild(themeSelect);
    navControls.appendChild(themeSwitcher);
    topNav.appendChild(navControls);
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
    initThemeSwitcher();
  }
})();
