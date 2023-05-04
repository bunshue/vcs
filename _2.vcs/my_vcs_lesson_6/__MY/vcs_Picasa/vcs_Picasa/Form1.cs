using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

namespace vcs_Picasa
{
    public partial class Form1 : Form
    {
        Graphics g;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //新建圖檔, 初始化畫布
            int W = 1920;
            int H = 1080;

            bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.Pink);

            //圖片的中心, 依此中心旋轉
            int cx = W / 2;
            int cy = H / 2;

            string filename = @"C:\______test_files1\picture1.jpg";

            int angle = 0;

            angle = -20;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            angle = 20;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            angle = 0;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            cx = 0+200;
            cy = 0+200;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            this.BackgroundImageLayout = ImageLayout.None;
            this.BackgroundImage = bitmap1;
        }

        void show_item_location()
        {
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
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

        void draw_bitmap_with_angle(string filename, Graphics g, int cx, int cy, int angle)
        {
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            Pen p = new Pen(Color.Red, 3);

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int x_st = cx - w / 2;   //圖片未旋轉時的原點(左上角)
            int y_st = cy - h / 2;

            g.ResetTransform();

            if (angle == 0)
            {
                //僅需平移
                g.TranslateTransform(x_st, y_st);   //平移原點 再右移 再下移 然後再進行畫圖

            }
            else
            {
                //需要平移
                //需要旋轉

                double radius = Math.Sqrt(w * w + h * h) / 2;

                double theta0 = Math.Atan((double)h / (double)w);
                //richTextBox1.Text += "theta0 = " + theta0.ToString() + " 弧度\n";
                //richTextBox1.Text += "theta0 = " + (theta0 * 180 / Math.PI).ToString() + " 度\n";

                double theta1 = theta0 + Math.PI * angle / 180;
                //richTextBox1.Text += "theta1 = " + theta1.ToString() + " 弧度\n";
                //richTextBox1.Text += "theta1 = " + (theta1 * 180 / Math.PI).ToString() + " 度\n";

                double x1 = radius * Math.Cos(theta1);
                double y1 = radius * Math.Sin(theta1);
                //richTextBox1.Text += "x1 = " + x1.ToString() + "\n";
                //richTextBox1.Text += "y1 = " + y1.ToString() + "\n";

                g.TranslateTransform(x_st + w / 2 - (float)x1, y_st + h / 2 - (float)y1);   //平移原點 再右移 再下移 然後再進行畫圖
                g.RotateTransform(angle);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
            }
            g.DrawImage(bitmap1, 0, 0, w, h);
            g.DrawRectangle(p, 0, 0, w, h);




        }


    }
}
