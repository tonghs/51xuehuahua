$(document).ready ->
    pathname = window.location.pathname
    bingo = false
    $('.sidebar').find('a').each ->
        if pathname == $(this).attr('href')
            treeview = $(this).parents('li')
            if treeview
                treeview.addClass('active')

            treeview_menu = $(this).parents('ul.treeview-menu')
            if treeview_menu
                treeview_menu.addClass('active')
