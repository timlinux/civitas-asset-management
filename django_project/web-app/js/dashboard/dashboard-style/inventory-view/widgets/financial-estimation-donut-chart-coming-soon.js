define([
    'underscore',
    '../../widget-base'], function (_, Base) {
    return Base.extend({
        id: 'financial-estimation-donut-chart',
        name: 'Financial Estimate Donut Charts',
        /** Abstract function called when data is presented
         */
        postRender: function () {
            this.$content.html(
                '<div>coming soon</div>'
            );

        }
    });
});