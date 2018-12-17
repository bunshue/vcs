using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_test_all_26_bmp2jpg
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        Bitmap bitmap1;
        Bitmap bitmap2;

        public Form1()
        {
            InitializeComponent();
            comboBox1.SelectedIndex = 1;
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
            pictureBox2.SizeMode = PictureBoxSizeMode.AutoSize;
            p = new Pen(Color.Red, 5);

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int ccc = 0;
            int xx;
            int yy;

            string filename = "C:\\______test_vcs\\picture1.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            bitmap2 = new Bitmap(filename);
            pictureBox1.Image = bitmap2;

            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            Color rr = Color.Red;
            Color gg = Color.Green;
            Color bb = Color.Blue;

            richTextBox1.Text += "R : " + rr.A.ToString("X2") + rr.R.ToString("X2") + rr.G.ToString("X2") + rr.B.ToString("X2") + "\n";
            richTextBox1.Text += "G : " + gg.A.ToString("X2") + gg.R.ToString("X2") + gg.G.ToString("X2") + gg.B.ToString("X2") + "\n";
            richTextBox1.Text += "B : " + bb.A.ToString("X2") + bb.R.ToString("X2") + bb.G.ToString("X2") + bb.B.ToString("X2") + "\n";

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    if ((yy % 120) == 0)
                    {
                        bitmap1.SetPixel(xx, yy, rr);
                    }
                    else if ((yy % 120) == 30)
                    {
                        bitmap1.SetPixel(xx, yy, gg);
                    }
                    else if ((yy % 120) == 60)
                    {
                        bitmap1.SetPixel(xx, yy, bb);
                    }
                    else if ((yy % 120) == 90)
                    {
                        bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, 0, 0));
                    }

                    ccc++;
                    if ((ccc % 30000) == 0)
                    {
                        Color p = bitmap1.GetPixel(xx, yy);
                        //richTextBox1.Text += p.ToString() + " ";
                        richTextBox1.Text += p.A.ToString("X2") + p.R.ToString("X2") + p.G.ToString("X2") + p.B.ToString("X2") + " ";
                        
                    }
                    
                }
            }
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (bitmap1 != null)
            {
                bitmap1.Save(@"C:\______test_vcs\\_transform_to_jpg.jpg", ImageFormat.Jpeg);
                bitmap1.Save(@"C:\______test_vcs\\_transform_to_bmp.bmp", ImageFormat.Bmp);
                bitmap1.Save(@"C:\______test_vcs\\_transform_to_png.png", ImageFormat.Png);
                richTextBox1.Text += "轉換成功\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            bitmap2 = null;
            pictureBox1.Image = null;
            pictureBox2.Image = null;
            richTextBox1.Clear();
        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            switch (comboBox1.SelectedIndex)
            {
                case 0:
                    richTextBox1.Text += "Normal\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Normal;
                    pictureBox2.SizeMode = PictureBoxSizeMode.Normal;
                    break;
                case 1:
                    richTextBox1.Text += "AutoSize\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
                    pictureBox2.SizeMode = PictureBoxSizeMode.AutoSize;
                    break;
                case 2:
                    richTextBox1.Text += "CenterImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.CenterImage;
                    pictureBox2.SizeMode = PictureBoxSizeMode.CenterImage;
                    break;
                case 3:
                    richTextBox1.Text += "StretchImage\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.StretchImage;
                    pictureBox2.SizeMode = PictureBoxSizeMode.StretchImage;
                    break;
                case 4:
                    richTextBox1.Text += "Zoom\n";
                    pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
                    pictureBox2.SizeMode = PictureBoxSizeMode.Zoom;
                    break;
                default:
                    richTextBox1.Text += "xxxxxxxxxx\n";
                    break;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if(bitmap1 == null)
                bitmap1 = new Bitmap(pictureBox2.Width, pictureBox2.Height);

            g = Graphics.FromImage(bitmap1);
            g.DrawRectangle(p, 50, 50, 100, 100);
            pictureBox2.Image = bitmap1;
        }
    }
}
