define([
    'backbone', 'leaflet'], function (Backbone, L) {
    return Backbone.View.extend({
        features: {},
        initialize: function (systemID, name, geojson) {
            const that = this;
            this.systemID = systemID;
            this.name = name;
            this.geojson = geojson;
            this.features = {};

            // create layer
            this.layer = L.geoJSON(geojson, {
                style: Style.get(name),
                pointToLayer: function (feature, latlng) {
                    let style = Style.get(name);
                    if (style && style.icon) {
                        return L.marker(latlng, style);
                    } else {
                        return L.circleMarker(latlng, style);
                    }
                },
                onEachFeature: function (feature, layer) {
                    that.features[feature.properties.uid] = layer
                    layer.on({
                        click: function (e) {
                            let feature = e.target.feature;
                        }
                    });
                    // bind popup
                    let popup = ''
                    $.each(feature.properties, function (key, value) {
                        popup += `<tr><td>${key.capitalize().replaceAll('_', ' ')}</td><td>${value}</td></tr>`
                    })
                    layer.bindPopup('<table>' + popup + '</table');
                }
            });
        },
        /** Get list of feature
         */
        getFeatures: function () {
            let features = [];
            let that = this;
            $.each(this.geojson['features'], function (index, feature) {
                let uid = feature.properties.uid;
                features.push(uid)
                that.listenTo(
                    dispatcher,
                    `system:click-${that.systemID}-${that.name}-${uid}`, that.click
                );
            });
            return features;
        },
        /** Feature is clicked
         */
        click: function (uid) {
            const feature = this.features[uid];
            feature.fire('click')
            if (feature.feature.geometry.type === 'Point') {
                dispatcher.trigger(
                    'map:pan',
                    feature.getLatLng().lat,
                    feature.getLatLng().lng)
            } else {
                map.fitBounds(feature.getBounds());
            }
        }
    });
});