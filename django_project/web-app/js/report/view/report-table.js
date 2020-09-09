define([
    'backbone',
    'jquery',
    'underscore'
], function (
    Backbone, $, _) {
    return Backbone.View.extend({
        el: "#table",
        maintenance: 'maintenance',
        replacement: 'replacement',
        annualReserve: 'annual_reserve',
        initialize: function () {
            this.template = _.template($('#_report_row').html());
        },
        /** Render data per row
         * @param rowKey
         * @param rowData
         */
        renderRow: function (rowKey, rowData, extraClass) {
            const name = rowKey ?
                `<a data-toggle="collapse" href="#${rowKey}" role="button" aria-expanded="false" aria-controls="${rowKey}">
                    ${rowData.name}
                 </a>` : rowData.name;
            return this.template({
                name: name,
                maintenance: toCurrency(rowData[this.maintenance]),
                maintenance_perc: rowData[`${this.maintenance}_perc`],
                replacement: toCurrency(rowData[this.replacement]),
                replacement_perc: rowData[`${this.replacement}_perc`],
                annual_reserve: toCurrency(rowData[this.annualReserve]),
                annual_reserve_perc: rowData[`${this.annualReserve}_perc`],
                extra_class: extraClass
            })
        },
        getPercentage: function (rowData, totalData, key) {
            rowData[`${key}_perc`] = rowData[key] ? (
                (rowData[key] / totalData[key]) * 100).toFixed(2) : 0
        },
        /** Render table from data
         * @param data
         */
        render: function (data) {
            const that = this;
            this.$el.html('<i>loading</i>');

            //render class
            this.$el.html('');
            $.each(data['reports'], function (classKey, classVal) {
                // calculate the percentage
                that.getPercentage(classVal, data, that.maintenance);
                that.getPercentage(classVal, data, that.replacement);
                that.getPercentage(classVal, data, that.annualReserve);

                const $el = that.$el;
                const classGroupID = `class-${classKey}`;
                $el.append(
                    that.renderRow(classGroupID, classVal)
                );
                $el.append(`<div id="${classGroupID}" class="collapse class"></div>`);

                //render sub class
                $.each(classVal, function (subClassKey, subClassVal) {
                    if (isNaN(subClassKey)) {
                        return
                    }
                    // calculate the percentage
                    that.getPercentage(subClassVal, classVal, that.maintenance);
                    that.getPercentage(subClassVal, classVal, that.replacement);
                    that.getPercentage(subClassVal, classVal, that.annualReserve);

                    const $el = $(`#${classGroupID}`);
                    const subClassGroupID = `sub-class-${classKey}-${subClassKey}`;
                    $el.append(
                        that.renderRow(subClassGroupID, subClassVal)
                    );
                    $el.append(`<div id="${subClassGroupID}" class="collapse subclass"></div>`);

                    //render type
                    $.each(subClassVal, function (typeKey, typeVal) {
                        if (isNaN(typeKey)) {
                            return
                        }
                        // calculate the percentage
                        that.getPercentage(typeVal, subClassVal, that.maintenance);
                        that.getPercentage(typeVal, subClassVal, that.replacement);
                        that.getPercentage(typeVal, subClassVal, that.annualReserve);

                        const $el = $(`#${subClassGroupID}`);
                        $el.append(
                            that.renderRow(typeKey, typeVal)
                        );
                    });
                });
            });

            data['maintenance_perc'] = 100;
            data['replacement_perc'] = 100;
            data['annual_reserve_perc'] = 100;
            this.$el.append(that.renderRow('', data, 'total'))
        },
    });
});