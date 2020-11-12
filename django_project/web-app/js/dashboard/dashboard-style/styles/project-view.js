define([
    './base'], function (Base) {
    return Base.extend({
        name: 'Project View',
        initialize: function () {
            this.widgets = [];
            this.listener();
        },
    });
});