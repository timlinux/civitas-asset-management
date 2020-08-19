define([
    'backbone', 'leaflet',
    'view/layer/feature'], function (Backbone, L, Feature) {
    return Backbone.View.extend({
        initialize: function (data) {
            this.listenTo(dispatcher, `system:click-${data.id}`, this.click);

            // initialize
            const that = this;
            this.layerGroup = L.featureGroup();
            this.data = data;
            this.layers = {};
            $.each(data['features'], function (name, geojson) {
                let feature = new Feature(that.data.id, name, geojson);
                that.layers[name] = feature;
                that.layerGroup.addLayer(feature.layer);

                // get features
                let features = feature.getFeatures();
                if (features.length > 0) {
                    features = features.map(function (feature) {
                        return `<a class="feature-link" onclick="dispatcher.trigger('system:click-${that.data.id}-${name}-${feature}','${feature}')">${feature}</a>`
                    })
                    dispatcher.trigger(
                        'side-panel:add-system-property',
                        that.data.id,
                        name,
                        features.join(', ')
                    )
                }
            });
            this.add();
        },
        /** Add layerGroup to map **/
        add: function () {
            this.layerGroup.addTo(map);
        },
        /** Remove layerGroup to map **/
        remove: function () {
            this.layerGroup.removeFrom(map);
        },
        /** System is clicked
         */
        click: function () {
            map.fitBounds(this.layerGroup.getBounds());
        }
    });
});