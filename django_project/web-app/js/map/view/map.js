define([
    'backbone',
    'jquery',
    'view/basemap',
    'view/layer/system'
], function (
    Backbone, $, Basemap, System) {
    return Backbone.View.extend({
        initBounds: [[-25.232732932266735, 93.85489258365217], [19.985307983544566, 142.16236486638226]],
        initialize: function () {
            // listeners
            this.listenTo(dispatcher, 'map:pan', this.panTo);

            // constructor
            this.map = L.map('map').fitBounds(this.initBounds);
            new Basemap(this);

            // initiate layers
            this.getSystems('water')
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
        /** Getting systems from API
         * @param assetClass = the name of asset class
         *  - water
         *  - box
         *  TODO:
         *   make API return all of assets
         */
        getSystems: function (assetClass) {
            const url = `/amlit/${assetClass}/api/system/`;
            Request.get(
                url, {}, null,
                /** SUCCESS **/
                function (systems) {
                    let firstID = null;
                    $.each(systems, function (index, system) {
                        dispatcher.trigger('side-panel:add-system', system);
                        new System(system);
                        firstID = firstID ? firstID : system.id;
                    });
                    dispatcher.trigger('side-panel:render');
                    dispatcher.trigger(`system:click-${firstID}`);
                }
            )
        }
    });
});