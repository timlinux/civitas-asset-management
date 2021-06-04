define([
    'backbone',
    'leaflet',
    'jquery'
], function (
    Backbone, L, $) {
    return Backbone.View.extend({
        QgisLayers: [],
        QgisLayersByName: [],
        /** Initialization
         */
        initialize: function (map) {
            this.map = map;
            const that = this;
            this.$el = $('#layers');
            $('#layer-list-toggle').click(function () {
                $('#left-top').toggleClass('show');
            })
            $.each(QGISLayers, function (key, layerName) {
                const objLayer = L.tileLayer.wms(QGISUrl, {
                    SERVICE: 'WMS',
                    VERSION: '1.3.0',
                    REQUEST: 'GetMap',
                    FORMAT: 'image/png',
                    TRANSPARENT: true,
                    LAYERS: layerName
                })
                const layer = {
                    'active': true,
                    'layer': objLayer
                }
                const legend = `${QGISUrl}?service=WMS&version=1.1.1&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetLegendGraphic&FORMAT=image%2Fpng&TRANSPARENT=true&LAYERS=${layerName}`
                that.QgisLayers.push(layer);
                that.QgisLayersByName[layerName] = layer;
                objLayer.addTo(that.map);

                // restructure the html
                const layerNameClean = layerName.replaceAll(' ', '-');
                const html = `
                    <div class="layer-row active" data-layername="${layerName}">
                        <a aria-hidden="true" data-toggle="collapse" href="#${layerNameClean}"
                           role="button" aria-expanded="false" aria-controls="collapseExample" class="collapsed button-collapse">
                            <i class="fa fa-caret-down"></i>
                            <i class="fa fa-caret-up"></i>
                        </a>
                        <i class="fa fa-check-square" aria-hidden="true"></i>
                        <i class="fa fa-square-o" aria-hidden="true"></i>
                         ${layerName}                       
                        <div class="layer-list collapse" id="${layerNameClean}">
                            <img src="${legend}">
                        </div>
                    </div>
                `;
                that.$el.append(html)
            });
            this.$el.find('.fa-check-square, .fa-square-o').click(function () {
                const $row = $(this).closest('.layer-row')
                $row.toggleClass('active')
                const layer = that.QgisLayersByName[$row.data('layername')];
                if ($row.hasClass('active')) {
                    layer.active = true;
                    event.trigger(evt.MAP_ADD_LAYER, layer.layer);
                } else {
                    layer.active = false;
                }
                that.rearrangeLayer();
            })
        },

        rearrangeLayer: function () {
            $.each(this.QgisLayers, function (key, layer) {
                if (layer.active) {
                    layer.layer.bringToFront();
                } else {
                    console.log(layer)
                    event.trigger(evt.MAP_REMOVE_LAYER, layer.layer);
                }
            });
        }
    });
});