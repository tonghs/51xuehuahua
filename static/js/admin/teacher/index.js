(function() {
  $(document).ready(function() {
    return $(".select2").select2();
  });

  $.upload({
    browse_button: 'btn-upload',
    BeforeUpload: function(up, file) {},
    UploadProgress: function(up, file) {
      console.log(file);
      return console.log(up);
    },
    FileUploaded: function(up, file, info, url) {
      console.log(info);
      return console.log(url);
    }
  });

}).call(this);
