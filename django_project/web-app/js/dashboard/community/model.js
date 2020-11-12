define([
    'backbone'], function (Backbone) {
    return Backbone.Model.extend({
        urlRoot: '/api/community',
        initialize: function () {
            this.on('sync', this.fetched, this);
            this.on('error', this.fetchError, this);
        },
        selected: function () {
            if (!this.get('geometry')) {
                this.fetch();
                return
            }
            event.trigger(evt.COMMUNITY_GEOJSON_CHANGE, {
                "type": "Feature",
                "properties": {
                    "id": this.id,
                    "name": this.get('name'),
                    "region": this.get('region'),
                    "province": this.get('province'),
                },
                "geometry": this.get('geometry')
            });
            event.trigger(evt.COMMUNITY_CHANGE, this);
        },
        /** after fetched **/
        fetched: function () {
            this.selected()
        },
        fetchError: function (error) {

        }
    });
});