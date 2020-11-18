define([
    'underscore',
    './base'], function (_, Base) {
    return Base.extend({
        id: 'consequence-of-failure-donut-graph',
        name: 'Consequence of Failure Donut Graph',
        /** Abstract function called when data is presented
         */
        postRender: function () {
            this.$content.html(
                '<div>coming soon</div>'
            );

        }
    });
});