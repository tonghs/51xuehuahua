get_captcha =->
    $.ajax({
        url: '/j/captcha'
        method: 'POST'
        success: (r)->
            $('#captcha').attr('src', "data:image/gif;base64,#{r.img}")
            $('#key').val(r.key)
    })

get_sms_code =->
    $._ajax({
        url: '/j/captcha'
        method: 'POST'
        success: (r)->
            $('#captcha').attr('src', "data:image/gif;base64,#{r.img}")
            $('#key').val(r.key)
    })


$(document).ready ->
    get_captcha()

$('#captcha').click ->
    get_captcha()

