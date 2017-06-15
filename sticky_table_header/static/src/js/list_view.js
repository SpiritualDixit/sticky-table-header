odoo.define('sticky_table_header.ListView',function(require){

    "use strict";

    var ListView = require("web.ListView");

    ListView.include({
        load_list: function(data, a)
        {
            var self = this;
            (!$(".o_content .o_form_view").length) && $(document).delegate("table.o_list_view","mouseenter", function(){

                var scrollArea = self.$el.parents(
                    '.o_view_manager_content'
                ).find('table.o_list_view')[0];

                self.$el.find('table.o_list_view').each(function()
                {
                    $(this).stickyTableHeaders({
                        scrollableArea: scrollArea, 
                        leftOffset: scrollArea, 
                        "fixedOffset": 0.1 
                    })
                });
                return ;
            });
            return this._super.apply(this, arguments);
        }
    });
});
