using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_sierpinski_gasket
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // Corner information.
        List<PointF> Corners;

        // The most recent point.
        PointF LastPoint;

        // Draw the Sierpinski gasket.
        private void Form1_Load(object sender, EventArgs e)
        {
            // Define the corners.
            DefineCorners();
        }

        // Start over.
        private void Form1_Resize(object sender, EventArgs e)
        {
            // Define the corners.
            DefineCorners();

            // Clear.
            using (Graphics gr = this.CreateGraphics())
            {
                gr.Clear(this.BackColor);
            }
        }

        // Define the corners.
        private void DefineCorners()
        {
            // Initialize the corners.
            Corners = new List<PointF>();
            Corners.Add(new PointF(this.ClientSize.Width / 2, 10));
            Corners.Add(new PointF(10, this.ClientSize.Height - 10));
            Corners.Add(new PointF(this.ClientSize.Width - 10, this.ClientSize.Height - 10));

            // Start at the first point.
            LastPoint = Corners[0];
        }

        // Add 1000 points to the gasket.
        private void tmrDraw_Tick(object sender, EventArgs e)
        {
            // Draw points.
            Random rand = new Random();
            using (Graphics gr = this.CreateGraphics())
            {
                // Draw the corners.
                foreach (PointF pt in Corners)
                {
                    gr.FillEllipse(Brushes.White, pt.X - 2, pt.Y - 2, 4, 4);
                    gr.DrawEllipse(Pens.Blue, pt.X - 2, pt.Y - 2, 4, 4);
                }

                // Draw 1000 points.
                for (int i = 1; i <= 1000; i++)
                {
                    int j = rand.Next(0, 3);
                    LastPoint = new PointF(
                        (LastPoint.X + Corners[j].X) / 2,
                        (LastPoint.Y + Corners[j].Y) / 2);
                    gr.DrawLine(Pens.Red, LastPoint.X, LastPoint.Y,
                        LastPoint.X + 1, LastPoint.Y + 1);
                }
            }
        }
    }
}
