define([
    './base',
    '../widget/consequence-of-failure-donut-graph'], function (Base, ConsequenceOfFailureDonutGraph) {
    return Base.extend({
        name: 'Prioritization View',
        initialize: function () {
            this.widgets = [new ConsequenceOfFailureDonutGraph()];
            this.listener();
        },
        /**
         *  This is function that called after render
         */
        rendered: function () {
            const that = this;
            this.widgets.forEach(function (widget) {
                widget.updateData('coming soon');
                if (that.active) {
                    widget.render()
                }
            });
        },
    });
});