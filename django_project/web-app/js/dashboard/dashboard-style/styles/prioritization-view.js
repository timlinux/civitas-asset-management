define([
    './base'], function (Base) {
    return Base.extend({
        name: 'Prioritization View',
        initialize: function () {
            this.widgets = [];
            this.listener();
        },
    });
});