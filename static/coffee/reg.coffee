$(document).ready ->
    get_captcha()

get_captcha =->
    $.ajax({
        url: '/j/captcha'
        method: 'POST'
        success: (r)->
            $('#captcha').attr('src', "data:image/gif;base64,#{r.img}")
            $('#key').val(r.key)
    })

$('#captcha').click ->
    get_captcha()
