using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_ZoomPicture4b
{
    public partial class Form1 : Form
    {
        private float PictureScale = 1.0f;

        // The Bitmap we display.
        private Bitmap Bm = null;

        // The dimensions of the drawing area in world coordinates.
        private const int WorldWidth = 100;
        private const int WorldHeight = 100;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SetScale(PictureScale);
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            int value = trackBar1.Value;
            switch (value)
            {
                case 0: PictureScale = 0.5f; break;
                case 1: PictureScale = 0.75f; break;
                case 2: PictureScale = 1.0f; break;
                case 3: PictureScale = 1.25f; break;
                case 4: PictureScale = 1.5f; break;
                case 5: PictureScale = 2f; break;
                default: PictureScale = 2.5f; break;
            }
            label1.Text = PictureScale.ToString() + " X";
            SetScale(PictureScale);
            //pictureBox1.ClientSize = new Size((int)(PictureScale * pictureBox1.Image.Width), (int)(PictureScale * pictureBox1.Image.Height));
        }

        // Set the scale and redraw.
        private void SetScale(float picture_scale)
        {
            // Set the scale.
            PictureScale = picture_scale;

            // Make a Bitmap of the right size.
            Bm = new Bitmap(
                (int)(PictureScale * WorldWidth),
                (int)(PictureScale * WorldHeight));

            // Make a Graphics object for the Bitmap.
            // (If you need to use this later, you can give it
            // class scope so you don't need to make a new one.)
            using (Graphics gr = Graphics.FromImage(Bm))
            {
                // Use a white background
                // (so you can see where the picture is).
                gr.Clear(Color.White);

                // Draw smoothly.
                //gr.SmoothingMode = SmoothingMode.AntiAlias;

                // Scale.
                gr.ScaleTransform(PictureScale, PictureScale);

                // Draw the image.
                DrawImage(gr);
            }

            // Display the result.
            pictureBox1.Image = Bm;
        }

        // Draw the image in world coordinates.
        private void DrawImage(Graphics gr)
        {
            Rectangle rect;

            rect = new Rectangle(10, 10, 80, 80);
            gr.FillEllipse(Brushes.LightGreen, rect);
            gr.DrawEllipse(Pens.Green, rect);

            rect = new Rectangle(40, 40, 20, 30);
            gr.FillEllipse(Brushes.LightBlue, rect);
            gr.DrawEllipse(Pens.Blue, rect);

            rect = new Rectangle(25, 30, 50, 50);
            gr.DrawArc(Pens.Red, rect, 20, 140);

            rect = new Rectangle(25, 25, 15, 20);
            gr.FillEllipse(Brushes.White, rect);
            gr.DrawEllipse(Pens.Black, rect);
            rect = new Rectangle(30, 30, 10, 10);
            gr.FillEllipse(Brushes.Black, rect);

            rect = new Rectangle(60, 25, 15, 20);
            gr.FillEllipse(Brushes.White, rect);
            gr.DrawEllipse(Pens.Black, rect);
            rect = new Rectangle(65, 30, 10, 10);
            gr.FillEllipse(Brushes.Black, rect);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = Application.StartupPath + "\\zoom_picture_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            // Make a bitmap of the correct size.
            using (Bitmap bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height))
            {
                // Copy the original image onto the new bitmap.
                using (Graphics gr = Graphics.FromImage(bitmap1))
                {
                    Rectangle source_rect = new Rectangle(
                        0, 0, pictureBox1.Image.Width, pictureBox1.Image.Height);
                    Rectangle dest_rect = new Rectangle(
                        0, 0, bitmap1.Width, bitmap1.Height);
                    gr.DrawImage(pictureBox1.Image,
                        dest_rect, source_rect, GraphicsUnit.Pixel);
                }

                // Save the bitmap.
                bitmap1.Save(filename, ImageFormat.Bmp);
                //richTextBox1.Text += "存檔成功\n";
                //richTextBox1.Text += "已存檔 : " + filename + "\n";
            }


        }
    }
}
