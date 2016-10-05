$(document).ready ->
    $(".select2").select2()

    v_add = new Vue({
        el: '#addition-form'
        data: {
            avatar: ''
            name: ''
            method: ''
            category: ''
            desc: ''
        }
        ready: ->
            $.upload({
                browse_button: 'btn-upload'

                BeforeUpload: (up, file)->
                    $('.progress').fadeIn()
                    
                UploadProgress: (up, file)->
                    percent = file.percent
                    $('#progress-bar').css('width', "#{percent}%")
                    $('#progress-bar').attr('aria-valuenow', percent)


                FileUploaded: (up, file, info, url)->
                    $('.progress').fadeOut()
                    $("#avatar-preview").css('background-image', "url('#{url}')")
                    v_add.avatar = info.key
            })
    })

