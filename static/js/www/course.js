(function() {
  $(window).scroll(function() {
    if ($(window).scrollTop() > 80) {
      $("#filter").css('position', 'fixed');
      $("#filter").css('width', '100%');
      $("#filter").css('top', '0');
      $("#filter").css('z-index', '999');
      return $('.section').css('margin-top', '135px');
    } else {
      $("#filter").css('position', 'relative');
      $("#filter").css('width', '100%');
      $("#filter").css('top', '0');
      $("#filter").css('z-index', '999');
      return $('.section').css('margin-top', '0');
    }
  });

}).call(this);
