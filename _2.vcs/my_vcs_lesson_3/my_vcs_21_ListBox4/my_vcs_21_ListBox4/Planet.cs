using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace my_vcs_21_ListBox4
{
    class Planet
    {
        public string Name = "";
        public string Stats = "";
        public Image Picture = null;

        public Planet(string name, Image picture, string stats)
        {
            Name = name;
            Stats = stats;
            Picture = picture;
        }
    }
}
