$('form').submit (e)->
    user_name = $("input[name='user_name']").val()
    password = $("input[name='password']").val()
    $._ajax({
        url: "/j/login",
        data: {user_name: user_name, password: password}
        success: (r)->
            if r.result
                window.location.href = '/'
    })
    e.preventDefault()
