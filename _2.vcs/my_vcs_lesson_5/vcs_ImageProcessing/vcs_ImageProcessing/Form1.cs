using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ImageProcessing
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files\_case1\\pic3.jpg";
        //Graphics g;
        Pen p;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
            pictureBox1.ClientSize = new Size(640, 480);    //設定pictureBox的大小
            pictureBox1.BorderStyle = BorderStyle.Fixed3D;
            pictureBox1.Cursor = Cursors.Cross;  //移到控件上，改變鼠標

            pictureBox2.SizeMode = PictureBoxSizeMode.Normal; //圖片Zoom的方法
            pictureBox2.ClientSize = new Size(640, 480);    //設定pictureBox的大小
            pictureBox2.BorderStyle = BorderStyle.Fixed3D;
            pictureBox2.Cursor = Cursors.Cross;  //移到控件上，改變鼠標
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            Image image1 = new Bitmap(filename, true);
            pictureBox1.Image = image1;
            richTextBox1.Text += "圖片大小 " + image1.Width.ToString() + " X " + image1.Height.ToString() + "\n";

        }

        private void trackBar_R_Scroll(object sender, EventArgs e)
        {
            tb_R.Text = trackBar_R.Value.ToString();

        }

        private void trackBar_G_Scroll(object sender, EventArgs e)
        {
            tb_G.Text = trackBar_G.Value.ToString();

        }

        private void trackBar_B_Scroll(object sender, EventArgs e)
        {
            tb_B.Text = trackBar_B.Value.ToString();

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int ratio_r;
            int ratio_g;
            int ratio_b;
            ratio_r = trackBar_R.Value;
            ratio_g = trackBar_G.Value;
            ratio_b = trackBar_B.Value;

            draw_picture(ratio_r, ratio_g, ratio_b);

        }

        int ratio = 100;
        private void button2_Click(object sender, EventArgs e)
        {
            if (ratio <= 255)
            {
                ratio += 10;
                richTextBox1.Text += ratio.ToString() + " %\n";

                draw_picture(ratio, ratio, ratio);
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (ratio >= 10)
            {
                ratio -= 10;
                richTextBox1.Text += ratio.ToString() + " %\n";

                draw_picture(ratio, ratio, ratio);
            }
        }


        private void button7_Click(object sender, EventArgs e)
        {
            bitmap1 = null;
            pictureBox2.Image = null;

        }

        void draw_picture(int ratio_r, int ratio_g, int ratio_b)
        {
            int xx;
            int yy;
            int ww;
            int hh;
            Color ppp;
            int A;
            int R;
            int G;
            int B;

            richTextBox1.Text += "處理中~~~~~~\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 2;
            hh = bitmap1.Height / 2;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap1.GetPixel(xx, yy);

                    A = pp.A;
                    R = pp.R;
                    G = pp.G;
                    B = pp.B;

                    R = R * ratio_r / 100;
                    if (R > 255)
                        R = 255;
                    G = G * ratio_g / 100;
                    if (G > 255)
                        G = 255;
                    B = B * ratio_b / 100;
                    if (B > 255)
                        B = 255;

                    ppp = Color.FromArgb(A, R, G, B);
                    bitmap1.SetPixel(xx, yy, ppp);
                }
            }
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            draw_picture(100, 0, 0);

        }

        private void button5_Click(object sender, EventArgs e)
        {
            draw_picture(0, 100, 0);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            draw_picture(0, 0, 100);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "水平Mirror處理中~~~~~~\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 2;
            hh = bitmap1.Height / 1;

            for (yy = 0; yy < hh; yy++)
            {
                for (xx = 0; xx < ww; xx++)
                {
                    Color pp = bitmap1.GetPixel(bitmap1.Width - xx - 1, yy);
                    bitmap1.SetPixel(bitmap1.Width - xx - 1, yy, bitmap1.GetPixel(xx, yy));
                    bitmap1.SetPixel(xx, yy, pp);
                }
            }
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";

        }

        private void button9_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "垂直Mirror處理中~~~~~~\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 1;
            hh = bitmap1.Height / 2;

            for (xx = 0; xx < ww; xx++)
            {
                for (yy = 0; yy < hh; yy++)
                {
                    Color pp = bitmap1.GetPixel(xx, bitmap1.Height - yy - 1);
                    bitmap1.SetPixel(xx, bitmap1.Height - yy - 1, bitmap1.GetPixel(xx, yy));
                    bitmap1.SetPixel(xx, yy, pp);
                }
            }
            pictureBox2.Image = bitmap1;
            richTextBox1.Text += "處理完成\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;
            int ww;
            int hh;

            richTextBox1.Text += "擷取其中一塊處理中~~~~~~, 九宮格之正中央\n";

            bitmap1 = new Bitmap(filename);
            //g = Graphics.FromImage(bitmap1);

            ww = bitmap1.Width / 3;
            hh = bitmap1.Height / 3;

            Bitmap bitmap2 = new Bitmap(ww, hh);

            int x_st = ww;
            int y_st = hh;

            for (xx = 0; xx < ww; xx++)
            {
                for (yy = 0; yy < hh; yy++)
                {
                    bitmap2.SetPixel(xx, yy, bitmap1.GetPixel(x_st + xx, y_st + yy));
                }
            }
            pictureBox2.Image = bitmap2;
            pictureBox2.SizeMode = PictureBoxSizeMode.Normal;   //圖片Zoom的方法
            richTextBox1.Text += "處理完成\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;

            bitmap1 = new Bitmap(filename);
            Graphics g = Graphics.FromImage(bitmap1);   //畫字用

            for (yy = 0; yy < bitmap1.Height; yy++)
            {
                for (xx = 0; xx < bitmap1.Width; xx++)
                {
                    byte rrr = bitmap1.GetPixel(xx, yy).R;
                    byte ggg = bitmap1.GetPixel(xx, yy).G;
                    byte bbb = bitmap1.GetPixel(xx, yy).B;


                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bitmap1.SetPixel(xx, yy, zz);
                }
            }
            g.DrawString("彩色轉灰階", new Font("標楷體", 100), new SolidBrush(Color.Blue), new PointF(20, 20));

            pictureBox2.Image = bitmap1;

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

    }
}
