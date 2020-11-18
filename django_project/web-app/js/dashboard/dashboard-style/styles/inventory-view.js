define([
    './base',
    '../widget/quantity',
    '../widget/financial-estimation-donut-chart'], function (Base, Quantity, FinancialEstimationDonutChart) {
    return Base.extend({
        name: 'Inventory View',
        data: null,
        initialize: function () {
            this.widgets = [new Quantity(), new FinancialEstimationDonutChart()];
            this.listener();
        },
        /**
         *  This is function that called after render
         */
        rendered: function () {
            const that = this;
            this.widgets.forEach(function (widget) {
                widget.updateData(that.data);
                if (that.active) {
                    widget.render()
                }
            });
        },
        /**
         *  This is abstract function that called after render
         */
        systemChanged: function (systems) {
            const that = this;
            this.data = null;
            this.rendered();
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
                    that.rendered();
                },
                function () {
                    /**fail**/
                })

        },
    });
});