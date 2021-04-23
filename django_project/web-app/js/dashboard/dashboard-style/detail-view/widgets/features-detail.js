define([
    'underscore',
    '../../widget-base'], function (_, Base) {
    return Base.extend({
        id: 'features-detail',
        name: 'Features',
        /** Abstract function called when data is presented
         */
        postRender: function () {
            if (this.data) {
                if (this.data.features.length > 0) {
                    let htmls = [];
                    this.data.features.map(function (feature) {
                        let html = `
                            <table>
                                <tr>
                                    <th colspan="2">${feature.id}</th>
                                </tr>`;
                        html += `
                            <tr>
                                <td>ID</td>
                                <td>${feature.properties.feature_id}</td>
                            </tr>`
                        if (Object.keys(feature.properties).length > 0) {
                            html += `
                                <tr>
                                    <td class="button hidden" colspan="2">Open attributes</td>
                                </tr>`;
                        }
                        $.each(feature.properties, function (key, value) {
                            if (key !== 'feature_id') {
                                html += `
                                <tr class="extra-property">
                                    <td>${capitalize(key)}</td>
                                    <td>${value}</td>
                                </tr>`
                            }
                        });
                        html += `</table>`;
                        htmls.push(html)
                    });
                    this.$content.html(htmls.join(''));
                    this.$content.find('table').find('.button').click(function () {
                        $(this).toggleClass('hidden');
                        $(this).toggleClass('expand');
                        $(this).closest('table').find('.extra-property').toggle();
                    })
                } else {
                    this.$content.html(
                        _.template($('#_no_data_found').html())
                    );
                }
            } else {
                this.$content.html(
                    _.template($('#_please_click_map').html())
                );
            }
        },
        /** When map clicked
         */
        mapClicked: function (latlng) {
            const that = this;
            const point = map.latLngToContainerPoint(
                latlng, map.getZoom());
            const size = map.getSize();
            const bounds = map.getBounds();
            const params = {
                SERVICE: 'WMS',
                REQUEST: 'GetFeatureInfo',
                BBOX: [
                    bounds._southWest.lat,
                    bounds._southWest.lng,
                    bounds._northEast.lat,
                    bounds._northEast.lng
                ].join(','),
                SRS: MAPSRS,
                HEIGHT: size.y,
                WIDTH: size.x,
                QUERY_LAYERS: QGISLayers.join(','),
                INFO_FORMAT: 'application/json',
                i: point.x,
                j: point.y
            };

            // get the featureinfo
            if (this.request) {
                this.request.abort()
            }
            this.$content.html(
                _.template($('#_loading').html())
            );
            this.request = Request.get(
                QGISUrl,
                params,
                null,
                function (data) {
                    /** success **/
                    that.data = data;
                    that.render();
                },
                function () {
                    /**fail**/
                })
            mapView.addMarkerIndicator(latlng);
        }
    });
});