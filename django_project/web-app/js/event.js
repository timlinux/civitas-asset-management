// this is identifier of dispatcher event
const evt = {
    COMMUNITY_CHANGE: 'community:change', // when community selected/changed
    COMMUNITY_GEOJSON_CHANGE: 'community:geojson:change', // when community geojson fetched
    MAP_PAN: 'map:pan', // pan the map
    MAP_FLY: 'map:fly', // fly the map
    MAP_ADD_LAYER: 'map:layer:add', // add layer to map
    MAP_REMOVE_LAYER: 'map:layer:remove', // remove layer from map
    MAP_ADD_OVERLAY_FEATURE: 'map:layer:add-overlay-feature', // add feature to overlay map
    MAP_REMOVE_OVERLAY_FEATURE: 'map:layer:remove-overlay-feature', // remove feature from overlay map
    MAP_REMOVE_ALL_OVERLAY_FEATURE: 'map:layer:remove-all-overlay-feature', // remove all feature from overlay map
    MAP_DRAW_DONE: 'map:draw:done', // draw done
    MAP_CLICKED: 'map:click', // draw click
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