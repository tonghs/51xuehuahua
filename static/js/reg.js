(function() {
  var get_captcha, get_sms_code;

  get_captcha = function() {
    return $.ajax({
      url: '/j/captcha',
      method: 'POST',
      success: function(r) {
        $('#captcha').attr('src', "data:image/gif;base64," + r.img);
        return $('#key').val(r.key);
      }
    });
  };

  get_sms_code = function() {
    return $._ajax({
      url: '/j/captcha',
      method: 'POST',
      success: function(r) {
        $('#captcha').attr('src', "data:image/gif;base64," + r.img);
        return $('#key').val(r.key);
      }
    });
  };

  $(document).ready(function() {
    return get_captcha();
  });

  $('#captcha').click(function() {
    return get_captcha();
  });

}).call(this);
