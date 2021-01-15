using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawH_StrangeAttractors
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        // The bitmap's size.
        private double m_Wid, m_Hgt;

        // The bitmap.
        private Bitmap Bm;

        // The coefficients.
        private double[] A = new double[12];

        // World coordinate bounds.
        private double Wxmin, Wxmax, Wymin, Wymax, Wwid, Whgt;

        // Make an initial selection.
        private void Form1_Load(object sender, EventArgs e)
        {
            cboCoefficients.SelectedIndex = 0;
            StartNewImage();
        }

        // Start the timer.
        private void btnStart_Click(object sender, EventArgs e)
        {
            timer1.Enabled = !timer1.Enabled;
            if (timer1.Enabled)
            {
                btnStart.Text = "Stop";
            }
            else
            {
                btnStart.Text = "Start";
            }
        }

        // Reset the coefficients for this size.
        private bool Resizing = false;
        private void pictureBox1_Resize(object sender, EventArgs e)
        {
            if (Resizing) return;

            Resizing = true;
            StartNewImage();
            Resizing = false;
        }

        // Make a new image.
        private void StartNewImage()
        {
            if (pictureBox1.ClientSize.Width <= 0 ||
                pictureBox1.ClientSize.Height <= 0) return;

            // Get the image's size.
            m_Wid = pictureBox1.ClientSize.Width;
            m_Hgt = pictureBox1.ClientSize.Height;

            // Get the selected coefficients.
            SetCoefficients(cboCoefficients.Text);

            // Make a new Bitmap.
            X = 0;
            Y = 0;
            Bm = new Bitmap((int)m_Wid, (int)m_Hgt);
            pictureBox1.Image = Bm;
            using (Graphics gr = Graphics.FromImage(Bm))
            {
                gr.Clear(Color.Black);

                // Draw axes if desired.
                if (chkDrawAxes.Checked)
                {
                    int pix_x = (int)((0 - Wxmin) / Wwid * m_Wid);
                    int pix_y = (int)(m_Hgt - (0 - Wymin) / Whgt * m_Hgt - 1);
                    gr.DrawLine(Pens.Red, pix_x, 0, pix_x, pictureBox1.ClientSize.Height);
                    gr.DrawLine(Pens.Red, 0, pix_y, pictureBox1.ClientSize.Width, pix_y);
                    for (double i = -5; i <= 5; i += 0.1)
                    {
                        pix_x = (int)((i - Wxmin) / Wwid * m_Wid);
                        gr.DrawLine(Pens.Orange, pix_x, pix_y - 3, pix_x, pix_y + 3);
                    }
                    for (double i = -5; i <= 5; i += 0.1)
                    {
                        pix_x = (int)((i - Wxmin) / Wwid * m_Wid);
                        gr.DrawLine(Pens.Yellow, pix_x, pix_y - 5, pix_x, pix_y + 5);
                    }

                    pix_x = (int)((0 - Wxmin) / Wwid * m_Wid);
                    for (double i = -5; i <= 5; i += 0.1)
                    {
                        pix_y = (int)(m_Hgt - (i - Wymin) / Whgt * m_Hgt - 1);
                        gr.DrawLine(Pens.Orange, pix_x - 3, pix_y, pix_x + 3, pix_y);
                    }
                    for (double i = -5; i <= 5; i++)
                    {
                        pix_y = (int)(m_Hgt - (i - Wymin) / Whgt * m_Hgt - 1);
                        gr.DrawLine(Pens.Yellow, pix_x - 5, pix_y, pix_x + 5, pix_y);
                    }
                }
            }

            pictureBox1.Refresh();
        }

        // Set the coefficients for the coefficient string.
        private void SetCoefficients(string coefficients)
        {
            if (coefficients.Length == 0) return;

            const int ASC_A = (int)'A';

            string[] pieces = coefficients.Split(' ');
            string coef_letters = pieces[0].ToUpper();
            char[] chars = coef_letters.ToCharArray();
            for (int i = 0; i < A.Length; i++)
            {
                A[i] = -1.2 + ((int)chars[i] - ASC_A) * 0.1;
            }

            Wxmin = Double.Parse(pieces[1]);
            Wxmax = Double.Parse(pieces[2]);
            Wymin = Double.Parse(pieces[3]);
            Wymax = Double.Parse(pieces[4]);
            Wwid = Wxmax - Wxmin;
            Whgt = Wymax - Wymin;
        }

        // Draw 1000 points.
        private double X, Y;
        private void timer1_Tick(object sender, EventArgs e)
        {
            for (int i = 1; i <= 1000; i++)
            {
                double new_x = A[0] + A[1] * X + A[2] * X * X + A[3] * X * Y + A[4] * Y + A[5] * Y * Y;
                double new_y = A[6] + A[7] * X + A[8] * X * X + A[9] * X * Y + A[10] * Y + A[11] * Y * Y;
                X = new_x;
                Y = new_y;

                int pix_x = (int)((X - Wxmin) / Wwid * m_Wid);
                int pix_y = (int)(m_Hgt - (Y - Wymin) / Whgt * m_Hgt - 1);
                if ((pix_x >= 0) && (pix_x < m_Wid) &&
                    (pix_y >= 0) && (pix_y < m_Hgt))
                {
                    Bm.SetPixel(pix_x, pix_y, Color.Blue);
                }
            }

            // Display the result.
            pictureBox1.Refresh();
        }

        // Use the selected coefficients.
        private void cboCoefficients_SelectedIndexChanged(object sender, EventArgs e)
        {
            StartNewImage();
        }

        // Start a new image to show the axes or not.
        private void chkDrawAxes_CheckedChanged(object sender, EventArgs e)
        {
            StartNewImage();
        }
    }
}
