define([
    'backbone',
    'leaflet',
    'jquery',
    './map-layers'
], function (
    Backbone, L, $, MapLayer) {
    return Backbone.View.extend({
        initBounds: [[-25.232732932266735, 93.85489258365217], [19.985307983544566, 142.16236486638226]],
        basemaps: {
            "OSM": L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            })
        },
        /** Initialization
         */
        initialize: function () {
            this.map = L.map('map',
                {
                    attributionControl: false,
                    zoomControl: false
                }
            ).fitBounds(this.initBounds);
            L.control.attribution({
                position: 'bottomleft'
            }).addTo(this.map);

            // init control
            L.control.zoom({ position: 'bottomleft' }).addTo(this.map);

            // Init layers
            this.layers = new MapLayer(this.map);

            // add listener
            this.listener();

            this.overlayLayer = new L.FeatureGroup();
            this.map.addLayer(this.overlayLayer);
            // Draw layer
            // var drawnItems = new L.FeatureGroup();
            // this.map.addLayer(drawnItems);
            // var drawControl = new L.Control.Draw({
            //     position: 'bottomleft',
            //     draw: {
            //         polygon: true,
            //         marker: false,
            //         polyline: false,
            //         rectangle: false,
            //         circle: false,
            //         circlemarker: false,
            //     },
            //     edit: {
            //         featureGroup: drawnItems,
            //         edit: false,
            //         remove: false
            //     }
            // });

            // this.map.addControl(drawControl);
            // this.map.on(L.Draw.Event.CREATED, function (e) {
            //     event.trigger(evt.MAP_DRAW_DONE, e.layer);
            // });
            this.map.on('click', function (e) {
                event.trigger(evt.MAP_CLICKED, e.latlng);
            });

        },
        /** Init listener for map
         */
        listener: function () {
            event.register(this, evt.MAP_PAN, this.panTo);
            event.register(this, evt.MAP_FLY, this.flyTo);
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
        },
        /**
         * Pan map to lat lng
         * @param bound
         * @param duration
         */
        flyTo: function (bound, duration = 1) {
            if (bound._southWest) {
                this.map.flyToBounds(bound, { 'duration': duration });
            }
        },
    });
});