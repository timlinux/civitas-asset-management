define([
    'underscore',
    '../widgets/base'], function (_, Base) {
    return Base.extend({
        id: 'financial-estimation-donut-chart',
        name: 'Financial Estimate Donut Charts',

        // charts
        renewalChart: null,
        maintenanceChart: null,
        reserveChart: null,

        // tree data
        labels: [],
        tree: [],
        renderData: function () {
            this.tree = [];
            this.$content.html(
                _.template($('#_financial-estimation-donut-chart').html())
            );
            this.renewalChart = this.initChart($('#renewal-cost-donut'))
            this.maintenanceChart = this.initChart($('#maintenance-cost-donut'))
            this.reserveChart = this.initChart($('#annual-reserve-donut'))
            this.$navigation = this.$el.find('.navigation')

            // render chart with data
            this.updateCharts(
                cloneObject(this.data)
            )
        },
        /** Initiate chart into variable
         */
        initChart: function ($canvas) {
            const that = this;
            return new Chart(
                $canvas[0].getContext('2d'), {
                    type: 'doughnut',
                    data: {
                        labels: [],
                        datasets: []
                    },
                    options: {
                        onClick: function (evt, obj) {
                            if (obj.length !== 0 && that.tree.length <= 1) {
                                let labelClicked = that.labels[obj[0]._index];
                                that.tree.push(labelClicked);
                                that.updateCharts();
                            }
                        },
                        hover: {
                            onHover: function (e) {
                                var point = this.getElementAtEvent(e);
                                if (point.length) e.target.style.cursor = 'pointer';
                                else e.target.style.cursor = 'default';
                            }
                        }
                    }
                });
        },
        /***
         * Update chart
         */
        updateChart: function (chart, labels, backgroundColours, data) {
            chart.data = {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: backgroundColours,
                    label: '1',
                }]
            };
            chart.update()
        },
        /** Update all chart from data
         */
        updateCharts: function () {
            // render data
            const that = this;
            let labels = [], backgroundColours = [], renewals = [], maintenances = [], reserves = [];
            this.labels = [];

            // update navigation
            this.$navigation.html('')
            if (this.tree.length !== 0) {
                this.$navigation.append(
                    '<span data-level="0">' +
                    '   <i class="fa fa-pie-chart" aria-hidden="true"></i>' +
                    '</span>')
            }

            // get data based on tree
            let data = this.data;
            this.tree.forEach(function (key, index) {
                data = data[key];
                that.$navigation.append(` ► <span data-level="${index + 1}">${data.name}</span>`)
                data = data['details'];
            });

            // when a navigation clicked
            // slice tree and rerun chart
            this.$navigation.find('span').click(function () {
                that.tree = that.tree.slice(0, $(this).data('level'));
                that.updateCharts();
            });


            let idx = 0;
            Object.keys(data).forEach(function (key) {
                that.labels.push(key);

                let value = data[key];
                labels.push(value.name);
                backgroundColours.push(COLOURS[idx]);

                // this is when feature selected
                if (that.featureSelected) {
                    if (value.selected) {
                        renewals.push(value.selected.renewal);
                        maintenances.push(value.selected.maintenance);
                        reserves.push(value.selected.annual_reserve);
                    } else {
                        renewals.push(0);
                        maintenances.push(0);
                        reserves.push(0);
                    }
                } else {
                    renewals.push(value.renewal);
                    maintenances.push(value.maintenance);
                    reserves.push(value.annual_reserve);
                }
                idx += 1;
            });

            // update chart with data
            this.updateChart(this.renewalChart, labels, backgroundColours, renewals);
            this.updateChart(this.maintenanceChart, labels, backgroundColours, maintenances);
            this.updateChart(this.reserveChart, labels, backgroundColours, reserves);
        }
    });
});