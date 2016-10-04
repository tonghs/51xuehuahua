(function() {
  $(document).ready(function() {
    var pager, v_add, v_list;
    v_add = new Vue({
      el: '#addition-form',
      data: {
        name: '',
        parent: 0,
        top_category: []
      },
      ready: function() {
        var self;
        self = this;
        return $.ajax({
          url: '/j/category/top',
          method: 'GET',
          success: function(r) {
            return self.top_category = r.li;
          }
        });
      },
      methods: {
        submit: function() {
          return $._ajax({
            url: '/j/category',
            data: this.$data,
            success: function(r) {
              v_add.name = '';
              v_add.parent = 0;
              $('.addition-modal').modal('hide');
              return $.ajax({
                url: '/j/category/top',
                method: 'GET',
                success: function(r) {
                  return v_add.top_category = r.li;
                }
              });
            }
          });
        }
      }
    });
    pager = function(page) {
      return $.ajax({
        url: '/j/category',
        method: 'GET',
        data: {
          page: page
        },
        success: function(r) {
          return v_list.$data = r;
        }
      });
    };
    return v_list = new Vue({
      el: '#category-list',
      data: {
        li: [],
        count: 0,
        total_page: 0,
        page: 0
      },
      methods: {
        pager: function(page) {
          return pager(page);
        },
        next: function() {
          return pager(++this.page);
        },
        prev: function() {
          return pager(--this.page);
        }
      },
      ready: function() {
        return pager(1);
      }
    });
  });

}).call(this);
