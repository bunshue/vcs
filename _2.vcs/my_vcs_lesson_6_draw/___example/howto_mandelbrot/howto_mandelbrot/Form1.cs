using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace howto_mandelbrot
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private bool m_DrawingBox;
        private double m_StartX, m_StartY, m_CurX, m_CurY;
        private double m_Xmin, m_Xmax, m_Ymin, m_Ymax;

        public int MaxIterations;
        public double Zr, Zim, Z2r, Z2im;

        public List<Color> Colors = new List<Color>();

        private Bitmap m_Bm;

        private const double MIN_X = -2.2;
        private const double MAX_X = 1;
        private const double MIN_Y = -1.2;
        private const double MAX_Y = 1.2;

        // Return this color's value.
        public Color Color(int index)
        {
            return Colors[index];
        }

        // Reset the number of colors to 0.
        public void ResetColors()
        {
            Colors = new List<Color>();
        }

        // Adjust the aspect ratio of the selected
        // coordinates so they fit the window properly.
        private void AdjustAspect()
        {
            double hgt, wid, mid;

            double want_aspect = (m_Ymax - m_Ymin) / (m_Xmax - m_Xmin);
            double picCanvas_aspect = picCanvas.ClientSize.Height / (double)picCanvas.ClientSize.Width;
            if (want_aspect > picCanvas_aspect)
            {
                // The selected area is too tall and thin.
                // Make it wider.
                wid = (m_Ymax - m_Ymin) / picCanvas_aspect;
                mid = (m_Xmin + m_Xmax) / 2;
                m_Xmin = mid - wid / 2;
                m_Xmax = mid + wid / 2;
            } else {
                // The selected area is too short and wide.
                // Make it taller.
                hgt = (m_Xmax - m_Xmin) * picCanvas_aspect;
                mid = (m_Ymin + m_Ymax) / 2;
                m_Ymin = mid - hgt / 2;
                m_Ymax = mid + hgt / 2;
            }
        }

        // Draw the Mandelbrot set.
        private void DrawMandelbrot()
        {
            richTextBox1.Text += "DrawMandelbrot()\n";

            // Work until the magnitude squared > 4.
            const int MAX_MAG_SQUARED = 4;

            // Make a Bitmap to draw on.
            m_Bm = new Bitmap(picCanvas.ClientSize.Width, picCanvas.ClientSize.Height);
            Graphics gr = Graphics.FromImage(m_Bm);

            // Clear.
            gr.Clear(picCanvas.BackColor);
            picCanvas.Image = m_Bm;
            Application.DoEvents();

            // Adjust the coordinate bounds to fit picCanvas.
            AdjustAspect();

            // dReaC is the change in the real part
            // (X value) for C. dImaC is the change in the
            // imaginary part (Y value).
            int wid = picCanvas.ClientRectangle.Width;
            int hgt = picCanvas.ClientRectangle.Height;
            double dReaC = (m_Xmax - m_Xmin) / (wid - 1);
            double dImaC = (m_Ymax - m_Ymin) / (hgt - 1);

            // Calculate the values.
            int num_colors = Colors.Count;
            double ReaC = m_Xmin;
            for (int X = 0; X < wid; X++)
            {
                double ImaC = m_Ymin;
                for (int Y = 0; Y < hgt; Y++)
                {
                    double ReaZ = Zr;
                    double ImaZ = Zim;
                    double ReaZ2 = Z2r;
                    double ImaZ2 = Z2im;
                    int clr = 1;
                    while ((clr < MaxIterations) && (ReaZ2 + ImaZ2 < MAX_MAG_SQUARED))
                    {
                        // Calculate Z(clr).
                        ReaZ2 = ReaZ * ReaZ;
                        ImaZ2 = ImaZ * ImaZ;
                        ImaZ = 2 * ImaZ * ReaZ + ImaC;
                        ReaZ = ReaZ2 - ImaZ2 + ReaC;
                        clr++;
                    }

                    // Set the pixel's value.
                    m_Bm.SetPixel(X, Y, Colors[clr % num_colors]);

                    ImaC += dImaC;
                }
                ReaC += dReaC;

                // Let the user know we're not dead.
                if (X % 10 == 0) picCanvas.Refresh();
            }

            Text = "Mandelbrot (" +
                m_Xmin.ToString("0.000000") + ", " +
                m_Ymin.ToString("0.000000") + ")-(" +
                m_Xmax.ToString("0.000000") + ", " +
                m_Ymax.ToString("0.000000") + ")";
        }

        // Scale the selected area by this factor.
        private void ScaleArea(int scale_factor)
        {
            richTextBox1.Text += "scale = " + scale_factor.ToString() + "\n";
            double size = scale_factor * (m_Xmax - m_Xmin);
            if (size > 3.2)
            {
                mnuScaleFull_Click(null, null);
                return;
            }
            double mid = (m_Xmin + m_Xmax) / 2;
            m_Xmin = mid - size / 2;
            m_Xmax = mid + size / 2;

            size = scale_factor * (m_Ymax - m_Ymin);
            if (size > 2.4)
            {
                mnuScaleFull_Click(null, null);
                return;
            }
            mid = (m_Ymin + m_Ymax) / 2;
            m_Ymin = mid - size / 2;
            m_Ymax = mid + size / 2;

            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();
            DrawMandelbrot();
            this.Cursor = Cursors.Default;
            picCanvas.Cursor = Cursors.Cross;
        }

        // Set the scale.
        private void mnuScale_Click(object sender, EventArgs e)
        {
            MenuItem mnu = sender as MenuItem;
            ScaleArea(int.Parse(mnu.Tag.ToString()));
        }

        // Zoom out to full scale.
        private void mnuScaleFull_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "full-scale\n";

            m_Xmin = MIN_X;
            m_Xmax = MAX_X;
            m_Ymin = MIN_Y;
            m_Ymax = MAX_Y;

            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();
            DrawMandelbrot();
            this.Cursor = Cursors.Default;
            picCanvas.Cursor = Cursors.Cross;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.Show();
            Application.DoEvents();

            MaxIterations = 64;

            // Create some default colors.
            ResetColors();
            MandelbrotConfig frm = new MandelbrotConfig();
            Colors.Add(frm.picColor_40.BackColor);
            Colors.Add(frm.picColor_17.BackColor);
            Colors.Add(frm.picColor_18.BackColor);
            Colors.Add(frm.picColor_19.BackColor);
            Colors.Add(frm.picColor_20.BackColor);
            Colors.Add(frm.picColor_21.BackColor);
            Colors.Add(frm.picColor_22.BackColor);
            Colors.Add(frm.picColor_23.BackColor);
            frm.Close();

            // Display the first Mandelbrot set.
            mnuScaleFull_Click(null, null);
        }

        private void mnuOptOptions_Click(object sender, EventArgs e)
        {
            MandelbrotConfig frm = new MandelbrotConfig();
            frm.Initialize(this);
            frm.ShowDialog();
        }

        // Refresh. This is useful when the user resizes the form.
        private void mnuScaleRefresh_Click(object sender, EventArgs e)
        {
            ScaleArea(1);
        }

        // Start selecting an area.
        private void picCanvas_MouseDown(object sender, MouseEventArgs e)
        {
            m_DrawingBox = true;
            m_StartX = e.X;
            m_StartY = e.Y;
            m_CurX = e.X;
            m_CurY = e.Y;
        }

        // Continue selecting an area.
        private void picCanvas_MouseMove(object sender, MouseEventArgs e)
        {
            if (!m_DrawingBox) return;

            m_CurX = e.X;
            m_CurY = e.Y;

            Bitmap bm = new Bitmap(m_Bm);
            Graphics gr = Graphics.FromImage(bm);
            gr.DrawRectangle(Pens.Yellow,
                (int)(Math.Min(m_StartX, m_CurX)), (int)(Math.Min(m_StartY, m_CurY)),
                (int)(Math.Abs(m_StartX - m_CurX)), (int)(Math.Abs(m_StartY - m_CurY)));
            picCanvas.Image = bm;
        }

        // Finish selecting an area.
        private void picCanvas_MouseUp(object sender, MouseEventArgs e)
        {
            if (!m_DrawingBox)
            {
                return;
            }
            m_DrawingBox = false;
            picCanvas.Image = m_Bm;

            m_CurX = e.X;
            m_CurY = e.Y;

            // Put the coordinates in proper order.
            double x1 = Math.Min(m_StartX, m_CurX);
            double x2 = Math.Max(m_StartX, m_CurX);
            if (x1 == x2) x2 = x1 + 1;

            double y1 = Math.Min(m_StartY, m_CurY);
            double y2 = Math.Max(m_StartY, m_CurY);
            if (y1 == y2) y2 = y1 + 1;

            // Convert screen coords into drawing coords.
            double factor = (m_Xmax - m_Xmin) / picCanvas.ClientSize.Width;
            m_Xmax = m_Xmin + x2 * factor;
            m_Xmin = m_Xmin + x1 * factor;

            factor = (m_Ymax - m_Ymin) / picCanvas.ClientSize.Height;
            m_Ymax = m_Ymin + y2 * factor;
            m_Ymin = m_Ymin + y1 * factor;

            this.Cursor = Cursors.WaitCursor;
            Application.DoEvents();
            DrawMandelbrot();
            this.Cursor = Cursors.Default;
            picCanvas.Cursor = Cursors.Cross;
        }

        // Save the image.
        private void mnuFileSaveAs_Click(object sender, EventArgs e)
        {
            if (dlgSaveFile.ShowDialog() == DialogResult.OK)
            {
                m_Bm.Save(dlgSaveFile.FileName);
                string filename = dlgSaveFile.FileName;
                string extension = filename.Substring(filename.LastIndexOf("."));
                switch (extension)
                {
                    case ".bmp":
                        m_Bm.Save(filename, ImageFormat.Bmp);
                        break;
                    case ".jpg":
                    case ".jpeg":
                        m_Bm.Save(filename, ImageFormat.Jpeg);
                        break;
                    case ".gif":
                        m_Bm.Save(filename, ImageFormat.Gif);
                        break;
                    case ".png":
                        m_Bm.Save(filename, ImageFormat.Png);
                        break;
                    case ".tif":
                    case ".tiff":
                        m_Bm.Save(filename, ImageFormat.Tiff);
                        break;
                }
            }
        }
    }
}
