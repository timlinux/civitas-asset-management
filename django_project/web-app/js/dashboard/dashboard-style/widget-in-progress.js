define([
    'underscore',
    '../dashboard-style/widget-base'], function (_, Base) {
    return Base.extend({
        id: 'in-progress',
        name: 'In progress',
        /** Abstract function called when data is presented
         */
        postRender: function () {
            this.$content.html(
                '<div>coming soon</div>'
            );

        }
    });
});