define([
    './base',
    '../widget/quantity',
    '../widget/financial-estimation-donut-chart'], function (Base, Quantity, FinancialEstimationDonutChart) {
    return Base.extend({
        name: 'Inventory View',
        initialize: function () {
            this.widgets = [new Quantity(), new FinancialEstimationDonutChart()];
            this.listener();
        },
        /**
         *  This is function that called after render
         */
        rendered: function () {
            const that = this;
            if (this.data) {
                this.widgets.forEach(function (widget) {
                    widget.render(that.data)
                });
            }
        },
        /**
         *  This is abstract function that called after render
         */
        systemChanged: function (systems) {
            const that = this;
            Request.get(
                '/api/feature/summary',
                {
                    'systems': systems.join(',')
                },
                null,
                function (data) {
                    /** success **/
                    that.data = data;
                    that.rendered();
                },
                function () {
                    /**fail**/
                })

        },
    });
});