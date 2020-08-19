define([
    'backbone',
    'jquery',
    'jqueryUI'
], function (Backbone, $, $ui) {
    return Backbone.View.extend({
        initialize: function () {
            this.listenTo(dispatcher, 'side-panel:render', this.render);
            this.listenTo(dispatcher, 'side-panel:add-system', this.addSystem);
            this.listenTo(dispatcher, 'side-panel:add-system-property', this.addSystemProperty);
            this.$el = $('#side-panel');
            this.$systemList = $("#system-list");
        },
        /** Make system list as accordion */
        render: function () {
            this.$systemList.show();
            this.$systemList.accordion();
            $('.system-header').click(function () {
                dispatcher.trigger(`system:click-${$(this).data('system-id')}`)
            })
        },
        /** Render system accordion */
        addSystem: function (data) {
            let template = _.template($('#_system').html());
            this.$systemList.append(template(data));
        },
        addSystemProperty: function (systemID, key, value) {
            $(`#system-${systemID} table`).append(
                '<tr>' +
                `   <td>${key.capitalize().replaceAll('_', ' ')}</td>` +
                `   <td>${value}</td>` +
                '</tr>')
        }

    });
});