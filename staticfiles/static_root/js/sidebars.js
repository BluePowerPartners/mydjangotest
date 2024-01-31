/* global bootstrap: false */
(function () {
  'use strict'
  var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
  tooltipTriggerList.forEach(function (tooltipTriggerEl) {
    new bootstrap.Tooltip(tooltipTriggerEl)
  })
})
// $(document).ready(function () {
//     $("ul.nav > li > a").click(function (e) {
//      $("ul.nav > li > a").removeClass("active");
//      $(this).addClass("active");
//       });
//  });
$(document).ready(function () {
    var url = window.location;
    $("ul.nav > li > a").removeClass("active");
    $('ul.nav > li > a').filter(function() {
          return this.href == url;
    }).addClass('active');
});
