using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_PictureResize2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            cboScale.Text = "1";
        }

        // Display the image at the selected size.
        private void cboScale_SelectedIndexChanged(object sender, EventArgs e)
        {
            int W = pictureBox1.Image.Width;
            int H = pictureBox1.Image.Height;

            // Get the scale.
            float scale = float.Parse(cboScale.Text);

            // Make a bitmap of the right size.
            int w = (int)(W * scale);
            int h = (int)(H * scale);
            Bitmap bm = new Bitmap(w, h);
            
            // Draw the image onto the new bitmap.
            using (Graphics gr = Graphics.FromImage(bm))
            {
                // No smoothing.
                gr.InterpolationMode = InterpolationMode.NearestNeighbor;

                Point[] dest =
                {
                    new Point(0, 0),
                    new Point(w, 0),
                    new Point(0, h),
                };
                Rectangle source = new Rectangle(0, 0, W, H);
                gr.DrawImage(pictureBox1.Image, dest, source, GraphicsUnit.Pixel);
            }

            // Display the result.
            pictureBox2.Image = bm;
        }
    }
}
