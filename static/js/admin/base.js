(function() {
  $(document).ready(function() {
    var bingo, pathname;
    pathname = window.location.pathname;
    bingo = false;
    return $('.sidebar').find('a').each(function() {
      var treeview, treeview_menu;
      if (pathname === $(this).attr('href')) {
        treeview = $(this).parents('li');
        if (treeview) {
          treeview.addClass('active');
        }
        treeview_menu = $(this).parents('ul.treeview-menu');
        if (treeview_menu) {
          return treeview_menu.addClass('active');
        }
      }
    });
  });

}).call(this);
