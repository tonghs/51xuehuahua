(function() {
  var getCaptcha, getSmsCode;

  getCaptcha = function() {
    return $.ajax({
      url: '/j/captcha',
      method: 'POST',
      success: function(r) {
        $('#captcha').attr('src', "data:image/gif;base64," + r.img);
        return $('#key').val(r.key);
      }
    });
  };

  getSmsCode = function() {
    return $._ajax({
      url: '/j/sms_code',
      method: 'POST',
      data: {
        token: $('#token').val(),
        key: $('#key').val(),
        user_name: $('#user_name').val()
      },
      success: function(r) {
        $('#btn-sms-code').attr('disable', 'true');
        $('#btn-sms-code').addClass('disabled');
        return $('#btn-sms-code').val('已发送(60)');
      }
    });
  };

  $(document).ready(function() {
    return getCaptcha();
  });

  $('#captcha').click(function() {
    return getCaptcha();
  });

  $('#btn-sms-code').click(function() {
    return getSmsCode();
  });

}).call(this);
