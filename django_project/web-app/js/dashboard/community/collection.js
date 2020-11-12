define([
    'backbone', './model'], function (Backbone, Community) {
    return Backbone.Collection.extend({
        model: Community,
        url: '/api/community'
    });
});