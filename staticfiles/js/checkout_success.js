
/* ------------------------- Prevent form resubmission / back button redirect ------------------------- */
// Prevents form resubmission if the user refreshes the page


if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}
window.onpopstate = function() {
  window.location.href = '/products/';
};
