using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Drawing.Drawing2D;

namespace vcs_ImageData
{
    public partial class Form1 : Form
    {
        private ImagingSolution.Imaging.ImageData image;
        private Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            /* old
            Image img = Image.FromFile(filename);
            pictureBox1.Image = img;
            */

            richTextBox1.Text += "開啟檔案 : " + filename + "\n";
            //richTextBox1.Text += "開啟檔案 : " + Path.GetFileName(filename) + "\n";   簡檔名

            image = new ImagingSolution.Imaging.ImageData(filename);

            bitmap1 = image.ToBitmap();

            richTextBox1.Text += "圖片大小 : " + image.Width.ToString() + " x " + image.Height.ToString() + " x " + image.ImageBit.ToString() + "bit\n";

            pictureBox1.Image = bitmap1;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (image == null)
            {
                return;
            }

            //image = new ImagingSolution.Imaging.ImageData(filename);
            // 表示用
            //bitmap1 = image.ToBitmap();

            //private void DispPixelInfo(Matrix mat, ImagingSolution.Imaging.ImageData image, PointF pointPictureBox)

            richTextBox1.Text += "image.Channel = " + image.Channel.ToString() + "\n";
            richTextBox1.Text += "image.Stride = " + image.Stride.ToString() + "\n";
            richTextBox1.Text += "image.Width = " + image.Width.ToString() + "\n";
            richTextBox1.Text += "image.Height = " + image.Height.ToString() + "\n";


            richTextBox1.Text += image.Width.ToString() + " x " + image.Height.ToString() + " x " + image.ImageBit.ToString() + "bit\n";

            int i, j;
            int x_st = 100;
            int y_st = 100;
            for (j = 0; j < 150; j += 1)
            {
                for (i = 0; i < 150; i += 1)
                {
                    //image[x_st + i, y_st + j, 0] = (i * 5 + j * 5) % 256;
                    //image[x_st + i, y_st + j, 1] = (i * 5 + j * 5) % 256;
                    //image[x_st + i, y_st + j, 2] = (i * 5 + j * 5) % 256;

                    image[x_st + i, y_st + j, 0] = 255;     //B
                    //image[x_st + i, y_st + j, 1] = 0;     //G
                    //image[x_st + i, y_st + j, 2] = 0;     //R
                    image[x_st + i, y_st + j, 3] = 0; //A
                    //richTextBox1.Text += image[x_st + i, y_st + j, 3].ToString() + " ";
                }
            }


            bitmap1 = image.ToBitmap();

            richTextBox1.Text += "圖片大小 : " + image.Width.ToString() + " x " + image.Height.ToString() + " x " + image.ImageBit.ToString() + "bit\n";

            pictureBox1.Image = bitmap1;
        }
    }
}

