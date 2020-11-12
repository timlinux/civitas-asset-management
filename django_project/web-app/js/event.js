// this is identifier of dispatcher event
const evt = {
    COMMUNITY_CHANGE: 'community:change', // when community selected/changed
    COMMUNITY_GEOJSON_CHANGE: 'community:geojson:change', // when community geojson fetched
    MAP_PAN: 'map:pan', // pan the map
    NOTIFICATION_ADD: 'notification:add', // add a notification
    SYSTEM_CHANGE: 'system:change', // when system change
}
define([
    'backbone'], function (Backbone) {
    return Backbone.View.extend({

        initialize: function () {
            this.dispatcher = _.extend({}, Backbone.Events);
        },
        register: function (obj, name, func) {
            obj.listenTo(this.dispatcher, name, func);
        },
        trigger: function (name, ...args) {
            this.dispatcher.trigger(name, ...args)
        }
    });
});