$(document).ready ->
    $(".select2").select2()

	$.upload({
		browse_button: 'btn-upload'

		BeforeUpload: (up, file)->
			
		UploadProgress: (up, file)->

		FileUploaded: (up, file, info)->
			
	})
