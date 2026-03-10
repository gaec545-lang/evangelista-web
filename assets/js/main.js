/**
 * Main UI — Evangelista & Co.
 * Mobile menu toggle
 */
(function () {
    'use strict';

    function initMobileMenu() {
        var btn = document.querySelector('.mobile-menu-btn');
        var nav = document.querySelector('.mobile-nav');
        if (!btn || !nav) return;

        btn.addEventListener('click', function () {
            var isOpen = nav.classList.toggle('open');
            btn.setAttribute('aria-expanded', String(isOpen));
            document.body.style.overflow = isOpen ? 'hidden' : '';

            var iconMenu  = btn.querySelector('.icon-menu');
            var iconClose = btn.querySelector('.icon-close');
            if (iconMenu)  iconMenu.style.display  = isOpen ? 'none' : '';
            if (iconClose) iconClose.style.display = isOpen ? '' : 'none';
        });

        nav.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                nav.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';

                var iconMenu  = btn.querySelector('.icon-menu');
                var iconClose = btn.querySelector('.icon-close');
                if (iconMenu)  iconMenu.style.display  = '';
                if (iconClose) iconClose.style.display = 'none';
            });
        });

        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && nav.classList.contains('open')) {
                nav.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
                btn.focus();
            }
        });
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initMobileMenu);
    } else {
        initMobileMenu();
    }
})();
