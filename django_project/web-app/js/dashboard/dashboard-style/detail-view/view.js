define([
    'leaflet',
    '../style-base',
    '../detail-view/widgets/ticket-list',
    '../detail-view/widgets/create-ticket',], function (L, Base, TicketList, CreateTicket) {
    return Base.extend({
        name: 'Detail View',
        lastLayer: null,
        init: function () {
            // create layer
            const that = this;
            this.widgets = [new TicketList(), new CreateTicket()];

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
                const layer = e.layer;
                if (that.lastLayer === layer) {
                    e.target.resetStyle(e.layer);
                    that.lastLayer = null;
                    that.rerenderWidgets();
                } else {
                    // select it
                    if (that.lastLayer) {
                        e.target.resetStyle(that.lastLayer);
                    }
                    that.lastLayer = layer
                    that.rerenderWidgets();
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
        /** Rerender all widgets
         *
         */
        rerenderWidgets: function () {
            const that = this;
            this.widgets.forEach(function (widget) {
                widget.featureSelectedFunction(that.lastLayer);
            });

            // render widgets
            this.renderWidgets();
        },
        /**
         *  This is abstract function that called after render
         */
        systemChanged: function (systems) {
            const that = this;

            // make everything default
            this.data = null;
            this.lastLayer = null;
            this.rerenderWidgets();

            // call API
            if (this.sumRequest) {
                this.sumRequest.abort()
            }
            this.layer.clearLayers();
            if (systems.length > 0) {
                // call layer
                this.layer.clearLayers();
                if (this.request) {
                    this.request.abort()
                }
                this.request = Request.get(
                    urls.feature_geojson,
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

        }
    });
});