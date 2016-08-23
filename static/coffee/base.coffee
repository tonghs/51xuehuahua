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
                option.success(r)

            fail: ->
                foption.ail()
        })
})

# 菜单高亮
$("#navbar>ul>li>a").each ->
    if $(this).attr('href') == window.location.pathname
        $(this).parent('li').addClass('active')
