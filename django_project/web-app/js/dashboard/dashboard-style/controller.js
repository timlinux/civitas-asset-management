define([
    'backbone',
    './styles/inventory-view',
    './styles/prioritization-view',
    './styles/project-view'
], function (
    Backbone, InventoryView, PrioritizationView, ProjectView) {
    return Backbone.View.extend({
        style: null,
        el: '#styles',
        initialize: function () {
            const that = this;
            const $ul = that.$el.find('ul');
            this.$el.find('.selection').click(function () {
                $ul.slideToggle('fast');
            })

            // render views as list
            this.views = [new InventoryView(), new PrioritizationView(), new ProjectView()];
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
            this.style = style;
            this.$el.find('.name').html(style.name);

            // destroy every view and render selected one
            this.views.forEach(function (view, idx) {
                view.destroy()
            });
            style.activate();
        },
    });
});