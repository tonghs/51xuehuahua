(function() {
  $(document).ready(function() {
    var v_add;
    return v_add = new Vue({
      el: '#addition-form',
      data: {
        avatar: '',
        name: '',
        method: [],
        category: [],
        desc: ''
      },
      ready: function() {
        $(".select2").select2().on('change', function() {
          return v_add.category = $('#category').val();
        });
        return $.upload({
          browse_button: 'btn-upload',
          BeforeUpload: function(up, file) {
            return $('.progress').fadeIn();
          },
          UploadProgress: function(up, file) {
            var percent;
            percent = file.percent;
            $('#progress-bar').css('width', percent + "%");
            return $('#progress-bar').attr('aria-valuenow', percent);
          },
          FileUploaded: function(up, file, info, url) {
            $('.progress').fadeOut();
            $("#avatar-preview").css('background-image', "url('" + url + "')");
            return v_add.avatar = info.key;
          }
        });
      },
      methods: {
        submit: function() {
          return $._ajax({
            url: '/j/teacher',
            method: 'POST',
            data: JSON.stringify(this.$data),
            success: function() {
              v_add.avatar = '';
              v_add.name = '';
              v_add.method = [];
              v_add.category = [];
              v_add.desc = '';
              $('.addition-modal').modal('hide');
              return $(".select2").val([]).trigger("change");
            }
          });
        }
      }
    });
  });

}).call(this);
