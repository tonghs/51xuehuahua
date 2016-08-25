$('#btn-login').click ->
    user_name = $("input[name='user_name']").val()
    password = $("input[name='password']").val()
    $._ajax({
        url: "/j/login",
        data: {user_name: user_name, password: password}
        success: (r)->
            if r.login
                window.location.href = '/'
            else
                $.alert r.msg
    })
