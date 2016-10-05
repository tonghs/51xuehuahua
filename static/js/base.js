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
      var target;
      target = option.target;
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
            option.success(r);
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
              option.fail();
            }
          }
          if (target) {
            target.attr('disabled', '');
            return target.removeClass('disabled');
          }
        },
        fail: function() {
          if (option.fail) {
            option.fail();
          }
          if (target) {
            target.attr('disabled', '');
            return target.removeClass('disabled');
          }
        }
      });
    },
    upload: function(option) {
      var browse_button, uploader;
      browse_button = option.browse_button;
      return uploader = Qiniu.uploader({
        runtimes: 'html5,flash,html4',
        browse_button: browse_button,
        uptoken_url: '/j/qiniu_token',
        domain: 'http://oc06pejhd.bkt.clouddn.com/',
        max_file_size: '100mb',
        max_retries: 3,
        dragdrop: true,
        save_key: true,
        chunk_size: '4mb',
        auto_start: true,
        filters: {
          mime_types: [
            option.mime_types || {
              title: "图片文件",
              extensions: "jpg,gif,png,bmp,jpeg"
            }
          ]
        },
        init: {
          'FilesAdded': function(up, files) {
            return plupload.each(files, function(file) {});
          },
          'BeforeUpload': function(up, file) {
            return option.BeforeUpload(up, file);
          },
          'UploadProgress': function(up, file) {
            return option.UploadProgress(up, file);
          },
          'FileUploaded': function(up, file, info) {
            var domain, res, url;
            domain = up.getOption('domain');
            res = $.parseJSON(info);
            url = domain + res.key;
            return option.FileUploaded(up, file, res, url);
          },
          'Error': function(up, err, errTip) {},
          'UploadComplete': function() {}
        }
      });
    }
  });

}).call(this);
