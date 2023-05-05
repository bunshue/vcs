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

//平移縮放旋轉

namespace vcs_Draw_Transform1
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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
        }

        //平移, 旋轉
        private void button0_Click(object sender, EventArgs e)
        {
            //準備
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(10, 10, 200, 50);

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int x_st = 50;
            int y_st = 50;
            Point p0 = new Point(0, 0);
            Point p1 = new Point(400, 0);
            Point p2 = new Point(0, 400);


            //原本的, 做相同的事
            p.Color = Color.Red;
            g.DrawRectangle(p, rect);   //用紅色筆畫矩形
            g.DrawString("平移, 紅色是原本的, 綠色是平移後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));
            g.DrawImage(bitmap1, x_st, y_st, w / 2, h / 2);
            g.DrawLine(p, p0, p1);
            g.DrawLine(p, p0, p2);


            g.DrawLine(p, p0.X + 150, p0.Y + 400, p1.X + 150, p1.Y + 400);
            g.DrawLine(p, p0.X + 150, p0.Y + 400, p2.X + 150, p2.Y + 400);

            //平移
            g.TranslateTransform(150, 400);  //平移原點 再右移 再下移 然後再進行畫圖

            if (checkBox2.Checked == true)
            {
                g.SmoothingMode = SmoothingMode.AntiAlias;
            }

            if (checkBox1.Checked == true)
            {
                g.RotateTransform(10);  //依原點旋轉
            }

            //平移後的, 做相同的事
            p.Color = Color.Green;
            p.Width = 3;
            g.DrawRectangle(p, rect);   //用綠色筆畫平移後的圖形
            g.DrawString("平移, 紅色是原本的, 綠色是平移後的", new Font("標楷體", 16), new SolidBrush(Color.Green), new PointF(0, 0));
            g.DrawImage(bitmap1, x_st, y_st, w / 2, h / 2);
            g.DrawLine(p, p0, p1);
            g.DrawLine(p, p0, p2);

            //恢復
            g.ResetTransform();
            g.Dispose();
            p.Dispose();
        }

        //旋轉
        private void button1_Click(object sender, EventArgs e)
        {
            int i;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);

            //未旋轉
            g.TranslateTransform(100, 100);   //平移原點 再右移 再下移 然後再進行畫圖

            g.DrawLine(p, 0, 0, 50, 0);
            for (i = 0; i < 10; i++)
            {
                g.TranslateTransform(50, 0);   //平移原點 再右移 再下移 然後再進行畫圖
                //g.RotateTransform(30);
                g.DrawLine(p, 0, 0, 50, 0);
            }

            //旋轉
            g.ResetTransform();
            g.TranslateTransform(100, 200);   //平移原點 再右移 再下移 然後再進行畫圖
            p.Color = Color.Green;
            g.DrawLine(p, 0, 0, 50, 0);
            for (i = 0; i < 10; i++)
            {
                g.TranslateTransform(50, 0);   //平移原點 再右移 再下移 然後再進行畫圖
                g.RotateTransform(30);
                g.DrawLine(p, 0, 0, 50, 0);
            }

            g.ResetTransform(); //恢復
            g.DrawString("旋轉, 紅色是原本的, 綠色是旋轉後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));

            g.Dispose();
            p.Dispose();
        }

        //縮放
        private void button2_Click(object sender, EventArgs e)
        {
            Font f = new Font("標楷體", 40);

            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);

            draw_grid(g);

            int w = 0;
            int h = 0;
            string str = "放大縮小";

            w = g.MeasureString(str, f).ToSize().Width;
            h = g.MeasureString(str, f).ToSize().Height;

            Pen p = new Pen(Color.Red, 3);

            g.DrawString("放大縮小1", f, new SolidBrush(Color.Blue), new PointF(0, 0));
            Rectangle rect1 = new Rectangle(0, 0, w / 4, h);
            g.DrawRectangle(p, rect1);   //用紅色筆畫矩形

            g.ScaleTransform(-1, 1);
            g.DrawString("反向字體", f, new SolidBrush(Color.Blue), new PointF(-w * 1, h));

            g.ResetTransform();
            g.ScaleTransform(0.5f, 2);  //x軸比例再放大, y軸比例再放大
            g.DrawString("放大縮小2", f, new SolidBrush(Color.Blue), new PointF(0, h * 1));
            Rectangle rect2 = new Rectangle(0, h * 1, w / 4, h);
            g.DrawRectangle(p, rect2);   //用紅色筆畫矩形

            g.ResetTransform();
            g.ScaleTransform(2.0f, 1);  //x軸比例再放大, y軸比例再放大
            g.DrawString("放大縮小3", f, new SolidBrush(Color.Blue), new PointF(0, h * 5));
            Rectangle rect3 = new Rectangle(0, h * 5, w / 4, h);
            g.DrawRectangle(p, rect3);   //用紅色筆畫矩形

            g.ResetTransform();
            g.ScaleTransform(3.0f, 3);  //x軸比例再放大, y軸比例再放大
            g.DrawString("放大縮小4", f, new SolidBrush(Color.Blue), new PointF(0, h * 3));
            Rectangle rect4 = new Rectangle(0, h * 3, w / 4, h);
            g.DrawRectangle(p, rect4);   //用紅色筆畫矩形

            //恢復比例, 寫說明
            w = w / 4 * 7;
            f = new Font("標楷體", 20);
            //標示放大縮小比例
            g.ResetTransform();
            g.DrawString("正常", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 0));
            g.DrawString("X負一倍, Y不變", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 1));
            g.DrawString("X一半, Y一倍", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 2));
            g.DrawString("X一倍, Y不變", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 6));
            g.DrawString("X三倍, Y三倍", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 8));

            g.Dispose();
            f.Dispose();
        }

        void draw_grid(Graphics g)
        {
            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;
            int i;
            int j;

            Font f = new Font("標楷體", 40);

            int w = 0;
            int h = 0;
            string str = "放大縮小";

            w = g.MeasureString(str, f).ToSize().Width;
            h = g.MeasureString(str, f).ToSize().Height;
            richTextBox1.Text += "w = " + (w / 4).ToString() + ", h = " + h.ToString() + "\n";

            for (i = 0; i <= W; i += w / 4)
            {
                g.DrawLine(Pens.Gray, i, 0, i, H);
            }
            for (j = 0; j <= H; j += h)
            {
                g.DrawLine(Pens.Gray, 0, j, W, j);
            }
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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
            //Pen p = new Pen(Color.Red, 3);
            g.Clear(Color.Pink);

            //圖片的中心, 依此中心旋轉
            int cx = W / 2;
            int cy = H / 2;

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";

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
            //旋轉一張圖片

            string filename = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = Image.FromFile(filename);

            #region 影像旋轉(以中心順時針轉10度)
            //建立新的影像
            Image rotateImage = new Bitmap(pictureBox1.Image.Width, pictureBox1.Image.Height) as Image;
            //準備繪製新的影像
            Graphics g = Graphics.FromImage(rotateImage);
            //設定中心點
            g.TranslateTransform((float)pictureBox1.Image.Width / 2, (float)pictureBox1.Image.Height / 2);
            //順時針轉10度
            g.RotateTransform(10);
            //還原中心點
            g.TranslateTransform(-(float)pictureBox1.Image.Width / 2, -(float)pictureBox1.Image.Height / 2);
            //於座標(0,0)開始繪製來源影像
            g.DrawImage(pictureBox1.Image, 0, 0, pictureBox1.Image.Width, pictureBox1.Image.Height);
            g.Dispose();
            pictureBox1.Image = rotateImage;

            /*
            //儲存新的影像
            string filename = Application.StartupPath + "\\rotate_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            rotateImage.Save(@filename, ImageFormat.Jpeg);
            richTextBox1.Text += "影像旋轉，存檔完成，檔名：" + filename + "\n";
            */
            #endregion
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
