define([
    'backbone',
    'leaflet',
    './collection'], function (Backbone, L, Community) {
    return Backbone.View.extend({
        community: null,
        layer: null,
        el: '#community',
        initialize: function () {
            const that = this;
            const $ul = that.$el.find('ul');
            this.$el.find('.selection').click(function () {
                $ul.slideToggle('fast');
            });

            // create layer
            // add community layer
            this.layer = L.geoJSON(null, {
                fillOpacity: 0,
                "color": "#f44a52",
                "weight": 2,
                "opacity": 1
            });
            event.trigger(evt.MAP_ADD_LAYER, this.layer);
            event.register(this, evt.COMMUNITY_GEOJSON_CHANGE, this.communityGeojsonChanged);

            // fetch community
            this.collection = new Community();
            this.collection.fetch({
                success: function () {
                    if (that.collection.models.length > 0) {
                        let defaultCommunity = 0;
                        that.collection.models.forEach(function (model, idx) {
                            if (user.communityID) {
                                if (model.id === user.communityID) {
                                    defaultCommunity = idx;
                                }
                            }
                            $ul.append(`<li value="${model.id}">${model.get('name')}</li>`)
                        });

                        // remove loading and show the list
                        that.$el.find('.fa-spinner').remove();
                        that.$el.find('.detail').show();

                        // onclick list
                        $ul.find('li').click(function () {
                            if (that.collection.get($(this).val()) !== that.community) {
                                that.change(that.collection.get($(this).val()))
                            }
                        });
                        console.log(defaultCommunity)
                        $($ul.find('li')[defaultCommunity]).click();
                        $ul.hide();
                    }
                }
            })
        },
        /** Change community **/
        change: function (community) {
            this.community = community;
            this.$el.find('.name').html(community.get('name'));
            this.$el.find('.region').html(community.get('region'));
            this.$el.find('.province').html(community.get('province'));
            event.trigger(evt.COMMUNITY_CHANGE, null);
            community.selected();
            setCookie('community', community.id);
        },
        /** Called when the geojson has changed
         * @param geojson
         */
        communityGeojsonChanged: function (geojson) {
            this.layer.clearLayers();
            this.layer.addData(geojson);
            event.trigger(evt.MAP_FLY, this.layer.getBounds());
        },
    });
});