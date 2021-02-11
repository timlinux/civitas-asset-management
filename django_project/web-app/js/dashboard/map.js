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
        layers: {
            "Natural": L.tileLayer.wms('/map/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities?', {
                format: 'image/png',
                transparent: true,
                layers: 'Natural'
            }),
            "Fleet and Equipment": L.tileLayer.wms('/map/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities?', {
                format: 'image/png',
                transparent: true,
                layers: 'Fleet and Equipment'
            }),
            "Structures": L.tileLayer.wms('/map/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities?', {
                format: 'image/png',
                transparent: true,
                layers: 'Structures'
            }),
            "Transportation Network": L.tileLayer.wms('/map/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities?', {
                format: 'image/png',
                transparent: true,
                layers: 'Transportation Network'
            }),
            "Water Network": L.tileLayer.wms('/map/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities?', {
                format: 'image/png',
                transparent: true,
                layers: 'Water Network'
            }),
            "Wastewater Network": L.tileLayer.wms('/map/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities?', {
                format: 'image/png',
                transparent: true,
                layers: 'Wastewater Network'
            }),
            "Stormwater Network": L.tileLayer.wms('/map/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities?', {
                format: 'image/png',
                transparent: true,
                layers: 'Stormwater Network'
            }),
        },
        /** Initialization
         */
        initialize: function () {
            this.map = L.map('map', { zoomControl: false }).fitBounds(this.initBounds);

            // init control
            L.control.zoom({ position: 'bottomleft' }).addTo(this.map);

            // add basemap
            this.basemaps['OSM'].addTo(this.map);
            Object.keys(this.layers).forEach(key => this.layers[key].addTo(this.map));

            // add listener
            this.listener()

            // Draw layer
            var drawnItems = new L.FeatureGroup();
            this.map.addLayer(drawnItems);
            var drawControl = new L.Control.Draw({
                position: 'bottomleft',
                draw: {
                    polygon: true,
                    marker: false,
                    polyline: false,
                    rectangle: false,
                    circle: false,
                    circlemarker: false,
                },
                edit: {
                    featureGroup: drawnItems,
                    edit: false,
                    remove: false
                }
            });
            this.map.addControl(drawControl);
            this.map.on(L.Draw.Event.CREATED, function (e) {
                event.trigger(evt.MAP_DRAW_DONE, e.layer);
            });

            L.control.layers(this.basemaps, this.layers, { position: 'bottomleft', }).addTo(this.map);

        },
        /** Init listener for map
         */
        listener: function () {
            event.register(this, evt.MAP_ADD_LAYER, this.addLayer);
            event.register(this, evt.MAP_REMOVE_LAYER, this.removeLayer);
            event.register(this, evt.MAP_PAN, this.panTo);
            event.register(this, evt.MAP_FLY, this.flyTo);
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