using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;
using System.Drawing.Drawing2D;
using System.Xml.Serialization;

namespace vcs_Scribble
{
    public class Polyline
    {
        [XmlIgnore]
        public Color Color = Color.Black;
        public int Thickness = 1;
        public DashStyle DashStyle = DashStyle.Solid;
        public List<Point> Points = new List<Point>();

        // Get or set the color as an ARGB value.
        public int Argb
        {
            get { return this.Color.ToArgb(); }
            set { Color = Color.FromArgb(value); }
        }

        public void Draw(Graphics gr)
        {
            using (Pen the_pen = new Pen(Color, Thickness))
            {
                the_pen.DashStyle = DashStyle;
                if (DashStyle == DashStyle.Custom)
                {
                    the_pen.DashPattern = new float[] { 10, 2 };
                }
                gr.DrawLines(the_pen, Points.ToArray());
            }
        }
    }
}
