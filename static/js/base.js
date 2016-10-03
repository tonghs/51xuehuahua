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
          var k, msg, p, v;
          $('.err').each(function() {
            return $(this).removeClass('err');
          });
          if (r.result) {
            return option.success(r);
          } else {
            for (k in r) {
              v = r[k];
              p = $("#" + k).parents("div.form-group");
              p.addClass('err');
              msg = v;
              if (Array.isArray(v)) {
                msg = v[0];
              }
              p.children('.error-msg').html(msg);
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

}).call(this);
