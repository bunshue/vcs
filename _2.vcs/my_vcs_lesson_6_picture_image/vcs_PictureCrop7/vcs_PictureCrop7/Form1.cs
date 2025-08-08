using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;//for Dash

namespace vcs_PictureCrop7
{
    public partial class Form1 : Form
    {
        string filename = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        Bitmap TheBitmap;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            using (Bitmap bm = new Bitmap(filename))
            {
                TheBitmap = new Bitmap(bm);
            }
            pictureBox1.Image = TheBitmap;
            this.ClientSize = new Size(
                pictureBox1.Right + pictureBox1.Left,
                pictureBox1.Bottom + pictureBox1.Left);

        }

        // Let the user click and drag to select an area.
        private int StartX, StartY;
        private bool Drawing = false;

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            Drawing = true;
            StartX = e.X;
            StartY = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Bitmap temp_bm = new Bitmap(TheBitmap);
            using (Graphics gr = Graphics.FromImage(temp_bm))
            {
                using (Pen dashed_pen = new Pen(Color.Black, 0))
                {
                    dashed_pen.DashStyle = DashStyle.Dash;
                    gr.DrawRectangle(dashed_pen,
                        Math.Min(StartX, e.X),
                        Math.Min(StartY, e.Y),
                        Math.Abs(StartX - e.X),
                        Math.Abs(StartY - e.Y));
                }
            }
            pictureBox1.Image = temp_bm;

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            if (!Drawing) return;
            Drawing = false;

            // Process the selected area.
            Rectangle rect = new Rectangle(
                Math.Min(StartX, e.X),
                Math.Min(StartY, e.Y),
                Math.Abs(StartX - e.X),
                Math.Abs(StartY - e.Y));
            Gray_Selection(TheBitmap, rect);
            pictureBox1.Image = TheBitmap;
            pictureBox1.Refresh();

        }

        private void Gray_Selection(Bitmap bm, Rectangle rect)
        {
            for (int y = rect.Top; y <= rect.Bottom; y++)
            {
                for (int x = rect.Left; x <= rect.Right; x++)
                {
                    Color clr = bm.GetPixel(x, y);
                    // Convert to grayscale.
                    byte new_clr = (byte)((clr.R + clr.G + clr.B) / 3);
                    bm.SetPixel(x, y, Color.FromArgb(new_clr, new_clr, new_clr));
                }
            }
        }

    }
}
