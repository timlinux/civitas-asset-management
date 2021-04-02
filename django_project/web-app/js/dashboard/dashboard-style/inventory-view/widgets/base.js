define([
    'underscore',
    '../../widget-base'], function (_, Base) {
    return Base.extend({
        /** Abstract function called after render
         */
        postRender: function () {
            // if data is null, show loading
            if (this.data == null) {
                this.$content.html(
                    '<div class="loading">' +
                    '   <p class="blink">Loading Data</p>' +
                    '</div>')
            } else if (Object.keys(this.data).length === 0) {
                this.$content.html(
                    '<div class="loading">' +
                    '   <p class="error">No data found</p>' +
                    '</div>')
            } else {
                this.$content.html('');
                this.renderData();
            }
        },
        /** Abstract function called after post render if data is presented
         */
        renderData: function () {

        },
    });
});