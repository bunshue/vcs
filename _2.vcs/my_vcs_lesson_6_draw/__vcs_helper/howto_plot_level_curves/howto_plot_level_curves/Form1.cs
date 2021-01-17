using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_plot_level_curves
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The function type.
        private delegate float FofXY(float x, float y);

        // Draw level curves for this function.
        private void DrawLevelCurves(FofXY func, float zmin, float zmax, float dz)
        {
            this.Cursor = Cursors.WaitCursor;

            // Make the Bitmap.
            Bitmap bm = new Bitmap(picGraph.ClientSize.Width, picGraph.ClientSize.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // Clear.
                gr.Clear(Color.White);
                gr.ScaleTransform(24f, -24f, System.Drawing.Drawing2D.MatrixOrder.Append);
                gr.TranslateTransform(bm.Width * 0.5f, bm.Height * 0.5f,
                    System.Drawing.Drawing2D.MatrixOrder.Append);

                // Draw axes.
                using (Pen axis_pen = new Pen(Color.Gray, 0))
                {
                    gr.DrawLine(axis_pen, -6, 0, 6, 0);
                    gr.DrawLine(axis_pen, 0, -6, 0, 6);
                    for (int i = -6; i <= 6; i++)
                    {
                        gr.DrawLine(axis_pen, i, -0.1f, i, 0.1f);
                        gr.DrawLine(axis_pen, -0.1f, i, 0.1f, i);
                    }
                }

                // Draw the level curves.
                float dx = 2f / bm.Width;
                float dy = 2f / bm.Height;
                for (float z = zmin; z <= zmax; z += dz)
                {
                    DrawLevelCurve(gr, func, z, dx, dy);
                }
            } // using gr.

            // Display the result.
            picGraph.Image = bm;
            this.Cursor = Cursors.Default;
        }

        // Plot a function.
        private void DrawLevelCurve(Graphics gr, FofXY func, float z, float dx, float dy)
        {
            // Console.WriteLine("z = " + z.ToString());

            // Plot the function.
            using (Pen thin_pen = new Pen(Color.Black, 0))
            {
                // Red for z < 0, blue for z > 0.
                if (z < 0)
                {
                    thin_pen.Color = Color.Red;
                }
                else if (z > 0)
                {
                    thin_pen.Color = Color.Blue;
                }

                // Horizontal comparisons.
                for (float x = -6f; x <= 6f; x += dx)
                {
                    float last_y = z - func(x, -6f);
                    for (float y = -6f + dy; y <= 6f; y += dy)
                    {
                        float next_y = z - func(x, y);
                        if (
                            ((last_y <= 0f) && (next_y >= 0f)) ||
                            ((last_y >= 0f) && (next_y <= 0f))
                           )
                        {
                            // Plot this point.
                            gr.DrawLine(thin_pen, x, y - dy, x, y);
                        }
                        last_y = next_y;
                    }
                } // Horizontal comparisons.

                // Vertical comparisons.
                for (float y = -6f + dy; y <= 6f; y += dy)
                {
                    float last_x = z - func(-6f, y);
                    for (float x = -6f; x <= 6f; x += dx)
                    {
                        float next_x = z - func(x, y);
                        if (
                            ((last_x <= 0f) && (next_x >= 0f)) ||
                            ((last_x >= 0f) && (next_x <= 0f))
                           )
                        {
                            // Plot this point.
                            gr.DrawLine(thin_pen, x - dx, y, x, y);
                        }
                        last_x = next_x;
                    }
                } // Vertical comparisons.
            } // using thin_pen.
        }

        // Bowl.
        private float F1(float x, float y)
        {
            return x * x + (y * 2) * (y * 2) - 75;
        }

        // Monkey saddle.
        private float F2(float x, float y)
        {
            return x * (x * x - 3 * y * y);
        }

        // Crossed trough.
        private float F3(float x, float y)
        {
            return x * x * y * y;
        }

        // Hemisphere.
        private float F4(float x, float y)
        {
            return (float)Math.Sqrt(25 - (x * x + y * y));
        }

        // Bowl.
        private void radF1_Click(object sender, EventArgs e)
        {
            DrawLevelCurves(F1, -75, 65, 20);
        }

        private void radF2_Click(object sender, EventArgs e)
        {
            DrawLevelCurves(F2, -200, 200, 40);
        }

        private void radF3_Click(object sender, EventArgs e)
        {
            DrawLevelCurves(F3, 0, 800, 100);
        }

        private void radF4_Click(object sender, EventArgs e)
        {
            DrawLevelCurves(F4, 0, 5, 0.75f);
        }
    }
}
