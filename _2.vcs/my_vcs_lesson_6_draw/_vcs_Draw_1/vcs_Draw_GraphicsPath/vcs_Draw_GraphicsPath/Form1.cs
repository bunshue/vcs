using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for GraphicsPath

/*
GraphicsPath 圖形路徑
路徑是通過組合直線、矩形和簡單的曲線而形成的。
GraphicsPath對象允許將基本構造塊收集到一個單元中，
用 DrawPath / FillPath 方法，就可以繪制出整個單元的直線、矩形、多邊形和曲線。
*/

namespace vcs_Draw_GraphicsPath
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        //Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            g = pictureBox1.CreateGraphics();
            g.Clear(SystemColors.ControlLight);
            p = new Pen(Color.Red, 5);     //default pen
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
            cb_grid.Location = new Point(x_st + dx * 1, y_st + dy * 10);

            label1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox1.Size = new Size(800, 640);
            pictureBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 30);
            groupBox2.Location = new Point(x_st + dx * 2, y_st + dy * 9 + 50);

            richTextBox1.Size = new Size(300, 700);
            richTextBox1.Location = new Point(x_st + dx * 6, y_st + dy * 0 + 30);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1600, 820);
            this.Text = "vcs_Draw_GraphicsPath";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            g.Clear(SystemColors.ControlLight);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //GraphicsPath 大全0

            int x_st = 20;
            int y_st = 20;
            int dx = 100;
            //int dy = 80;
            //int w = 100;
            //int h = 100;
            Pen p = new Pen(Color.Red, 3);
            Font f = new Font("標楷體", 18);

            g.DrawString("2 AddCurve", f, Brushes.Red, x_st, y_st);

            GraphicsPath gp2 = new GraphicsPath();

            Point[] pa =
            {
                new Point(x_st+0, y_st+0), 
                new Point(x_st+0, y_st+100), 
                new Point(x_st+100, y_st+100),
                new Point(x_st+100, y_st+0)
            };

            gp2.StartFigure();
            gp2.AddCurve(pa);
            gp2.AddCurve(pa, 0.1f); // 加入曲線
            gp2.AddCurve(pa, 0.3f); // 加入曲線
            gp2.AddCurve(pa, 0.6f); // 加入曲線
            gp2.AddCurve(pa, 0.9f); // 加入曲線

            p = new Pen(Color.Blue, 1);
            g.DrawPath(p, gp2);

            x_st += 220;

            gp2.Reset();
            PointF[] pts = new PointF[]
            {
                new PointF(x_st, y_st),
                new PointF(x_st-100, y_st+200),
                new PointF(x_st+100, y_st+100),
                new PointF(x_st-100, y_st+100),
                new PointF(x_st+100, y_st+200),
                new PointF(x_st, y_st),
            };

            gp2.AddCurve(pts, 0.6f); // 加入曲線
            gp2.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接

            g.DrawPath(Pens.Black, gp2); // 繪出GraphicsPath物件

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st += dx * 3;
            g.DrawString("4", f, Brushes.Red, x_st, y_st);

            int x = x_st;
            int y = y_st;
            int width = 200;
            int height = 100;
            int cornerRadius = 20;

            //GraphicsPath gp = new GraphicsPath();  // GraphicsPath物件
            GraphicsPath gp = CreateRoundedRectanglePath(new Rectangle(x, y, width, height), cornerRadius);

            //g.DrawPath(Pens.Red, gp);
            g.FillPath(Brushes.Lime, gp);

            richTextBox1.Text += "------------------------------\n";  // 30個

            //畫圓角矩形

            x_st += dx * 2;
            x_st += 50;
            g.DrawString("5", f, Brushes.Red, x_st, y_st);

            FillRoundRectangle(g, Brushes.Plum, new Rectangle(x_st, y_st, 200, 120), 50);//圓角半徑50
            DrawRoundRectangle(g, Pens.Yellow, new Rectangle(x_st, y_st, 200, 120), 50);//圓角半徑50

            richTextBox1.Text += "------------------------------\n";  // 30個

            gp = new GraphicsPath();  // GraphicsPath物件

            x_st = 20;
            y_st = 350;


            richTextBox1.Text += "------------------------------\n";  // 30個

            //GraphicsPath - AddArc() 倒角矩形

            gp = new GraphicsPath(); // GraphicsPath物件

            int Cx = 540;
            int Cy = 400;
            int D1 = 100;

            g.DrawString("9", f, Brushes.Red, Cx, Cy);

            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 30, 30);
            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 90 + 30, 30);
            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 180 + 30, 30);
            gp.AddArc(Cx - D1, Cy - D1, 2 * D1, 2 * D1, 270 + 30, 30);
            gp.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接

            g.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件

            richTextBox1.Text += "------------------------------\n";  // 30個

            //繪製圓角矩形

            x_st = 20;
            y_st = 400;

            p = new Pen(Color.Red, 10);
            sb = new SolidBrush(Color.Blue);

            g.DrawString("10", f, Brushes.Red, x_st - 20, y_st - 20);

            GraphicsPath myPath1 = CreateRoundedRectanglePath(new Rectangle(x_st, y_st, 200, 100), 30);
            g.FillPath(sb, myPath1);

            GraphicsPath myPath2 = CreateRoundedRectanglePath(new Rectangle(x_st, y_st + 110, 200, 100), 50);
            g.DrawPath(p, myPath2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            gp = new GraphicsPath(); // GraphicsPath物件

            //gp.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接, 先封閉 第一條直線

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st = 250;
            y_st = 300;
            g.DrawString("7", f, Brushes.Red, x_st, y_st);
            //GraphicsPath - AddLines() 一系列的直線
            //GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件
            Point[] pts2 = new Point[3];  // 點陣列
            pts2[0] = new Point(x_st + 20, y_st + 120);
            pts2[1] = new Point(x_st + 120, y_st + 20);
            pts2[2] = new Point(x_st + 220, y_st + 120);

            gp.AddLines(pts2); // 將 一系列的直線 加入到 GraphicsPath物件
            //gp.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接

            g.DrawPath(Pens.Red, gp); // 繪出GraphicsPath物件

            richTextBox1.Text += "------------------------------\n";  // 30個

            //畫聯結線條
            gp = new GraphicsPath();
            Pen penJoin = new Pen(Color.Red, 20);

            gp.StartFigure();
            x_st = 500;
            y_st = 360;
            int D = 100;
            g.DrawString("8", f, Brushes.Red, x_st - 20, y_st);

            gp.AddLine(new Point(x_st, y_st), new Point(x_st + D, y_st));
            gp.AddLine(new Point(x_st + D, y_st), new Point(x_st + D, y_st + D));
            penJoin.LineJoin = LineJoin.Bevel;
            g.DrawPath(penJoin, gp);
        }

        public void DrawRoundRectangle(Graphics g, Pen pen, Rectangle rect, int cornerRadius)
        {
            using (GraphicsPath gp = CreateRoundedRectanglePath(rect, cornerRadius))
            {
                g.DrawPath(pen, gp);
            }
        }

        public void FillRoundRectangle(Graphics g, Brush brush, Rectangle rect, int cornerRadius)
        {
            using (GraphicsPath gp = CreateRoundedRectanglePath(rect, cornerRadius))
            {
                g.FillPath(brush, gp);
                /*
                //左上
                g.DrawArc(Pens.Red, rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
                //上
                g.DrawLine(Pens.Green, rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
                //右上
                g.DrawArc(Pens.Blue, rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
                //右
                g.DrawLine(Pens.Cyan, rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
                //右下
                g.DrawArc(Pens.Magenta, rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
                //下
                g.DrawLine(Pens.Yellow, rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
                //左下
                g.DrawArc(Pens.Black, rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
                //左
                g.DrawLine(Pens.Lime, rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
                */
            }
        }

        //繪製圓角矩形
        private GraphicsPath CreateRoundedRectanglePath(Rectangle rect, int cornerRadius)
        {
            GraphicsPath roundedRect = new GraphicsPath();
            //左上
            roundedRect.AddArc(rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
            //上
            roundedRect.AddLine(rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
            //右上
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
            //右
            roundedRect.AddLine(rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
            //右下
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
            //下
            roundedRect.AddLine(rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
            //左下
            roundedRect.AddArc(rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
            //左
            roundedRect.AddLine(rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
            roundedRect.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接
            return roundedRect;
        }

        //------------------------------------------------------------  # 60個

        private void button1_Click(object sender, EventArgs e)
        {
            //GraphicsPath 大全1

            GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件
            int Cx = 150;
            int Cy = 50;

            Point p1 = new Point(Cx - 100, Cy); // 計算出 直線的兩端
            Point p2 = new Point(Cx + 100, Cy);
            gp.AddLine(p1, p2); // 將 直線 加入到 GraphicsPath物件

            Rectangle rect1 = new Rectangle(Cx - 100 - 20, Cy - 20, 40, 40);
            Rectangle rect2 = new Rectangle(Cx + 100 - 20, Cy - 20, 40, 40);
            gp.AddRectangle(rect1);  // 將 兩個矩形 加入到 GraphicsPath物件
            gp.AddRectangle(rect2);

            g.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件
            g.FillPath(Brushes.Lime, gp);

            richTextBox1.Text += "------------------------------\n";  // 30個

            GraphicsPath gp2 = new GraphicsPath();
            Region region1; // 宣告一個 Region區域表面 物件

            Cx = 200;
            Cy = 350;
            richTextBox1.Text += Cx.ToString() + "\t" + Cy.ToString() + "\n";

            int W = 250;  // 矩形的寬
            int H = 150; // 矩形的高
            richTextBox1.Text += W.ToString() + "\t" + H.ToString() + "\n";

            Rectangle rect3 = new Rectangle(Cx - W / 2, Cy - H / 2, W, H);
            gp2.AddRectangle(rect3); // 加入一個矩形形狀

            region1 = new Region(gp2); // 新增一個 Region 區域表面物件，以 gp2 為參數
            // region1 = new Region(rect3);  // 或是直接以 rect3 為參數

            g.FillRegion(Brushes.Cyan, region1); // 區域表面 繪出

            //g.FillPath(Brushes.Lime, gp2);
            g.DrawPath(Pens.Red, gp2);

            richTextBox1.Text += "------------------------------\n";  // 30個

            GraphicsPath gp3 = new GraphicsPath();

            int x = 550;
            int y = 300;

            // 圓形的半徑
            int D = 50;

            //多邊形
            PointF[] points = new PointF[]
            {
                //new PointF(40, 80),
                //new PointF(120, 100),
                //new PointF(230, 70),
                new Point(x - 2 * D,y - 3*D),
                new Point(x + 2 * D,y - 3*D),
                new Point(x + 5 * D,y ),
                new Point(x + 2 * D,y + 3*D),
                new Point(x - 2 * D,y + 3*D),
                new Point(x - 5 * D,y),
            };

            gp3.AddPolygon(points);  // 多邊形
            gp3.AddEllipse(x - D, y - D, 2 * D, 2 * D);  // 在 多邊形 正中的 圓形

            Region region2 = new Region(gp3); // 區域表面 物件
            LinearGradientBrush brush = new LinearGradientBrush(
                             new Point(x - 2 * D, y - 3 * D), // 線形漸層的開始點。
                             new Point(x + 2 * D, y + 3 * D), // 線形漸層的結束點。
                             Color.White,
                             Color.Red); // 線形漸層塗刷

            g.FillRegion(brush, region2); // 區域表面 繪出
            g.DrawPath(Pens.Black, gp3);

            g.DrawLines(new Pen(Color.Blue, 10), points);

            return;

            richTextBox1.Text += "------------------------------\n";  // 30個

            GraphicsPath gp4 = new GraphicsPath(); // GraphicsPath物件

            int x_st = 500;
            int y_st = 500;
            D = 100;

            // 第一個矩形
            Rectangle rect1a = new Rectangle(x_st, y_st, D, D);
            gp4.AddRectangle(rect1a); // 將 矩形 加入到 GraphicsPath物件            

            // 第二個矩形
            Rectangle rect2a = new Rectangle(x_st - 20, y_st - 20, 40, 40);
            gp4.AddRectangle(rect2a); // 將 矩形 加入到 GraphicsPath物件

            // 第三個矩形
            Rectangle rect3a = new Rectangle(x_st + D - 20, y_st - 20, 40, 40);
            gp4.AddRectangle(rect3a); // 將 矩形 加入到 GraphicsPath物件

            // 第四個矩形
            Rectangle rect4a = new Rectangle(x_st - 20, y_st + D - 20, 40, 40);
            gp4.AddRectangle(rect4a); // 將 矩形 加入到 GraphicsPath物件

            // 第五個矩形
            Rectangle rect5a = new Rectangle(x_st + D - 20, y_st + D - 20, 40, 40);
            gp4.AddRectangle(rect5a); // 將 矩形 加入到 GraphicsPath物件

            g.DrawPath(Pens.Black, gp4); // 繪出GraphicsPath物件
            //g.FillPath(Brushes.Red, gp4);

            richTextBox1.Text += "------------------------------\n";  // 30個

            GraphicsPath gp5 = new GraphicsPath(); // GraphicsPath物件

            Rectangle[] rects = new Rectangle[5];

            x_st = 650;
            y_st = 500;
            D = 100;

            // 第一個矩形
            rects[0] = new Rectangle(x_st, y_st, D, D);
            // 第二個矩形
            rects[1] = new Rectangle(x_st - 20, y_st - 20, 40, 40);
            // 第三個矩形
            rects[2] = new Rectangle(x_st + D - 20, y_st - 20, 40, 40);
            // 第四個矩形
            rects[3] = new Rectangle(x_st - 20, y_st + D - 20, 40, 40);
            // 第五個矩形
            rects[4] = new Rectangle(x_st + D - 20, y_st + D - 20, 40, 40);

            gp5.AddRectangles(rects); // 將 矩形陣列 加入到 GraphicsPath物件

            g.DrawPath(Pens.Red, gp5); // 繪出GraphicsPath物件

            richTextBox1.Text += "------------------------------\n";  // 30個

            Rectangle rect = new Rectangle(30, 100, 300, 150);

            g.DrawRectangle(Pens.Red, rect);

            int i;
            for (i = 10; i < 100; i += 20)
            {
                GraphicsPath gps = CreateRoundRectangle(rect, i);
                g.DrawPath(Pens.Green, gps);
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            x_st = 20;
            y_st = 450;

            gp = new GraphicsPath(); // GraphicsPath物件
            Pen p = new Pen(Color.Blue, 1);
            Point[] pts = { new Point(x_st + 15, y_st + 30), new Point(x_st + 30, y_st + 40), new Point(x_st + 50, y_st + 30) };
            gp.AddArc(x_st + 15, y_st + 20, 80, 50, 210, 120);
            gp.StartFigure();
            gp.AddCurve(pts);
            gp.AddPie(x_st + 180, y_st + 20, 80, 50, 210, 120);

            g.DrawPath(p, gp);  // 繪出GraphicsPath物件

            richTextBox1.Text += "------------------------------\n";  // 30個


        }

        //DrawHelper的创建圆角矩形函数
        /// <summary>
        /// 创建圆角矩形
        /// </summary>
        /// <param name="rectangle">圆角矩形的边界矩形</param>
        /// <param name="radius">圆角大小</param>
        /// <returns>返回圆角矩形的路径</returns>

        public static GraphicsPath CreateRoundRectangle(Rectangle rectangle, int radius)
        {
            GraphicsPath path = new GraphicsPath(FillMode.Winding);
            int l = rectangle.Left;
            int t = rectangle.Top;
            int w = rectangle.Width;
            int h = rectangle.Height;
            int d = radius << 1;
            path.AddArc(l, t, d, d, 180, 90); // topleft
            path.AddArc(l + w - d, t, d, d, 270, 90); // topright
            path.AddArc(l + w - d, t + h - d, d, d, 0, 90); // bottomright
            path.AddArc(l, t + h - d, d, d, 90, 90); // bottomleft
            path.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接
            return path;
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            //GraphicsPath 整理

            int x_st = 0;
            int y_st = 0;
            //int dx = 100;
            //int dy = 80;
            //int w = 100;
            //int h = 100;
            //int R = 100;
            Pen p = new Pen(Color.Red, 1);
            Font f = new Font("標楷體", 18);

            g.DrawString("1", f, Brushes.Red, x_st, y_st);

            GraphicsPath gp1 = new GraphicsPath();
            gp1.Reset();

            gp1.AddLine(new Point(x_st, y_st + 100), new Point(x_st + 200, y_st + 100 + 200));
            gp1.AddLine(new Point(x_st, y_st + 100 + 200), new Point(x_st + 200, y_st + 100));
            gp1.AddRectangle(new Rectangle(x_st + 0, y_st + 100, 200, 200));
            gp1.AddEllipse(x_st + 0, y_st + 100, 200, 200);

            //         圓左上x,y  圓寬 圓高 起角 順範圍
            gp1.AddPie(30, 30, 140, 140, 200, 140);

            //           圓左上x,y         圓寬 圓高 起角 順範圍
            gp1.AddArc(x_st + 0, x_st + 0, 200, 200, 180, 180);

            //加入貝茲線
            x_st += 150;
            gp1.AddBezier(x_st + 50 + 100, y_st + 50, x_st + 200, 0, x_st + 300, 180, x_st + 400, 20);

            g.DrawPath(p, gp1);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //箭頭樣式

            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a GraphicsPath to define the start cap.
            GraphicsPath gp1 = new GraphicsPath();
            gp1.AddArc(-2, 0, 4, 4, 180, 180);

            // Make the start cap.
            CustomLineCap start_cap = new CustomLineCap(null, gp1);
            // Make a GraphicsPath to define the end cap.
            GraphicsPath gp2 = new GraphicsPath();
            gp2.AddLine(0, 0, -2, -2);
            gp2.AddLine(0, 0, 2, -2);

            // Make the end cap.
            CustomLineCap end_cap = new CustomLineCap(null, gp2);
            // Make a pen that uses the custom caps.

            Pen p1 = new Pen(Color.Red, 5);
            p1.CustomStartCap = start_cap;
            p1.CustomEndCap = end_cap;
            Pen p2 = new Pen(Color.Green, 5);
            p2.CustomStartCap = start_cap;
            p2.CustomEndCap = end_cap;
            Pen p3 = new Pen(Color.Blue, 5);
            p3.CustomStartCap = start_cap;
            p3.CustomEndCap = end_cap;

            richTextBox1.Text += "------------------------------\n";  // 30個

            // Draw a line.
            g.DrawLine(p1, 50, 50, 200, 50);

            richTextBox1.Text += "------------------------------\n";  // 30個

            // Draw a polygon.
            PointF[] points = new PointF[]
            {
                new PointF(40, 100),
                new PointF(120, 120),
                new PointF(230, 90),
            };
            g.DrawLines(p2, points);

            richTextBox1.Text += "------------------------------\n";  // 30個

            g.DrawArc(p3, 50, 150, 150, 80, 180, 270);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //在曲線的上下畫字
            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.High;

            // Draw some text along some paths.
            GraphicsPath gp = new GraphicsPath();
            gp.AddArc(new RectangleF(40, 40, 320, 220), 180, 180);
            g.DrawPath(Pens.Green, gp);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", gp, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", gp, false);

            gp = new GraphicsPath();
            gp.AddArc(new RectangleF(40, 50, 320, 220), 0, 180);
            g.DrawPath(Pens.Red, gp);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", gp, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", gp, false);
        }

        // Draw some text along a GraphicsPath.
        private void DrawTextOnPath(Graphics gr, Brush brush, Font font, string txt, GraphicsPath path, bool text_above_path)
        {
            // Make a copy so we don't mess up the original.
            path = (GraphicsPath)path.Clone();

            // Flatten the path into segments.
            path.Flatten();

            // Draw characters.
            int start_ch = 0;
            PointF start_point = path.PathPoints[0];  // 取得路徑中的點 第0點
            for (int i = 1; i < path.PointCount; i++)
            {
                PointF end_point = path.PathPoints[i];  // 取得路徑中的點 第i點
                DrawTextOnSegment2(gr, brush, font, txt, ref start_ch, ref start_point, end_point, text_above_path);
                if (start_ch >= txt.Length)
                {
                    break;
                }
            }
        }

        // Draw some text along a line segment.
        // Leave char_num pointing to the next character to be drawn.
        // Leave start_point holding the coordinates of the last point used.
        private void DrawTextOnSegment2(Graphics gr, Brush brush, Font font, string txt, ref int first_ch, ref PointF start_point, PointF end_point, bool text_above_segment)
        {
            float dx = end_point.X - start_point.X;
            float dy = end_point.Y - start_point.Y;
            float dist = (float)Math.Sqrt(dx * dx + dy * dy);
            dx /= dist;
            dy /= dist;

            // See how many characters will fit.
            int last_ch = first_ch;
            while (last_ch < txt.Length)
            {
                string test_string = txt.Substring(first_ch, last_ch - first_ch + 1);
                if (gr.MeasureString(test_string, font).Width > dist)
                {
                    // This is one too many characters.
                    last_ch--;
                    break;
                }
                last_ch++;
            }

            if (last_ch < first_ch)
            {
                return;
            }

            if (last_ch >= txt.Length)
            {
                last_ch = txt.Length - 1;
            }

            string chars_that_fit = txt.Substring(first_ch, last_ch - first_ch + 1);

            // Rotate and translate to position the characters.
            GraphicsState state = gr.Save();
            if (text_above_segment)
            {
                gr.TranslateTransform(0, -gr.MeasureString(chars_that_fit, font).Height, MatrixOrder.Append);
            }
            float angle = (float)(180 * Math.Atan2(dy, dx) / Math.PI);
            gr.RotateTransform(angle, MatrixOrder.Append);
            gr.TranslateTransform(start_point.X, start_point.Y, MatrixOrder.Append);

            // Draw the characters that fit.
            gr.DrawString(chars_that_fit, font, brush, 0, 0);

            // Restore the saved state.
            gr.Restore(state);

            // Update first_ch and start_point.
            first_ch = last_ch + 1;
            float text_width = gr.MeasureString(chars_that_fit, font).Width;
            start_point = new PointF(start_point.X + dx * text_width, start_point.Y + dy * text_width);
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //不規則圖形裁剪圖片

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename, false);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            GraphicsPath path = new GraphicsPath();

            Point[] pts =
            {
                new Point(W/2,10),
                new Point(W/5,H/5),
                new Point(10,H/2),
                new Point(W/5,H*4/5),
                new Point(W/2,H-10),
                new Point(W*4/5,H*4/5),
                new Point(W-10,H/2),
                new Point(W*4/5,H/5),
                new Point(W/2,10)
            };
            path.AddLines(pts);

            Bitmap bitmap2 = null;
            BitmapCrop(bitmap1, path, out bitmap2);
            pictureBox1.Image = bitmap2;
        }

        /// 圖片截圖
        /// <param name="bitmap">原圖</param>
        /// <param name="path">裁剪路徑</param>
        /// <param name="outputBitmap">輸出圖</param>
        public static Bitmap BitmapCrop(Bitmap bitmap, GraphicsPath path, out Bitmap outputBitmap)
        {
            RectangleF rect = path.GetBounds();
            int left = (int)rect.Left;
            int top = (int)rect.Top;
            int width = (int)rect.Width;
            int height = (int)rect.Height;
            Bitmap image = (Bitmap)bitmap.Clone();
            outputBitmap = new Bitmap(width, height);
            for (int i = left; i < left + width; i++)
            {
                for (int j = top; j < top + height; j++)
                {
                    //判斷坐標是否在路徑中   
                    if (path.IsVisible(i, j))
                    {
                        //復制原圖區域的像素到輸出圖片   
                        outputBitmap.SetPixel(i - left, j - top, image.GetPixel(i, j));
                        //設置原圖這部分區域為透明   
                        image.SetPixel(i, j, Color.FromArgb(0, image.GetPixel(i, j)));
                    }
                    else
                    {
                        outputBitmap.SetPixel(i - left, j - top, Color.FromArgb(0, 255, 255, 255));
                    }
                }
            }
            bitmap.Dispose();
            return image;
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //GraphicsPath 大全 字

            int x_st = 360;
            int y_st = 20;
            Pen p = new Pen(Color.Red, 3);
            Font f = new Font("標楷體", 18);

            g.DrawString("3加入字串", f, Brushes.Red, x_st, y_st);

            p = new Pen(Color.Blue, 1);

            GraphicsPath gp = new GraphicsPath();
            FontFamily font_family = new FontFamily("標楷體");//設定字體樣式

            int fontStyle = (int)FontStyle.Italic;
            int emSize = 40;
            PointF pt = new PointF(x_st, y_st);
            StringFormat format = StringFormat.GenericDefault;
            // format.FormatFlags = StringFormatFlags.DirectionVertical;　// 垂直

            // GP加入字串
            string text = "加入字串範例";
            gp.AddString(text, font_family, fontStyle, emSize, pt, format);
            gp.AddString(text, font_family, (int)FontStyle.Regular, 50, new Point(x_st, y_st + 30), format);
            gp.AddString(text, new FontFamily("標楷體"), (int)FontStyle.Underline, 50, new PointF(x_st, y_st + 80), new StringFormat());

            g.DrawPath(p, gp); // 繪出GraphicsPath物件

            richTextBox1.Text += "------------------------------\n";  // 30個

            //畫字範例 + 放大

            float size = 2.0f;//放大倍率

            text = size.ToString() + " 倍\n海納百川，\n有容乃大；\n壁立千仞，\n無欲則剛。";//設定字串

            GraphicsPath gp1 = new GraphicsPath();//實例化GraphicsPath對像
            // GP加入字串
            gp1.AddString(text, font_family, (int)FontStyle.Regular, 36, new Point(0, 0), new StringFormat());//在路徑中新增文字

            richTextBox1.Text += "------------------------------\n";  // 30個

            //取出圖形路徑的所有點 => 矩陣轉換 => 轉 圖形路徑gp => 畫出來

            PointF[] Var_PointS = gp1.PathPoints;  // 取得路徑中的點
            Byte[] Car_Types = gp1.PathTypes;  // 取得對應點的類型

            //richTextBox1.Text += "len = " + Var_PointS.Length.ToString() + "\n";

            Matrix matrix = new Matrix((float)size, 0.0F, 0.0F, (float)size, 0.0F, 0.0F);//設定仿射矩陣
            matrix.TransformPoints(Var_PointS);

            GraphicsPath gp2 = new GraphicsPath(Var_PointS, Car_Types);

            //g.FillPath(Brushes.Red, gp2);
            g.DrawPath(p, gp2);
        }

        Point[] get_star_points(Point center,int R1, int R2)
        {
            Point[] pts = new Point[10];    //一維陣列內有10個Point

            for (int i = 0; i < 10; i++)
            {
                int angle = -90 + 36 * i;
                if (i % 2 == 0)
                {
                    pts[i].X = (int)(R1 * Math.Cos(angle * Math.PI / 180));
                    pts[i].Y = (int)(R1 * Math.Sin(angle * Math.PI / 180));
                }
                else
                {
                    pts[i].X = (int)(R2 * Math.Cos(angle * Math.PI / 180));
                    pts[i].Y = (int)(R2 * Math.Sin(angle * Math.PI / 180));
                }
                pts[i].X += center.X;
                pts[i].Y += center.Y;
                //richTextBox1.Text += "pts[" + i.ToString() + "].X " + pts[i].X.ToString() + "   " + "pts[" + i.ToString() + "].Y " + pts[i].Y.ToString() + "\n";
            }
            return pts;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //測試AddLine AddLines AddEllipse

            //原本畫在原點
            Point center = new Point(200, 200);
            int radius1 = 100;
            int radius2 = 60;
            Point[] pts = get_star_points(center, radius1, radius2);

            GraphicsPath gp = new GraphicsPath();

            gp.StartFigure();
            gp.AddLine(pts[0], pts[1]);
            gp.AddLine(pts[1], pts[2]);
            gp.AddLine(pts[2], pts[3]);
            gp.AddLine(pts[3], pts[4]);
            gp.AddLine(pts[4], pts[5]);
            gp.AddLine(pts[5], pts[6]);
            gp.AddLine(pts[6], pts[7]);
            gp.AddLine(pts[7], pts[8]);
            gp.AddLine(pts[8], pts[9]);
            gp.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接
            gp.AddEllipse(center.X - radius1, center.Y - radius1, radius1 * 2, radius1 * 2);
            gp.AddRectangle(new Rectangle(center.X - radius1, center.Y - radius1, radius1 * 2, radius1 * 2));

            //g.DrawPath(Pens.Red, gp); // 繪出GraphicsPath物件
            g.FillPath(Brushes.Red, gp);  // FillPath會自動CloseFigure()

            richTextBox1.Text += "------------------------------\n";  // 30個

            center = new Point(450, 200);
            radius1 = 100;
            radius2 = 60;
            pts = get_star_points(center, radius1, radius2);

            //GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件

            gp.Reset();
            gp.StartFigure();

            gp.AddLines(pts); // 將 一系列的直線 加入到 GraphicsPath物件
            gp.CloseFigure();  // 封閉圖形路徑, 將圖形的頭尾座標連接

            g.DrawPath(Pens.Red, gp); // 繪出GraphicsPath物件
            g.FillPath(Brushes.Yellow, gp);  // FillPath會自動CloseFigure()
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
            Application.Exit();
        }

        private GraphicsPath CreateRound(Rectangle rectangle, int r)
        {
            int l = 2 * r;
            // 把圆角矩形分成八段直线、弧的组合，依次加到路径中 
            GraphicsPath gp = new GraphicsPath();
            //上
            gp.AddLine(new Point(rectangle.X + r, rectangle.Y), new Point(rectangle.Right - r, rectangle.Y));
            //右上
            gp.AddArc(new Rectangle(rectangle.Right - l, rectangle.Y, l, l), 270F, 90F);
            //右
            gp.AddLine(new Point(rectangle.Right, rectangle.Y + r), new Point(rectangle.Right, rectangle.Bottom - r));
            //右下
            gp.AddArc(new Rectangle(rectangle.Right - l, rectangle.Bottom - l, l, l), 0F, 90F);
            //下
            gp.AddLine(new Point(rectangle.Right - r, rectangle.Bottom), new Point(rectangle.X + r, rectangle.Bottom));
            //左下
            gp.AddArc(new Rectangle(rectangle.X, rectangle.Bottom - l, l, l), 90F, 90F);
            //左
            gp.AddLine(new Point(rectangle.X, rectangle.Bottom - r), new Point(rectangle.X, rectangle.Y + r));
            //左上
            gp.AddArc(new Rectangle(rectangle.X, rectangle.Y, l, l), 180F, 90F);
            return gp;
        }

        private void pictureBox_progressbar_Paint(object sender, PaintEventArgs e)
        {
            //畫背景
            Rectangle rect = e.ClipRectangle;
            int x_st = 0;
            int y_st = 0;
            int w = 530;
            int h = 12;
            rect = new Rectangle(x_st, y_st, w - 1, h);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;//消除锯齿
            GraphicsPath round = CreateRound(rect, 5);
            e.Graphics.FillPath(new SolidBrush(Color.FromArgb(217, 218, 219)), round);

            //畫前景進度
            rect = new Rectangle(x_st, y_st, ((w * percentageValues) / 100) - 1, h);
            e.Graphics.SmoothingMode = SmoothingMode.AntiAlias;//消除锯齿
            round = CreateRound(rect, 5);
            if (percentageValues <= 70)
            {
                e.Graphics.FillPath(new SolidBrush(Color.FromArgb(25, 176, 132)), round);
            }
            else
            {
                e.Graphics.FillPath(new SolidBrush(Color.Red), round);
            }
        }

        int percentageValues = 0;
        private void timer_progressbar_Tick(object sender, EventArgs e)
        {
            this.pictureBox_progressbar.Invalidate();
            percentageValues++;
            if (percentageValues > 100)
            {
                percentageValues = 0;
            }
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Form1_Resize(object sender, EventArgs e)
        {
        }

        private void cb_grid_CheckedChanged(object sender, EventArgs e)
        {
            if (cb_grid.Checked == true)
            {
                // 輔助線
                for (int i = 0; i < 8; i++)
                {
                    g.DrawLine(Pens.Gray, 0, i * 100, 640, i * 100);//橫線
                    g.DrawLine(Pens.Gray, i * 100, 0, i * 100, 500);//直線
                }
                //g.DrawRectangle(Pens.Red, 100, 100, 200, 200);
            }
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


/*

*/



// Draw a transformed arc. 放大3倍??
//g.ScaleTransform(3, 1);


//填滿組合路徑 fill
// 繪出文字字串//繪出組合路徑 draw



//  Pen penJoin = new Pen(Color.Red, 5);
//  penJoin.LineJoin = LineJoin.Bevel;//看不出效果


