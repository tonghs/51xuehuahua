$(document).ready ->
    $(".select2").select2()

	$.upload({
		browse_button: 'btn-upload'

		BeforeUpload: (up, file)->
			
		UploadProgress: (up, file)->
			console.log file
			console.log up

		FileUploaded: (up, file, info, url)->
			console.log info
			console.log url
	})
