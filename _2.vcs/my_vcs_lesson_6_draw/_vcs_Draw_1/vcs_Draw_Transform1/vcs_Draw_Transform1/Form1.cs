using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D; //SmoothingMode, Matrix

//使用 Matrix
//平移縮放旋轉

namespace vcs_Draw_Transform1
{
    public partial class Form1 : Form
    {
        List<double> x = new List<double>();
        List<double> y = new List<double>();

        /*
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
        */
        Point[] Points = new Point[8];    //一維陣列內有 8 個Point

        Bitmap bitmap1;
        Graphics g;
        SolidBrush sb1 = new SolidBrush(Color.Red);
        SolidBrush sb2 = new SolidBrush(Color.Green);
        SolidBrush sb3 = new SolidBrush(Color.Blue);

        //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\tiger.jpg";  // 100 X 100
        //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\smile.jpg";  // 200 X 200
        //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\peony.bmp";  // 200 X 200

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

            reset_pictureBox();

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
            dy = 60 + 10;

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

            pictureBox1.Size = new Size(820, 880);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_reset.Location = new Point(pictureBox1.Location.X + pictureBox1.Size.Width - bt_reset.Size.Width, pictureBox1.Location.Y);

            pictureBox2.Size = new Size(410, 230);
            pictureBox2.Location = new Point(x_st + dx * 0, y_st + dy * 10);

            richTextBox1.Size = new Size(300, 880);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 940);
            this.Text = "vcs_Draw_Transform1";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            reset_pictureBox();
        }

        void reset_pictureBox()
        {
            pictureBox1.Size = new Size(820, 880);
            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            g = Graphics.FromImage(bitmap1);
            g.ResetTransform();  // 重置轉換, 恢復
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.Clear(Color.White);
            draw_grid(g, Color.Gray);
            pictureBox1.Image = bitmap1;
        }

        void draw_grid(Graphics g, Color c)
        {
            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;

            for (int i = 0; i <= W; i += 100)
            {
                g.DrawLine(new Pen(c, 3), i, 0, i, H);
            }
            for (int j = 0; j <= H; j += 100)
            {
                g.DrawLine(new Pen(c, 3), 0, j, W, j);
            }
        }

        void show_matrix(Matrix mtx)
        {
            richTextBox1.Text += "Matrix :\n";
            richTextBox1.Text += mtx.Elements[0].ToString() + "\t" + mtx.Elements[1].ToString() + "\n";
            richTextBox1.Text += mtx.Elements[2].ToString() + "\t" + mtx.Elements[3].ToString() + "\n";
            richTextBox1.Text += mtx.Elements[4].ToString() + "\t" + mtx.Elements[5].ToString() + "\n";
        }

        //平移, 旋轉
        private void button0_Click(object sender, EventArgs e)
        {
            //準備
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 5);
            Rectangle rect = new Rectangle(10, 10, 200, 50);

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            int w = bmp.Width;
            int h = bmp.Height;
            int x_st = 50;
            int y_st = 50;
            Point p0 = new Point(0, 0);
            Point p1 = new Point(400, 0);
            Point p2 = new Point(0, 400);

            //原本的, 做相同的事
            p.Color = Color.Red;
            g.DrawRectangle(p, rect);   //用紅色筆畫矩形
            g.DrawString("平移, 紅色是原本的, 綠色是平移後的", new Font("標楷體", 16), new SolidBrush(Color.Blue), new PointF(0, 0));
            g.DrawImage(bmp, x_st, y_st, w / 2, h / 2);
            g.DrawLine(p, p0, p1);
            g.DrawLine(p, p0, p2);

            g.DrawLine(p, p0.X + 150, p0.Y + 400, p1.X + 150, p1.Y + 400);
            g.DrawLine(p, p0.X + 150, p0.Y + 400, p2.X + 150, p2.Y + 400);

            // 原點平移, 右移, 下移
            g.TranslateTransform(150, 400);  // 原點平移, 右移, 下移

            if (checkBox1.Checked == true)
            {
                g.RotateTransform(10);  //依原點旋轉
            }

            //平移後的, 做相同的事
            p.Color = Color.Green;
            p.Width = 3;
            g.DrawRectangle(p, rect);   //用綠色筆畫平移後的圖形
            g.DrawString("平移, 紅色是原本的, 綠色是平移後的", new Font("標楷體", 16), new SolidBrush(Color.Green), new PointF(0, 0));
            g.DrawImage(bmp, x_st, y_st, w / 2, h / 2);
            g.DrawLine(p, p0, p1);
            g.DrawLine(p, p0, p2);

            g.ResetTransform();  // 重置轉換, 恢復

            pictureBox1.Image = bitmap1;
        }

        //旋轉
        private void button1_Click(object sender, EventArgs e)
        {
            reset_pictureBox();

            Pen p = new Pen(Color.Red, 5);

            // 未旋轉, 平移 + 畫線
            // Reset後, 移動原點
            g.TranslateTransform(100, 100);  // 原點平移, 右移, 下移
            g.DrawString("無旋轉", new Font("標楷體", 16), new SolidBrush(Color.Red), new PointF(0, 0));

            g.DrawLine(p, 0, 0, 50, 0);
            for (int i = 0; i < 10; i++)
            {
                // 原點平移, 右移, 下移
                g.TranslateTransform(50, 0);  // 原點平移, 右移, 下移
                //g.RotateTransform(30);
                g.DrawLine(p, 0, 0, 50, 0);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            g.ResetTransform();  // 重置轉換, 恢復

            // 旋轉, 平移 + 旋轉 + 畫線
            // Reset後, 移動原點
            g.TranslateTransform(100, 200);  // 原點平移, 右移, 下移
            g.DrawString("有旋轉", new Font("標楷體", 16), new SolidBrush(Color.Green), new PointF(0, 0));

            p = new Pen(Color.Green, 5);
            g.DrawLine(p, 0, 0, 50, 0);
            for (int i = 0; i < 10; i++)
            {
                // 原點平移, 右移, 下移
                g.TranslateTransform(50, 0);  // 原點平移, 右移, 下移
                g.RotateTransform(30);
                g.DrawLine(p, 0, 0, 50, 0);
            }

            g.ResetTransform();  // 重置轉換, 恢復

            pictureBox1.Image = bitmap1;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //轉換範例
            reset_pictureBox();

            richTextBox1.Text += "------------------------------\n";  // 30個

            //來源矩形
            float sx = -50f;
            float sy = -50f;
            int sw = 100;
            int sh = 100;
            // 原始資料範圍 rect
            RectangleF src_rect = new RectangleF(sx, sy, sw, sh);

            richTextBox1.Text += "------------------------------\n";  // 30個

            g.ResetTransform();  // 重置轉換, 恢復

            // 畫在原點, 只看到右下角
            DrawFigure(g, Color.Red);

            // 水平垂直放大2倍, 
            // g.ScaleTransform(2.0f, 2.0f);  // 縮放, 水平縮放, 垂直縮放

            // 原點平移, 右移, 下移
            g.TranslateTransform(150, 50, MatrixOrder.Append);
            DrawFigure(g, Color.Green);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 矩陣轉置

            // 目標矩形, 平移 + 縮放
            // 欲映射的繪圖範圍
            float dx = 300f;
            float dy = 50f;
            int dw = 200;
            int dh = 200;
            PointF[] dst_points1 = new PointF[]
            {
                new PointF(dx, dy),     // 左上
                new PointF(dx+dw, dy),  // 右上
                new PointF(dx, dy+dh),  // 左下
            };

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            Matrix mtx = new Matrix(src_rect, dst_points1);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            DrawFigure(g, Color.Blue);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //目標矩形, 平移 + 縮放 + 歪曲
            dx = 600;
            dy = 100f;
            dw = 200;
            dh = 200;
            int dd = 100;
            PointF[] dst_points2 = new PointF[]
            {
                new PointF(dx, dy),        // 左上
                new PointF(dx+dw, dy),     // 右上
                new PointF(dx-dd, dy+dh),  // 左下
            };

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            mtx = new Matrix(src_rect, dst_points2);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            DrawFigure(g, Color.Cyan);

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "右下: 原圖放大平移 且 Y軸反相\n";
            //反相畫圖  Y軸反相
            //原圖在 (-1,-1) w = 2 h = 2
            //轉換到 (100,450) w = 100 h = 100  //放大又平移 且 Y軸反相

            //目標矩形, 平移 + 縮放 + 反相
            dx = 50f;
            dy = 350f;
            dw = 200;
            dh = 200;
            PointF[] dst_points3 = new PointF[]
            {
                new PointF(dx, dy),     // 左上
                new PointF(dx+dw, dy),  // 右上
                new PointF(dx, dy-dh),  // 左下
            };

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            mtx = new Matrix(src_rect, dst_points3);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            DrawFigure(g, Color.Magenta);

            richTextBox1.Text += "------------------------------\n";  // 30個

            g.ResetTransform();  // 重置轉換, 恢復

            Pen p1 = new Pen(Color.Red, 10);
            Pen p2 = new Pen(Color.Green, 10);
            PointF pt0 = dst_points1[0];
            PointF pt1 = dst_points1[1];
            PointF pt2 = dst_points1[2];
            g.DrawLine(p1, pt0, pt1);
            g.DrawLine(p2, pt0, pt2);
            pt0 = dst_points2[0];
            pt1 = dst_points2[1];
            pt2 = dst_points2[2];
            g.DrawLine(p1, pt0, pt1);
            g.DrawLine(p2, pt0, pt2);
            pt0 = dst_points3[0];
            pt1 = dst_points3[1];
            pt2 = dst_points3[2];
            g.DrawLine(p1, pt0, pt1);
            g.DrawLine(p2, pt0, pt2);

            Font f = new Font("標楷體", 16);
            g.DrawString("原圖", f, Brushes.Red, new PointF(0, 60));
            g.DrawString("平移", f, Brushes.Red, new PointF(100, 100));
            g.DrawString("平移 + 縮放", f, Brushes.Red, new PointF(dst_points1[0].X, dst_points1[0].Y - 30));
            g.DrawString("平移 + 縮放 + 歪曲", f, Brushes.Red, new PointF(dst_points2[0].X, dst_points2[0].Y - 30));
            g.DrawString("平移 + 縮放 + 反相", f, Brushes.Red, new PointF(dst_points3[0].X, dst_points3[0].Y + 10));
            g.DrawString("原圖", f, Brushes.Red, new PointF(0, 500 - 25));

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            g.ResetTransform();  // 重置轉換, 恢復

            //來源矩形
            sx = 0f;
            sy = 500f;
            sw = 100;
            sh = 100;
            Rectangle src_rect2 = new Rectangle((int)sx, (int)sy, sw, sh);
            RectangleF src_rect2f = new RectangleF(sx, sy, sw, sh);

            // 原圖畫在 src_rect2
            DrawFigure2(g, src_rect2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // 矩陣轉置

            //準備Transform            
            //目標矩形, 平移 + 縮放 + 歪曲
            dx = 500;
            dy = 300;
            dw = 300;
            dh = 200;
            dd = 100;
            PointF[] pts = 
            {
                // 左上                    //右上
                new PointF(dx, dy),    new PointF(dx + dw, dy+dd),
                new PointF(dx, dy + dh),
                // 左下
            };
            //draw_pts(g, pts);

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            mtx = new Matrix(src_rect2f, pts);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            DrawFigure2(g, src_rect2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //準備Transform            
            //目標矩形, 平移 + 縮放 + 歪曲
            dx = 500;
            dy = 300;
            dw = 200;
            dh = 200;
            dd = 200;
            pts = new PointF[]
            {
                // 左上                    //右上
                new PointF(dx, dy),    new PointF(dx + dw, dy+dd),
                new PointF(dx, dy + dh),
                // 左下
            };
            //draw_pts(g, pts);

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            mtx = new Matrix(src_rect2f, pts);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            DrawFigure2(g, src_rect2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //準備Transform            
            //目標矩形, 平移 + 縮放 + 歪曲
            dx = 500;
            dy = 300;
            dw = -300;
            dh = 200;
            dd = 100;
            pts = new PointF[]
            {
                // 左上                    //右上
                new PointF(dx, dy),    new PointF(dx + dw, dy+dd),
                new PointF(dx, dy + dh),
                // 左下
            };
            //draw_pts(g, pts);

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            mtx = new Matrix(src_rect2f, pts);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            DrawFigure2(g, src_rect2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //準備Transform            
            //目標矩形, 平移 + 縮放 + 歪曲
            dx = 500;
            dy = 300;
            dw = -200;
            dh = 200;
            dd = 200;
            pts = new PointF[]
            {
                // 左上                    //右上
                new PointF(dx, dy),    new PointF(dx + dw, dy+dd),
                new PointF(dx, dy + dh),
                // 左下
            };
            //draw_pts(g, pts);

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            mtx = new Matrix(src_rect2f, pts);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            DrawFigure2(g, src_rect2);

            pictureBox1.Image = bitmap1;
        }

        private void DrawFigure2(Graphics g, Rectangle src_rect2)
        {
            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\tiger.jpg";  // 100 X 100
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\smile.jpg";  // 200 X 200
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\peony.bmp";  // 200 X 200
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\peony.bmp";  // 200 X 200
            Bitmap bmp = new Bitmap(filename);
            g.DrawImage(bmp, src_rect2.X, src_rect2.Y, bmp.Width, bmp.Height);
        }

        private void DrawFigure(Graphics g, Color c)
        {
            richTextBox1.Text += "畫上影像, 大小為 100 X 100, 中心在原點\n";

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\tiger.jpg";  // 100 X 100
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\smile.jpg";  // 200 X 200
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\peony.bmp";  // 200 X 200
            //string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\peony.bmp";  // 200 X 200
            Bitmap bmp = new Bitmap(filename);
            g.DrawImage(bmp, -50, -50, bmp.Width, bmp.Height);
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

        private void button3_Click(object sender, EventArgs e)
        {
            //平移旋轉一張圖片1
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            int w = bmp.Width * 3 / 4;
            int h = bmp.Height * 3 / 4;
            int x_st = 0;
            int y_st = 0;

            g.Clear(Color.Pink);

            // 原點平移, 右移, 下移
            g.TranslateTransform(305 + 100, 420);  // 原點平移, 右移, 下移

            //            貼上的位置  貼上的大小 放大縮小用
            g.DrawImage(bmp, x_st, y_st, w, h);

            g.DrawString("未旋轉", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 100, 10));

            for (int i = 0; i < 24; i++)
            {
                g.RotateTransform(15);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉, 累計旋轉
                g.DrawImage(bmp, x_st, y_st, w, h);
                g.DrawString(((i + 1) * 15).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }
            g.DrawRectangle(new Pen(Color.Green, 10), x_st, y_st, w, h);
            g.ResetTransform();  // 重置轉換, 恢復

            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //平移旋轉一張圖片2
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            int w = bmp.Width * 3 / 4;
            int h = bmp.Height * 3 / 4;
            int x_st = 0;
            int y_st = 0;

            g.Clear(Color.Pink);

            // 原點平移, 右移, 下移
            g.TranslateTransform(305, 400);  // 原點平移, 右移, 下移

            for (int i = 0; i < 24; i++)
            {
                g.RotateTransform(15);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
                g.DrawImage(bmp, x_st, y_st, w, h);
                g.DrawString(((i + 1) * 15).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }

            // 原點平移, 右移, 下移
            g.TranslateTransform(0, 400);  // 原點平移, 右移, 下移
            for (int i = 0; i < 24; i++)
            {
                g.RotateTransform(15);//再旋轉指定的角度, 以全圖的左上角為原點, 順時鐘旋轉
                g.DrawImage(bmp, x_st, y_st, w, h);
                g.DrawString(((i + 1) * 15).ToString(), new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 - 50, 10));
            }

            g.ResetTransform();  // 重置轉換, 恢復

            //g.DrawImage(bmp, x_st + 305, y_st, w, h);
            //g.DrawString("原圖平移", new Font("標楷體", 20), new SolidBrush(Color.Green), new PointF(305 + 305 - 130, 10));

            pictureBox1.Image = bitmap1;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //平移旋轉一張圖片3
            int W = 305 * 2;
            int H = 400 * 2;
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
                // 原點平移, 右移, 下移
                g.TranslateTransform(x_st, y_st);  // 原點平移, 右移, 下移
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

                // 原點平移, 右移, 下移
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

            // 原點平移, 右移, 下移
            g.TranslateTransform((float)bmp.Width / 2, (float)bmp.Height / 2);

            //順時針轉10度
            g.RotateTransform(10);

            // 原點平移, 右移, 下移
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

        //畫Sinc ST
        private void button7_Click(object sender, EventArgs e)
        {
            //畫Sinc
            //畫Sinc
            MakeGraph();
        }
        // Make the graph.
        private void MakeGraph()
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Transform to map the graph bounds to the Bitmap.
            // The bounds to draw.
            float xmin = -20;
            float xmax = 20;
            float ymin = -5;
            float ymax = 12;
            RectangleF rect = new RectangleF(xmin, ymin, xmax - xmin, ymax - ymin);

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            PointF[] pts = 
            {
                new PointF(0, H),
                new PointF(W, H),
                new PointF(0, 0),
            };
            g.Transform = new Matrix(rect, pts);  // 設定仿射矩陣, 矩陣轉置, 只能 矩形範圍 轉 平行四邊形範圍

            // Draw the graph.
            Pen p = new Pen(Color.Blue, 0);
            // Draw the axes.
            g.DrawLine(p, xmin, 0, xmax, 0);
            g.DrawLine(p, 0, ymin, 0, ymax);
            for (int x = (int)xmin; x <= xmax; x++)
            {
                g.DrawLine(p, x, -0.1f, x, 0.1f);
            }
            for (int y = (int)ymin; y <= ymax; y++)
            {
                g.DrawLine(p, -0.1f, y, 0.1f, y);
            }
            p.Color = Color.Red;

            // See how big 1 pixel is horizontally.
            Matrix inverse = g.Transform;
            inverse.Invert();
            PointF[] pixel_pts =
            {
                new PointF(0, 0),
                new PointF(1, 0)
            };
            inverse.TransformPoints(pixel_pts);
            float dx = pixel_pts[1].X - pixel_pts[0].X;
            dx /= 2;

            // Loop over x values to generate points.
            List<PointF> points = new List<PointF>();
            for (float x = xmin; x <= xmax; x += dx)
            {
                bool valid_point = false;
                try
                {
                    // Get the next point.
                    float y = F(x);

                    // If the slope is reasonable, this is a valid point.
                    if (points.Count == 0)
                    {
                        valid_point = true;
                    }
                    else
                    {
                        float dy = y - points[points.Count - 1].Y;
                        if (Math.Abs(dy / dx) < 1000)
                        {
                            valid_point = true;
                        }
                    }
                    if (valid_point)
                    {
                        points.Add(new PointF(x, y));
                    }
                }
                catch
                {
                }

                // If the new point is invalid, draw
                // the points in the latest batch.
                if (!valid_point)
                {
                    if (points.Count > 1)
                    {
                        g.DrawLines(p, points.ToArray());
                    }
                    points.Clear();
                }
            }

            // Draw the last batch of points.
            if (points.Count > 1)
            {
                g.DrawLines(p, points.ToArray());
            }

            pictureBox1.Image = bitmap1;
        }

        // The function to graph.
        private float F(float x)
        {
            //return (float)((1 / x + 1 / (x + 1) - 2 * x * x) / 10);
            //return x;
            //return (float)Math.Sin(x);
            return (float)(10 * Math.Sin(x) / x);
        }
        //畫Sinc SP

        // Return a rotation matrix to rotate around a point.
        private Matrix RotateAroundPoint(float angle, Point center)
        {
            // Translate the point to the origin.
            // 轉置矩陣 mtx
            Matrix mtx = new Matrix();
            mtx.RotateAt(angle, center);
            return mtx;
        }

        int angle8 = 0;
        private void button8_Click(object sender, EventArgs e)
        {
            //旋轉
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            angle8 += 30;
            Bitmap bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            Bitmap bitmap2 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap2);

            Matrix mx = new Matrix();
            //mx.Rotate(30);//以左上角為圓心順時鐘旋轉角度
            mx.RotateAt(angle8, new PointF(W / 2, H / 2));//以(cx,cy)為圓心順時鐘旋轉角度
            g.Transform = mx;

            g.DrawImage(bitmap1, new Rectangle(0, 0, W, H));

            g.Dispose();

            pictureBox1.Image = bitmap2;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            pictureBox1.ClientSize = new Size(960, 960 + 30);
            richTextBox1.Visible = false;

            timer1.Enabled = true;
        }


        private void button10_Click(object sender, EventArgs e)
        {
            //旋轉轉置
            //在PictureBox上測試旋轉圖片
            //測試RotateTransform, TranslateTransform和ResetTransform

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

            int W = this.pictureBox1.Width;
            int H = this.pictureBox1.Height;

            Bitmap bitmap1 = new Bitmap(W, H);

            Graphics g = Graphics.FromImage(bitmap1);

            Pen p = new Pen(Color.Gray, 1);

            int i;
            for (i = 0; i <= W; i += 100)
            {
                g.DrawLine(p, i, 0, i, H);
            }
            for (i = 0; i <= H; i += 100)
            {
                g.DrawLine(p, 0, i, W, i);
            }

            Rectangle src_rect = new Rectangle(0, 0, W, H);   //擷取部分區域
            GraphicsUnit units = GraphicsUnit.Pixel;
            Image img = Image.FromFile(filename);

            int x_st = 0;
            int y_st = 0;
            int angle = 0;

            Point ulCorner = new Point(0, 0);
            Point urCorner = new Point(W, 0);
            Point llCorner = new Point(0, H);
            Point[] destRect = { ulCorner, urCorner, llCorner };

            x_st = 350 * 0;
            y_st = 200;
            angle = -10;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, src_rect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度

            x_st = 350 * 1;
            y_st = 200;
            angle = 0;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, src_rect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度

            x_st = 350 * 2;
            y_st = 200;
            angle = 10;
            ulCorner = new Point(0, 0);
            urCorner = new Point(W, 0);
            llCorner = new Point(0, H);
            destRect = new Point[] { ulCorner, urCorner, llCorner };

            g.TranslateTransform(x_st, y_st);
            g.RotateTransform(angle);//旋轉指定的角度
            g.DrawImage(img, destRect, src_rect, units);
            g.ResetTransform();//恢復坐標軸坐標 回 0 度

            pictureBox1.Image = bitmap1;
        }

        //連續旋轉一張圖片 ST
        float angle11 = 0;
        private void button11_Click(object sender, EventArgs e)
        {
            //連續旋轉一張圖片
            angle11 += 15;
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image = Image.FromFile(filename);

            Image image_rotated = image.GetRotateImage(angle11);

            pictureBox1.Image = image_rotated;
            pictureBox1.Size = new Size(image_rotated.Width, image_rotated.Height);
        }
        //連續旋轉一張圖片 SP

        float theta = 0; // 旋轉角度
        private void button12_Click(object sender, EventArgs e)
        {
            //連續旋轉一張圖片
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bm = new Bitmap(filename);

            theta = theta + 2;  // 旋轉角度 遞增

            Graphics g = this.pictureBox1.CreateGraphics();

            //畫布轉換矩陣的旋轉設定 - 在固定點自轉
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區正中心點
            int Cy = this.pictureBox1.ClientSize.Height / 2;//

            g.ResetTransform(); // 畫布的矩陣 = 單位矩陣

            g.TranslateTransform(-bm.Width / 2, -bm.Height / 2, MatrixOrder.Append);
            g.RotateTransform(theta, MatrixOrder.Append);  // 乘上 旋轉矩陣
            g.TranslateTransform(Cx, Cy, MatrixOrder.Append); // 再搬到視窗客戶區正中心點

            g.DrawImage(bm, 0, 0); // 繪出圖形
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //轉置矩陣範例1, 矩形範圍 轉 平行四邊形範圍

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\tiger.jpg";  // 100 X 100
            Bitmap bmp = new Bitmap(filename);
            int W = bmp.Width;
            int H = bmp.Height;

            Graphics g = pictureBox1.CreateGraphics();
            draw_grid(g, Color.Gray);
            g.ResetTransform();  // 重置轉換, 恢復

            // 來源矩形, 矩形範圍 src_rect
            int sx = 0;
            int sy = 0;
            int sw = W;
            int sh = H;
            Rectangle src_rect = new Rectangle(sx, sy, sw, sh);

            //原圖
            g.DrawImage(bmp, src_rect);
            g.DrawRectangle(new Pen(Color.Blue, 10), src_rect);

            // 欲映射的繪圖範圍, 目標矩形, 平行四邊形範圍 dst_rect
            int dx = 205;
            int dy = 205;
            int dw = W;
            int dh = H * 3 / 2;
            Rectangle dst_rect = new Rectangle(dx, dy, dw, dh);
            Point[] dst_points1 = new Point[]
            {
                new Point(dx, dy),       // 左上
                new Point(dx + dw, dy - 50),  // 右上
                new Point(dx - 50, dy + dh),  // 左下
            };

            g.DrawRectangle(new Pen(Color.Blue, 10), dst_rect);

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            Matrix mtx = new Matrix(src_rect, dst_points1);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            draw_grid(g, Color.Lime);
            //貼上轉換後的原圖
            g.DrawImage(bmp, src_rect);
            g.DrawRectangle(new Pen(Color.Blue, 10), dst_rect);

            //richTextBox1.Text += "src_rect : " + src_rect.ToString() + "\n";
            //richTextBox1.Text += "dst_rect : " + dst_rect.ToString() + "\n";
            show_matrix(mtx);
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //轉置矩陣範例2, 直接使用轉置矩陣

            string filename = @"D:\_git\vcs\_2.vcs\my_vcs_lesson_6_draw\data\tiger.jpg";  // 100 X 100
            Bitmap bmp = new Bitmap(filename);
            int W = bmp.Width;
            int H = bmp.Height;

            Graphics g = pictureBox1.CreateGraphics();
            draw_grid(g, Color.Gray);
            g.ResetTransform();  // 重置轉換, 恢復

            // 來源矩形, 矩形範圍 src_rect
            int sx = 0;
            int sy = 0;
            int sw = W;
            int sh = H;
            Rectangle src_rect = new Rectangle(sx, sy, sw, sh);

            // 原圖
            g.DrawImage(bmp, src_rect);
            g.DrawRectangle(new Pen(Color.Blue, 10), src_rect);

            // 欲映射的繪圖範圍, 目標矩形, 平行四邊形範圍 dst_rect
            int dx = 205;
            int dy = 205;
            int dw = W;
            int dh = H * 3 / 2;
            Rectangle dst_rect = new Rectangle(dx, dy, dw, dh);
            Point[] dst_points1 = new Point[]
            {
                new Point(dx, dy),       // 左上
                new Point(dx + dw, dy - 50),  // 右上
                new Point(dx - 50, dy + dh),  // 左下
            };

            g.DrawRectangle(new Pen(Color.Blue, 10), dst_rect);

            // 轉置矩陣 mtx, 矩形範圍 轉 平行四邊形範圍
            //Matrix mtx = new Matrix(src_rect, dst_points1);

            // 使用矩陣物件做轉換
            //float m11 = 1.2f;  // x軸縮放1.2倍
            //float m12 = 0.7f;  // y軸歪曲0.7倍
            //float m21 = 0.3f;  // x軸歪曲0.3倍
            //float m22 = 1.8f;  // y軸縮放1.8倍
            //float mdx = 100f;  // x軸平移
            //float mdy = 100f;  // y軸平移
            float m11 = 1.0f;  // x軸縮放1.0倍
            float m12 = 0f;  // y軸歪曲0倍
            float m21 = -0.5f;  // x軸歪曲-0.5倍
            float m22 = 1.5f;  // y軸縮放1.5倍
            float mdx = 205f;  // x軸平移
            float mdy = 205f;  // y軸平移

            // 轉置矩陣 mtx, 直接設定Matrix參數
            Matrix mtx = new Matrix(m11, m12, m21, m22, mdx, mdy);
            g.Transform = mtx;  // 設定仿射矩陣, 矩陣轉置

            draw_grid(g, Color.Lime);
            //貼上轉換後的原圖
            g.DrawImage(bmp, src_rect);
            g.DrawRectangle(new Pen(Color.Blue, 10), dst_rect);

            //richTextBox1.Text += "src_rect : " + src_rect.ToString() + "\n";
            //richTextBox1.Text += "dst_rect : " + dst_rect.ToString() + "\n";
            show_matrix(mtx);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            Matrix mtx = new Matrix();
            show_matrix(mtx);

            float angle = 10;
            richTextBox1.Text += "angle = " + angle.ToString() + "\n";
            mtx.Rotate(angle);
            show_matrix(mtx);

            SizeF size = new SizeF(300, 100);
            PointF[] array = new PointF[4];
            array[0].X = (0f - size.Width) / 2f;
            array[0].Y = (0f - size.Height) / 2f;
            array[1].X = (0f - size.Width) / 2f;
            array[1].Y = size.Height / 2f;
            array[2].X = size.Width / 2f;
            array[2].Y = size.Height / 2f;
            array[3].X = size.Width / 2f;
            array[3].Y = (0f - size.Height) / 2f;
            mtx.TransformPoints(array);

            show_matrix(mtx);


            float num = float.MaxValue;
            float num2 = float.MinValue;
            float num3 = float.MaxValue;
            float num4 = float.MinValue;
            PointF[] array2 = array;
            for (int i = 0; i < array2.Length; i++)
            {
                PointF pointF = array2[i];
                if (pointF.X < num)
                {
                    num = pointF.X;
                }
                if (pointF.X > num2)
                {
                    num2 = pointF.X;
                }
                if (pointF.Y < num3)
                {
                    num3 = pointF.Y;
                }
                if (pointF.Y > num4)
                {
                    num4 = pointF.Y;
                }
            }
            SizeF new_size = new SizeF(num2 - num, num4 - num3);
            richTextBox1.Text += "new_size : " + new_size.ToSize() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //測試Matrix

            // 建立一個矩陣物件, 轉置矩陣 mtx
            Matrix mtx2 = new Matrix();
            show_matrix(mtx2);

            int theta = 10;
            int Cx = 0;
            int Cy = 0;
            richTextBox1.Text += "theta = " + theta.ToString() + "\n";
            mtx2.Reset();
            mtx2.Rotate(theta, MatrixOrder.Append);
            mtx2.Translate(Cx, Cy, MatrixOrder.Append);  // 平移, 右移下移
            show_matrix(mtx2);
        }

        //測試矩陣旋轉 ST
        PointF RotationMatrix(PointF pt, double theta)
        {
            float xx = (float)(Math.Cos(theta) * pt.X - Math.Sin(theta) * pt.Y);
            float yy = (float)(Math.Sin(theta) * pt.X + Math.Cos(theta) * pt.Y);

            return new PointF(xx, yy);
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //測試矩陣旋轉
            //測試矩陣旋轉
            //測試矩陣旋轉
            g.Clear(Color.White);
            Pen p = new Pen(Color.Red, 10);
            Point point1a = new Point(0, 0);
            Point point2a = new Point(500, 0);
            //g.DrawLine(p, point1a, point2a);

            p = new Pen(Color.Green, 10);

            double theta = Math.PI / 6;
            PointF point1aa = RotationMatrix(point1a, theta);
            PointF point2aa = RotationMatrix(point2a, theta);
            //g.DrawLine(p, point1aa, point2aa);
            richTextBox1.Text += "point1aa=" + point1aa + "\n";
            richTextBox1.Text += "point2aa=" + point2aa + "\n";

            PointF[] curvePoints = new PointF[8];    //一維陣列內有 8 個Point
            for (int i = 0; i < 8; i++)
            {
                curvePoints[i].X = 50 * i;
                curvePoints[i].Y = 0;
            }
            Pen redPen = new Pen(Color.Red, 3);
            Pen grayPen = new Pen(Color.Gray, 10);
            g.DrawLines(grayPen, curvePoints);   //畫直線
            for (int i = 0; i < 8; i++)
            {
                curvePoints[i] = RotationMatrix(curvePoints[i], theta);
            }

            g.DrawLines(redPen, curvePoints);   //畫直線
            for (int i = 0; i < 8; i++)
            {
                g.FillEllipse(Brushes.Red, curvePoints[i].X - 10, curvePoints[i].Y - 10, 20, 20);
            }

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bmp = new Bitmap(filename);
            Rectangle src_area = new Rectangle(100, 100, 100, 100);//要截取的矩形區域
            Rectangle dst_area = new Rectangle(400, 50, 100, 100);//要截取的矩形區域
            //g.DrawImage(bmp, dst_area, src_area, GraphicsUnit.Pixel);
            g.DrawImage(bmp, src_area, src_area, GraphicsUnit.Pixel);

            int x_st = 100;
            int y_st = 100;
            int w = 100;
            int h = 100;
            for (int j = 0; j < h; j++)
            {
                for (int i = 0; i < w; i++)
                {
                    Color clr = bitmap1.GetPixel(x_st + i, y_st + j);
                    PointF new_pt = RotationMatrix(new PointF(x_st + i, y_st + j), theta);
                    if ((new_pt.X > 0) && (new_pt.Y > 0))
                    {
                        bitmap1.SetPixel((int)new_pt.X, (int)new_pt.Y, clr);
                    }

                }
            }
            pictureBox1.Image = bitmap1;
        }
        //測試矩陣旋轉 SP

        private void button17_Click(object sender, EventArgs e)
        {
            //Matrix 測試 1
            //Matrix 測試 1

            //矩陣的定義
            Matrix myMatrix1 = new Matrix();  // 第一種方式
            Matrix myMatrix2 = new Matrix(1, 2, 4, 5, 7, 8); // 第二種方式

            float m11 = myMatrix2.Elements[0];
            float m12 = myMatrix2.Elements[1];
            float m21 = myMatrix2.Elements[2];
            float m22 = myMatrix2.Elements[3];
            float dx = myMatrix2.Elements[4];
            float dy = myMatrix2.Elements[5];

            float dx2 = myMatrix2.OffsetX;
            float dy2 = myMatrix2.OffsetY;


            Rectangle rect = new Rectangle(0, 0, 100, 100);
            Point[] pt = new Point[3] { new Point(0, 0), new Point(100, 0), new Point(0, 100) };
            Matrix myMatrix3 = new Matrix(rect, pt); // 第三種方式

            RectangleF rect2 = new Rectangle(0, 0, 100, 100);
            PointF[] pt2 = new PointF[3] { new PointF(0, 0), new PointF(100, 0), new PointF(0, 100) };
            Matrix myMatrix4 = new Matrix(rect2, pt2); // 第四種方式

            //e.Graphics.Transform = myMatrix1;

            //矩陣的相乘的順序
            Matrix A = new Matrix(0, 1, -1, 0, 0, 0);
            Matrix B = new Matrix(1, 0, 0, 1, 1, 0);

            A.Multiply(B);  // A = B x A
            //A.Multiply(B, MatrixOrder.Prepend); // A = B x A
            //A.Multiply(B, MatrixOrder.Append);  // A = A x B
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //Matrix 測試 2
            //Matrix 測試 2
            g.Clear(Color.Pink);

            //原始資料
            int N = 10;
            PointF[] pts = new PointF[N];
            for (int i = 0; i < N; i++)
            {
                pts[i].X = 30 * i;
                pts[i].Y = 30 * i;
            }

            Matrix mtx = new Matrix();

            for (int i = 0; i < N; i++)
            {
                g.FillEllipse(Brushes.Red, pts[i].X - 15, pts[i].Y - 15, 30, 30);
            }
            g.DrawString("原始資料", new Font("標楷體", 20), new SolidBrush(Color.Red), new PointF(470, 0));

            //float angle = 45;
            //mtx.Rotate(angle);  // 旋轉
            //mtx.Translate(100, 100);  // 平移, 右移下移
            //mtx.Scale(1.5f, 1.5f);  //縮放, 水平 垂直

            // 使用矩陣物件做轉換
            float m11 = 1.0f;  // x軸縮放1.0倍
            float m12 = 0.0f;  // y軸歪曲0.0倍
            float m21 = 0.0f;  // x軸歪曲0.0倍
            float m22 = 1.0f;  // y軸縮放1.0倍
            float dx = 0.0f;  // x軸平移
            float dy = 0.0f;  // y軸平移
            Matrix matrix2 = new Matrix(m11, m12, m21, m22, dx, dy);  // 設定仿射矩陣, 矩陣轉置, 只能 矩形範圍 轉 平行四邊形範圍
            mtx.Multiply(matrix2);

            //平移倍數
            float scaleX = 1.0f;  // x軸平移 1.0倍
            float scaleY = 1.0f;  // x軸平移 1.5倍
            mtx.Scale(scaleX, scaleY);

            // 剪切, 歪曲
            float shearX = 0.0f;  // x軸歪曲0.0倍
            float shearY = 0.0f;  // y軸歪曲0.0倍
            mtx.Shear(shearX, shearY);

            mtx.TransformPoints(pts);

            for (int i = 0; i < N; i++)
            {
                g.FillEllipse(Brushes.Green, pts[i].X - 10, pts[i].Y - 10, 20, 20);
            }

            /*
            mtx.Reset();
            //mtx.Translate(100, 100);  // 平移, 右移下移
            mtx.TransformPoints(pts);

            for (int i = 0; i < N; i++)
            {
                g.FillEllipse(Brushes.Blue, pts[i].X - 5, pts[i].Y - 5, 10, 10);
            }

            mtx.Reset();
            mtx.Translate(100, 100);  // 平移, 右移下移
            mtx.TransformPoints(pts);

            for (int i = 0; i < N; i++)
            {
                g.FillEllipse(Brushes.Lime, pts[i].X - 5, pts[i].Y - 5, 10, 10);
            }
            */
            pictureBox1.Image = bitmap1;
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        float angle1 = 0;
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            return;

            // 影像旋轉(以中心順時針轉10度)
            // 旋轉一張圖片, 用圖片的中心為旋轉中心
            // 若無設定平移, 則只會以原點為旋轉中心

            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;
            // 原點平移, 右移, 下移
            e.Graphics.TranslateTransform((float)bmp.Width / 2, (float)bmp.Height / 2);

            //順時針轉10度
            angle1 += 27f;
            e.Graphics.RotateTransform(angle1);

            // 原點平移, 右移, 下移
            e.Graphics.TranslateTransform(-(float)bmp.Width / 2, -(float)bmp.Height / 2);

            //於座標(0,0)開始繪製來源影像
            e.Graphics.DrawImage(bmp, 0, 0, bmp.Width, bmp.Height);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            pictureBox1.Invalidate();
        }

        //畫一個旋轉的矩形 ST
        float angle2 = 0;  // 矩形的旋轉角度
        bool dragging = true; // 是否開始拖拉
        int Mx, My;  // 滑鼠的位置

        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            if (dragging) // 如果是在拖拉中
            {
                e.Graphics.TranslateTransform(Mx, My);
                e.Graphics.RotateTransform(angle2);
                e.Graphics.DrawRectangle(Pens.Black, -50, -50, 100, 100);
            }
        }

        private void pictureBox2_MouseMove(object sender, MouseEventArgs e)
        {
            Mx = e.X;  // 記錄滑鼠的位置
            My = e.Y;
            angle2 = angle2 + 10; // 增加 旋轉角度
            this.pictureBox2.Invalidate();
        }
        //畫一個旋轉的矩形 SP
    }

    public static class ImageEx
    {
        public static Image GetRotateImage(this Image img, float angle)
        {
            angle = angle % 360;//弧度轉換
            double radian = angle * Math.PI / 180.0;
            double cos = Math.Cos(radian);
            double sin = Math.Sin(radian);
            //原圖的寬和高
            int w = img.Width;
            int h = img.Height;
            int W = (int)(Math.Max(Math.Abs(w * cos - h * sin), Math.Abs(w * cos + h * sin)));
            int H = (int)(Math.Max(Math.Abs(w * sin - h * cos), Math.Abs(w * sin + h * cos)));

            Console.WriteLine("W = " + W.ToString() + ", H = " + H.ToString());

            //目標位圖
            Image dsImage = new Bitmap(W, H, img.PixelFormat);
            using (System.Drawing.Graphics g = System.Drawing.Graphics.FromImage(dsImage))
            {
                g.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.Bilinear;
                g.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.HighQuality;
                g.Clear(Color.White);
                //計算偏移量
                Point Offset = new Point((W - w) / 2, (H - h) / 2);
                //構造圖像顯示區域：讓圖像的中心與窗口的中心點一致
                Rectangle rect = new Rectangle(Offset.X, Offset.Y, w, h);
                Point center = new Point(rect.X + rect.Width / 2, rect.Y + rect.Height / 2);
                g.TranslateTransform(center.X, center.Y);
                g.RotateTransform(360 - angle);
                //恢復圖像在水平和垂直方向的平移
                g.TranslateTransform(-center.X, -center.Y);
                g.DrawImage(img, rect);
                //重至繪圖的所有變換
                g.ResetTransform();
                g.Save();
            }
            return dsImage;
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
            // 縮旋平
            //g.ScaleTransform(2.0f, 0.5f);  // 縮放, 水平縮放, 垂直縮放
            //g.RotateTransform(45.0f, MatrixOrder.Append);  // 旋轉, 對原點順時針旋轉
            //g.RotateTransform(45.0f, MatrixOrder.Prepend);  // 旋轉
            g.TranslateTransform(200.0f, 100.0f, MatrixOrder.Append);  // 原點平移, 右移, 下移
*/


/*
            //反向縮放
            g.ScaleTransform(-1, 1);  // 縮放, 水平縮放, 垂直縮放
            //縮放
            g.ScaleTransform(0.5f, 2);  // 縮放, 水平縮放, 垂直縮放  //x軸比例再放大, y軸比例再放大
            //縮放
            g.ScaleTransform(2.0f, 1);  // 縮放, 水平縮放, 垂直縮放  //x軸比例再放大, y軸比例再放大
            //縮放
            g.ScaleTransform(3.0f, 3);  // 縮放, 水平縮放, 垂直縮放  //x軸比例再放大, y軸比例再放大
*/

  
/*
        protected override void OnPaint(PaintEventArgs e)
        {
            SetStyle(ControlStyles.UserPaint | ControlStyles.AllPaintingInWmPaint | ControlStyles.DoubleBuffer, true);
            Graphics g = e.Graphics;
            g.SmoothingMode = SmoothingMode.HighQuality;

            foreach (Flakes s in flyFlakeList)
            {
                g.ResetTransform();
                //g.TranslateTransform(-16, -16, MatrixOrder.Append);
                g.ScaleTransform(s.Scale, s.Scale, MatrixOrder.Append);
                g.RotateTransform(s.Rotation, MatrixOrder.Append);
                g.TranslateTransform(s.X, s.Y, MatrixOrder.Append);

                g.DrawImage(s.ShowImage, 0, 0);
            }
            //base.OnPaint(e);
        }
*/
