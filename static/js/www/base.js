(function() {
  $("#navbar>ul#mian-nav>li>a").each(function() {
    if ($(this).attr('href') === window.location.pathname) {
      return $(this).parent('li').addClass('active');
    }
  });

}).call(this);
