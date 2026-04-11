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
            show_item_location();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
            
            //pictureBox1.Size = new Size(400, 450);
            //pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            //richTextBox1.Size = new Size(300, 690);
            //richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1273, 750);
            this.Text = "vcs_ImageData";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
