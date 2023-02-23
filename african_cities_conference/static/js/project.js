/* Project specific Javascript goes here. */

(function ($) {
  "use strict";

  // TODO: Create a sticky navbar using jquery
  $(window).scroll(function () {
    var startPx = $(window).scrollTop();
    startPx >= 100
      ? $("#main-nav").addClass("sticky-nav")
      : $("#main-nav").removeClass("sticky-nav");
  });
})(jQuery);
