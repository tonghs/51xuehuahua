getCaptcha =->
    $.ajax({
        url: '/j/captcha'
        method: 'POST'
        success: (r)->
            $('#captcha').attr('src', "data:image/gif;base64,#{r.img}")
            $('#key').val(r.key)
    })

getSmsCode =->
    $._ajax({
        url: '/j/sms_code'
        method: 'POST'
        data: {
            token: $('#token').val(),
            key: $('#key').val(),
            user_name: $('#user_name').val()
        }
        success: (r)->
            $('#btn-sms-code').attr('disable', 'true')
            $('#btn-sms-code').addClass('disabled')
            $('#btn-sms-code').val('已发送(60)')
    })


$(document).ready ->
    getCaptcha()

$('#captcha').click ->
    getCaptcha()


$('#btn-sms-code').click ->
    getSmsCode()

