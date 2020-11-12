define([
    'backbone',
    'leaflet',
    'jquery'
], function (
    Backbone, L, $) {
    return Backbone.View.extend({
        initBounds: [[-25.232732932266735, 93.85489258365217], [19.985307983544566, 142.16236486638226]],
        basemaps: {
            "OSM": L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            })
        },
        communityLayer: null,
        /** Initialization
         */
        initialize: function () {
            this.map = L.map('map', {zoomControl: false}).fitBounds(this.initBounds);

            // init control
            L.control.zoom({position: 'bottomleft'}).addTo(this.map);

            // add basemap
            this.basemaps['OSM'].addTo(this.map);

            // add community layer
            this.communityLayer = L.geoJSON(null, {
                fillOpacity: 0,
                "color": "#f44a52",
                "weight": 2,
                "opacity": 1
            }).addTo(this.map);

            // add listener
            this.listener()
        },
        /** Init listener for map
         */
        listener: function () {
            event.register(this, evt.MAP_PAN, this.panTo);
            event.register(this, evt.COMMUNITY_GEOJSON_CHANGE, this.communityLayerChanged);
        },
        communityLayerChanged: function (geojson) {
            this.communityLayer.clearLayers();
            this.communityLayer.addData(geojson);
            this.map.flyToBounds(this.communityLayer.getBounds(), {'duration': 1});
        },
        /**
         * Pan map to lat lng
         * @param lat
         * @param lng
         * @param zoom
         */
        panTo: function (lat, lng, zoom) {
            if (zoom) {
                this.map.flyTo([lat, lng], zoom, {
                    duration: 0.5
                });
            } else {
                this.map.panTo(new L.LatLng(lat, lng));
            }
        }
    });
});