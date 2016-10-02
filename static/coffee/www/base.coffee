# 菜单高亮
$("#navbar>ul#mian-nav>li>a").each ->
    if $(this).attr('href') == window.location.pathname
        $(this).parent('li').addClass('active')
