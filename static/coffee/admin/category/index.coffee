v_add = new Vue({
    el: '#addition-form'
    data: {
        name: ''
        parent: 0
    }
    methods: {
        submit: ->
            $._ajax(
                url: '/j/category'
                data: this.$data
                success: (r)->
                    v_add.name = ''
                    v_add.parent = 0
                    $('.addition-modal').modal('hide')
            )
    }
})
