define([
    './base',
    '../widget/in-progress'], function (Base, InProgress) {
    return Base.extend({
        name: 'Project View',
        initialize: function () {
            this.widgets = [new InProgress()];
            this.listener();
        },
        /**
         *  This is function that called after render
         */
        rendered: function () {
            const that = this;
            this.widgets.forEach(function (widget) {
                widget.updateData('coming soon');
                if (that.active) {
                    widget.render()
                }
            });
        },
    });
});