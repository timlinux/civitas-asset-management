define([
    'backbone',
    'jquery',
    'underscore',
    'view/report-table'
], function (
    Backbone, $, _, Table) {
    return Backbone.View.extend({
        el: "#navigation",
        initialize: function () {
            this.table = new Table();
            this.table.initData(reports['summary']);
            this.table.render()

            // get projected data
            this.getProjectedData((new Date()).getFullYear() + 1, 0)
        },
        getProjectedData: function (year, yearIdx) {
            const that = this;
            if (yearIdx === 30) {
                return;
            }
            Request.get(
                '/amlit/api/report/projected/' + year,
                {}, {},
                function (data) {
                    // success
                    reports[year] = data;
                    that.$el.append(`<div class="col-4">${year}</div>`);
                    that.getProjectedData(year + 1, yearIdx + 1);
                    that.$el.find('div').off("click")
                    that.$el.find('div').click(function () {
                        that.table.initData(reports[$(this).html()]);
                        that.table.render()
                        $('#report-header').html($(this).html())
                    })
                },
                function () {
                    // fail

                }
            )

        }
    });
});