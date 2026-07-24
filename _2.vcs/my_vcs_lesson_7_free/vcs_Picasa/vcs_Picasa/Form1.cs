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
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            do_picasa();
        }

        void show_item_location()
        {
            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;  // 設定無邊框
            this.WindowState = FormWindowState.Maximized;
        }

        private void Form1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();
        }

        //------------------------------------------------------------  # 60個

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

        void do_picasa()
        {
            //新建圖檔, 初始化畫布
            int W = 1920;
            int H = 1080;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);

            g.Clear(Color.Pink);

            //圖片的中心, 依此中心旋轉
            int cx = W / 2;
            int cy = H / 2;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            int angle = 0;

            angle = -20;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            angle = 20;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            angle = 0;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            cx = 0 + 200;
            cy = 0 + 200;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            this.BackgroundImageLayout = ImageLayout.None;
            this.BackgroundImage = bitmap1;

        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個


