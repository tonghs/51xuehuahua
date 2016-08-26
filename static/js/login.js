(function() {
  $('#btn-login').click(function() {
    var password, user_name;
    user_name = $("input[name='user_name']").val();
    password = $("input[name='password']").val();
    return $._ajax({
      url: "/j/login",
      data: {
        user_name: user_name,
        password: password
      },
      success: function(r) {
        if (r.login) {
          return window.location.href = '/';
        } else {
          return $.alert(r.msg);
        }
      }
    });
  });

}).call(this);
