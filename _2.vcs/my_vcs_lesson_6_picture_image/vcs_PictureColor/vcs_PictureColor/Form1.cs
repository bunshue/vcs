using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

namespace vcs_PictureColor
{
    public partial class Form1 : Form
    {
        public Point firstPoint = new Point(0, 0);  //鼠標第一點 
        public Point secondPoint = new Point(0, 0);  //鼠標第二點 
        public bool begin = false;   //是否開始畫矩形 
        Graphics g1;

        private int W = 0;  //原圖的寬
        private int H = 0;  //原圖的高
        private int w = 0;  //擷取圖的寬
        private int h = 0;  //擷取圖的高

        int x_st = 0;
        int y_st = 0;
        int x_sp = 0;
        int y_sp = 0;

        Image image;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            x_st = 50;
            y_st = 50;
            w = 640 - 100;
            h = 480 - 100;

            string filename = @"C:\______test_files\ims01.bmp";
            pictureBox1.Image = Image.FromFile(filename);

            g1 = this.pictureBox1.CreateGraphics();

            int W = pictureBox1.Image.Width;
            int H = pictureBox1.Image.Height;

            nud_x_st.Maximum = W;
            nud_y_st.Maximum = H;
            nud_w.Maximum = W;
            nud_h.Maximum = H;
            nud_x_st.Value = x_st;
            nud_y_st.Value = y_st;
            nud_w.Value = w;
            nud_h.Value = h;
            update_crop_picture();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "選取")
            {
                button1.Text = "選取中";
                w = 0;
                h = 0;
                nud_w.Value = w;
                nud_h.Value = h;
                pictureBox1.MouseDown += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
            }
            else
            {
                button1.Text = "選取";

            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            begin = true;
            firstPoint = new Point(e.X, e.Y);
            nud_x_st.Value = x_st;
            nud_y_st.Value = y_st;
            x_st = e.X;
            y_st = e.Y;
            w = 0;
            h = 0;

            pictureBox1.MouseDown -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);

            nud_x_st.Value = e.X;
            nud_y_st.Value = e.Y;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if (begin == true)
            {
                //重新在pictureBox1上面繪圖
                this.Refresh();
                //獲取新的右下角坐標 
                secondPoint = new Point(e.X, e.Y);
                int minX = Math.Min(firstPoint.X, secondPoint.X);
                int minY = Math.Min(firstPoint.Y, secondPoint.Y);
                int maxX = Math.Max(firstPoint.X, secondPoint.X);
                int maxY = Math.Max(firstPoint.Y, secondPoint.Y);

                x_st = minX;
                y_st = minY;
                w = maxX - minX;
                h = maxY - minY;

                //畫矩形
                g1.DrawRectangle(new Pen(Color.Red), x_st, y_st, w, h);
                nud_x_st.Value = x_st;
                nud_y_st.Value = y_st;
                nud_w.Value = w;
                nud_h.Value = h;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            begin = false;

            pictureBox1.MouseMove -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);
            button1.Text = "選取";

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            Rectangle cropArea = new Rectangle(x_st, y_st, w, h);    //要截取的區域大小
            //pictureBox2.Image = bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb);
        }

        private void nud_x_st_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();
        }

        private void nud_y_st_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();
        }

        private void nud_w_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();
        }

        private void nud_h_ValueChanged(object sender, EventArgs e)
        {
            update_crop_picture();

        }

        private void button2_Click(object sender, EventArgs e)
        {
            if ((x_st < 0) || (y_st < 0) || (w <= 0) || (h <= 0))
            {
                richTextBox1.Text += "選取位置錯誤\n";

                return;
            }

            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
                Rectangle cropArea = new Rectangle(x_st, y_st, w, h);    //要截取的區域大小
                //pictureBox2.Image = bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb);

                bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb).Save(filename, ImageFormat.Bmp);

                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                //bitmap1.Save(filename, ImageFormat.Bmp);
                //bitmap1.Save(@file3, ImageFormat.Png);

                //richTextBox1.Text += "已存檔 : " + file1 + "\n";
                richTextBox1.Text += "已存檔 : " + filename + "\n";
                //richTextBox1.Text += "已存檔 : " + file3 + "\n";
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        void update_crop_picture()
        {
            if ((nud_x_st.Value < 0) || (nud_y_st.Value < 0) || (nud_w.Value <= 0) || (nud_h.Value <= 0))
            {
                //richTextBox1.Text += "選取位置錯誤\n";
                return;
            }

            //重新在pictureBox1上面繪圖
            this.Refresh();
            //獲取新的右下角坐標 

            x_st = (int)nud_x_st.Value;
            y_st = (int)nud_y_st.Value;
            w = (int)nud_w.Value;
            h = (int)nud_h.Value;

            //畫矩形
            g1.DrawRectangle(new Pen(Color.Green), x_st, y_st, w, h);

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            Rectangle cropArea = new Rectangle(x_st, y_st, w, h);    //要截取的區域大小
            //pictureBox2.Image = bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //SetPixel 彩色轉灰階
            string filename = @"C:\______test_files\ims01.bmp";
            color_to_gray_1(filename);
        }

        void color_to_gray_1(string filename)
        {
            richTextBox1.Text += "SetPixel 彩色轉灰階\n";

            Bitmap bmp0 = new Bitmap(filename);
            Bitmap bmp = new Bitmap(filename);
            pictureBox1.Image = bmp0;

            int xx;
            int yy;

            for (yy = 0; yy < bmp.Height; yy++)
            {
                for (xx = 0; xx < bmp.Width; xx++)
                {
                    byte rrr = bmp.GetPixel(xx, yy).R;
                    byte ggg = bmp.GetPixel(xx, yy).G;
                    byte bbb = bmp.GetPixel(xx, yy).B;

                    int Gray = (rrr * 299 + ggg * 587 + bbb * 114 + 500) / 1000;
                    Color zz = Color.FromArgb(255, Gray, Gray, Gray);

                    bmp.SetPixel(xx, yy, zz);
                }
            }
            pictureBox1.Image = bmp;
            //pictureBox2.Image = bmp;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //加強

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image.Clone();
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            int i;
            int j;
            byte max = 0;
            byte min = 255;

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    byte rrr = bitmap1.GetPixel(i, j).R;
                    //richTextBox1.Text += rrr.ToString() + " ";
                    if (rrr > max)
                        max = rrr;
                    if (rrr < min)
                        min = rrr;
                }
            }
            richTextBox1.Text += "\nmax = " + max.ToString() + ", min = " + min.ToString() + "\n";
            lb_max.Text = max.ToString();
            lb_min.Text = min.ToString();

            double ratio = 255.0 / (max - min);

            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";
            lb_ratio.Text = ratio.ToString();

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    byte rrr = bitmap1.GetPixel(i, j).R;
                    //richTextBox1.Text += rrr.ToString() + "-";

                    double gray = ratio * (rrr - min);

                    //richTextBox1.Text += gray.ToString() + " ";

                    Color zz = Color.FromArgb(255, (int)gray, (int)gray, (int)gray);

                    bitmap1.SetPixel(i, j, zz);

                    if (gray > 240)
                    {
                        //bitmap1.SetPixel(i, j, Color.Red);
                    }
                    else if (gray < 10)
                    {
                        //bitmap1.SetPixel(i, j, Color.Green);

                    }


                }


            }

            richTextBox1.Text += "\nmax = " + max.ToString() + ", min = " + min.ToString() + "\n";

            pictureBox2.Image = bitmap1;

        }

        private void button3_Click(object sender, EventArgs e)
        {
            x_st = 50;
            y_st = 50;
            w = 640 - 100;
            h = 480-100;

            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            int i;
            int j;
            int[] brightness = new int[256];
            int total_points = 0;

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    byte rrr = bitmap1.GetPixel(i, j).R;
                    //richTextBox1.Text += rrr.ToString() + "-";
                    brightness[rrr]++;
                    total_points++;
                }
            }



            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";

            int most = 0;
            for (i = 0; i < 256; i++)
            {
                richTextBox1.Text += brightness[i].ToString() + " ";
                if (brightness[i] > most)
                    most = brightness[i];
                if (brightness[i] == 0)
                    brightness[i] = 5;
            }
            richTextBox1.Text += "\n最多 " + most.ToString() + "\n";

            int ww = 512;
            int hh = 200;
            Bitmap bitmap2 = new Bitmap(ww, hh);
            Graphics g2 = Graphics.FromImage(bitmap2);
            //g2.Clear(Color.Pink);

            double ratio =0;
            ratio = (double)hh / most;

            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                //g2.FillRectangle(Brushes.Red, i * 2, 0, 2, (float)(brightness[i] * ratio));


                g2.FillRectangle(Brushes.Red, i * 2, hh - (float)(brightness[i] * ratio), 2, (float)(brightness[i] * ratio));

            }

            g2.DrawRectangle(Pens.Red, 0, 0, ww-1, hh-1);




            pictureBox2.Image = bitmap2;

        }

        private void button6_Click(object sender, EventArgs e)
        {
            Form1_Load(sender, e);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            x_st = 50;
            y_st = 50;
            w = 640 - 100;
            h = 480 - 100;

            Bitmap bitmap2 = (Bitmap)pictureBox2.Image;
            int W = bitmap2.Width;
            int H = bitmap2.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            int i;
            int j;
            int[] brightness = new int[256];
            int total_points = 0;

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    byte rrr = bitmap2.GetPixel(i, j).R;
                    //richTextBox1.Text += rrr.ToString() + "-";
                    brightness[rrr]++;
                    total_points++;
                }
            }



            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";

            int most = 0;
            for (i = 0; i < 256; i++)
            {
                richTextBox1.Text += brightness[i].ToString() + " ";
                if (brightness[i] > most)
                    most = brightness[i];
                if (brightness[i] == 0)
                    brightness[i] = 5;
            }
            richTextBox1.Text += "\n最多 " + most.ToString() + "\n";

            int ww = 512;
            int hh = 200;
            Bitmap bitmap3 = new Bitmap(ww, hh);
            Graphics g3 = Graphics.FromImage(bitmap3);
            //g3.Clear(Color.Pink);

            double ratio = 0;
            ratio = (double)hh / most;

            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                //g2.FillRectangle(Brushes.Red, i * 2, 0, 2, (float)(brightness[i] * ratio));


                g3.FillRectangle(Brushes.Red, i * 2, hh - (float)(brightness[i] * ratio), 2, (float)(brightness[i] * ratio));

            }

            g3.DrawRectangle(Pens.Red, 0, 0, ww - 1, hh - 1);




            pictureBox3.Image = bitmap3;

        }

    }
}

