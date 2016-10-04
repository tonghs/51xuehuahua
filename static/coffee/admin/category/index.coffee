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
            url: '/j/category'
            method: 'GET'
            data: {page: page}
            success: (r)->
                v_list.$data = r
        )

    v_list = new Vue({
        el: '#category-list'
        data: {
            li: []
            count: 0
            total_page: 0
            page: 0
        }
        methods: {
            pager: (page)->
                pager(page)

            next: ->
                pager(++this.page)

            prev: ->
                pager(--this.page)


        }
        ready: ->
            pager(1)
    })
