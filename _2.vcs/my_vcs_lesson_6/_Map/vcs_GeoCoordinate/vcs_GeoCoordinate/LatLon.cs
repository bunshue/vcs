using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_GeoCoordinate
{
    public class LatLon
    {
        public string Name, Lat, Lon;
        public LatLon(string name, string lat, string lon)
        {
            Name = name;
            Lat = lat;
            Lon = lon;
        }
        public override string ToString()
        {
            return Name;
        }
    }
}
