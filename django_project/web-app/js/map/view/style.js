define([
    'backbone', 'leaflet'], function (Backbone, L) {
    return Backbone.View.extend({
        initialize: function () {
            this.renderLegend()
        },
        /** Return style by subClass, e.g: hydrant, box, valve, etc
         * @param subClass
         * TODO:
         *  The style returns from API
         *  do we need per asset sub class
         */
        styles: {
            'hydrants': {
                iconUrl: 'static/img/hydrant.png',
                iconSize: [20, 20], // size of the icon
            },
            'boxes': {
                color: "#ff0000",
                weight: 1,
                opacity: 0.4,
                fillOpacity: 0.4,
                type: 'Point'
            },
            'chambers': {
                color: "#ff0000",
                weight: 1,
                fillColor: "#ff0000",
                fillOpacity: 0.4,
                radius: 5,
                type: 'Polygon'
            },
            'meters': {
                color: "#345",
                weight: 1,
                fillColor: "#345",
                fillOpacity: 0.4,
                radius: 5,
                type: 'Point'
            },
            'pipes': {
                color: "#3a3",
                weight: 4,
                type: 'Line'
            }
        },
        /** Return style based on the name of sub class
         * @param name = sub class name
         * @returns {*}
         */
        get: function (name) {
            let style = this.styles[name];
            if (style) {
                if (style.iconUrl) {
                    return {
                        icon: L.icon(style)
                    }
                }
            }
            return this.styles[name]
        },
        /** Render Legend
         */
        renderLegend: function () {
            let html = '<table>'
            $.each(this.styles, function (name, style) {
                if (style.iconUrl) {
                    style = `<img src="${style.iconUrl}">`
                } else {
                    style = `<div class="${style.type}" style="background: ${style.color}"></div>`
                }
                html += '' +
                    '<tr>' +
                    `   <td>${style}</td>` +
                    `   <td>${name.capitalize()}</td>` +
                    '</tr>'

            })
            html += '</table>'
            $('#legend').html(html)
        }
    });
});