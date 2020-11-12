define([
    'backbone'], function (Backbone) {
    return Backbone.View.extend({
        el: '#side-panel',
        initialize: function () {
            const that = this;
            this.$content = this.$el.find('.content');
            this.$el.find('.toggle-button').click(function () {
                $(this).toggleClass('hidden');
                if ($(this).hasClass('hidden')) {
                    that.$el.animate({right: "-400px"}, 100);
                } else {
                    that.$el.animate({right: "0"}, 100);
                }
            })
            this.loading();
        },
        /** Make a loading statement
         */
        loading: function () {
            this.$content.html('' +
                '<div class="loading full">' +
                '   <p>Loading Data</p>' +
                '</div>')
        }
    });
});