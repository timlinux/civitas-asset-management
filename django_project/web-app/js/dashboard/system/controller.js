define([
    'backbone'], function (Backbone) {
    return Backbone.View.extend({
        system: null,
        systems: {},
        el: '#system',
        initialize: function () {
            const that = this;
            const $ul = that.$el.find('ul');
            this.$el.find('.selection').click(function () {
                $ul.slideToggle('fast');
            })
            event.register(this, evt.COMMUNITY_CHANGE, this.communityChanged)
        },
        /** when community changes, system changed too **/
        communityChanged: function (community) {
            const that = this;
            const $ul = that.$el.find('ul');
            const $name = that.$el.find('.name');
            const $description = that.$el.find('.description');
            $ul.html('')
            $name.html('');
            $description.html('');
            this.systems = {};

            this.$el.slideDown('fast')
            if (!community) {
                return
            }

            // render system list
            if (community.get('systems').length === 0) {
                this.$el.slideUp('fast')
            } else {
                community.get('systems').forEach(function (system) {
                    $ul.append(`
                        <li>
                            <input type="checkbox" value="${system.id}" checked>${system.name}
                            <div class="description">${system.description}</div>
                        </li>`
                    )
                    that.systems[system.id] = system;
                });
                $ul.find('input').change(function () {
                    that.systemChanged()
                })

                // remove loading and show the list
                this.$el.find('.fa-spinner').remove();
                this.$el.find('.detail').show();
            }
            that.systemChanged();
        },
        /** When system changed **/
        systemChanged: function () {
            let ids = [];
            $(this.$el.find('input:checked')).each(function () {
                ids.push($(this).val());
            });
            event.trigger(evt.SYSTEM_CHANGE, ids);
        }

    });
});