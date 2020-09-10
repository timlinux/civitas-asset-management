define([
    'backbone',
    'jquery',
    'underscore',
    'view/report-table'
], function (
    Backbone, $, _, Table) {
    return Backbone.View.extend({
        el: "#report-chart",
        initialize: function () {
        },
        initData(data, labels) {
            const that = this;
            this.data = [];
            $.each(data, function (key, value) {
                that.data.push({
                    label: key,
                    backgroundColor: getRandomColor(),
                    data: value
                })
            });
            this.labels = labels;
        },
        render: function () {
            var ctx = document.getElementById('report-chart').getContext('2d');
            console.log(this.data)
            window.myBar = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: this.labels,
                    datasets: this.data
                },
                options: {
                    title: {
                        display: true,
                        text: 'Projected Expenditure'
                    },
                    tooltips: {
                        mode: 'index',
                        intersect: false
                    },
                    responsive: true,
                    scales: {
                        xAxes: [{
                            stacked: true,
                        }],
                        yAxes: [{
                            stacked: true
                        }]
                    }
                }
            });
        }
    })
});