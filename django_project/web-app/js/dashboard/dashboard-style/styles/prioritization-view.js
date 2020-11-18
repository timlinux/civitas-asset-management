define([
    './base',
    '../widget/consequence-of-failure-donut-graph'], function (Base, ConsequenceOfFailureDonutGraph) {
    return Base.extend({
        name: 'Prioritization View',
        data: 'coming soon',
        init: function () {
            this.widgets = [new ConsequenceOfFailureDonutGraph()];
        }
    });
});