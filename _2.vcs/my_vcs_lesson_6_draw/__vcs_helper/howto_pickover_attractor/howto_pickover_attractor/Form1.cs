using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_pickover_attractor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The plane we should project on.
        private enum Plane
        {
            XY,
            YZ,
            XZ,
        }
        private Plane SelectedPlane;

        // The Bitmap and Graphics object.
        private Bitmap bm;
        private Graphics gr;

        // Drawing size variables.
        private int wid, hgt;
        private double xoff, yoff, zoff, xscale, yscale, zscale;

        // Drawing parameters.
        private double A, B, C, D, E, X0, Y0, Z0;

        // The colors.
        Color BgColor, FgColor;

        // Start with the first plane selected.
        private void Form1_Load(object sender, EventArgs e)
        {
            cboPlane.SelectedIndex = 0;
            SelectedPlane = Plane.XY;
        }

        // Let the user pick a new color.
        private void ColorSample_Click(object sender, EventArgs e)
        {
            Label lbl = sender as Label;
            cdColor.Color = lbl.BackColor;
            if (cdColor.ShowDialog() == DialogResult.OK)
            {
                lbl.BackColor = cdColor.Color;
            }
        }

        // Start or stop drawing.
        bool Running = false;
        private void btnStart_Click(object sender, EventArgs e)
        {
            if (Running)
            {
                Running = false;
                btnStart.Text = "Stopped";
            }
            else
            {
                Running = true;
                btnStart.Text = "Stop";
                DrawCurve();
                btnStart.Text = "Go";
            }
        }

        // Draw the curve.
        private void DrawCurve()
        {
            // Get the parameters and otherwise get ready.
            Prepare();

            // Start drawing.
            double x = X0, y = Y0, z = Z0;
            while (Running)
            {
                // Plot a bunch of points.
                for (int i = 1; i<=1000; i++)
                {
                    // Move to the next point.
                    double x2 = Math.Sin(A * y) - z * Math.Cos(B * x);
                    double y2 = z * Math.Sin(C * x) - Math.Cos(D * y);
                    z = Math.Sin(x);
                    x = x2;
                    y = y2;

                    // Plot the point.
                    switch (SelectedPlane)
                    {
                        case Plane.XY:
                            bm.SetPixel((int)(x * xscale + xoff), (int)(y * yscale + yoff), FgColor);
                            break;
                        case Plane.YZ:
                            bm.SetPixel((int)(y * yscale + yoff), (int)(z * zscale + zoff), FgColor);
                            break;
                        case Plane.XZ:
                            bm.SetPixel((int)(x * xscale + xoff), (int)(z * zscale + zoff), FgColor);
                            break;
                    }
                }

                // Refresh.
                picCanvas.Refresh();

                // Check events to see if the user clicked Stop.
                Application.DoEvents();
            }
        }

        // Get ready to draw.
        private void Prepare()
        {
            // Get the colors.
            BgColor = lblBackColor.BackColor;
            FgColor = lblForeColor.BackColor;

            // Make the Bitmap and Graphics object.
            wid = picCanvas.ClientSize.Width;
            hgt = picCanvas.ClientSize.Height;
            bm = new Bitmap(wid, hgt);
            gr = Graphics.FromImage(bm);
            gr.Clear(BgColor);
            picCanvas.Image = bm;

            // Calculate scaling parameters.
            const double XMIN = -2.1;
            const double XMAX = 2.1;
            const double YMIN = -2.1;
            const double YMAX = 2.1;
            const double ZMIN = -1.2;
            const double ZMAX = 1.2;
            SelectedPlane = (Plane)cboPlane.SelectedIndex;
            switch (SelectedPlane)
            {
                case Plane.XY:
                    xoff = wid / 2;
                    yoff = hgt / 2;
                    xscale = wid / (XMAX - XMIN);
                    yscale = hgt / (YMAX - YMIN);
                    break;
                case Plane.YZ:
                    yoff = wid / 2;
                    zoff = hgt / 2;
                    yscale = wid / (YMAX - YMIN);
                    zscale = hgt / (ZMAX - ZMIN);
                    break;
                case Plane.XZ:
                    xoff = wid / 2;
                    zoff = hgt / 2;
                    xscale = wid / (XMAX - XMIN);
                    zscale = hgt / (ZMAX - ZMIN);
                    break;
            }

            // Get the parameters.
            if (double.TryParse(txtA.Text, out A)) A = 2.0;
            if (double.TryParse(txtB.Text, out B)) B = 0.5;
            if (double.TryParse(txtC.Text, out C)) C = -0.6;
            if (double.TryParse(txtD.Text, out D)) D = -2.5;
            if (double.TryParse(txtE.Text, out E)) E = 1.0;
            if (double.TryParse(txtX0.Text, out X0)) X0 = 0.0;
            if (double.TryParse(txtY0.Text, out Y0)) Y0 = 0.0;
            if (double.TryParse(txtZ0.Text, out Z0)) Z0 = 0.0;
        }

        // Adjust for the new size.
        private void picCanvas_Resize(object sender, EventArgs e)
        {
            Prepare();
        }
    }
}
