using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode //提供畫高級二維，矢量圖形功能
using System.Drawing.Imaging;   //for ImageFormat   //提供畫GDI+圖形的高級功能

using System.Runtime.InteropServices;   //for Marshal

using System.Drawing.Text;      //for TextRenderingHint //提供畫GDI+圖形的高級功能

using System.Diagnostics;       //for Debug
using System.Reflection;    //PropertyInfo
using System.Threading;

using System.IO;

namespace vcs_Draw_Example3
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        //重寫表單的OnPaint範例 直接寫在此即可
        protected override void OnPaint(PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 5, 5, this.Width - 10, this.Height - 10);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 2);     // 設定畫筆為紅色、粗細為 2 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            timer_random_pattern_Tick(sender, e);
        }

        void show_item_location()
        {
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1050;
            y_st = 10;
            dx = 140;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button5.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button9.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button11.Location = new Point(x_st + dx * 5, y_st + dy * 1);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button16.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button17.Location = new Point(x_st + dx * 5, y_st + dy * 2);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button21.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button22.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button23.Location = new Point(x_st + dx * 5, y_st + dy * 3);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button27.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button28.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 5, y_st + dy * 4);

            button30.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button34.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button35.Location = new Point(x_st + dx * 5, y_st + dy * 5);

            button36.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button38.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button40.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button41.Location = new Point(x_st + dx * 5, y_st + dy * 6);

            button42.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button43.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button44.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button45.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            button47.Location = new Point(x_st + dx * 5, y_st + dy * 7);

            button48.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button50.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button51.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button52.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            button53.Location = new Point(x_st + dx * 5, y_st + dy * 8);

            button54.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button55.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button56.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button57.Location = new Point(x_st + dx * 3, y_st + dy * 9);
            button58.Location = new Point(x_st + dx * 4, y_st + dy * 9);
            button59.Location = new Point(x_st + dx * 5, y_st + dy * 9);

            button60.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button61.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button62.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button63.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            button64.Location = new Point(x_st + dx * 4, y_st + dy * 10);
            button65.Location = new Point(x_st + dx * 5, y_st + dy * 10);

            button66.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button67.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button68.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            button69.Location = new Point(x_st + dx * 3, y_st + dy * 11);
            button70.Location = new Point(x_st + dx * 4, y_st + dy * 11);
            button71.Location = new Point(x_st + dx * 5, y_st + dy * 11);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 12);

            bt_reset.Location = new Point(x_st + dx * 4, y_st + dy * 15);
            bt_save.Location = new Point(x_st + dx * 5, y_st + dy * 15);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 16);
            richTextBox1.Size = new Size(richTextBox1.Size.Width + 200, 250);

            pictureBox1.Location = new Point(10, 10);
            pictureBox1.Size = new Size(900, 600);
            pictureBox1.BackColor = Color.White;

            int W = 250;
            int H = 250;
            x_st = 10;
            //y_st = 800;
            dx = W + 10;
            pictureBox_random0.Location = new Point(x_st + dx * 0, y_st + dy * 16);
            pictureBox_random1.Location = new Point(x_st + dx * 1, y_st + dy * 16);
            pictureBox_random2.Location = new Point(x_st + dx * 2, y_st + dy * 16);
            pictureBox_random3.Location = new Point(x_st + dx * 3, y_st + dy * 16);
            pictureBox_random0.Size = new Size(W, H);
            pictureBox_random1.Size = new Size(W, H);
            pictureBox_random2.Size = new Size(W, H);
            pictureBox_random3.Size = new Size(W, H);
            pictureBox_random0.BackColor = Color.Pink;
            pictureBox_random1.BackColor = Color.Pink;
            pictureBox_random2.BackColor = Color.Pink;
            pictureBox_random3.BackColor = Color.Pink;


            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
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
            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            pictureBox1.Location = new Point(10, 10);
            pictureBox1.Size = new Size(900, 600);
            pictureBox1.BackColor = Color.White;
            pictureBox1.SizeMode = PictureBoxSizeMode.Normal;

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            //----開新的Bitmap----
            bitmap1 = new Bitmap(W, H);
            //----使用上面的Bitmap畫圖----
            g = Graphics.FromImage(bitmap1);

            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        //沒用到????
        void open_new_file()
        {
            richTextBox1.Text += "開啟一個 640 X 480 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = 640;
            pictureBox1.Height = 480;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                string filename1 = filename + ".jpg";
                string filename2 = filename + ".bmp";
                string filename3 = filename + ".png";

                try
                {
                    bitmap1.Save(@filename1, ImageFormat.Jpeg);
                    bitmap1.Save(@filename2, ImageFormat.Bmp);
                    bitmap1.Save(@filename3, ImageFormat.Png);

                    richTextBox1.Text += "存檔成功\n";
                    richTextBox1.Text += "已存檔 : " + filename1 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename2 + "\n";
                    richTextBox1.Text += "已存檔 : " + filename3 + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            else
                richTextBox1.Text += "無圖可存\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
        }

        private void button21_Click(object sender, EventArgs e)
        {
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
        }

        private void button32_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button36_Click(object sender, EventArgs e)
        {
        }

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
        }

        private void button39_Click(object sender, EventArgs e)
        {
        }

        private void button40_Click(object sender, EventArgs e)
        {
        }

        private void button41_Click(object sender, EventArgs e)
        {
        }

        private void button42_Click(object sender, EventArgs e)
        {
        }

        private void button43_Click(object sender, EventArgs e)
        {
        }

        private void button44_Click(object sender, EventArgs e)
        {
        }

        private void button45_Click(object sender, EventArgs e)
        {
        }

        private void button46_Click(object sender, EventArgs e)
        {
        }

        private void button47_Click(object sender, EventArgs e)
        {
        }

        private void button48_Click(object sender, EventArgs e)
        {
        }

        private void button49_Click(object sender, EventArgs e)
        {
        }

        private void button50_Click(object sender, EventArgs e)
        {
        }

        private void button51_Click(object sender, EventArgs e)
        {
        }

        private void button52_Click(object sender, EventArgs e)
        {
        }

        private void button53_Click(object sender, EventArgs e)
        {
        }

        private void button54_Click(object sender, EventArgs e)
        {
        }

        private void button55_Click(object sender, EventArgs e)
        {
        }

        private void button56_Click(object sender, EventArgs e)
        {
        }

        private void button57_Click(object sender, EventArgs e)
        {
        }

        private void button58_Click(object sender, EventArgs e)
        {
        }

        private void button59_Click(object sender, EventArgs e)
        {
        }

        private void button60_Click(object sender, EventArgs e)
        {
        }

        private void button61_Click(object sender, EventArgs e)
        {
        }

        private void button62_Click(object sender, EventArgs e)
        {
        }

        private void button63_Click(object sender, EventArgs e)
        {
        }

        private void button64_Click(object sender, EventArgs e)
        {
        }

        private void button65_Click(object sender, EventArgs e)
        {
        }

        private void button66_Click(object sender, EventArgs e)
        {
        }

        private void button67_Click(object sender, EventArgs e)
        {
        }

        private void button68_Click(object sender, EventArgs e)
        {
        }

        private void button69_Click(object sender, EventArgs e)
        {
        }

        private void button70_Click(object sender, EventArgs e)
        {
        }

        private void button71_Click(object sender, EventArgs e)
        {
        }

        private void bt_long0_Click(object sender, EventArgs e)
        {
        }

        private void bt_long1_Click(object sender, EventArgs e)
        {
        }

        private void bt_long2_Click(object sender, EventArgs e)
        {
        }

        private void bt_long3_Click(object sender, EventArgs e)
        {
        }

        private void bt_long4_Click(object sender, EventArgs e)
        {
        }

        private void bt_long5_Click(object sender, EventArgs e)
        {
        }

        private void bt_long6_Click(object sender, EventArgs e)
        {
        }

        private void bt_long7_Click(object sender, EventArgs e)
        {
        }

        private void bt_long8_Click(object sender, EventArgs e)
        {
        }

        private void bt_long9_Click(object sender, EventArgs e)
        {
        }

        private void bt_long10_Click(object sender, EventArgs e)
        {
        }

        private void bt_long11_Click(object sender, EventArgs e)
        {
        }

        private int RetrievRandomCorners(int minCorners, int maxCorners)
        {
            return new Random(Guid.NewGuid().GetHashCode()).Next(minCorners, maxCorners);
        }

        void draw_random_pattern(int type, int minCorners, int maxCorners, PictureBox pbox)
        {
            int width = pbox.Width;
            int height = pbox.Height;
            int numX = 10;
            int numY = 10;
            float perX = width * 1f / numX;
            float perY = height * 1f / numY;
            Bitmap bitmap1 = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bitmap1);

            g.CompositingQuality = CompositingQuality.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;

            g.FillRectangle(Brushes.Black, new Rectangle(0, 0, width, height));

            int lastCorners = minCorners;
            for (int i = 0; i < numX; i++)
            {
                for (int j = 0; j < numY; j++)
                {
                    long tick = DateTime.Now.Ticks;
                    Random random = new Random((int)(tick & 0xffffffff) | (int)(tick >> 32));
                    int corners = random.Next(minCorners, maxCorners);
                    if (Math.Abs(corners - lastCorners) < (maxCorners - minCorners) / 2)
                    {
                        corners = RetrievRandomCorners(minCorners, maxCorners);
                    }
                    lastCorners = corners;

                    if (type == 0)
                    {
                        //this.Text = "竹葉";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 1.4f), (int)(perX * 0.009f), corners);
                        g.FillClosedCurve(Brushes.Green, points, FillMode.Winding);
                    }
                    else if (type == 1)
                    {
                        //this.Text = "長葉草";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.88f), (int)(perX * 0.01f), corners);
                        g.FillClosedCurve(Brushes.Green, points, FillMode.Winding);
                    }
                    else if (type == 2)
                    {
                        //this.Text = "雜亂石頭";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.4f), (int)(perX * 0.396f), corners);
                        g.FillClosedCurve(Brushes.Gray, points, FillMode.Winding);
                    }
                    else if (type == 3)
                    {
                        //this.Text = "天上繁星";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.18f), (int)(perX * 0.06f), corners);
                        g.FillClosedCurve(Brushes.White, points, FillMode.Winding);
                    }
                    else
                    {
                        //this.Text = "未選取";
                        return;
                    }
                }
            }
            pbox.Image = bitmap1;
        }

        void draw_random_pattern0()
        {
            //this.Text = "竹葉";
            int type = 0;
            int minCorners = 3;
            int maxCorners = 4;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox_random0);
        }

        void draw_random_pattern1()
        {
            //this.Text = "長葉草";
            int type = 1;
            int minCorners = 20;
            int maxCorners = 38;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox_random1);
        }

        void draw_random_pattern2()
        {
            //this.Text = "雜亂石頭";
            int type = 2;
            int minCorners = 3;
            int maxCorners = 4;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox_random2);
        }

        void draw_random_pattern3()
        {
            //this.Text = "天上繁星";
            int type = 3;
            int minCorners = 3;
            int maxCorners = 4;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox_random3);
        }

        private void timer_random_pattern_Tick(object sender, EventArgs e)
        {
            //模擬雜亂無章的現實場景
            draw_random_pattern0();
            draw_random_pattern1();
            draw_random_pattern2();
            draw_random_pattern3();

        }
    }
    public static class Stone
    {
        public static PointF[] CreateStone(Point center, int outerRadius, int inner_radius, int arms)
        {
            int center_x = center.X;
            int center_y = center.Y;
            PointF[] points = new PointF[arms * 2];
            double offset = Math.PI / 2;
            double arc = 2 * Math.PI / arms;
            double half = arc / 2;
            double angle = 0;
            for (int i = 0; i < arms; i++)
            {
                Random randomOuter = new Random((int)DateTime.Now.Ticks);
                outerRadius = outerRadius - randomOuter.Next((int)(inner_radius * 0.06 * new Random().Next(-20, 20) / 30d), (int)(inner_radius * 0.08));
                //outerRadius = outerRadius - randomOuter.Next((int)(inner_radius * 0.16 * new Random().Next(-20, 20) / 30d), (int)(inner_radius * 0.18));
                Random randomInner = new Random(Guid.NewGuid().GetHashCode());
                inner_radius = inner_radius + randomInner.Next((int)(inner_radius * 0.02 * new Random().Next(-100, 100) / 150d), (int)(inner_radius * 0.08));
                //inner_radius = inner_radius + randomInner.Next((int)(inner_radius * 0.02 * new Random().Next(-100, 100) / 150d), (int)(inner_radius * 0.22));

                if (inner_radius > outerRadius)
                {
                    int temp = outerRadius;
                    outerRadius = inner_radius;
                    inner_radius = temp;
                }
                double angleTemp = arc * randomInner.Next(-5, 5) / 10d;
                angle = i * arc;
                angle += angleTemp;
                points[i * 2].X = (float)(center_x + Math.Cos(angle - offset) * outerRadius);
                points[i * 2].Y = (float)(center_y + Math.Sin(angle - offset) * outerRadius);
                points[i * 2 + 1].X = (float)(center_x + Math.Cos(angle + half - offset) * inner_radius);
                points[i * 2 + 1].Y = (float)(center_y + Math.Sin(angle + half - offset) * inner_radius);
            }

            return points;
        }
    }
}
