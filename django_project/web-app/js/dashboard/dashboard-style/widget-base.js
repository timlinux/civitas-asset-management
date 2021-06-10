define([
    'backbone'], function (Backbone) {
    return Backbone.View.extend({
        icon: 'fa-exclamation-circle',
        initialize: function () {
            this.$rightPanel = $('#right-panel');
            this.$wrapper = $('#right-panel .inner');
            this.$wrapperButton = $('#side-panel-toggle-button');

            // events
            event.register(this, evt.MAP_CLICKED, this._mapClicked);
            event.register(this, evt.WIDGETS_HIDE, this.hide);
            this.init();
        },
        /**
         *  This is abstract function that called after initialize
         */
        init: function () {

        },

        render: function () {
            // append to wrapper
            const that = this;
            this.active = true;
            if (this.$wrapper.find(`#${this.id}`).length === 0) {
                this.$wrapper.append(`
                    <div id="${this.id}" class="content full widget" style="display: none">
                        <div class="title">${this.name}</div>
                        <div class="content-widget"></div>
                    </div>
                `);
                this.$wrapperButton.append(
                    `<div id="${this.id}-button" class="toggle-button"">
                        <i class="fa ${this.icon}" aria-hidden="true"></i>
                    </div>`
                )
                this.$content = $(`#${this.id} .content-widget`);
                this.$el = $(`#${this.id}`);
                this.$button = $(`#${this.id}-button`);
                this.$button.click(function () {
                    that.show();
                });
            }
            this.postRender();
        },
        show: function () {
            const that = this;
            const ID = $(this.$rightPanel.find('.content:visible')[0]).attr('id');
            if (!this.$rightPanel.hasClass('hidden') && ID === that.id) {
                this.$rightPanel.animate({ right: "-350px" }, 100, function () {
                    that.$rightPanel.addClass('hidden');
                });
            } else {
                if (this.$rightPanel.hasClass('hidden')) {
                    this.$rightPanel.removeClass('hidden');
                    this.$rightPanel.animate({ right: "0" }, 100);
                }
                if (ID !== that.id) {
                    event.trigger(evt.WIDGETS_HIDE);
                    this.$button.removeClass('hidden');
                    this.$el.show();
                    this.extraShow()
                }
            }
        },
        extraShow: function () {

        },
        hide: function () {
            if (this.$button) {
                this.$button.addClass('hidden');
            }
            this.$el.hide();
            this.extraHide();
        },
        extraHide: function () {

        },
        destroy: function () {
            this.active = false;
            this.postDestroy();
            this.$el.remove();
            if (this.$button) {
                this.$button.remove();
            }
            this.extraHide();
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
        /** When map clicked and check if active
         */
        _mapClicked: function (latlng) {
            if (this.active) {
                this.mapClicked(latlng)
            }
        },
        /** When map clicked
         */
        mapClicked: function (latlng) {

        }
    });
});