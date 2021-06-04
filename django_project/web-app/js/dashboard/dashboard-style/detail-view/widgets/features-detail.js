define([
    'underscore',
    '../../widget-base'], function (_, Base) {
    return Base.extend({
        id: 'features-detail',
        name: 'Features',
        featuresGeometry: {},
        featuresSelected: [],
        styles: {
            marker: {
                radius: 6,
                fillColor: "#0F0",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 1
            },
            nonMarker: {
                fillOpacity: 1,
                color: "#0F0",
                weight: 5,
                opacity: 1
            },
            highlightMarker: {
                radius: 6,
                fillColor: "#F00",
                color: "#000",
                weight: 1,
                opacity: 1,
                fillOpacity: 1
            },
            highlightNonMarker: {
                fillOpacity: 1,
                color: "#F00",
                weight: 5,
                opacity: 1
            }
        },
        highlightID: null,
        highlightGeom: null,
        /** Abstract function called when data is presented
         */
        postRender: function () {
            const that = this;
            if (this.data) {
                if (this.data.features.length > 0) {
                    let htmls = [];
                    let tabs = []
                    this.featuresSelected = [];
                    for (let idx = 0; idx < this.data.features.length; idx++) {
                        const feature = this.data.features[idx];
                        const ID = feature.properties.feature_id;
                        this.featuresSelected.push(ID);
                        tabs.push(`
                            <li><a data-toggle="tab" data-id="${ID}" href="#feature-${ID}" class="${idx === 0 ? 'active' : ''}">${ID}</a></li>
                        `)
                        let html = `                            
                                <tr>
                                    <th colspan="2">
                                        <div class="feature-header">${feature.id.replaceAll('_', ' ')}
                                            <div class="feature-title"></div> 
                                        </div>
                                    </th>
                                </tr>                          
                                <tr class="feature-create-ticket-row">
                                    <td colspan="2">                                        
                                        <div class="feature-create-ticket" data-toggle="modal" data-target="#create-ticket-modal" data-feature-id="${ID}" >
                                            <i class="fa fa-ticket" aria-hidden="true"></i>
                                            Create ticket
                                        </div>
                                    </td>
                                </tr>`;
                        html += `
                            <tr>
                                <td>ID</td>
                                <td>${ID}</td>
                            </tr>`
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
                        htmls.push(
                            `<div id="feature-${ID}" class="tab-pane fade ${idx === 0 ? 'true active show' : ''}"><table>${html}</table></div>`
                        )

                        // --------------------------------
                        // save the geometry
                        // --------------------------------
                        // TODO :
                        //  We need to use from GFI
                        if (!this.featuresGeometry[ID]) {
                            Request.get(
                                urls.feature_detail.replaceAll('999', ID),
                                [],
                                null,
                                function (data) {
                                    if (!that.featuresGeometry[ID]) {
                                        that.featuresGeometry[ID] = {
                                            'data': data,
                                            'geom': L.geoJSON(data, {
                                                pointToLayer: function (feature, latlng) {
                                                    return L.circleMarker(latlng, that.styles.marker);
                                                },
                                                style: function (feature) {
                                                    switch (feature.geometry.type) {
                                                        case 'Point':
                                                            return {};
                                                        default:
                                                            return that.styles.nonMarker

                                                    }
                                                }
                                            })
                                        };
                                        if (that.featuresSelected.includes(ID)) {
                                            event.trigger(
                                                evt.MAP_ADD_OVERLAY_FEATURE,
                                                that.featuresGeometry[ID].geom
                                            );
                                            if (idx === 0) {
                                                that.featureSelected(ID);
                                            }
                                        }
                                    }
                                },
                                function () {
                                    /**fail**/
                                })
                        } else {
                            if (that.featuresSelected.includes(ID)) {
                                event.trigger(
                                    evt.MAP_ADD_OVERLAY_FEATURE,
                                    that.featuresGeometry[ID].geom
                                );
                                if (idx === 0) {
                                    that.featureSelected(ID);
                                }
                            }
                        }
                    }
                    this.$content.html(`
                        <ul class="nav nav-tabs">${tabs.join('')}</ul>
                    `);
                    this.$content.append(
                        `<div class="tab-content">${htmls.join('')}</div>`
                    );
                    this.$content.find('table').find('.feature-create-ticket').click(function () {
                        const ID = $(this).data('feature-id');
                        $("#create-ticket-modal").find('select, input, textarea').not('*[name="csrfmiddlewaretoken"]').val('');
                        $('.feature-id-title').html(ID);
                        $('#feature-id-input').val(ID);
                        $('#id_priority').attr('required', true)
                        $('#id_priority').val(3)
                    })
                    this.$content.find('.nav-tabs a').click(function () {
                        that.featureSelected($(this).data('id'));
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
        /***
         * When feature selected, highlight it to map
         */
        featureSelected: function (ID) {
            const that = this;
            if (this.highlightGeom) {
                event.trigger(
                    evt.MAP_REMOVE_OVERLAY_FEATURE,
                    this.highlightGeom
                );
            }

            this.highlightID = ID;
            if (this.featuresGeometry[ID]) {
                this.highlightGeom = L.geoJSON(this.featuresGeometry[ID].data, {
                        pointToLayer: function (feature, latlng) {
                            return L.circleMarker(latlng, that.styles.highlightMarker);
                        },
                        style: function (feature) {
                            switch (feature.geometry.type) {
                                case 'Point':
                                    return {};
                                default:
                                    return that.styles.highlightNonMarker

                            }
                        }
                    }
                );
                event.trigger(
                    evt.MAP_ADD_OVERLAY_FEATURE,
                    this.highlightGeom
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
                SRS: 'EPSG:4326',
                HEIGHT: size.y,
                WIDTH: size.x,
                QUERY_LAYERS: QGISLayers.join(','),
                INFO_FORMAT: 'application/json',
                i: Math.floor(point.x),
                j: Math.floor(point.y)
            };

            // get the featureinfo
            if (this.request) {
                this.request.abort()
            }
            this.$content.html(
                _.template($('#_loading').html())
            );
            event.trigger(evt.MAP_REMOVE_ALL_OVERLAY_FEATURE);
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
        }
    });
});