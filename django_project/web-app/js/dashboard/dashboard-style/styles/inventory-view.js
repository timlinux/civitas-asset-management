define([
    './base',
    '../widget/quantity',
    '../widget/financial-estimation-donut-chart'], function (Base, Quantity, FinancialEstimationDonutChart) {
    return Base.extend({
        name: 'Inventory View',
        init: function () {
            this.widgets = [new Quantity(), new FinancialEstimationDonutChart()];
        },
        /**
         *  This is abstract function that called after render
         */
        systemChanged: function (systems) {
            const that = this;
            this.data = null;
            this.renderWidgets();
            if (this.request) {
                this.request.abort()
            }
            this.request = Request.get(
                '/api/feature/summary',
                {
                    'systems': systems.join(',')
                },
                null,
                function (data) {
                    /** success **/
                    that.data = data;
                    that.renderWidgets();
                },
                function () {
                    /**fail**/
                })

        },
    });
});