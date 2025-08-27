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
        string filename = string.Empty;

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
        int[] brightness_data = new int[256];

        int max = 255;
        int min = 0;
        int brightness = 128;
        int brightness_old = 128;
        int contrast = 128;
        int contrast_old = 128;

        bool flag_no_update_crop_picture = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (radioButton0.Checked == true)
                filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp"; //stomach
            else if (radioButton1.Checked == true)
                filename = @"D:\_git\vcs\_1.data\______test_files1\ims04.bmp"; //normal
            else if (radioButton2.Checked == true)
                filename = @"D:\_git\vcs\_1.data\______test_files1\ims05.bmp"; //black
            else if (radioButton3.Checked == true)
                filename = @"D:\_git\vcs\_1.data\______test_files1\ims06.bmp"; //color bar
            else
                filename = @"D:\_git\vcs\_1.data\______test_files1\ims01.bmp"; //stomach

            show_item_location();

            if (checkBox1.Checked == true)
            {
                x_st = 0;
                y_st = 0;
                w = 640;
                h = 480;
            }
            else
            {
                x_st = 50;
                y_st = 50;
                w = 640 - 100;
                h = 480 - 100;
            }

            pictureBox0.Image = Image.FromFile(filename);

            g1 = this.pictureBox0.CreateGraphics();

            int W = pictureBox0.Image.Width;
            int H = pictureBox0.Image.Height;

            nud_x_st.Maximum = W;
            nud_y_st.Maximum = H;
            nud_w.Maximum = W;
            nud_h.Maximum = H;
            nud_x_st.Value = x_st;
            nud_y_st.Value = y_st;
            nud_w.Value = w;
            nud_h.Value = h;
            update_crop_picture();

            lb_max.Text = "";
            lb_min.Text = "";
            lb_ratio.Text = "";
            lb_v1_name.Text = "Minimum";
            lb_v2_name.Text = "Maximum";
            lb_v3_name.Text = "Brightness";
            lb_v4_name.Text = "Contrast";

            measure_brightness(pictureBox0, pictureBox3);
            this.BackColor = Color.Yellow;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int W = 640;
            int H = 480;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(512, 300);
            pictureBox4.Size = new Size(512, 300);
            int tt = 290;
            pictureBox5.Size = new Size(512, 300 - tt);
            groupBox1.Size = new Size(W * 2 - 20, 1080 - 480 - 200 - 150);
            richTextBox1.Size = new Size(W, 1080 - 480 - 200 + tt - 140);

            x_st = 0;
            y_st = 00;
            dx = W;
            dy = H;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox5.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            groupBox1.Location = new Point(x_st + dx * 0 + 10, y_st + dy * 1 + 330);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 1 + 330 - tt);
            richTextBox1.BringToFront();

            //button
            x_st = 20;
            y_st = 30;
            dx = 190;
            dy = 45;

            x_st = 610;
            y_st = 30;

            lb_v1_name.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            lb_v2_name.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            lb_v3_name.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            lb_v4_name.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            x_st += 110;
            trackBar1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            trackBar2.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            trackBar3.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            trackBar4.Location = new Point(x_st + dx * 0, y_st + dy * 3);

            lb_v1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            lb_v2.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            lb_v3.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            lb_v4.Location = new Point(x_st + dx * 1, y_st + dy * 3);

            button8.Location = new Point(x_st + dx * 1 - 20, y_st + dy * 3 + 30);
            button8.BringToFront();


            //button6
            radioButton0.Location = new Point(button6.Location.X, button6.Location.Y + 45);
            radioButton1.Location = new Point(button6.Location.X, button6.Location.Y + 45 + 18);
            radioButton2.Location = new Point(button6.Location.X, button6.Location.Y + 45 + 18 * 2);
            radioButton3.Location = new Point(button6.Location.X, button6.Location.Y + 45 + 18 * 3);

            button10.Location = new Point(button7.Location.X + 500, button7.Location.Y);

            trackBar1.Size = new Size(180, 20);
            trackBar2.Size = new Size(180, 20);
            trackBar3.Size = new Size(180, 20);
            trackBar4.Size = new Size(180, 20);
            trackBar1.Minimum = 0;
            trackBar2.Minimum = 0;
            trackBar3.Minimum = 0;
            trackBar4.Minimum = 0;
            trackBar1.Maximum = 255;
            trackBar2.Maximum = 255;
            trackBar3.Maximum = 255;
            trackBar4.Maximum = 255;
            trackBar1.Value = 0;
            trackBar2.Value = 255;
            trackBar3.Value = 128;
            trackBar4.Value = 128;
            max = 255;
            min = 0;
            brightness = 128;
            brightness_old = 128;
            contrast = 128;
            contrast_old = 128;
            lb_v1.Text = trackBar1.Value.ToString();
            lb_v2.Text = trackBar2.Value.ToString();
            lb_v3.Text = trackBar3.Value.ToString();
            lb_v4.Text = trackBar4.Value.ToString();

            checkBox1.Location = new Point(nud_h.Location.X, nud_h.Location.Y + 50);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            bt_clear.BringToFront();

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            //this.Size = new Size(1300, 1080);

            //離開按鈕的寫法
            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
                pictureBox0.MouseDown += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
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

            pictureBox0.MouseDown -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseDown);
            pictureBox0.MouseMove += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox0.MouseUp += new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);

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

            pictureBox0.MouseMove -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseMove);
            pictureBox0.MouseUp -= new System.Windows.Forms.MouseEventHandler(pictureBox1_MouseUp);
            button1.Text = "選取";

            Bitmap bitmap1 = (Bitmap)pictureBox0.Image;
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
                Bitmap bitmap1 = (Bitmap)pictureBox0.Image;
                Rectangle cropArea = new Rectangle(x_st, y_st, w, h);    //要截取的區域大小
                //pictureBox2.Image = bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb);

                bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb).Save(filename, ImageFormat.Bmp);

                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                bitmap1.Save(filename, ImageFormat.Bmp);
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
            if (flag_no_update_crop_picture == true)
            {
                return;
            }

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

            Bitmap bitmap1 = (Bitmap)pictureBox0.Image;
            Rectangle cropArea = new Rectangle(x_st, y_st, w, h);    //要截取的區域大小
            //pictureBox2.Image = bitmap1.Clone(cropArea, PixelFormat.Format32bppArgb);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //SetPixel 彩色轉灰階
            color_to_gray_1(filename);

            draw_brightness(pictureBox3);
            do_brightness_contrast(0);
            measure_brightness(pictureBox0, pictureBox3);
            measure_brightness(pictureBox1, pictureBox4);
        }

        void color_to_gray_1(string filename)
        {
            richTextBox1.Text += "SetPixel 彩色轉灰階\n";

            Bitmap bmp0 = new Bitmap(filename);
            Bitmap bmp = new Bitmap(filename);
            pictureBox0.Image = bmp0;

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
            pictureBox0.Image = bmp;
            //pictureBox2.Image = bmp;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            do_brightness_contrast(1);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            measure_brightness(pictureBox0, pictureBox3);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Form1_Load(sender, e);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            measure_brightness(pictureBox1, pictureBox4);
        }

        void measure_brightness(PictureBox pbox1, PictureBox pbox2)
        {
            richTextBox1.Text += "\n\n圖片 : " + filename + "\n";
            if (pbox1.Image == null)
            {
                richTextBox1.Text += pbox1.Name + " 無影像, 離開\n";
                return;
            }

            brightness_data = new int[256];

            if (checkBox1.Checked == true)
            {
                x_st = 0;
                y_st = 0;
                w = 640;
                h = 480;
            }
            else
            {
                x_st = 50;
                y_st = 50;
                w = 640 - 100;
                h = 480 - 100;
            }

            Bitmap bitmap1 = (Bitmap)pbox1.Image;
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            int i;
            int j;
            int total_points = 0;

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    byte rrr = bitmap1.GetPixel(i, j).R;
                    //richTextBox1.Text += rrr.ToString() + "-";
                    brightness_data[rrr]++;
                    total_points++;
                }
            }

            //一律忽視最亮和最暗的數值
            brightness_data[0] = 0;
            brightness_data[255] = 0;

            richTextBox1.Text += "共有 " + total_points.ToString() + " 個點\n";

            draw_brightness(pbox2);
        }

        void draw_brightness(PictureBox pbox)
        {
            int i;
            int most = 0;
            for (i = 0; i < 256; i++)
            {
                //richTextBox1.Text += brightness_data[i].ToString() + " ";
                if (brightness_data[i] > most)
                    most = brightness_data[i];
                if (brightness_data[i] == 0)
                    brightness_data[i] = 5;
            }
            richTextBox1.Text += "\n最多 " + most.ToString() + "\n";

            int ww = 512;
            int hh1 = 300;
            int hh2 = 256;
            Bitmap bitmap2 = new Bitmap(ww, hh1);
            Graphics g2 = Graphics.FromImage(bitmap2);
            g2.Clear(Color.Pink);
            Pen p = new Pen(Color.Blue, 2);

            double ratio = 0;
            ratio = (double)hh2 / most;

            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            for (i = 0; i < 256; i++)
            {
                //g2.FillRectangle(Brushes.Red, i * 2, 0, 2, (float)(brightness_data[i] * ratio));
                g2.FillRectangle(Brushes.Red, i * 2, hh2 - (float)(brightness_data[i] * ratio), 2, (float)(brightness_data[i] * ratio));
            }

            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh1 - 2);
            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh2 - 2);


            Brush b = new SolidBrush(Color.FromArgb(33, Color.RoyalBlue.R, Color.RoyalBlue.G, Color.RoyalBlue.B));

            g2.FillRectangle(b, min * 2, 0, (max - min) * 2, hh1);


            p = new Pen(Color.Green, 3);

            g2.DrawLine(p, min * 2, hh2, max * 2, 0);

            Font f = new Font("標楷體", 20);

            if ((min >= 0) && (min <= 103))
            {
                g2.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(min * 2, hh2));
            }
            else if (min < 0)
            {
                g2.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(0, hh2));
            }
            else
            {
                g2.DrawString(min.ToString(), f, new SolidBrush(Color.Blue), new PointF(103 * 2, hh2));
            }

            if ((max <= 255) && (max >= 152))
            {
                g2.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(max * 2 - 50, hh2));
            }
            else if (max > 255)
            {
                g2.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(512 - 50, hh2));
            }
            else
            {
                g2.DrawString(max.ToString(), f, new SolidBrush(Color.Blue), new PointF(152 * 2 - 50, hh2));
            }
            pbox.Image = bitmap2;
        }

        private void trackBar1_Scroll(object sender, EventArgs e)
        {
            //min
            if (trackBar1.Value > trackBar2.Value)
            {
                trackBar2.Value = trackBar1.Value;
            }

            trackBar3.Value = 128 - trackBar1.Value / 2;
            trackBar4.Value = 128 + trackBar1.Value / 2;

            min = trackBar1.Value;
            max = trackBar2.Value;

            lb_v1.Text = trackBar1.Value.ToString();
            draw_brightness(pictureBox3);
        }

        private void trackBar2_Scroll(object sender, EventArgs e)
        {
            //max
            if (trackBar2.Value < trackBar1.Value)
            {
                trackBar1.Value = trackBar2.Value;
            }

            trackBar3.Value = 255 - trackBar2.Value / 2;
            trackBar4.Value = 255 - trackBar2.Value / 2;

            min = trackBar1.Value;
            max = trackBar2.Value;

            lb_v2.Text = trackBar2.Value.ToString();
            draw_brightness(pictureBox3);
        }

        private void trackBar3_Scroll(object sender, EventArgs e)
        {
            //brightness
            int dd = 0;

            brightness = trackBar3.Value;
            dd = brightness - brightness_old;

            min -= dd;
            max -= dd;

            brightness_old = brightness;

            if (min >= 0)
                trackBar1.Value = min;
            if (max <= 255)
                trackBar2.Value = max;

            lb_v3.Text = trackBar3.Value.ToString();
            draw_brightness(pictureBox3);
        }

        private void trackBar4_Scroll(object sender, EventArgs e)
        {
            //contrast
            int dd = 0;

            contrast = trackBar4.Value;
            dd = contrast - contrast_old;

            min += dd;
            max -= dd;

            contrast_old = contrast;

            if (min >= 0)
                trackBar1.Value = min;
            if (max <= 255)
                trackBar2.Value = max;

            lb_v4.Text = trackBar4.Value.ToString();
            draw_brightness(pictureBox3);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            trackBar1.Value = 0;
            trackBar2.Value = 255;
            trackBar3.Value = 128;
            trackBar4.Value = 128;
            max = 255;
            min = 0;
            brightness = 128;
            brightness_old = 128;
            contrast = 128;
            contrast_old = 128;
            lb_v1.Text = trackBar1.Value.ToString();
            lb_v2.Text = trackBar2.Value.ToString();
            lb_v3.Text = trackBar3.Value.ToString();
            lb_v4.Text = trackBar4.Value.ToString();

            draw_brightness(pictureBox3);
            do_brightness_contrast(0);
            measure_brightness(pictureBox0, pictureBox3);
            measure_brightness(pictureBox1, pictureBox4);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            do_brightness_contrast(0);
        }

        void do_brightness_contrast(int auto)
        {
            //加強

            Bitmap bitmap1 = (Bitmap)pictureBox0.Image.Clone();
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
            int i;
            int j;

            if (auto == 1)
            {
                max = 0;
                min = 255;

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
            }

            lb_max.Text = "最大 : " + max.ToString();
            lb_min.Text = "最小 : " + min.ToString();

            double ratio = 255.0 / (max - min);

            richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";
            lb_ratio.Text = "倍率 : " + ratio.ToString();

            for (j = y_st; j < (y_st + h); j++)
            {
                for (i = x_st; i < (x_st + w); i++)
                {
                    byte rrr = bitmap1.GetPixel(i, j).R;
                    //richTextBox1.Text += rrr.ToString() + "-";

                    double gray = ratio * (rrr - min);
                    if (gray > 255)
                        gray = 255;
                    else if (gray < 0)
                        gray = 0;

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

            pictureBox1.Image = bitmap1;
        }

        private void trackBar1_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void trackBar1_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void trackBar1_MouseUp(object sender, MouseEventArgs e)
        {
            do_brightness_contrast(0);
            measure_brightness(pictureBox1, pictureBox4);
        }

        private void trackBar2_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void trackBar2_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void trackBar2_MouseUp(object sender, MouseEventArgs e)
        {
            do_brightness_contrast(0);
            measure_brightness(pictureBox1, pictureBox4);
        }

        private void trackBar3_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void trackBar3_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void trackBar3_MouseUp(object sender, MouseEventArgs e)
        {
            do_brightness_contrast(0);
            measure_brightness(pictureBox1, pictureBox4);
        }

        private void trackBar4_MouseDown(object sender, MouseEventArgs e)
        {

        }

        private void trackBar4_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void trackBar4_MouseUp(object sender, MouseEventArgs e)
        {
            do_brightness_contrast(0);
            measure_brightness(pictureBox1, pictureBox4);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
            {
                pictureBox1.Image = pictureBox0.Image;
                //richTextBox1.Text += pictureBox1.Name + " 無影像, 離開\n";
                //return;
            }

            //顏色統計
            richTextBox1.Text += "顏色統計\n";

            int[] r_data = new int[256];
            int[] g_data = new int[256];
            int[] b_data = new int[256];

            //Bitmap bitmap1 = new Bitmap(filename);
            Bitmap bitmap1 = (Bitmap)pictureBox1.Image;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            int i;
            int j;

            for (j = 0; j < H; j++)
            {
                for (i = 0; i < W; i++)
                {
                    byte rr = bitmap1.GetPixel(i, j).R;
                    byte gg = bitmap1.GetPixel(i, j).G;
                    byte bb = bitmap1.GetPixel(i, j).B;

                    r_data[rr]++;
                    g_data[gg]++;
                    b_data[bb]++;
                }
            }

            int ww = 512;
            int hh1 = 300;
            int hh2 = 256;
            Bitmap bitmap2 = new Bitmap(ww, hh1);
            Graphics g2 = Graphics.FromImage(bitmap2);
            g2.Clear(Color.Black);

            Pen p = new Pen(Color.Red, 2);

            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh1 - 2);
            g2.DrawRectangle(p, 0 + 1, 0 + 1, ww - 2, hh2 - 2);

            draw_rgb_data(g2, r_data, Color.Red);
            draw_rgb_data(g2, b_data, Color.Blue);
            draw_rgb_data(g2, g_data, Color.Green);

            pictureBox2.Image = bitmap2;
        }

        void draw_rgb_data(Graphics g, int[] rgb_data, Color c)
        {
            int hh2 = 256;
            int i;
            int most = 0;
            for (i = 0; i < 256; i++)
            {
                //richTextBox1.Text += r_data[i].ToString() + " ";
                if (rgb_data[i] > most)
                    most = rgb_data[i];
                if (rgb_data[i] == 0)
                    rgb_data[i] = 5;
            }
            //richTextBox1.Text += "\n最多 " + most.ToString() + "\n";

            double ratio = 0;
            ratio = (double)hh2 / most;

            //richTextBox1.Text += "ratio = " + ratio.ToString() + "\n";

            /*
            // 畫柱狀圖
            Brush b = new SolidBrush(Color.FromArgb(150, c.R, c.G, c.B));

            for (i = 0; i < 256; i++)
            {
                //g2.FillRectangle(Brushes.Red, i * 2, 0, 2, (float)(r_data[i] * ratio));
                g.FillRectangle(b, i * 2, hh2 - (float)(rgb_data[i] * ratio), 2, (float)(rgb_data[i] * ratio));
            }
            */

            // 畫曲線圖
            Pen p = new Pen(c, 1);

            Point[] curvePoints = new Point[256];    //一維陣列內有 8 個Point
            for (i = 0; i < 256; i++)
            {
                curvePoints[i].X = i * 2;
                curvePoints[i].Y = (int)(hh2 - (float)(rgb_data[i] * ratio));
            }

            // Draw lines between original points to screen.
            g.DrawLines(p, curvePoints);   //畫直線
            // Draw curve to screen.
            //g.DrawCurve(redPen, curvePoints); //畫曲線
        }

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            flag_no_update_crop_picture = true;
            if (checkBox1.Checked == true)
            {
                button1.Enabled = false;
                x_st = 0;
                y_st = 0;
                w = 640;
                h = 480;
            }
            else
            {
                button1.Enabled = true;
                x_st = 50;
                y_st = 50;
                w = 640 - 100;
                h = 480 - 100;
            }
            nud_x_st.Value = x_st;
            nud_y_st.Value = y_st;
            nud_w.Value = w;
            nud_h.Value = h;
            flag_no_update_crop_picture = false;
        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (((RadioButton)sender).Checked == true)
            {
                Form1_Load(sender, e);
            }
        }
    }
}

