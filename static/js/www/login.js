(function() {
  $('form').submit(function(e) {
    var password, user_name;
    user_name = $("input[name='user_name']").val();
    password = $("input[name='password']").val();
    $._ajax({
      url: "/j/login",
      data: {
        user_name: user_name,
        password: password
      },
      success: function(r) {
        if (r.result) {
          return window.location.href = '/';
        }
      }
    });
    return e.preventDefault();
  });

}).call(this);
