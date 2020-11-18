define([
    'underscore',
    './base'], function (_, Base) {
    return Base.extend({
        id: 'consequence-of-failure-donut-graph',
        name: 'Consequence of Failure Donut Graph',
        /** Function called when data is presented
         */
        renderData: function () {
            this.$content.html(
                '<div>coming soon</div>'
            );

        }
    });
});