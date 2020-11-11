define([
    'backbone',
    'jquery',
    'underscore',
    'view/report-table',
    'view/chart',
], function (
    Backbone, $, _, Table, Chart) {
    return Backbone.View.extend({
        el: "#navigation",
        initialize: function () {
            this.chart = new Chart();
            this.table = new Table();
            this.table.initData(reports['summary']);
            this.table.render();
            this.$table = $('#report-table');
            this.$chart = $('#report-chart');
            this.years = [];

            // get projected data
            // this.getProjectedData((new Date()).getFullYear() + 1, 0)
        },
        getProjectedData: function (year, yearIdx) {
            const that = this;
            $('#projected-loading ').css('width', `${yearIdx * 100 / maxProjectedYear}%`)
            if (yearIdx === maxProjectedYear) {
                $('#projected-loading ').hide()
                $('#projected-expenditure').removeClass('disabled')
                return;
            }
            Request.get(
                '/amlit/api/report/projected/' + year,
                {}, {},
                function (data) {
                    // success
                    reports[year] = data;
                    that.$el.append(`<div class="col-4" data-report="${year}">${year}</div>`);
                    that.getProjectedData(year + 1, yearIdx + 1);
                    that.$el.find('div').off("click")
                    that.$el.find('div').click(function () {
                        that.clicked($(this))
                    })
                    $.each(data['details'], function (key, value) {
                        if (!reports['projected-graph'][value.name]) {
                            reports['projected-graph'][value.name] = []
                        }
                        reports['projected-graph'][value.name].push(value.total)
                    })
                    that.years.push(year)
                },
                function () {
                    // fail

                }
            )
        },
        clicked: function ($el) {
            let reportName = $el.data('report');
            this.$table.hide();
            this.$chart.hide();
            if (reportName === 'projected-graph') {
                this.$chart.show();
                this.chart.initData(reports[reportName], this.years);
                this.chart.render()
            } else {
                this.$table.show();
                this.table.initData(reports[reportName]);
                this.table.render()
            }
            $('#report-header').html($el.html())
        }
    });
});