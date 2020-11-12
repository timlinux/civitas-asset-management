define([
    'backbone', './collection'], function (Backbone, Community) {
    return Backbone.View.extend({
        community: null,
        el: '#community',
        initialize: function () {
            const that = this;
            const $ul = that.$el.find('ul');
            this.$el.find('.selection').click(function () {
                $ul.slideToggle('fast');
            })
            this.collection = new Community();
            this.collection.fetch({
                success: function () {
                    if (that.collection.models.length > 0) {

                        that.collection.models.forEach(function (model) {
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
                        })
                        $($ul.find('li')[0]).click();
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
        },
    });
});