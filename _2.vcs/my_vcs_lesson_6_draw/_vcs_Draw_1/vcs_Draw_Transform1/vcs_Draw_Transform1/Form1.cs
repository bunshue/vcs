using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D; //SmoothingMode

//平移縮放旋轉

namespace vcs_Draw_Transform1
{
    public partial class Form1 : Form
    {
        List<double> x = new List<double>();
        List<double> y = new List<double>();

        int xmin;
        int xmax;
        float ymin;
        float ymax;
        float xmargin_perncent = 5;
        float ymargin_perncent = 5;
        float xmargin;
        float ymargin;
        float xratio;
        float yratio;

        Point[] Points = new Point[8];    //一維陣列內有 8 個Point

        Bitmap bitmap1;
        Graphics g;
        SolidBrush sb1 = new SolidBrush(Color.Red);
        SolidBrush sb2 = new SolidBrush(Color.Green);
        SolidBrush sb3 = new SolidBrush(Color.Blue);

        //string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\volkswagen.png";
        Bitmap bmp;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;

            bmp = new Bitmap(filename);
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
            dx = 200 + 10;
            dy = 60 + 5;

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
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            pictureBox1.Size = new Size(820, 600);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            richTextBox1.Size = new Size(300, 700);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 760);
            this.Text = "vcs_Draw_Transform1";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();

            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);
            pictureBox1.Image = bitmap1;
        }

        //平移, 旋轉
        private void button0_Click(object sender, EventArgs e)
        {
            //準備
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(10, 10, 200, 50);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
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

            // 平移, 右移, 下移
            g.TranslateTransform(150, 400);

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

            g.ResetTransform();  // 重置轉換, 恢復

            g.Dispose();
            p.Dispose();
        }

        //旋轉
        private void button1_Click(object sender, EventArgs e)
        {
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);

            // 未旋轉, 平移 + 畫線
            // Reset後, 移動原點
            g.TranslateTransform(100, 100);// 平移, 右移, 下移
            g.DrawString("無旋轉", new Font("標楷體", 16), new SolidBrush(Color.Red), new PointF(0, 0));

            g.DrawLine(p, 0, 0, 50, 0);
            for (int i = 0; i < 10; i++)
            {
                // 平移, 右移, 下移
                g.TranslateTransform(50, 0);
                //g.RotateTransform(30);
                g.DrawLine(p, 0, 0, 50, 0);
            }

            //6060

            g.ResetTransform();  // 重置轉換, 恢復

            // 旋轉, 平移 + 旋轉 + 畫線
            // Reset後, 移動原點
            g.TranslateTransform(100, 200);  // 平移, 右移, 下移
            g.DrawString("有旋轉", new Font("標楷體", 16), new SolidBrush(Color.Green), new PointF(0, 0));

            p = new Pen(Color.Green, 5);
            g.DrawLine(p, 0, 0, 50, 0);
            for (int i = 0; i < 10; i++)
            {
                // 平移, 右移, 下移
                g.TranslateTransform(50, 0);
                g.RotateTransform(30);
                g.DrawLine(p, 0, 0, 50, 0);
            }

            g.ResetTransform();  // 重置轉換, 恢復

            pictureBox1.Image = bitmap1;
        }

        //縮放
        private void button2_Click(object sender, EventArgs e)
        {
            Font f = new Font("標楷體", 40);

            g.Clear(Color.White);
            draw_grid1(g);

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

            g.ResetTransform();  // 重置轉換, 恢復

            g.ScaleTransform(0.5f, 2);  //x軸比例再放大, y軸比例再放大
            g.DrawString("放大縮小2", f, new SolidBrush(Color.Blue), new PointF(0, h * 1));
            Rectangle rect2 = new Rectangle(0, h * 1, w / 4, h);
            g.DrawRectangle(p, rect2);   //用紅色筆畫矩形

            g.ResetTransform();  // 重置轉換, 恢復

            g.ScaleTransform(2.0f, 1);  //x軸比例再放大, y軸比例再放大
            g.DrawString("放大縮小3", f, new SolidBrush(Color.Blue), new PointF(0, h * 5));
            Rectangle rect3 = new Rectangle(0, h * 5, w / 4, h);
            g.DrawRectangle(p, rect3);   //用紅色筆畫矩形

            g.ResetTransform();  // 重置轉換, 恢復

            g.ScaleTransform(3.0f, 3);  //x軸比例再放大, y軸比例再放大
            g.DrawString("放大縮小4", f, new SolidBrush(Color.Blue), new PointF(0, h * 3));
            Rectangle rect4 = new Rectangle(0, h * 3, w / 4, h);
            g.DrawRectangle(p, rect4);   //用紅色筆畫矩形

            //恢復比例, 寫說明
            w = w / 4 * 7;
            f = new Font("標楷體", 20);
            //標示放大縮小比例

            g.ResetTransform();  // 重置轉換, 恢復

            g.DrawString("正常", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 0));
            g.DrawString("X負一倍, Y不變", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 1));
            g.DrawString("X一半, Y一倍", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 2));
            g.DrawString("X一倍, Y不變", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 6));
            g.DrawString("X三倍, Y三倍", f, new SolidBrush(Color.Black), new PointF(w * 1, h * 8));


            pictureBox1.Image = bitmap1;

        }

        void draw_grid1(Graphics g)
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
            //平移旋轉一張圖片1
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int W = 305 * 2;
            int H = 400 * 2;

            pictureBox1.Size = new Size(W, H);

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);
            Pen p = new Pen(Color.Red, 3);
            g.Clear(Color.White);

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int x_st = 0;
            int y_st = 0;
            x_st = 0;
            y_st = 0;

            // 平移, 右移, 下移
            g.TranslateTransform(305, 400);

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

            g.ResetTransform();  // 重置轉換, 恢復

            g.DrawImage(bitmap1, x_st + 305, y_st, w, h);
            g.DrawString("原圖平移", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 + 305 - 130, 10));

            pictureBox1.Image = bitmap2;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //平移旋轉一張圖片2
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式

            int W = 305 * 2;
            int H = 400 * 2;

            pictureBox1.Size = new Size(W, H);

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);
            Pen p = new Pen(Color.Red, 3);
            g.Clear(Color.White);

            int w = bitmap1.Width;
            int h = bitmap1.Height;
            int x_st = 0;
            int y_st = 0;
            x_st = 0;
            y_st = 0;

            // 平移, 右移, 下移
            g.TranslateTransform(305, 400 / 2);

            int i;
            for (i = 0; i < 18; i++)
            {
                g.RotateTransform(20);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
                g.DrawImage(bitmap1, x_st, y_st, (w / 2), (h / 2));
                //g.DrawString(((i + 1) * 20).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }

            // 平移, 右移, 下移
            g.TranslateTransform(0, 400);
            for (i = 0; i < 18; i++)
            {
                g.RotateTransform(20);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
                g.DrawImage(bitmap1, x_st, y_st, (w / 2), (h / 2));
                //g.DrawString(((i + 1) * 20).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }

            g.ResetTransform();  // 重置轉換, 恢復

            //g.DrawImage(bitmap1, x_st + 305, y_st, w / 2, h / 2);
            //g.DrawString("原圖平移", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 + 305 - 130, 10));

            pictureBox1.Image = bitmap2;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //平移旋轉一張圖片3
            int W = 305 * 2;
            int H = 400 * 2;

            pictureBox1.Size = new Size(W, H);

            Bitmap bitmap2 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap2);
            //Pen p = new Pen(Color.Red, 3);
            g.Clear(Color.White);

            //圖片的中心, 依此中心旋轉
            int cx = W / 2;
            int cy = H / 2;
            cx = 200;
            cy = 200;

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            for (int angle = 0; angle <= 360; angle += 30)
            {
                draw_bitmap_with_angle(filename, g, cx, cy, angle);
            }
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

            g.ResetTransform();  // 重置轉換, 恢復

            if (angle == 0)
            {
                // 平移, 右移, 下移
                g.TranslateTransform(x_st, y_st);
            }
            else
            {
                //需要平移
                //需要旋轉

                double radius = Math.Sqrt(w * w + h * h) / 2;
                double theta0 = Math.Atan((double)h / (double)w);
                double theta1 = theta0 + Math.PI * angle / 180;
                double x1 = radius * Math.Cos(theta1);
                double y1 = radius * Math.Sin(theta1);

                // 平移, 右移, 下移
                g.TranslateTransform(x_st + w / 2 - (float)x1, y_st + h / 2 - (float)y1);
                g.RotateTransform(angle);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
            }
            g.DrawImage(bitmap1, 0, 0, w, h);
            g.DrawRectangle(p, 0, 0, w, h);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 影像旋轉(以中心順時針轉10度)
            // 旋轉一張圖片, 用圖片的中心為旋轉中心
            // 若無設定平移, 則只會以原點為旋轉中心

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = new Bitmap(filename);

            // 平移, 右移, 下移
            g.TranslateTransform((float)bmp.Width / 2, (float)bmp.Height / 2);

            //順時針轉10度
            g.RotateTransform(10);

            // 平移, 右移, 下移
            g.TranslateTransform(-(float)bmp.Width / 2, -(float)bmp.Height / 2);

            //於座標(0,0)開始繪製來源影像
            g.DrawImage(bmp, 0, 0, bmp.Width, bmp.Height);

            pictureBox1.Image = bitmap1;
        }

        private double rad(double d)
        {
            return d * Math.PI / 180.0;
        }

        private double sind(double d)
        {
            return Math.Sin(d * Math.PI / 180.0);
        }

        private double cosd(double d)
        {
            return Math.Cos(d * Math.PI / 180.0);
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
            g.Clear(Color.White);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            draw_grid(g);

            richTextBox1.Text += "幾何圖形, 大小為2X2, 中心在原點\n";

            g.ResetTransform();  // 重置轉換, 恢復

            //水平垂直放大100倍, 畫在原點, 只看到右下角
            g.ScaleTransform(100, 100);
            DrawFigure(g, Color.Red);

            // 平移, 右移, 下移
            g.TranslateTransform(200, 200, MatrixOrder.Append);
            DrawFigure(g, Color.Green);

            float x_st = 400f;
            float y_st = 100f;
            int w = 200;
            int h = 200;

            RectangleF from_rect = new RectangleF(-1, -1, 2, 2);
            PointF[] to_points =
            {
                new PointF(x_st, y_st),    // 左上
                new PointF(x_st+w, y_st),  // 右上
                new PointF(x_st, y_st+h),  // 左下
            };

            Matrix map_matrix = new Matrix(from_rect, to_points);
            g.Transform = map_matrix;

            DrawFigure(g, Color.Blue);

            //原圖在 (-1,-1) w = 2 h = 2
            //轉換到 (400,120) w = 180 h = 100  //放大又平移 且 歪曲50
            x_st = 400;
            y_st = 100f + 210f;
            w = 200;
            h = 200;

            from_rect = new RectangleF(-1, -1, 2, 2);
            to_points = new PointF[]
            {
                new PointF(x_st, y_st),       // 左上
                new PointF(x_st+w, y_st),     // 右上
                new PointF(x_st-50, y_st+h),  // 左下
            };
            map_matrix = new Matrix(from_rect, to_points);
            g.Transform = map_matrix;

            DrawFigure(g, Color.Cyan);

            richTextBox1.Text += "右下: 原圖放大平移 且 Y軸反相\n";
            //反相畫圖  Y軸反相
            //原圖在 (-1,-1) w = 2 h = 2
            //轉換到 (100,450) w = 100 h = 100  //放大又平移 且 Y軸反相

            x_st = 100f;
            y_st = 330f + 200f;
            w = 200;
            h = 200;

            from_rect = new RectangleF(-1, -1, 2, 2);
            to_points = new PointF[]
            {
                new PointF(x_st, y_st),   // Upper left.
                new PointF(x_st+w, y_st),   // Upper right.
                new PointF(x_st, y_st-h),   // Lower left.
            };
            map_matrix = new Matrix(from_rect, to_points);
            g.Transform = map_matrix;
            DrawFigure(g, Color.Magenta);

            pictureBox1.Image = bitmap1;
        }

        //把圖畫在(-1,-1) w = 2 h = 2
        private void DrawFigure(Graphics g, Color c)
        {
            int linewidth = 0;  // 線寬大於0會讓轉換後線變粗
            Pen p = new Pen(c, linewidth);

            g.DrawLine(p, -1, 1, 1, 1);//下
            g.DrawLine(p, -1, 1, -1, -1);//左
            g.DrawLine(p, 1, -1, 1, 1);//右
            g.DrawLine(p, 1, -1, -1, -1);//上

            g.DrawLine(p, -1, -1, 1, 1);
            g.DrawLine(p, -1, -1, 1, 0);
            g.DrawLine(p, -1, -1, 0, 1);

            g.DrawEllipse(p, -0.05f, -0.05f, 0.1f, 0.1f);

            p.Dispose();
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //測試Matrix

            float size = 2.0f;

            // 建立一個矩陣物件
            Matrix Var_Matrix = new Matrix((float)size, 0.0F, 0.0F, (float)size, 0.0F, 0.0F);//設定仿射矩陣
            //Var_Matrix.TransformPoints(Var_PointS); //不會用 TransformPoints

            richTextBox1.Text += Var_Matrix.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 建立一個矩陣物件
            Matrix A = new Matrix();
            int theta = 0;
            int Cx = 100;
            int Cy = 100;
            for (int i = theta; i < 180 + theta; i += 45)
            {
                A.Reset();
                A.Rotate(i, MatrixOrder.Append);
                A.Translate(Cx, Cy, MatrixOrder.Append);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            Rectangle rect = new Rectangle(-2, -2, 4, 4);
            Point[] pts = new Point[]
            { 
                new Point(0, pictureBox1.ClientSize.Height),
                new Point(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height), 
                new Point(0, 0)
            };

            // 建立一個矩陣物件
            Matrix transform = new Matrix(rect, pts);

            //richTextBox1.Text += transform..Elements.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        // Return a rotation matrix to rotate around a point.
        private Matrix RotateAroundPoint(float angle, Point center)
        {
            // Translate the point to the origin.
            // 建立一個矩陣物件
            Matrix result = new Matrix();
            result.RotateAt(angle, center);
            return result;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            // Matrix1

            Rectangle rect = new Rectangle(0, 0, 200, 200);

            // 畫一個基準
            g.DrawRectangle(Pens.Red, rect);
            g.DrawRectangle(Pens.Red, 50, 50, 50, 50);

            // 有轉換
            // 建立一個矩陣物件
            //Matrix M = new Matrix(1, 0, 0.5f, 1, 0, 0);
            //Matrix M = new Matrix(1, 0.5f, 0, 1, 0, 0);
            //Matrix M = new Matrix(1, 1, 1, -1, 0, 0);

            float dx = 50;
            float dy = 50;
            //Matrix M = new Matrix(1.2f, 0, 0, 1.8f, dx, dy);
            Matrix M = new Matrix(1.2f, 0, 0, 1.8f, dx, dy);

            //g.RotateTransform(45.0f, MatrixOrder.Prepend);  // 旋轉
            // 平移, 右移, 下移
            //g.TranslateTransform(-20, -70);  // 平移
            g.Transform = M;

            g.DrawString("Welcome to the United States and have a nice day.",
                new Font("Verdana", 20),
                new SolidBrush(Color.Blue),
                rect);
            g.DrawRectangle(Pens.Green, rect);

            pictureBox1.Image = bitmap1;
        }

        private void button15_Click(object sender, EventArgs e)
        {
            // Transform

            g.Clear(Color.White);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            draw_grid(g);

            Rectangle rect = new Rectangle(100, 0, 100, 100);

            // 原圖
            g.FillRectangle(sb1, rect);

            // 縮旋平
            //g.ScaleTransform(2.0f, 0.5f);  // 縮放, 水平縮放, 垂直縮放
            //g.RotateTransform(45.0f, MatrixOrder.Append);  // 旋轉, 對原點順時針旋轉
            g.TranslateTransform(200.0f, 100.0f, MatrixOrder.Append);  // 平移, 右移, 下移

            // 使用 transform 再畫一次
            g.FillRectangle(sb2, rect);

            g.ResetTransform();  // 重置轉換, 恢復

            // 重置後 再畫一次
            rect = new Rectangle(100 + 20, 0 + 20, 100, 100);
            g.FillRectangle(sb3, rect);

            pictureBox1.Image = bitmap1;
        }

        void draw_pts(Graphics g, PointF[] pts)
        {
            PointF p0 = pts[0];//左上
            PointF p1 = pts[1];//右上
            PointF p2 = new PointF(pts[1].X, pts[1].Y + (pts[2].Y - pts[0].Y));
            PointF p3 = pts[2];//左下

            //Pen p = new Pen(Color.Red, 20);
            g.DrawLine(new Pen(Color.Red, 20), p0, p1);//上
            g.DrawLine(new Pen(Color.Green, 20), p1, p2);//右
            g.DrawLine(new Pen(Color.Blue, 20), p2, p3);//下
            g.DrawLine(new Pen(Color.Cyan, 20), p3, p0);//左
        }

        private void button16_Click(object sender, EventArgs e)
        {
            // 矩陣轉置, 只能 矩形範圍 轉 平行四邊形範圍

            string filename = @"D:\_git\vcs\_1.data\______test_files1\__pic\_chicken\chicken1.bmp";
            Bitmap bmp = new Bitmap(filename);

            g.Clear(Color.White);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            draw_grid(g);

            g.FillRectangle(Brushes.Lime, 0, 100, 200, 100);
            g.DrawEllipse(Pens.Red, 0, 100, 200, 100);
            g.DrawImage(bmp, 60, 110, 80, 80);

            //準備Transform
            int x_st = 0;
            int y_st = 100;
            int w = 200;
            int h = 100;
            RectangleF rect = new RectangleF(x_st, y_st, w, h);
            g.DrawRectangle(new Pen(Color.Red, 0), x_st, y_st, w, h);

            x_st = 300;
            y_st = 50;
            w = 300;
            h = 200;
            int dd = 100;

            g.DrawRectangle(new Pen(Color.Red, 0), x_st, y_st, w, h);

            PointF[] pts = 
            {
                // 左上                    //右上
                new PointF(x_st, y_st),    new PointF(x_st + w, y_st+dd),
                new PointF(x_st, y_st + h),
                // 左下
            };
            draw_pts(g, pts);

            g.Transform = new Matrix(rect, pts);  // 矩陣轉置, 只能 矩形範圍 轉 平行四邊形範圍

            g.FillRectangle(Brushes.Lime, 0, 100, 200, 100);
            g.DrawEllipse(Pens.Red, 0, 100, 200, 100);
            g.DrawImage(bmp, 60, 110, 80, 80);

            pictureBox1.Image = bitmap1;
        }

        void MakeData2()
        {
            richTextBox1.Text += "製作資料\n";
            // Make data
            Points[0].X = 0;
            Points[0].Y = 0;
            Points[1].X = 1;
            Points[1].Y = 1;
            Points[2].X = 2;
            Points[2].Y = 0;
            Points[3].X = 3;
            Points[3].Y = 2;
            Points[4].X = 4;
            Points[4].Y = 1;
            Points[5].X = 5;
            Points[5].Y = 3;
            Points[6].X = 6;
            Points[6].Y = 2;
            Points[7].X = 7;
            Points[7].Y = 4;

            int i;
            for (i = 0; i < 8; i++)
            {
                Points[i].X = 10 * Points[i].X;
                Points[i].Y = 40 * Points[i].Y;
            }
        }

        void DrawData2()
        {
            int len = Points.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += Points[i].ToString() + "\n";
            }

            int W = 800;
            int H = 250;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.Clear(Color.White);

            // Create pens.
            Pen redPen = new Pen(Color.Red, 2);     //線寬大於0會讓轉換後線變粗
            Pen bluePen = new Pen(Color.Blue, 2);

            //g.DrawLines(bluePen, Points);   //畫直線
            g.DrawCurve(bluePen, Points);   //畫曲線
            g.DrawString("轉換前10", new Font("標楷體", 10), new SolidBrush(Color.Blue), new PointF(22, 20));

            //準備Transform
            int x_st = 0;
            int y_st = 0;
            int w = 70;
            int h = 160;

            //原始資料範圍
            RectangleF rect = new RectangleF(x_st, y_st, w, h);
            g.DrawRectangle(new Pen(Color.Red, 0), x_st, y_st, w, h);

            //欲轉換資料範圍
            x_st = W * 1 / 10;
            y_st = H * 1 / 10;
            w = W * 8 / 10;
            h = H * 8 / 10;

            PointF[] pts =
            {
                //new PointF(x_st, y_st+h),//左上
                //new PointF(x_st+w, y_st+h),//右上
                //new PointF(x_st, y_st),//左下
                new PointF(x_st, y_st),//左上
                new PointF(x_st+w, y_st),//右上
                new PointF(x_st, y_st+h),//左下
            };
            g.DrawRectangle(new Pen(Color.Green, 5), x_st, y_st, w, h);

            g.Transform = new Matrix(rect, pts);  // 矩陣轉置, 只能 矩形範圍 轉 平行四邊形範圍

            //g.DrawLines(redPen, Points);   //畫直線
            g.DrawCurve(redPen, Points);   //畫曲線
            g.DrawString("轉換後10", new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(22, 20));

            g.ResetTransform();  // 重置轉換, 恢復

            g.DrawString("恢復轉換後10", new Font("標楷體", 10), new SolidBrush(Color.Red), new PointF(100, 20));

            pictureBox1.Image = bitmap1;
        }

        private void button17_Click(object sender, EventArgs e)
        {
            MakeData2();
            DrawData2();

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {
            pictureBox1.ClientSize = new Size(960, 960 + 30);
            richTextBox1.Visible = false;

            timer1.Enabled = true;
        }

        void draw_grid(Graphics g)
        {
            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;
            int i;
            int j;

            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(Pens.Gray, i, 0, i, H);
            }
            for (j = 0; j <= H; j += 100)
            {
                g.DrawLine(Pens.Gray, 0, j, W, j);
            }
        }

        float angle = 0;
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            return;

            // 影像旋轉(以中心順時針轉10度)
            // 旋轉一張圖片, 用圖片的中心為旋轉中心
            // 若無設定平移, 則只會以原點為旋轉中心

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            // 平移, 右移, 下移
            e.Graphics.TranslateTransform((float)bmp.Width / 2, (float)bmp.Height / 2);

            //順時針轉10度
            angle += 27f;
            e.Graphics.RotateTransform(angle);

            // 平移, 右移, 下移
            e.Graphics.TranslateTransform(-(float)bmp.Width / 2, -(float)bmp.Height / 2);

            //於座標(0,0)開始繪製來源影像
            e.Graphics.DrawImage(bmp, 0, 0, bmp.Width, bmp.Height);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/



/*
//儲存新的影像
string filename = Application.StartupPath + "\\rotate_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
rotateImage.Save(@filename, ImageFormat.Jpeg);
richTextBox1.Text += "影像旋轉，存檔完成，檔名：" + filename + "\n";
*/



/*
            //矩陣轉置
            //原始資料範圍很小, 用 矩陣轉置 方法, 可以剛好畫滿pictureBox


            // 原始資料範圍 rect
            // Scale to fit the data.
            RectangleF rect = new RectangleF(x_min, y_min, x_max, y_max - y_min);
            g.DrawRectangle(redPen, x_min, y_min, x_max, y_max - y_min);

            // 欲映射的pictureBox範圍
            PointF[] pts = 
                {
                    new PointF(0, pictureBox1.ClientSize.Height),
                    new PointF(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height),
                    new PointF(0, 0),
                };

            //轉置
            g.Transform = new Matrix(rect, pts);  // 矩陣轉置, 只能 矩形範圍 轉 平行四邊形範圍

            //畫圖

*/
