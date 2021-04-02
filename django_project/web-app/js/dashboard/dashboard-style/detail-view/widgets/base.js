define([
    'underscore',
    '../../widget-base'], function (_, Base) {
    return Base.extend({
        /** Abstract function called when data is presented
         */
        featureSelectedFunction: function (feature) {
            this.featureSelected = feature;
            this.postFeatureSelected()
        },
        /** Abstract function called when the feature selected
         */
        postFeatureSelected: function () {

        },
    });
});