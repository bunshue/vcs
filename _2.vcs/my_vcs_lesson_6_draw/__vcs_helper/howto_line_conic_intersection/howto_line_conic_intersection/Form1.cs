using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace howto_line_conic_intersection
{
    public partial class Form1 : Form
    {
        private List<PointF> MousePoints = new List<PointF>();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        // Save a point.
        private void picGraph_MouseClick(object sender, MouseEventArgs e)
        {
            if (MousePoints.Count == 10)
            {
                MousePoints = new List<PointF>();
            }

            // Save the point.
            MousePoints.Add(e.Location);
            richTextBox1.Text += "滑鼠按鍵   " + e.Location.ToString() + " 共有 " + MousePoints.Count.ToString() + " 點\n";

            // Redraw.
            DrawGraph();
        }

        // Draw the conic section.
        private void Form1_Resize(object sender, EventArgs e)
        {
            DrawGraph();
        }

        // Draw the conic section.
        private void DrawGraph()
        {
            Bitmap bm = new Bitmap(picGraph.ClientSize.Width, picGraph.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.Clear(picGraph.BackColor);
                gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Draw the points.
                const float radius = 30;
                foreach (PointF pt in MousePoints)
                {
                    gr.DrawEllipse(Pens.Blue, pt.X - radius, pt.Y - radius, 2 * radius, 2 * radius);
                }

                //e.Graphics.DrawLines(Pens.Black, points.ToArray());
                if (MousePoints.Count > 1)
                {
                    gr.DrawLines(Pens.Black, MousePoints.ToArray());
                }
            }
            // Display the result.
            picGraph.Image = bm;
        }
    }
}
