define([
    'underscore',
    '../widgets/base'], function (_, Base) {
    return Base.extend({
        id: 'ticket-list',
        name: 'Ticket List',
        /** Abstract function called when data is presented
         */
        postRender: function () {
            if (this.featureSelected) {
                const template = _.template($('#_create-ticket').html())
                this.$content.html(
                    template({
                        id: this.featureSelected.feature.id
                    })
                );
            } else {
                this.$content.html(
                    _.template($('#_please_select_feature').html())
                );
            }
        },
        /** Abstract function called when the feature selected
         */
        postFeatureSelected: function () {
            if (this.featureSelected) {
                this.data = null;
                return;
            }
            if (this.request) {
                this.request.abort()
            }
            this.request = Request.get(
                urls.feature_ticket_list.replace('/0/', `/${this.featureSelected.id}/`),
                {
                    'systems': systems.join(',')
                },
                null,
                function (geojson) {
                    /** success **/
                    that.layer.addData(geojson);
                },
                function () {
                    /**fail**/
                })
        }
    });
});