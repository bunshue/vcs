using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;

//平移縮放旋轉

namespace vcs_Draw7_Transform2
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
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 140 + 10;
            dy = 50 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            bt_save.Location = new Point(x_st + dx * 0, y_st + dy * 12);

            pictureBox1.Location = new Point(160, 10);
            richTextBox1.Location = new Point(820, 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //平移 旋轉 座標軸

            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);

            richTextBox1.Text += "平移坐標軸至指定座標(100, 100) 然後畫一線\n";
            g.TranslateTransform(100, 100);
            g.DrawLine(p, 0, 0, 100, 0);
            g.ResetTransform();

            richTextBox1.Text += "平移坐標軸至指定座標(200, 200) 然後再進行旋轉座標畫線\n";
            g.TranslateTransform(200, 200);
            for (int i = 0; i < 8; i++)
            {
                //g.RotateTransform(45);
                g.RotateTransform(10);//旋轉指定的角度
                g.DrawLine(p, 0, 0, 100, 0);
            }
            g.Dispose();
        }

        //平移
        private void button1_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);

            g.DrawRectangle(p, rect);   //用紅色筆畫矩形

            //向左平移100向下平移50
            g.TranslateTransform(100, 50);
            p.Color = Color.Green;
            g.DrawRectangle(p, rect);   //用綠色筆畫平移後的圖形

            g.ResetTransform(); //恢復
            g.DrawString("平移, 紅色是原本的, 綠色是平移後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));

            g.Dispose();
            p.Dispose();
        }

        //縮放
        private void button2_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);
            g.DrawRectangle(p, rect);   //用紅色筆畫矩形
            g.ScaleTransform(0.5f, 2);

            p.Color = Color.Green;
            g.DrawRectangle(p, rect);   //用綠色筆畫縮放後的圖形

            g.ResetTransform(); //恢復
            g.DrawString("縮放, 紅色是原本的, 綠色是縮放後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));

            g.Dispose();
            p.Dispose();

            //寬縮小一半，高放大一倍
        }

        //旋轉
        //坐標原點為矩形的左上點
        private void button3_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);
            g.DrawRectangle(p, rect);   //用紅色筆畫矩形
            g.TranslateTransform(200, 0);
            g.RotateTransform(90);

            p.Color = Color.Green;
            g.DrawRectangle(p, rect);   //用綠色筆畫旋轉後的圖形

            g.ResetTransform(); //恢復
            g.DrawString("旋轉, 紅色是原本的, 綠色是旋轉後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));

            g.Dispose();
            p.Dispose();

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //字串旋轉列印
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawString("字串旋轉列印", new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(20, 20));

            Font f = new Font("標楷體", 50);
            RotateDeawString(g, f, 35, "字串旋轉列印", 20, 20);


        }

        /// <summary>
        /// 旋轉列印字串
        /// </summary>
        /// <param name="e">PrintPageEventArgs</param>
        /// <param name="font">字型</param>
        /// <param name="degree">旋轉角度</param>
        /// <param name="msg">列印訊息</param>
        /// <param name="x">重設原點 X 位置</param>
        /// <param name="y">重設原點 Y 位置</param>
        private void RotateDeawString(Graphics g, Font font, int degree, string msg, int x, int y)
        {
            // 原點位置重設
            g.TranslateTransform(mmTo100InchX(x), mmTo100InchY(y));
            // 設定旋轉角度
            g.RotateTransform(degree);
            // 標題
            g.DrawString(msg, font, Brushes.Black, mmTo100InchX(0), mmTo100InchY(0));
            //繪圖畫布還原
            g.ResetTransform();
        }

        private int mmTo100InchX(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }

        private int mmTo100InchY(int mm)
        {
            int times = 100;
            double result = (mm * times / 25.4);
            return (int)Math.Floor(result);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //轉變座標軸角度

            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(0, 0, 200, 50);

            richTextBox1.Text += "轉變坐標軸角度\n";

            for (int i = 0; i <= 90; i += 10)
            {
                g.RotateTransform(i);//旋轉指定的角度
                g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
                g.ResetTransform();//恢復坐標軸坐標 回 0 度
            }

            p = new Pen(Color.Blue, 2);
            g.RotateTransform(20);//旋轉指定的角度
            g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
            g.ResetTransform();//恢復坐標軸坐標 回 0 度

            g.RotateTransform(30);//旋轉指定的角度
            g.DrawLine(p, 0, 0, 500, 0);    //畫一條線
            g.ResetTransform();//恢復坐標軸坐標 回 0 度

            g.Dispose();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int W = 305 * 2;
            int H = 400 * 2;

            pictureBox1.Size = new Size(W, H);

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);
            Pen p = new Pen(Color.Red, 3);
            g.Clear(Color.Pink);

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int x_st = 0;
            int y_st = 0;
            x_st = 0;
            y_st = 0;

            g.TranslateTransform(305, 400); //平移原點 再右移 再下移 然後再進行畫圖
            //                  貼上的位置  貼上的大小 放大縮小用
            g.DrawImage(bitmap1, x_st, y_st, w, h);
            g.DrawString("未旋轉", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 100, 10));

            int i;
            for (i = 0; i < 9; i++)
            {
                g.RotateTransform(20);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
                g.DrawImage(bitmap1, x_st, y_st, w, h);
                g.DrawString(((i + 1) * 20).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }
            g.ResetTransform();
            g.DrawImage(bitmap1, x_st + 305, y_st, w, h);
            g.DrawString("原圖平移", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 + 305 - 130, 10));

            pictureBox1.Image = bitmap2;

        }

        private void button7_Click(object sender, EventArgs e)
        {
            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int W = 305 * 2;
            int H = 400 * 2;

            pictureBox1.Size = new Size(W, H);

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);
            Pen p = new Pen(Color.Red, 3);
            g.Clear(Color.Pink);

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int x_st = 0;
            int y_st = 0;
            x_st = 0;
            y_st = 0;

            g.TranslateTransform(305, 400 / 2); //平移原點 再右移 再下移 然後再進行畫圖

            int i;
            for (i = 0; i < 18; i++)
            {
                g.RotateTransform(20);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
                g.DrawImage(bitmap1, x_st, y_st, (w / 2), (h / 2));
                //g.DrawString(((i + 1) * 20).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }

            g.TranslateTransform(0, 400);   //平移原點 再右移 再下移 然後再進行畫圖
            for (i = 0; i < 18; i++)
            {
                g.RotateTransform(20);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
                g.DrawImage(bitmap1, x_st, y_st, (w / 2), (h / 2));
                //g.DrawString(((i + 1) * 20).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }

            g.ResetTransform();
            //g.DrawImage(bitmap1, x_st + 305, y_st, w / 2, h / 2);
            //g.DrawString("原圖平移", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 + 305 - 130, 10));

            pictureBox1.Image = bitmap2;
        }

        private void button8_Click(object sender, EventArgs e)
        {
            int W = 305 * 2;
            int H = 400 * 2;

            pictureBox1.Size = new Size(W, H);

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);
            Pen p = new Pen(Color.Red, 3);
            g.Clear(Color.Pink);

            //圖片的中心, 依此中心旋轉
            int cx = W / 2;
            int cy = H / 2;

            string filename = @"C:\______test_files\picture1.jpg";

            int angle = 0;

            for (angle = 0; angle <= 360; angle += 20)
            {
                draw_bitmap_with_angle(filename, g, cx, cy, angle);
            }

            /*
            angle = 20;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            angle = 40;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);

            angle = 60;
            draw_bitmap_with_angle(filename, g, cx, cy, angle);
            */

            pictureBox1.Image = bitmap2;
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



        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            if (pictureBox1.Image == null)
            {
                richTextBox1.Text += "無圖片, 離開\n";
                return;
            }


            Image image = new Bitmap(pictureBox1.Image.Width, pictureBox1.Image.Height) as Image;

            //儲存新的影像
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";

            try
            {
                //bitmap1.Save(@file1, ImageFormat.Jpeg);
                image.Save(filename, ImageFormat.Bmp);
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
    }
}

