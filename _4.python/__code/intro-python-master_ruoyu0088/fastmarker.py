import folium
import pandas as pd
import numpy as np
from folium.plugins import MarkerCluster

folium.map._default_css[7] = ("awesome_markers_font_css", 
  "https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css")


class FastMarkerCluster(MarkerCluster):
    def __init__(self, data, callback, settings=None):
        from jinja2 import Template
        import json
        super(FastMarkerCluster, self).__init__([])
        self._name = 'Script'
        self._data = data
        if settings is None:
            settings = {}
        self._settings = json.dumps(settings)
        if callable(callback):
            from flexx.pyscript import py2js
            self._callback =  py2js(callback, new_name="callback")
        else:
            self._callback = "var callback = {};".format(_callback)
        
        self._template = Template(u"""
{% macro script(this, kwargs) %}
(function(){
    var data = {{this._data}};
    var map = {{this._parent.get_name()}};
    var cluster = L.markerClusterGroup({{this._settings}});
    {{this._callback}}
    
    for (var i = 0; i < data.length; i++) {
        var row = data[i];
        var marker = callback(row);
        marker.addTo(cluster);
    }
    
    cluster.addTo(map);
})();
{% endmacro %}
            """)
