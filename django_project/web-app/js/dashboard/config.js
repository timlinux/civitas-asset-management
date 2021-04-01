let map;

require.config({
    paths: {
        'jquery': '../../libs/jquery.js/3.4.1/jquery.min',
        'jqueryUI': '../../libs/jquery-ui/1.12.1/jquery-ui',
        'backbone': '../../libs/backbone.js/1.4.0/backbone-min',
        'leaflet': '../../libs/leaflet/1.5.1/leaflet-src',
        'underscore': '../../libs/underscore.js/1.9.1/underscore-min',
        'leafletDraw': '../../libs/leaflet.draw/1.0.4/leaflet.draw'
    },
    shim: {
        leaflet: {
            exports: ['L']
        },
        jqueryUI: {
            deps: ["jquery"]
        },
        rangeSlider: {
            deps: ["jquery"]
        },
        leafletDraw: {
            deps: ['leaflet'],
            exports: 'LeafletDraw'
        },
    }
});
require([
    'jquery',
    'backbone',
    'underscore',
    'leaflet',
    'leafletDraw',
    'map',
    '../event',
    '../request',
    'dashboard-style/controller',
    'side-panel/controller',
    'community/controller',
    'system/controller',
], function (
    $, Backbone, _, L, LDraw, Map, _Event, _Request,
    DashboardStyleController, SidePanelController, CommunityConstroller, SystemConstroller) {
    csrfmiddlewaretoken = $('input[name ="csrfmiddlewaretoken"]').val();
    event = new _Event();
    Request = new _Request();

    // initiate all view
    let mapiew = new Map();
    map = mapiew.map;

    // init system/community controller
    new DashboardStyleController();
    new CommunityConstroller();
    new SystemConstroller();
    new SidePanelController();
});