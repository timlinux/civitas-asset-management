define([
    'underscore',
    '../../widget-base'], function (_, Base) {
    return Base.extend({
        id: 'widget-ticket',
        name: 'Tickets',
        icon: 'fa-ticket',
        data: null,
        init: function () {
            event.register(this, evt.COMMUNITY_CHANGE, this.communityChanged);

            // get ticket list
            const that = this;
            if (this.request) {
                this.request.abort()
            }
            this.request = Request.get(
                urls.ticket_list,
                {},
                null,
                function (data) {
                    console.log(data)
                    that.data = data;
                    that.render();
                },
                function () {
                    /**fail**/
                })
        },
        communityChanged(community) {
            // TODO:
            //  show the ticket by selected community
        },
        postRender: function () {
            const that = this;
            if (this.data) {
                for (let idx = 0; idx < this.data.length; idx++) {
                    const ticket = this.data[idx];
                    that.$el.append(`
                        <a class="ticket-row" href="${urls.ticket_detail.replaceAll(0, ticket.id)}" target="_blank">
                            <div style="margin-bottom: 5px">
                                <b>${ticket.ticket}</b>                                
                            </div>
                            <div>
                               ${ticket.description}
                            </div>
                            <div class="created">${ticket.created}</div>
                        </a>
                    `)
                }
            }
        },
    });
});