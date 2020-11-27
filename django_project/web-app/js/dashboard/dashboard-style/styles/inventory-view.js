define([
    'leaflet',
    './base',
    '../widget/quantity',
    '../widget/financial-estimation-donut-chart'], function (L, Base, Quantity, FinancialEstimationDonutChart) {
    return Base.extend({
        name: 'Inventory View',
        layerSelected: [],
        init: function () {
            this.widgets = [new Quantity(), new FinancialEstimationDonutChart()];
            // create layer
            const that = this;

            // non point style
            const nonMarker = {
                fillOpacity: 1,
                color: "#ff7800",
                weight: 4,
                opacity: 1
            }
            let nonMarkerSelected = cloneObject(nonMarker);
            nonMarkerSelected['color'] = '#ffff00';

            // point style
            const marker = {
                radius: 5,
                fillColor: "#ff7800",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 0.8
            };
            let markerSelected = cloneObject(nonMarker);
            markerSelected['fillColor'] = '#ffff00';
            this.layer = L.geoJSON(null, {
                pointToLayer: function (feature, latlng) {
                    return L.circleMarker(latlng, marker);
                },
                style: function (feature) {
                    switch (feature.geometry.type) {
                        case 'Point':
                            return {};
                        default:
                            return nonMarker

                    }
                }
            }).on('click', function (e) {
                const feature = e.layer.feature;
                const id = feature.id;
                if (that.layerSelected.includes(id)) {
                    // unselect it
                    e.target.resetStyle(e.layer);

                    // remove from list
                    const index = that.layerSelected.indexOf(id);
                    if (index > -1) {
                        that.layerSelected.splice(index, 1);
                    }
                    that.toggleFeatures([feature], false);
                } else {
                    // select it
                    that.layerSelected.push(id);
                    that.toggleFeatures([feature], true);
                    switch (feature.geometry.type) {
                        case 'Point':
                            e.layer.setStyle(markerSelected);
                            return;
                        default:
                            e.layer.setStyle(nonMarkerSelected);
                            return;
                    }

                }
            });
        },
        /** Update the data with new properties
         */
        updateDataWithSelection: function (featureInData, properties, isSelected) {
            if (!featureInData['selected']) {
                featureInData['selected'] = {
                    quantity: 0,
                    renewal: 0,
                    maintenance: 0,
                    annual_reserve: 0,
                }
            }
            if (isSelected) {
                featureInData['selected']['quantity'] += properties['quantity'];
                featureInData['selected']['renewal'] += properties['renewal'];
                featureInData['selected']['maintenance'] += properties['maintenance'];
                featureInData['selected']['annual_reserve'] += properties['annual_reserve'];
            } else {
                featureInData['selected']['quantity'] -= properties['quantity'];
                featureInData['selected']['renewal'] -= properties['renewal'];
                featureInData['selected']['maintenance'] -= properties['maintenance'];
                featureInData['selected']['annual_reserve'] -= properties['annual_reserve'];
            }
        },
        /** Select or unselect features change data
         */
        toggleFeatures: function (features, isSelected) {
            const that = this;
            let data = this.data;
            features.forEach(function (feature) {
                const id = feature.id;
                const properties = feature.properties;

                // check if it's already selected
                if (
                    (isSelected && that.layerSelected.includes(id)) ||
                    (!isSelected && !that.layerSelected.includes(id))) {
                    that.updateDataWithSelection(
                        data[properties['cls']],
                        properties, isSelected);
                    that.updateDataWithSelection(
                        data[properties['cls']]['details'][properties['sub_cls']],
                        properties, isSelected);
                    that.updateDataWithSelection(
                        data[properties['cls']]['details'][properties['sub_cls']]['details'][properties['type']],
                        properties, isSelected);
                }
            })
            this.widgets.forEach(function (widget) {
                widget.featureSelected = (that.layerSelected.length >= 1)
            });
            that.renderWidgets();
        },
        /**
         *  This is abstract function that called after render
         */
        systemChanged: function (systems) {
            const that = this;

            // make everything default
            this.data = null;
            this.layerSelected = [];
            this.widgets.forEach(function (widget) {
                widget.featureSelected = (that.layerSelected.length >= 1)
            });

            // render widgets
            this.renderWidgets();

            // call API
            if (this.sumRequest) {
                this.sumRequest.abort()
            }
            that.layer.clearLayers();
            if (systems.length > 0) {
                this.sumRequest = Request.get(
                    '/api/features/summary',
                    {
                        'systems': systems.join(',')
                    },
                    null,
                    function (data) {
                        /** success **/
                        that.data = data;
                        that.originalData = cloneObject(data);
                        that.renderWidgets();
                    },
                    function () {
                        /**fail**/
                    })

                // call layer
                this.layer.clearLayers();
                if (this.layerRequest) {
                    this.layerRequest.abort()
                }
                this.layerRequest = Request.get(
                    '/api/features/geojson',
                    {
                        'systems': systems.join(',')
                    },
                    null,
                    function (geojson) {
                        /** success **/
                        that.layer.addData(geojson);
                        event.trigger(evt.MAP_FLY, that.layer.getBounds());
                    },
                    function () {
                        /**fail**/
                    })
            }

        },
        /** When map done on drawing
         */
        mapDrawDone: function (layer) {
            console.log(layer)
        }
    });
});