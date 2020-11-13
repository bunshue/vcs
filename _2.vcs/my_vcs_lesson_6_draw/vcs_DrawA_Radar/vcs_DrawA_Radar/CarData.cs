using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_DrawA_Radar
{
    public class CarData
    {
        public string Name;
        public Color Color;
        public float[] Values;
        public PointF[] Points = null;

        public CarData(string name, Color color,
            params float[] values)
        {
            Name = name;
            Color = color;
            Values = (float[])values.Clone();
        }
    }
}
