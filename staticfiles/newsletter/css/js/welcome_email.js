/* jshint esversion: 11, jquery: true */
/* globals document */
// Dealna.de_v1.7/newsletter/static/newsletter/css/js/welcome_email.js
/**
 * Adds a subtle hover animation effect to the newsletter CTA button.
 */
(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    const ctaButton = document.querySelector('.cta a');
    if (ctaButton) {
      ctaButton.addEventListener('mouseenter', function () {
        this.style.transform = 'scale(1.05)';
        this.style.transition = 'transform 0.2s ease-in-out';
      });

      ctaButton.addEventListener('mouseleave', function () {
        this.style.transform = 'scale(1)';
      });
    }
  });
})();
