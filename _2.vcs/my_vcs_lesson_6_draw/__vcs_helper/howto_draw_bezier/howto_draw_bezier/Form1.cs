using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_draw_bezier
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The end points are points 0 and 3. 
        // The interior control points are points 1 and 2.
        private PointF[] Points = new PointF[4];

        // The index of the next point to define.
        private int NextPoint = 0;

        // Select a point.
        private void picCanvas_MouseClick(object sender, MouseEventArgs e)
        {
            // If we're starting a new set of four points,
            // get the first point.
            if (NextPoint > 3) NextPoint = 0;

            // Save this point.
            Points[NextPoint].X = e.X;
            Points[NextPoint].Y = e.Y;

            // Move to the next point.
            NextPoint++;

            // Redraw.
            picCanvas.Refresh();
        }

        // Draw the currently selected points. 
        // If we have four points, draw the Bezier curve.
        private void picCanvas_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            e.Graphics.Clear(picCanvas.BackColor);
            if (NextPoint >= 4)
            {
                // Draw the curve.
                e.Graphics.DrawBezier(Pens.Red,
                    Points[0], Points[1], Points[2], Points[3]);
            }

            // Draw the control points.
            for (int i = 0; i < NextPoint; i++)
            {
                e.Graphics.FillRectangle(Brushes.White, Points[i].X - 3, Points[i].Y - 3, 6, 6);
                e.Graphics.DrawRectangle(Pens.Black, Points[i].X - 3, Points[i].Y - 3, 6, 6);
            }
        }
    }
}
