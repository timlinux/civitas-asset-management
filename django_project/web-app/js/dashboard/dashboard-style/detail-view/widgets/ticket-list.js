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
                this.$content.html(
                    '<div class="loading">' +
                    '   <p class="blink">Loading Ticket</p>' +
                    '</div>');
            } else {
                this.$content.html(
                    _.template($('#_please_select_feature').html())
                );
            }

            const that = this;
            if (this.data) {
                const template = _.template($('#_ticket-detail').html())
                this.$content.html('');
                if (this.data.length > 0) {
                    $.each(this.data, function (index, ticket) {
                        ticket['url'] = urls.ticket_detail.replace('/0/', `/${ticket.id}/`)
                        that.$content.append(template(ticket))
                    });
                } else {
                    this.$content.html(
                        '<div class="loading">' +
                        '   <p class="error">No data found</p>' +
                        '</div>')
                }
            }
        },
        /** Abstract function called when the feature selected
         */
        postFeatureSelected: function () {
            if (!this.featureSelected) {
                this.data = null;
                return;
            }
            if (this.request) {
                this.request.abort()
            }
            this.render();
            const that = this;
            this.request = Request.get(
                urls.feature_ticket_list.replace('/0/', `/${this.featureSelected.feature.id}/`),
                {},
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