define([
    'underscore',
    './base'], function (_, Base) {
    return Base.extend({
        id: 'widget-quantity',
        name: 'Quantity',
        /** Abstract function called when data is presented
         */
        postRender: function () {
            this.template = _.template($('#_quantity-widget_row').html());
            this.$content.html(
                `<div class="box-overlay">${this.renderRows(this.data, 0)}</div>`
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
                }
                if (tree >= 1) {
                    row['open'] = false;
                }
                if (row['details']) {
                    row['rows'] = that.renderRows(row['details'], tree + 1)
                }
                html += that.template(row)
            });
            return html;
        }
    });
});