(function() {
  $.extend({
    tip: function(msg) {
      $('#msg').attr('class', 'alert alert-info');
      $('#msg').css('display', 'block');
      return $('#msg').html(msg);
    },
    alert: function(msg) {
      $('#msg').attr('class', 'alert alert-danger');
      $('#msg').css('display', 'block');
      return $('#msg').html(msg);
    },
    _ajax: function(option) {
      return $.ajax({
        method: option.method,
        url: option.url,
        data: option.data,
        type: option.type || 'POST',
        success: function(r) {
          var k, p, v;
          if (r.result) {
            option.success(r);
            return $('.has-error').each(function() {
              return $(this).removeClass('has-error');
            });
          } else {
            for (k in r) {
              v = r[k];
              p = $("#" + k).parent("div");
              p.addClass('has-error');
              p.children('label').children('.error-msg').html(v[0]);
            }
            if (option.fail) {
              return option.fail();
            }
          }
        },
        fail: function() {
          if (option.fail) {
            return option.fail();
          }
        }
      });
    }
  });

  $("#navbar>ul#mian-nav>li>a").each(function() {
    if ($(this).attr('href') === window.location.pathname) {
      return $(this).parent('li').addClass('active');
    }
  });

}).call(this);
