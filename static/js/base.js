/* jshint esversion: 11 */
/* globals document, window, jQuery */

/**
 * Handles toast notifications positioning and display.
 * Ensures they appear below the fixed navbar.
 */
(function () {
  'use strict';
  function placeToast() {
    const header = document.querySelector('header.container-fluid.fixed-top');
    const mc = document.querySelector('.message-container');
    if (!header || !mc) {
      return;
    }
    mc.style.top = header.offsetHeight + 10 + 'px';
  }

  function showToasts() {
    const toasts = document.querySelectorAll('.toast');
    if (!toasts.length) {
      return;
    }
    try {
      if (window.jQuery && typeof jQuery.fn.toast === 'function') {
        jQuery(toasts).toast({ autohide: false }).toast('show');
      } else {
        toasts.forEach(function (t) {
          t.classList.add('show');
        });
      }
    } catch (err) {
      toasts.forEach(function (t) {
        t.classList.add('show');
      });
    }
  }

  function initToasts() {
    placeToast();
    showToasts();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initToasts);
  } else {
    initToasts();
  }

  window.addEventListener('resize', placeToast);
})();

/**
 * Keep a CSS variable in sync with the current fixed header height
 * so content/pages can offset correctly.
 */
(function () {
  function setHeaderVar() {
    const header = document.querySelector('header.container-fluid.fixed-top');
    if (header) {
      document.documentElement.style.setProperty(
        '--header-height',
        header.offsetHeight + 'px'
      );
    }
  }

  window.addEventListener('load', setHeaderVar, { passive: true });
  window.addEventListener('resize', setHeaderVar, { passive: true });
})();

/**
 * Scroll-to-top button.
 * Shows after some scroll, smooth-scrolls to top on click.
 */
(function () {
  const btn = document.getElementById('scrollToTopBtn');
  if (!btn) {
    return;
  }

  let ticking = false;
  function onScroll() {
    if (ticking) {
      return;
    }
    ticking = true;
    window.requestAnimationFrame(function () {
      const show = window.scrollY > 200;
      btn.classList.toggle('show', show);
      btn.setAttribute('aria-hidden', show ? 'false' : 'true');
      ticking = false;
    });
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  btn.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  btn.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      btn.click();
    }
  });
})();