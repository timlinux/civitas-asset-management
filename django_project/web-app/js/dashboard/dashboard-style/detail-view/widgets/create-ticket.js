define([
    'underscore',
    '../widgets/base'], function (_, Base) {
    return Base.extend({
        id: 'create-ticket',
        name: 'Create Ticket',
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
        }
    });
});