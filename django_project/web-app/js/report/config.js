let table;
require.config({
    paths: {
        'jquery': '../libs/jquery.js/3.4.1/jquery.min',
        'jqueryUI': '../libs/jquery-ui/1.12.1/jquery-ui',
        'backbone': '../libs/backbone.js/1.4.0/backbone-min',
        'popper': '../libs/bootstrap/4.5.2/popper.min',
        'bootstrap': '../libs/bootstrap/4.5.2/bootstrap.bundle.min',
        'underscore': '../libs/underscore.js/1.9.1/underscore-min',
        'request': '../request',
    },
    shim: {
        bootstrap: {
            deps: ["jquery"]
        },
        jqueryUI: {
            deps: ["jquery"]
        }
    }
});
require([
    'jquery',
    'bootstrap',
    'backbone',
    'underscore',
    'request',
    'view/navigation',
], function ($, bootstrap, Backbone, _, _Request, Navigation) {
    csrfmiddlewaretoken = $('input[name ="csrfmiddlewaretoken"]').val();
    dispatcher = _.extend({}, Backbone.Events);
    Request = new _Request();
    new Navigation();
});