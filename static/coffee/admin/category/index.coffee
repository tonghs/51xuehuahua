$(document).ready ->
    v_add = new Vue({
        el: '#addition-form'
        data: {
            name: ''
            parent: 0
            top_category: []
        }
        ready: ->
            self = this
            $.ajax(
                url: '/j/category/top'
                method: 'GET'
                success: (r)->
                    self.top_category = r.li
            )
        methods: {
            submit: ->
                $._ajax(
                    url: '/j/category'
                    data: this.$data
                    success: (r)->
                        v_add.name = ''
                        v_add.parent = 0
                        $('.addition-modal').modal('hide')

                        $.ajax(
                            url: '/j/category/top'
                            method: 'GET'
                            success: (r)->
                                v_add.top_category = r.li
                        )
                )
        }
    })

    pager = (page)->
        $.ajax(
            url: '/j/category/list'
            method: 'GET'
            data: {page: page}
            success: (r)->
                v_list.$data = r
        )

    v_edit = new Vue({
        el: '#edition-form'
        data: {
            id: 0
            name: ''
            parent: 0
            top_category: []
        }
        ready: ->
            self = this
            $.ajax(
                url: '/j/category/top'
                method: 'GET'
                success: (r)->
                    self.top_category = r.li
            )
        methods: {
            submit: ->
                $.ajax(
                    url: '/j/category/edit'
                    method: 'POST'
                    data: this.$data
                    success: (r)->
                        pager(v_list.page)
                        $('.edition-modal').modal('hide')

                )
        }
    })


    v_list = new Vue({
        el: '#category-list'
        data: {
            li: []
            count: 0
            total_page: 0
            page: 1
        }
        methods: {
            pager: (page)->
                pager(page)

            next: ->
                pager(++this.page)

            prev: ->
                pager(--this.page)
            
            edit: (id)->
                $.ajax(
                    url: '/j/category'
                    method: 'GET'
                    data: {id: id}
                    success: (r)->
                        v_edit.id = r.id
                        v_edit.name = r.name
                        v_edit.parent = r.parent

                )

            rm: (id)->
                $._ajax(
                    url: '/j/category/rm'
                    method: 'POST'
                    data: {id: id}
                    success: (r)->
                        pager(this.page)
                )

        }
        ready: ->
            pager(1)
    })
