define([
    'backbone'], function (Backbone) {
    return Backbone.View.extend({
        el: '#right-panel',
        initialize: function () {
            const that = this;
            this.$el.find('.toggle-button').click(function () {
                $(this).toggleClass('hidden');
                if ($(this).hasClass('hidden')) {
                    that.$el.animate({right: "-350px"}, 100);
                } else {
                    that.$el.animate({right: "0"}, 100);
                }
            })
        },
    });
});