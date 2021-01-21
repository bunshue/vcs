using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace howto_strange_attractor
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private Bitmap Bm;
        private double[] A = new double[12];
        private double X, Y, Wxmin, Wxmax, Wymin, Wymax, Wwid, Whgt;
        private double Wid, Hgt;

        // Select initial coefficients.
        private void Form1_Load(object sender, EventArgs e)
        {
            cboCoefficients.SelectedIndex = 0;
            StartNewImage();
        }

        // Plot 1,000 points.
        private void tmrDrawPoint_Tick(object sender, EventArgs e)
        {
            for (int i = 1; i <= 1000; i++)
            {
                double new_x = A[0] + A[1] * X + A[2] * X * X + A[3] * X * Y + A[4] * Y + A[5] * Y * Y;
                double new_y = A[6] + A[7] * X + A[8] * X * X + A[9] * X * Y + A[10] * Y + A[11] * Y * Y;
                X = new_x;
                Y = new_y;

                int pix_x = (int)Math.Round((X - Wxmin) / Wwid * Wid);
                int pix_y = (int)Math.Round(Hgt - (Y - Wymin) / Whgt * Hgt - 1);
                if ((pix_x >= 0) && (pix_x < Wid) &&
                    (pix_y >= 0) && (pix_y < Hgt))
                {
                    Bm.SetPixel(pix_x, pix_y, Color.Blue);
                }
            }

            // Display the result.
            picCanvas.Refresh();
        }

        // Start a new image for the new available area.
        private void picCanvas_Resize(object sender, EventArgs e)
        {
            StartNewImage();
        }

        // Make a new bitmap and draw axes if desired.
        private void StartNewImage()
        {
            if (picCanvas.ClientSize.Width <= 0 ||
                picCanvas.ClientSize.Height <= 0) return;

            // Get the current bounds.
            Wid = picCanvas.ClientSize.Width;
            Hgt = picCanvas.ClientSize.Height;

            // Set the coefficients.
            SetCoefficients(cboCoefficients.Text);

            X = 0;
            Y = 0;

            // Make the new bitmap.
            Bm = new Bitmap((int)Wid, (int)Hgt);
            picCanvas.BackgroundImage = Bm;
            using (Graphics gr = Graphics.FromImage(Bm))
            {
                gr.Clear(Color.Black);

                // Draw axes is desired.
                if (chkDrawAxes.Checked)
                {
                    int pix_x = (int)Math.Round((0 - Wxmin) / Wwid * Wid);
                    int pix_y = (int)Math.Round(Hgt - (0 - Wymin) / Whgt * Hgt - 1);
                    gr.DrawLine(Pens.Red, pix_x, 0, pix_x, picCanvas.ClientSize.Height);
                    gr.DrawLine(Pens.Red, 0, pix_y, picCanvas.ClientSize.Width, pix_y);
                    for (float i = -5; i <= 5; i += 0.1f)
                    {
                        pix_x = (int)Math.Round((i - Wxmin) / Wwid * Wid);
                        gr.DrawLine(Pens.Orange, pix_x, pix_y - 3, pix_x, pix_y + 3);
                    }
                    for (float i = -5; i <= 5; i += 1)
                    {
                        pix_x = (int)Math.Round((i - Wxmin) / Wwid * Wid);
                        gr.DrawLine(Pens.Yellow, pix_x, pix_y - 5, pix_x, pix_y + 5);
                    }

                    pix_x = (int)Math.Round((0 - Wxmin) / Wwid * Wid);
                    for (float i = -5; i <= 5; i += 0.1f)
                    {
                        pix_y = (int)Math.Round(Hgt - (i - Wymin) / Whgt * Hgt - 1);
                        gr.DrawLine(Pens.Orange, pix_x - 3, pix_y, pix_x + 3, pix_y);
                    }
                    for (float i = -5; i <= 5; i += 1)
                    {
                        pix_y = (int)Math.Round(Hgt - (i - Wymin) / Whgt * Hgt - 1);
                        gr.DrawLine(Pens.Yellow, pix_x - 5, pix_y, pix_x + 5, pix_y);
                    }
                }
            }

            picCanvas.Invalidate();
        }

        // Set fractal coefficients from the ComboBox's value.
        private void SetCoefficients(string coefficients)
        {
            if (coefficients.Length == 0) return;

            const int ASC_A = (int)'A';

            string[] pieces = coefficients.Split(' ');
            char[] coef_letters = pieces[0].ToUpper().ToCharArray();
            for (int i = 0; i < 12; i++)
            {
                A[i] = -1.2 + ((int)coef_letters[i] - ASC_A) * 0.1;
            }

            Wxmin = Double.Parse(pieces[1]);
            Wxmax = Double.Parse(pieces[2]);
            Wymin = Double.Parse(pieces[3]);
            Wymax = Double.Parse(pieces[4]);
            Wwid = Wxmax - Wxmin;
            Whgt = Wymax - Wymin;
        }

        // Start or stop.
        private void btnStart_Click(object sender, EventArgs e)
        {
            tmrDrawPoint.Enabled = !tmrDrawPoint.Enabled;
            if (tmrDrawPoint.Enabled)
            {
                btnStart.Text = "Stop";
            }
            else
            {
                btnStart.Text = "Start";
            }
        }

        // Select new coefficients.
        private void cboCoefficients_SelectedIndexChanged(object sender, EventArgs e)
        {
            StartNewImage();
        }

        // Redraw with or without axes.
        private void chkDrawAxes_CheckedChanged(object sender, EventArgs e)
        {
            StartNewImage();
        }
    }
}
