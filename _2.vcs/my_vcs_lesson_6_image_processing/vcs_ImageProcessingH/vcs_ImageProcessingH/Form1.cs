using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Imaging;   //for ImageAttributes

namespace vcs_ImageProcessingH
{
    public partial class Form1 : Form
    {
        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            scrRed.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);
            scrGreen.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);
            scrBlue.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);
            scrBright.Scroll += new ScrollEventHandler(ChangeColorTone_Scroll);

            // Display the image converted to sepia tone.
            scrRed.Value = 128;
            scrGreen.Value = 128;
            scrBlue.Value = 128;
            scrBright.Value = 128;
            picColor.BackColor = Color.FromArgb(scrRed.Value, scrGreen.Value, scrBlue.Value);
            ColorPicture();
        }

        void show_item_location()
        {
            int W = 305;
            int H = 400;
            int x_st = 20;
            int y_st = 20;
            int dx = W + 50;
            int dy = H + 100;
            int dd2 = 85;

            richTextBox1.Size = new Size(W, H);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + dd2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);

            this.Size = new Size(1100, 600);
            this.Text = "vcs_ImageProcessingH";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Color the picture.
        private void ColorPicture()
        {
            picToned.Image = ToColorTone(picOriginal.Image, picColor.BackColor);
        }

        // Convert an image to sepia tone.
        private Bitmap ToColorTone(Image image, Color color)
        {
            float scale = scrBright.Value / 128f;

            float r = color.R / 255f * scale;
            float g = color.G / 255f * scale;
            float b = color.B / 255f * scale;

            // Make the ColorMatrix.
            ColorMatrix cm = new ColorMatrix(new float[][]
            {
                new float[] {r, 0, 0, 0, 0},
                new float[] {0, g, 0, 0, 0},
                new float[] {0, 0, b, 0, 0},
                new float[] {0, 0, 0, 1, 0},
                new float[] {0, 0, 0, 0, 1}
            });
            ImageAttributes ia = new ImageAttributes();
            ia.SetColorMatrix(cm);

            // Draw the image onto the new bitmap while applying the new ColorMatrix.
            Point[] points =
            {
                new Point(0, 0),
                new Point(image.Width - 1, 0),
                new Point(0, image.Height - 1),
            };
            Rectangle rect = new Rectangle(0, 0, image.Width, image.Height);

            // Make the result bitmap.
            Bitmap bm = new Bitmap(image.Width, image.Height);
            using (Graphics gr = Graphics.FromImage(bm))
            {
                gr.DrawImage(image, points, rect, GraphicsUnit.Pixel, ia);
            }

            // Return the result.
            return bm;
        }

        private void ChangeColorTone_Scroll(object sender, ScrollEventArgs e)
        {
            picColor.BackColor = Color.FromArgb(scrRed.Value, scrGreen.Value, scrBlue.Value);
            ColorPicture();
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


