using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using System.Drawing;

namespace vcs_Draw9_Example5
{
    class Pentagon
    {
        // Colors.
        private static Random Rand = new Random();
        private static Color[] MyColors =
        {
            Color.Black, Color.Red, Color.Orange,
            Color.Yellow, Color.Lime, Color.LightGreen,
            Color.Cyan, Color.Blue, Color.LightBlue,
            Color.Fuchsia,
        };

        public PointF[] Points = null;
        public Color FillColor = Color.Black;
        public List<Pentagon> Children = new List<Pentagon>();

        // Constructor.
        public Pentagon(PointF[] points)
        {
            Points = points;
            FillColor = MyColors[Rand.Next(0, MyColors.Length)];
            FillColor = Color.FromArgb(128, FillColor);
        }

        // Draw.
        public void Draw(Graphics gr)
        {
            // Draw this Pentagon.
            using (Brush brush = new SolidBrush(FillColor))
            {
                gr.FillPolygon(brush, Points);
            }
            gr.DrawPolygon(Pens.Black, Points);

            // Draw child Pentagons (if any).
            foreach (Pentagon child in Children) child.Draw(gr);
        }
    }
}
