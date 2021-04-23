define([
    'leaflet',
    '../style-base',
    '../detail-view/widgets/features-detail'
], function (L, Base, FeaturesDetail) {
    return Base.extend({
        name: 'Detail View',
        lastLayer: null,
        init: function () {
            // create layer
            this.widgets = [new FeaturesDetail()];
        },
        /** Rerender all widgets
         *
         */
        rerenderWidgets: function () {
            const that = this;
            this.widgets.forEach(function (widget) {
                widget.featureSelectedFunction(that.lastLayer);
            });

            // render widgets
            this.renderWidgets();
        }
    });
});