define([
    'underscore',
    './base'], function (_, Base) {
    return Base.extend({
        id: 'in-progress',
        name: 'In progress',
        /** Function called when data is presented
         */
        renderData: function () {
            this.$content.html(
                '<div>coming soon</div>'
            );

        }
    });
});