// this is identifier of dispatcher event
const evt = {
    COMMUNITY_CHANGE: 'community:change', // when community selected/changed
    COMMUNITY_GEOJSON_CHANGE: 'community:geojson:change', // when community geojson fetched
    MAP_PAN: 'map:pan', // pan the map
    MAP_FLY: 'map:fly', // fly the map
    MAP_ADD_LAYER: 'map:layer:add', // add layer to map
    MAP_REMOVE_LAYER: 'map:layer:remove', // add layer to map
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