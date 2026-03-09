/**
 * Main UI — Evangelista & Co.
 * Mobile menu + scroll header shadow
 */
(function () {
    'use strict';

    function initHeader() {
        const header = document.querySelector('.site-header');
        if (!header) return;

        window.addEventListener('scroll', function () {
            if (window.scrollY > 40) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        }, { passive: true });
    }

    function initMobileMenu() {
        const btn = document.querySelector('.mobile-menu-btn');
        const nav = document.querySelector('.mobile-nav');
        if (!btn || !nav) return;

        btn.addEventListener('click', function () {
            const isOpen = nav.classList.toggle('open');
            btn.setAttribute('aria-expanded', isOpen);
            document.body.style.overflow = isOpen ? 'hidden' : '';
            // Swap icon
            btn.querySelector('.icon-menu') && (btn.querySelector('.icon-menu').style.display = isOpen ? 'none' : '');
            btn.querySelector('.icon-close') && (btn.querySelector('.icon-close').style.display = isOpen ? '' : 'none');
        });

        // Close on nav link click
        nav.querySelectorAll('a').forEach(function (link) {
            link.addEventListener('click', function () {
                nav.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
            });
        });

        // Close on Escape
        document.addEventListener('keydown', function (e) {
            if (e.key === 'Escape' && nav.classList.contains('open')) {
                nav.classList.remove('open');
                btn.setAttribute('aria-expanded', 'false');
                document.body.style.overflow = '';
                btn.focus();
            }
        });
    }

    function init() {
        initHeader();
        initMobileMenu();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
