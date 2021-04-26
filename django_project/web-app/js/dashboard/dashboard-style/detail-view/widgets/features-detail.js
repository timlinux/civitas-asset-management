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
                    let tabs = []
                    for (let idx = 0; idx < this.data.features.length; idx++) {
                        const feature = this.data.features[idx];
                        const ID = feature.properties.feature_id;
                        tabs.push(`
                            <li><a data-toggle="tab" href="#feature-${ID}" class="${idx === 0 ? 'active' : ''}">${ID}</a></li>
                        `)
                        let html = `                            
                                <tr>
                                    <th colspan="2">${feature.id} 
                                        <i class="fa fa-ticket pull-right" 
                                        data-toggle="modal" data-target="#create-ticket-modal" data-feature-id="${ID}" aria-hidden="true"></i>
                                    </th>
                                </tr>`;
                        html += `
                            <tr>
                                <td>ID</td>
                                <td>${ID}</td>
                            </tr>`
                        if (Object.keys(feature.properties).length > 0) {
                            html += `
                                <tr>
                                    <td class="button hidden" colspan="2">Attributes</td>
                                </tr>`;
                        }
                        const keys = Object.keys(feature.properties).sort();
                        $.each(keys, function (value, key) {
                            value = feature.properties[key];
                            if (key !== 'feature_id') {
                                html += `
                                <tr class="extra-property">
                                    <td>${capitalize(key)}</td>
                                    <td>${value ? value : '-'}</td>
                                </tr>`
                            }
                        });
                        htmls.push(`<div id="feature-${ID}" class="tab-pane fade ${idx === 0 ? 'true active show' : ''}"><table>${html}</table></div>`)
                    }
                    this.$content.html(`
                        <ul class="nav nav-tabs">${tabs.join('')}</ul>
                    `);
                    this.$content.append(
                        `<div class="tab-content">${htmls.join('')}</div>`
                    );
                    this.$content.find('table').find('.button').click(function () {
                        $(this).toggleClass('hidden');
                        $(this).toggleClass('expand');
                        $(this).closest('table').find('.extra-property').toggle();
                    })
                    this.$content.find('table').find('.fa-ticket').click(function () {
                        const ID = $(this).data('feature-id');
                        $("#create-ticket-modal").find('select, input, textarea').not('*[name="csrfmiddlewaretoken"]').val('');
                        $('.feature-id-title').html(ID);
                        $('#feature-id-input').val(ID);
                        $('#id_priority').attr('required', true)
                        $('#id_priority').val(3)
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