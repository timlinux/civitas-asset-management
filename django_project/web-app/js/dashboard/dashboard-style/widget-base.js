define([
    'backbone'], function (Backbone) {
    return Backbone.View.extend({
        initialize: function () {
            this.$wrapper = $('#side-panel .content');
        },
        render: function () {
            // append to wrapper
            if (this.$wrapper.find(`#${this.id}`).length === 0) {
                this.$wrapper.append(`
                    <div id="${this.id}" class="widget">
                        <div class="title">${this.name}</div>
                        <div class="content-widget"></div>
                    </div>
                `)
                this.$content = $(`#${this.id} .content-widget`)
                this.$el = $(`#${this.id}`)
            }
            this.postRender();
        },
        destroy: function () {
            this.postDestroy()
            this.$el.remove()
        },
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
            }
        },
        /** Abstract function called when widget destroyed
         */
        postDestroy: function () {

        },
    });
});