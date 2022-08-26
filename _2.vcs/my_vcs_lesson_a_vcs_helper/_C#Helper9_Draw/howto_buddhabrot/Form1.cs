using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace howto_buddhabrot
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const double Wxmin = -1.5;
        private const double Wxmax = 1.5;
        private const double Wymin = -1.5;
        private const double Wymax = 1.5;

        private Bitmap BrotBitmap = null;
        private bool IsDrawing = false;
        private Random Rand = new Random();

        private void mnuFileSave_Click(object sender, EventArgs e)
        {
            if (sfdBrot.ShowDialog() == DialogResult.OK)
            {
                string file_name = sfdBrot.FileName;
                if (!file_name.Contains(".")) file_name += ".bmp";
                string ext = file_name.Substring(file_name.LastIndexOf(".")).ToLower();

                switch (ext)
                {
                    case ".bmp":
                        BrotBitmap.Save(file_name, ImageFormat.Bmp);
                        break;
                    case ".bmgif":
                        BrotBitmap.Save(file_name, ImageFormat.Gif);
                        break;
                    case ".jpg":
                    case ".jpeg":
                        BrotBitmap.Save(file_name, ImageFormat.Jpeg);
                        break;
                    case ".png":
                        BrotBitmap.Save(file_name, ImageFormat.Png);
                        break;
                    case ".tif":
                    case ".tiff":
                        BrotBitmap.Save(file_name, ImageFormat.Tiff);
                        break;
                    default:
                        MessageBox.Show("Unknown file type " + ext);
                        break;
                }
            }
        }

        private void btnDraw_Click(object sender, EventArgs e)
        {
            if (btnDraw.Text == "Draw")
            {
                btnDraw.Text = "Stop";
                DrawBrot();
            }

            IsDrawing = false;
            btnDraw.Text = "Draw";
        }

        // Draw the Buddhabrot until stopped or
        // we plot the desired number of points.
        private void DrawBrot()
        {
            // Get parameters.
            int wid = int.Parse(txtWidth.Text);
            int hgt = int.Parse(txtHeight.Text);
            int cut_r = int.Parse(txtRedCutoff.Text);
            int cut_g = int.Parse(txtGreenCutoff.Text);
            int cut_b = int.Parse(txtBlueCutoff.Text);
            int stop_after = int.Parse(txtStopAfter.Text);
            int draw_every = int.Parse(txtDrawEvery.Text);

            if ((wid <= 0) || (hgt <= 0))
            {
                MessageBox.Show("Invalid parameter", "Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
                return;
            }

            // Make hit count arrays.
            int[,] hit_r = new int[wid, hgt];
            int[,] hit_g = new int[wid, hgt];
            int[,] hit_b = new int[wid, hgt];

            // Make the bitmap.
            BrotBitmap = new Bitmap(wid, hgt);
            picCanvas.Image = BrotBitmap;
            this.ClientSize = new Size(
                picCanvas.Left + picCanvas.Width + 8,
                System.Math.Max(
                    btnDraw.Top + btnDraw.Height,
                    picCanvas.Top + picCanvas.Height) + 8);
            mnuFileSave.Enabled = true;

            // Start drawing.
            DateTime start_time = DateTime.Now;
            DateTime stop_time;
            TimeSpan elapsed;
            IsDrawing = true;

            // Build the hit counts.
            double dx = (Wxmax - Wxmin) / hgt;
            double dy = (Wymax - Wymin) / wid;
            int max_r = 0, max_g = 0, max_b = 0, hits = 0, total_hits = 0;

            while (total_hits < stop_after)
            {
                double cx = Wxmin + Rand.NextDouble() * (Wxmax - Wxmin);
                double cy = Wymin + Rand.NextDouble() * (Wymax - Wymin);
                double dd = cx * cx + cy * cy;
                if (dd < 1)
                {
                    DrawPoint(cx, cy, wid, hgt, dx, dy,
                        ref max_r, hit_r, cut_r, ref hits);
                }
                else if (dd < 2)
                {
                    DrawPoint(cx, cy, wid, hgt, dx, dy,
                        ref max_g, hit_g, cut_g, ref hits);
                }
                else
                {
                    DrawPoint(cx, cy, wid, hgt, dx, dy,
                        ref max_b, hit_b, cut_b, ref hits);
                }

                if (hits >= draw_every)
                {
                    total_hits += hits;
                    hits = 0;
                    DisplayBrot(wid, hgt, max_r, max_g, max_b, hit_r, hit_g, hit_b);

                    stop_time = DateTime.Now;
                    elapsed = stop_time.Subtract(start_time);
                    this.Text = elapsed.TotalSeconds.ToString("0.00") +
                        " sec, " + total_hits.ToString() + " hits";

                    Application.DoEvents();
                    if (!IsDrawing) break;
                }
            }
        }

        // Plot one point.
        private void DrawPoint(double cx, double cy, int wid, int hgt, double dx, double dy, ref int max_hits, int[,] hits, int cutoff, ref int num_hits)
        {
            const double ESCAPING = 4;

            // Zet Z0.
            double x, xx, y, yy;
            x = cx;
            y = cy;
            xx = x * x;
            yy = y * y;

            // Iterate.
            for (int i = 1; i <= cutoff; i++)
            {
                y = 2 * x * y + cy;
                x = xx - yy + cx;
                xx = x * x;
                yy = y * y;
                if (xx + yy >= ESCAPING) break;
            }

            // See if we escaped.
            if (xx + yy >= ESCAPING)
            {
                // Plot.
                x = cx;
                y = cy;
                xx = x * x;
                yy = y * y;

                // Iterate.
                for (int i = 1; i <= cutoff; i++)
                {
                    int ix = (int)Math.Round((x - Wxmin) / dx);
                    int iy = (int)Math.Round((y - Wymin) / dy);
                    if ((ix >= 0) && (ix < hgt) && (iy >= 0) && (iy < wid))
                    {
                        hits[iy, ix] += 1;
                        if (max_hits < hits[iy, ix]) max_hits = hits[iy, ix];
                    }
                    else
                    {
                        break;
                    }

                    y = 2 * x * y + cy;
                    x = xx - yy + cx;
                    xx = x * x;
                    yy = y * y;
                    if (xx + yy >= ESCAPING) break;
                }

                num_hits += 1;
            }
        }

        // Draw the current image.
        private void DisplayBrot(int wid, int hgt, int max_r, int max_g, int max_b, int[,] hit_r, int[,] hit_g, int[,] hit_b)
        {
            using (Graphics gr = Graphics.FromImage(BrotBitmap))
            {
                gr.Clear(Color.Black);
            }

            double scale_r = 255 * 2.5 / max_r;
            double scale_g = 255 * 2.5 / max_g;
            double scale_b = 255 * 2.5 / max_b;

            for (int y = 0; y < hgt; y++)
            {
                for (int x = 0; x < wid; x++)
                {
                    int r = (int)Math.Round(hit_r[x, y] * scale_r);
                    if (r > 255) r = 255;
                    int g = (int)Math.Round(hit_g[x, y] * scale_g);
                    if (g > 255) g = 255;
                    int b = (int)Math.Round(hit_b[x, y] * scale_b);
                    if (b > 255) b = 255;

                    BrotBitmap.SetPixel(x, y, Color.FromArgb(255, r, g, b));
                }
            }

            picCanvas.Refresh();
        }
    }
}
