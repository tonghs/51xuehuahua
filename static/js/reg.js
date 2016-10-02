(function() {
  var countDown, getCaptcha, getSmsCode, intval, sec;

  sec = 59;

  intval = null;

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
        $('#btn-sms-code').attr('disabled', 'true');
        $('#btn-sms-code').addClass('disabled');
        $('#btn-sms-code').val('已发送(60)');
        return intval = setInterval(countDown, 1000);
      }
    });
  };

  countDown = function() {
    if (sec === 0) {
      clearInterval(intval);
      $('#btn-sms-code').attr('disabled', 'false');
      $('#btn-sms-code').removeClass('disabled');
      return $('#btn-sms-code').val('获取动态验证码');
    } else {
      $('#btn-sms-code').val("已发送(" + sec + ")");
      return sec--;
    }
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
