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
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            })
        },
        /** Initialization
         */
        initialize: function () {
            const that = this;
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

            // add basemap
            this.basemaps['OSM'].addTo(this.map);

            // create layers
            let layers = {};
            QGISLayers.forEach(layer => {
                const layerObj = L.tileLayer.wms(QGISUrl, {
                    SERVICE: 'WMS',
                    VERSION: '1.3.0',
                    REQUEST: 'GetMap',
                    FORMAT: 'image/png',
                    TRANSPARENT: true,
                    LAYERS: layer
                });
                layers[layer] = layerObj;
                layerObj.addTo(this.map);
            });

            // add listener
            this.listener();

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

            this.markerIndicator = null;
            this.map.on('click', function (e) {
                event.trigger(evt.MAP_CLICKED, e.latlng);
            });

            L.control.layers(
                this.basemaps, layers, { position: 'bottomleft', }
            ).addTo(this.map);

        },
        /** Init listener for map
         */
        listener: function () {
            event.register(this, evt.MAP_ADD_LAYER, this.addLayer);
            event.register(this, evt.MAP_REMOVE_LAYER, this.removeLayer);
            event.register(this, evt.MAP_PAN, this.panTo);
            event.register(this, evt.MAP_FLY, this.flyTo);
        },
        addMarkerIndicator: function (latlng) {
            // add marker indicator
            if (this.markerIndicator) {
                this.markerIndicator.removeFrom(this.map);
            }
            this.markerIndicator = new L.marker(latlng)
            this.markerIndicator.addTo(this.map);
        },
        /**
         * Add layer to map
         */
        addLayer: function (layer) {
            try {
                layer.addTo(this.map)
            } catch (e) {

            }
        },
        /**
         * Remove layer from map
         */
        removeLayer: function (layer) {
            try {
                this.map.removeLayer(layer)
            } catch (e) {

            }
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