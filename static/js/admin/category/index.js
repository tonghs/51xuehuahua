(function() {
  var v_add;

  v_add = new Vue({
    el: '#addition-form',
    data: {
      name: '',
      parent: 0
    },
    methods: {
      submit: function() {
        return $._ajax({
          url: '/j/category',
          data: this.$data,
          success: function(r) {
            v_add.name = '';
            v_add.parent = 0;
            return $('.addition-modal').modal('hide');
          }
        });
      }
    }
  });

}).call(this);
