sec = 59
intval = null

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
            $('#btn-sms-code').attr('disabled', 'true')
            $('#btn-sms-code').addClass('disabled')
            $('#btn-sms-code').val('已发送(60)')
            intval = setInterval(countDown, 1000)
    })

countDown = ->
    if sec == 0
        clearInterval(intval)
        $('#btn-sms-code').removeAttr('disabled')
        $('#btn-sms-code').removeClass('disabled')
        $('#btn-sms-code').val('获取动态验证码')
        sec = 59
    else
        $('#btn-sms-code').val("已发送(#{sec})")
        sec--


$('form').submit (e)->
    $._ajax({
        url: '/j/reg'
        method: 'POST'
        data: {
            sms_code: $('#sms_code').val(),
            user_name: $('#user_name').val()
            password: $('#password').val()
        }
        success: (r)->
            window.locatin.href='/login'
    })
    e.preventDefault()


$(document).ready ->
    getCaptcha()

$('#captcha').click ->
    getCaptcha()


$('#btn-sms-code').click ->
    getSmsCode()

