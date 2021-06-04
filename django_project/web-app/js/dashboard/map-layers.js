define([
    'backbone',
    'leaflet',
    'jquery'
], function (
    Backbone, L, $) {
    return Backbone.View.extend({
        layers: [],
        qgisLayers: {},
        overlayLayer: null,
        basemaps: {
            "OSM": L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
            })
        },
        /** Initialization
         */
        initialize: function (map) {
            this.map = map;

            // add basemap
            this.basemaps['OSM'].addTo(this.map);

            // QGIS Layers
            QGISLayers.forEach(layer => {
                const layerObj = L.tileLayer.wms(QGISUrl, {
                    SERVICE: 'WMS',
                    VERSION: '1.3.0',
                    REQUEST: 'GetMap',
                    FORMAT: 'image/png',
                    TRANSPARENT: true,
                    LAYERS: layer
                });
                this.qgisLayers[layer] = layerObj;
                layerObj.addTo(this.map);
            });

            L.control.layers(
                this.basemaps, this.qgisLayers, { position: 'bottomleft', }
            ).addTo(this.map);

            // add overlay layer
            this.overlayLayer = new L.FeatureGroup();
            this.map.addLayer(this.overlayLayer);

            this.listener();
        },
        /** Init listener for layers
         */
        listener: function () {
            event.register(this, evt.MAP_ADD_LAYER, this.addLayer);
            event.register(this, evt.MAP_REMOVE_LAYER, this.removeLayer);
            event.register(this, evt.MAP_ADD_OVERLAY_FEATURE, this.addFeatureToOverlay);
            event.register(this, evt.MAP_REMOVE_OVERLAY_FEATURE, this.removeFeatureToOverlay);
            event.register(this, evt.MAP_REMOVE_ALL_OVERLAY_FEATURE, this.removeAllFeatureToOverlay);
            event.register(this, evt.COMMUNITY_CHANGE, this.communityChanged);
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
         * Add feature to overlay map
         */
        addFeatureToOverlay: function (feature) {
            try {
                feature.addTo(this.overlayLayer)
            } catch (e) {
                console.log(e)
            }
        },
        /**
         * Remove feature from overlay map
         */
        removeFeatureToOverlay: function (feature) {
            try {
                this.overlayLayer.removeLayer(feature)
            } catch (e) {

            }
        },
        /**
         * Remove feature from overlay map
         */
        removeAllFeatureToOverlay: function () {
            try {
                this.overlayLayer.clearLayers()
            } catch (e) {

            }
        },
        /**
         * When community changed
         */
        communityChanged: function (community) {
            console.log(community)
        }
    });
});