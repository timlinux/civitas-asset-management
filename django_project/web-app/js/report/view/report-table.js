define([
    'backbone',
    'jquery',
    'underscore'
], function (
    Backbone, $, _) {
    return Backbone.View.extend({
        el: "#table",
        initialize: function () {
            this.template = _.template($('#_report_row').html());
        },
        /** Render data per row
         * @param extraClass
         * @param treeIdx
         * @param rowKey
         * @param rowData
         * @param parentData
         */
        renderRow: function (rowKey, rowData, parentData, treeIdx, extraClass) {
            const name = rowKey ?
                `<a data-toggle="collapse" href="#${rowKey}" role="button" aria-expanded="false" aria-controls="${rowKey}" style="margin-left: ${10 * treeIdx}px">
                    ${rowData.name}
                 </a>` : rowData.name;
            let html = `<div class="row ${extraClass}"><div class="col-3 col-name">${name}</div>`;
            $.each(this.headers, function (key, header) {
                html += `
                    <div class="col number">${toCurrency(rowData[header])}</div>
                    <div class="col percent">${
                    parentData[header] ? ((rowData[header] / parentData[header]) * 100).toFixed(2) : 100
                    }%</div>
                `
            })
            html += '</div>';
            return html
        },
        /** Init data for table
         *
         * @param data
         */
        initData(data) {
            const that = this;
            this.subIdx = 1;
            this.data = data;
            this.headers = [];
            const $el = $('#header');
            $el.html('<div class="col-3 col-name"></div>')
            $.each(data, function (key, value) {
                if (!isNaN(value)) {
                    $el.append(
                        `<div class="col">${capitalize(key)}</div>` +
                        '<div class="col percent"></div>')
                    that.headers.push(key)
                }
            })

        },
        renderGroupData($el, data, parentData, tree) {
            const that = this;
            $.each(data, function (key, value) {
                const subID = `sub-${that.subIdx}`;
                that.subIdx += 1;
                $el.append(
                    that.renderRow(subID, value, parentData, tree)
                );
                if (Object.keys(value['details']).length !== 0) {
                    $el.append(`<div id="${subID}" class="collapse sub"></div>`);
                    that.renderGroupData($(`#${subID}`), value['details'], value, tree + 1)
                }
            });
        },
        /** Render table from data
         */
        render: function () {
            const that = this;
            const data = this.data;
            this.$el.html('<i>loading</i>');

            //render class
            this.$el.html('');
            this.renderGroupData(this.$el, data['details'], data, 0);
            this.$el.append(that.renderRow('', data, 0, 0, 'total'))
        },
    });
});