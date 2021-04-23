define([
    'underscore',
    '../../widget-base'], function (_, Base) {
    return Base.extend({
        id: 'widget-quantity',
        name: 'Quantity',
        /** Abstract function called when data is presented
         */
        postRender: function () {
            this.$content.html(
                '<div>coming soon</div>'
            );

        }
    });
});