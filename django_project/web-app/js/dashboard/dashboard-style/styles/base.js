define([
    'backbone'], function (Backbone) {
    return Backbone.View.extend({
        widgets: [],
        active: false,
        listener: function () {
            event.register(this, evt.SYSTEM_CHANGE, this.systemChangedListener);
        },
        render: function () {
            this.widgets.forEach(function (widget) {
                widget.render()
            });
            this.active = true;
            this.rendered();
        },
        destroy: function () {
            this.widgets.forEach(function (widget) {
                widget.destroy()
            });
            this.active = false;
        },
        /** listen When the system changes **/
        systemChangedListener(systems) {
            if (this.active) {
                this.systemChanged(systems)
            }
        },
        /**
         *  This is abstract function that called after render
         */
        rendered: function () {

        },
        /**
         *  This is abstract function that called after render
         */
        systemChanged: function (systems) {

        },
    });
});