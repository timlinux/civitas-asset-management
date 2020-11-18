define([
    'underscore',
    './base'], function (_, Base) {
    return Base.extend({
        id: 'widget-quantity',
        name: 'Quantity',
        /** Function called when data is presented
         */
        renderData: function () {
            this.template = _.template($('#_quantity-widget_row').html());
            this.$content.html(
                this.renderRows(this.data, 0)
            );

        },
        renderRows: function (rows, tree) {
            const that = this;
            let html = '';
            this.$content.addClass('box-overlay');
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