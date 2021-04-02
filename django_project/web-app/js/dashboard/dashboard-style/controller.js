define([
    'backbone',
    './detail-view/view',
    './inventory-view/view',
    './prioritization-view/view',
    './project-view/view'
], function (
    Backbone, DetailView, InventoryView, PrioritizationView, ProjectView) {
    return Backbone.View.extend({
        el: '#styles',
        style: null,
        initialize: function () {
            const that = this;
            const $ul = that.$el.find('ul');
            this.$el.find('.selection').click(function () {
                $ul.slideToggle('fast');
            })

            // render views as list
            this.views = [new DetailView(), new InventoryView(), new PrioritizationView(), new ProjectView()];
            this.views.forEach(function (view, idx) {
                $ul.append(`<li value="${idx}">${view.name}</li>`)
            });

            // onclick list
            $ul.find('li').click(function () {
                if (that.views[$(this).val()] !== that.style) {
                    that.change(that.views[$(this).val()])
                }
            });
            $($ul.find('li')[0]).click();
            $ul.hide()
        },
        /** Change dashboard style **/
        change: function (style) {
            // render layer to map
            // remove previous style
            if (this.style) {
                event.trigger(evt.MAP_REMOVE_LAYER, style.layer);
            }

            this.style = style;
            this.$el.find('.name').html(style.name);

            // destroy every view and render selected one
            this.views.forEach(function (view, idx) {
                view.destroy()
            });
            style.activate();

            // add layer
            event.trigger(evt.MAP_ADD_LAYER, style.layer);
            event.trigger(evt.MAP_FLY, style.layer.getBounds());
        },
    });
});