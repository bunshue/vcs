using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_Draw9_Example5
{
    class Octagon
    {
        // Colors.
        private static Random Rand = new Random();
        private static Color[] MyColors =
        {
            Color.Aquamarine, Color.Red, Color.Orange,
            Color.Yellow, Color.SeaShell, Color.RosyBrown,
            Color.Cyan, Color.Blue, Color.LightBlue,
            Color.Fuchsia, Color.Beige, Color.BlueViolet, Color.Orange,
        };

        public PointF[] Points = null;
        public Color FillColor = Color.Black;
        public List<Octagon> Children = new List<Octagon>();

        // Constructor.
        public Octagon(PointF[] points)
        {
            Points = points;
            FillColor = MyColors[Rand.Next(0, MyColors.Length)];
            FillColor = Color.FromArgb(80, FillColor);
        }

        // Draw.
        public void Draw(Graphics gr)
        {
            // Draw this Octagon.
            using (Brush brush = new SolidBrush(FillColor))
            {
                gr.FillPolygon(brush, Points);
            }
            gr.DrawPolygon(Pens.Black, Points);

            // Draw child Octagons (if any).
            foreach (Octagon child in Children) child.Draw(gr);
        }
    }
}
