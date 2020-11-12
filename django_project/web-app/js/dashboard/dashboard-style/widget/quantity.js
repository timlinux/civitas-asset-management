define([
    './base'], function (Base) {
    return Base.extend({
        id: 'widget-quantity',
        name: 'Quantity',
        /** Function called when data is presented
         */
        renderData: function (data) {
            console.log(data)
        },
    });
});