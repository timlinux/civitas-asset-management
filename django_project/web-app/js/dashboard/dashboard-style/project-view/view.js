define([
    '../style-base',
    '../widget-in-progress'], function (Base, InProgress) {
    return Base.extend({
        name: 'Project View',
        data: 'coming soon',
        init: function () {
            this.widgets = [new InProgress()];
        }
    });
});