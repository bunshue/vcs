using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_pickover_popcorn
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The bitmap.
        private Bitmap Bm;

        // Parameters;
        private int IterationsPerPixel;
        private float H;

        // Make a bitmap of the appropriate size.
        private void Form1_Load(object sender, EventArgs e)
        {
            picCanvas.ClientSize = new Size((int)Dxmax, (int)Dymax);

            Bm = new Bitmap(picCanvas.ClientSize.Width, picCanvas.ClientSize.Height);
            picCanvas.Image = Bm;
        }

        // Plot a bunch of points.
        private void btnPlotAll_Click(object sender, EventArgs e)
        {
            GetParameters();

            // Make a new bitmap.
            Bm = new Bitmap(picCanvas.ClientSize.Width, picCanvas.ClientSize.Height);
            picCanvas.Image = Bm;

            // Plot a series for each point.
            int dx = int.Parse(txtDx.Text);
            for (int x = 0; x < Bm.Width; x += dx)
            {
                for (int y = 0; y < Bm.Height; y += dx)
                {
                    PlotPoints(Bm, H, x, y, IterationsPerPixel);
                }
                picCanvas.Refresh();
            }
            picCanvas.Refresh();
        }

        // Clear.
        private void btnClear_Click(object sender, EventArgs e)
        {
            // Make a new bitmap.
            Bm = new Bitmap(picCanvas.ClientSize.Width, picCanvas.ClientSize.Height);
            picCanvas.Image = Bm;
            picCanvas.Refresh();
        }

        // Plot points for the clicked pixel.
        private void picCanvas_MouseClick(object sender, MouseEventArgs e)
        {
            GetParameters();

            // Plot the point's series.
            PlotPoints(Bm, H, e.X, e.Y, IterationsPerPixel);
            picCanvas.Refresh();
        }

        // Get the parameters.
        private void GetParameters()
        {
            IterationsPerPixel = int.Parse(txtIterationsPerPixel.Text);
            H = float.Parse(txtH.Text);
        }

        // Plot points for a pixel using the equations:
        //      x(n + 1) = x(n) - h * Sin(y(n) + Tan(3 * y(n)))
        //      y(n + 1) = y(n) - h * Sin(x(n) + Tan(3 * x(n)))
        private void PlotPoints(Bitmap bm, float h, int pix_x, int pix_y, int iterations)
        {
            // Convert the first point to world coordinates.
            float wx, wy;
            DeviceToWorld(pix_x, pix_y, out wx, out wy);

            // Plot points.
            bm.SetPixel(pix_x, pix_y, Color.Blue);
            for (int i = 0; i < iterations; i++)
            {
                float new_x = (float)(wx - h * Math.Sin(wy + Math.Tan(3 * wy)));
                float new_y = (float)(wy - h * Math.Sin(wx + Math.Tan(3 * wx)));
                wx = new_x;
                wy = new_y;

                WorldToDevice(wx, wy, out pix_x, out pix_y);
                if (pix_x >= 0 && pix_x < bm.Width &&
                    pix_y >= 0 && pix_y < bm.Height)
                {
                    bm.SetPixel(pix_x, pix_y, Color.Red);
                }
            }
        }

        // Convert between world and device coordinates.
        private const float Wxmin = -4.0f;
        private const float Wxmax = 4.0f;
        private const float Wymin = -3.0f;
        private const float Wymax = 3.0f;
        private const float Wwid = (Wxmax - Wxmin);
        private const float Whgt = (Wymax - Wymin);
        private const float Dxmin = 0f;
        private const float Dxmax = 600f;
        private const float Dymin = 0f;
        private const float Dymax = 500f;
        private const float Dwid = (Dxmax - Dxmin);
        private const float Dhgt = (Dymax - Dymin);
        private void WorldToDevice(float wx, float wy, out int dx, out int dy)
        {
            dx = (int)(Dxmin + Dwid * (wx - Wxmin) / Wwid);
            dy = (int)(Dymin + Dhgt * (wy - Wymin) / Whgt);
        }
        private void DeviceToWorld(int dx, int dy, out float wx, out float wy)
        {
            wx = Wxmin + Wwid * (dx - Dxmin) / Dwid;
            wy = Wymin + Whgt * (dy - Dymin) / Dhgt;
        }
    }
}
