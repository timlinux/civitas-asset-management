define([
    'underscore',
    '../widgets/base'], function (_, Base) {
    return Base.extend({
        id: 'widget-quantity',
        name: 'Quantity',
        renderData: function () {
            this.template = _.template($('#_quantity-widget_row').html());
            this.$content.html(
                `<div class="box-overlay">${this.renderRows(cloneObject(this.data), 0)}</div>`
            );
        },
        /** Rendering rows from data
         */
        renderRows: function (rows, tree) {
            const that = this;
            let html = '';
            $.each(rows, function (key, row) {
                row['id'] = `${tree}-${key}`;
                row['rows'] = '';
                row['margin'] = 5 * tree;
                row['open'] = true;
                if (tree === 0) {
                    row['unit'] = '';
                    row['quantity'] = '';
                } else {
                    row['open'] = false;
                    // this is when feature selected
                    if (that.featureSelected) {
                        if (row.selected) {
                            row['quantity'] = row.selected.quantity + ' / ' + row.quantity
                        } else {
                            row['quantity'] = 0 + ' / ' + row.quantity
                        }
                    }
                }

                // render every details
                if (row.details) {
                    row['rows'] = that.renderRows(row.details, tree + 1)
                }
                html += that.template(row)
            });
            return html;
        }
    });
});