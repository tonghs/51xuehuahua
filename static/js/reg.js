(function() {
  var get_captcha;

  $(document).ready(function() {
    return get_captcha();
  });

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

  $('#captcha').click(function() {
    return get_captcha();
  });

}).call(this);
