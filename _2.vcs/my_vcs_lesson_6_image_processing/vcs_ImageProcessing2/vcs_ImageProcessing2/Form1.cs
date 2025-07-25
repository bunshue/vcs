using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for PixelFormat
using System.IO;    //for Path

namespace vcs_ImageProcessing2
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            pictureBox1.Image = Bitmap.FromFile(filename1);
            PictureToGray4();//用Bitmap32做灰階


        }

        void show_item_location()
        {
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom; //原圖
            pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox3.SizeMode = PictureBoxSizeMode.Zoom;

            int x_st=12;
            int y_st=50;
            int W = 250;
            int H = 250;
            int dx = W+20;
            int dy = H+50;

            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0 - 25);
            label2.Location = new Point(x_st + dx * 1, y_st + dy * 0 - 25);
            label3.Location = new Point(x_st + dx * 2, y_st + dy * 0 - 25);

            label1.Text = "原圖";
            label2.Text = "";
            label3.Text = "";

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            richTextBox1.Size = new Size(300, 600);

            this.Size = new Size(1200, 700);
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        #region 將圖片改為灰階 Grayscale Average

        private void PictureToGray4()
        {
            //將圖片改為灰階 Grayscale
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            //pictureBox11.Image = Bitmap.FromFile(filename);

            Bitmap bmp;
            Bitmap bm = new Bitmap(filename);
            bmp = new Bitmap(bm.Width, bm.Height);
            using (Graphics gr = Graphics.FromImage(bmp))
            {
                gr.DrawImage(bm, 0, 0);
            }

            // Make a Bitmap32 object.
            Bitmap32 bm32 = new Bitmap32(bmp);

            // Lock the bitmap.
            bm32.LockBitmap();

            // Process the pixels.
            for (int x = 0; x < bmp.Width; x++)
            {
                for (int y = 0; y < bmp.Height; y++)
                {
                    byte r = bm32.GetRed(x, y);
                    byte g = bm32.GetGreen(x, y);
                    byte b = bm32.GetBlue(x, y);
                    byte gray = (byte)(0.3 * r + 0.5 * g + 0.2 * b);
                    bm32.SetPixel(x, y, gray, gray, gray, 255);
                }
            }
            bm32.UnlockBitmap();

            //pictureBox3.Image = Bitmap.FromFile(filename);
            pictureBox3.Image = bmp;
        }
        #endregion

    }
}
