$.extend({
    # app: angular.module('app', ['ngRoute'])

    tip: (msg)->
        $('#msg').attr('class', 'alert alert-info')
        $('#msg').css('display', 'block')
        $('#msg').html(msg)

    alert: (msg)->
        $('#msg').attr('class', 'alert alert-danger')
        $('#msg').css('display', 'block')
        $('#msg').html(msg)

    _ajax: (option)->
        $.ajax({
            method: option.method,
            url: option.url,
            data: option.data,
            type: option.type or 'POST'
            success: (r)->
                if r.result
                    option.success(r)
                    $('.has-error').each ->
                        $(this).removeClass('has-error')
                else
                    for k, v of r
                        p = $("##{k}").parent("div")
                        p.addClass('has-error')
                        p.children('label').children('.error-msg').html(v[0])

                    if option.fail
                        option.fail()

            fail: ->
                if option.fail
                    option.fail()
        })
})

# 菜单高亮
$("#navbar>ul#mian-nav>li>a").each ->
    if $(this).attr('href') == window.location.pathname
        $(this).parent('li').addClass('active')
