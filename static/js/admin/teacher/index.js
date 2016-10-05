(function() {
  $(document).ready(function() {
    return $(".select2").select2();
  });

  $.upload({
    browse_button: 'btn-upload',
    BeforeUpload: function(up, file) {},
    UploadProgress: function(up, file) {},
    FileUploaded: function(up, file, info) {}
  });

}).call(this);
