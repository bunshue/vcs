using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for GraphicsPath

namespace vcs_Draw_GraphicsPath
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

        private void Form1_Load(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 3);
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 10);     //default pen

            show_item_location();

            //繪製圓角表單
            this.BackColor = Color.Pink;
            this.FormBorderStyle = FormBorderStyle.None;
            this.Region = null;
            SetWindowRegion();
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
            dx = 180;
            dy = 80;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //畫圖形路徑
            //繪制圖形路徑
            //路徑是通過組合直線、矩形和簡單的曲線而形成的。
            //在GDI+中，GraphicsPath對象允許將基本構造塊收集到一個單元中，調用一次Graphics類的DrawPath方法，就可以繪制出整個單元的直線、矩形、多邊形和曲線。

            Graphics g = this.pictureBox1.CreateGraphics();
            GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件
            Pen p = new Pen(Color.Blue, 1);
            Point[] pts = { new Point(15, 30), new Point(30, 40), new Point(50, 30) };
            gp.AddArc(15, 20, 80, 50, 210, 120);
            gp.StartFigure();
            gp.AddCurve(pts);
            gp.AddPie(180, 20, 80, 50, 210, 120);

            // 繪出文字字串
            gp.AddString("圖形路徑", new FontFamily("標楷體"), (int)FontStyle.Underline, 50, new PointF(20, 50), new StringFormat());

            // 將 gp 內的形狀 繪出
            g.DrawPath(p, gp);  // 繪出GraphicsPath物件

            //參數分開寫
            string text = "天若有情天亦老"; // 文字字串
            FontFamily family = new FontFamily("標楷體");
            StringFormat format = StringFormat.GenericDefault;
            // format.FormatFlags = StringFormatFlags.DirectionVertical;　// 垂直

            // 繪出文字字串
            gp.AddString(text, family, (int)FontStyle.Regular, 50, new Point(20, 120), format);

            // 將 gp 內的形狀 繪出
            g.DrawPath(p, gp); // 繪出GraphicsPath物件
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //畫聯結線條
            GraphicsPath gp = new GraphicsPath();
            Pen penJoin = new Pen(Color.FromArgb(255, 0, 0, 255), 20);

            gp.StartFigure();
            gp.AddLine(new Point(50, 200), new Point(100, 200));
            gp.AddLine(new Point(100, 200), new Point(100, 250));

            penJoin.LineJoin = LineJoin.Bevel;
            g.DrawPath(penJoin, gp);
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        //箭頭樣式
        private void button3_Click(object sender, EventArgs e)
        {
            g.SmoothingMode = SmoothingMode.AntiAlias;

            // Make a GraphicsPath to define the start cap.
            using (GraphicsPath start_path = new GraphicsPath())
            {
                start_path.AddArc(-2, 0, 4, 4, 180, 180);

                // Make the start cap.
                using (CustomLineCap start_cap = new CustomLineCap(null, start_path))
                {
                    // Make a GraphicsPath to define the end cap.
                    using (GraphicsPath end_path = new GraphicsPath())
                    {
                        end_path.AddLine(0, 0, -2, -2);
                        end_path.AddLine(0, 0, 2, -2);

                        // Make the end cap.
                        using (CustomLineCap end_cap = new CustomLineCap(null, end_path))
                        {
                            // Make a pen that uses the custom caps.
                            using (Pen the_pen = new Pen(Color.Blue, 5))
                            {
                                the_pen.CustomStartCap = start_cap;
                                the_pen.CustomEndCap = end_cap;

                                // Draw a line.
                                g.DrawLine(the_pen, 40, 40, 200, 40);

                                // Draw a polygon.
                                PointF[] points = new PointF[] 
                                {
                                    new PointF(40, 80),
                                    new PointF(120, 100),
                                    new PointF(230, 70),
                                };
                                the_pen.Color = Color.Green;
                                g.DrawLines(the_pen, points);

                                // Draw a transformed arc.
                                g.ScaleTransform(3, 1);
                                the_pen.Color = Color.Red;
                                g.DrawArc(the_pen, 20, 120, 70, 60, 180, 270);
                            }
                        }
                    }
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //繪製圓角矩形
            p = new Pen(Color.Red, 10);     // 設定畫筆為藍色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);

            GraphicsPath myPath1 = DrawRoundRect(100, 100, 200, 100, 30);
            g.FillPath(sb, myPath1);

            GraphicsPath myPath2 = DrawRoundRect(100, 250, 400, 300, 50);
            g.DrawPath(p, myPath2);
        }

        //繪製圓角矩形
        private GraphicsPath DrawRoundRect(float x, float y, float width, float height, float cornerRadius)
        {
            GraphicsPath roundedRect = new GraphicsPath();
            Rectangle rect = new Rectangle((int)x, (int)y, (int)width, (int)height);
            roundedRect.AddArc(rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
            roundedRect.AddLine(rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
            roundedRect.AddLine(rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
            roundedRect.AddLine(rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
            roundedRect.AddArc(rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
            roundedRect.AddLine(rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
            roundedRect.CloseFigure();
            return roundedRect;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            g.Clear(Color.White);

            Rectangle rect = new Rectangle(100, 100, 400, 200);

            g.DrawRectangle(Pens.Red, rect);

            int i;
            for (i = 10; i < 100; i += 20)
            {
                GraphicsPath gp = CreateRoundRectangle(rect, i);
                g.DrawPath(Pens.Green, gp);
            }
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
            path.CloseFigure();
            return path;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Graphics g = pictureBox1.CreateGraphics();

            GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件

            Point p1 = new Point(10, 20); // 直線的兩端
            Point p2 = new Point(100, 20);

            //GraphicsPath - AddLine() 頭尾相連的兩條直線
            gp.AddLine(p1, p2); // 將 直線 加入到 GraphicsPath物件
            //gp.AddLine(10, 20, 100, 20);  same

            g.DrawPath(Pens.Red, gp); // 繪出GraphicsPath物件

            //gp.CloseFigure(); // 先封閉 第一條直線

            Point p3 = new Point(10, 50); // 直線的兩端
            Point p4 = new Point(100, 50);
            gp.AddLine(p3, p4); // 將第二條直線 加入到 GraphicsPath物件

            g.DrawPath(Pens.Red, gp); // 繪出GraphicsPath物件

            /*
            //GraphicsPath - AddLines() 一系列的直線
            //GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件
            Point[] pt = new Point[3];  // 點陣列
            pt[0] = new Point(20, 120);
            pt[1] = new Point(120, 20);
            pt[2] = new Point(220, 120);

            gp.AddLines(pt); // 將 一系列的直線 加入到 GraphicsPath物件
            //gp.CloseFigure(); // 封閉 該形狀

            g.DrawPath(Pens.Red, gp); // 繪出GraphicsPath物件
            */

        }

        private void button7_Click(object sender, EventArgs e)
        {



            //連接繪圖物件
            GraphicsPath gp = new GraphicsPath(); // GraphicsPath物件
            int Cx = this.pictureBox1.ClientSize.Width * 1 / 4;   // 找到視窗客戶區中心點
            int Cy = this.pictureBox1.ClientSize.Height / 4;

            Point p1 = new Point(Cx - 100, Cy); // 計算出 直線的兩端
            Point p2 = new Point(Cx + 100, Cy);
            gp.AddLine(p1, p2); // 將 直線 加入到 GraphicsPath物件

            Rectangle rect1 = new Rectangle(Cx - 100 - 20, Cy - 20, 40, 40);
            Rectangle rect2 = new Rectangle(Cx + 100 - 20, Cy - 20, 40, 40);
            gp.AddRectangle(rect1);  // 將 兩個矩形 加入到 GraphicsPath物件
            gp.AddRectangle(rect2);

            g.DrawPath(Pens.Black, gp); // 繪出GraphicsPath物件

            GraphicsPath gp2 = new GraphicsPath(); // GraphicsPath圖形軌跡物件
            Region rgn; // 宣告一個 Region區域表面 物件

            Cx = this.pictureBox1.ClientSize.Width * 1 / 4; // 視窗客戶區的中心點
            Cy = this.pictureBox1.ClientSize.Height * 3 / 4;
            int W = this.pictureBox1.ClientSize.Width / 3;  // 矩形的寬
            int H = this.pictureBox1.ClientSize.Height / 3; // 矩形的高

            Rectangle rect3 = new Rectangle(Cx - W / 2, Cy - H / 2, W, H);
            gp2.AddRectangle(rect3); // 圖形軌跡物件 加入一個矩形形狀

            rgn = new Region(gp2); // 新增一個 Region 區域表面物件，以 gp2 為參數
            // rgn = new Region(rect3);  // 或是直接以 rect3 為參數

            g.FillRegion(Brushes.Cyan, rgn); // 區域表面 繪出
            g.DrawPath(Pens.Black, gp2); // 圖形軌跡 繪出


            GraphicsPath gp3 = new GraphicsPath(); // GraphicsPath圖形軌跡物件

            int x = this.pictureBox1.ClientSize.Width * 3 / 4; // 視窗客戶區的正中央
            int y = this.pictureBox1.ClientSize.Height * 3 / 4;
            // 圓形的  半徑
            int D = Math.Min(this.pictureBox1.ClientSize.Width, this.pictureBox1.ClientSize.Height) / 8;

            gp3.AddPolygon(new Point[]{
                 new Point(x - 2 * D,y - 3*D),
                 new Point(x + 2 * D,y - 3*D),
                 new Point(x + 5 * D,y ),
                 new Point(x + 2 * D,y + 3*D),
                 new Point(x - 2 * D,y + 3*D),
                 new Point(x - 5 * D,y),
               });  // 多邊形
            gp3.AddEllipse(x - D, y - D, 2 * D, 2 * D);  // 在 多邊形 正中的 圓形

            Region rgn2 = new Region(gp3); // 區域表面 物件
            LinearGradientBrush brush = new LinearGradientBrush(
                             new Point(x - 2 * D, y - 3 * D), // 線形漸層的開始點。
                             new Point(x + 2 * D, y + 3 * D), // 線形漸層的結束點。
                             Color.White,
                             Color.Red); // 線形漸層塗刷

            g.FillRegion(brush, rgn2); // 區域表面 繪出
            g.DrawPath(Pens.Black, gp3); // 圖形軌跡 繪出





            GraphicsPath gp4 = new GraphicsPath(); // GraphicsPath物件

            int Cx4 = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區的正中央
            int Cy4 = this.pictureBox1.ClientSize.Height / 3;
            // 第一個矩形的 寬高是取自視窗客戶區寬高最小者的一半
            int D4 = Math.Min(this.pictureBox1.ClientSize.Width, this.pictureBox1.ClientSize.Height) / 4;

            // 第一個矩形
            Rectangle rect1a = new Rectangle(Cx4 - D4, Cy4 - D4, 2 * D4, 2 * D4);
            gp4.AddRectangle(rect1a); // 將 矩形 加入到 GraphicsPath物件

            // 第二個矩形
            Rectangle rect2a = new Rectangle(Cx4 - D4 - 20, Cy4 - D4 - 20, 40, 40);
            gp4.AddRectangle(rect2a); // 將 矩形 加入到 GraphicsPath物件

            // 第三個矩形
            Rectangle rect3a = new Rectangle(Cx4 - D4 + 2 * D4 - 20, Cy4 - D4 - 20, 40, 40);
            gp4.AddRectangle(rect3a); // 將 矩形 加入到 GraphicsPath物件

            // 第四個矩形
            Rectangle rect4a = new Rectangle(Cx4 - D4 - 20, Cy4 - D4 + 2 * D4 - 20, 40, 40);
            gp4.AddRectangle(rect4a); // 將 矩形 加入到 GraphicsPath物件

            // 第五個矩形
            Rectangle rect5a = new Rectangle(Cx4 - D4 + 2 * D4 - 20, Cy4 - D4 + 2 * D4 - 20, 40, 40);
            gp4.AddRectangle(rect5a); // 將 矩形 加入到 GraphicsPath物件

            // 將 gp 內的形狀 繪出
            g.DrawPath(Pens.Black, gp4); // 繪出GraphicsPath物件



            GraphicsPath gp5 = new GraphicsPath(); // GraphicsPath物件

            int Cx5 = this.pictureBox1.ClientSize.Width / 2 + 50; // 視窗客戶區的正中央
            int Cy5 = this.pictureBox1.ClientSize.Height / 2 + 50;
            // 第一個矩形的 寬高是取自視窗客戶區寬高最小者的一半
            int D5 = Math.Min(this.pictureBox1.ClientSize.Width, this.pictureBox1.ClientSize.Height) / 4;

            Rectangle[] rects = new Rectangle[5];
            // 第一個矩形
            rects[0] = new Rectangle(Cx5 - D5, Cy5 - D5, 2 * D5, 2 * D5);

            // 第二個矩形
            rects[1] = new Rectangle(Cx5 - D5 - 20, Cy5 - D5 - 20, 40, 40);

            // 第三個矩形
            rects[2] = new Rectangle(Cx5 - D5 + 2 * D5 - 20, Cy5 - D5 - 20, 40, 40);

            // 第四個矩形
            rects[3] = new Rectangle(Cx5 - D5 - 20, Cy5 - D5 + 2 * D5 - 20, 40, 40);

            // 第五個矩形
            rects[4] = new Rectangle(Cx5 - D5 + 2 * D5 - 20, Cy5 - D5 + 2 * D5 - 20, 40, 40);

            gp5.AddRectangles(rects); // 將 矩形陣列 加入到 GraphicsPath物件

            // 將 gp5 內的形狀 繪出
            g.DrawPath(Pens.Red, gp5); // 繪出GraphicsPath物件


        }

        private void button8_Click(object sender, EventArgs e)
        {
            //在曲線的上下畫字
            Graphics g = pictureBox1.CreateGraphics();

            g.TextRenderingHint = System.Drawing.Text.TextRenderingHint.AntiAliasGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.High;

            // Draw some text along some paths.
            GraphicsPath path = new GraphicsPath();
            path.AddArc(new RectangleF(40, 40, 320, 220), 180, 180);
            g.DrawPath(Pens.Green, path);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, false);

            path = new GraphicsPath();
            path.AddArc(new RectangleF(40, 50, 320, 220), 0, 180);
            g.DrawPath(Pens.Red, path);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, true);
            DrawTextOnPath(g, Brushes.Blue, this.Font, "This is some text drawn along a path", path, false);
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
            PointF start_point = path.PathPoints[0];
            for (int i = 1; i < path.PointCount; i++)
            {
                PointF end_point = path.PathPoints[i];
                DrawTextOnSegment2(gr, brush, font, txt, ref start_ch,
                    ref start_point, end_point, text_above_path);
                if (start_ch >= txt.Length) break;
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
            if (last_ch < first_ch) return;
            if (last_ch >= txt.Length) last_ch = txt.Length - 1;
            string chars_that_fit = txt.Substring(first_ch, last_ch - first_ch + 1);

            // Rotate and translate to position the characters.
            GraphicsState state = gr.Save();
            if (text_above_segment)
            {
                gr.TranslateTransform(0,
                    -gr.MeasureString(chars_that_fit, font).Height,
                    MatrixOrder.Append);
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
            start_point = new PointF(
                start_point.X + dx * text_width,
                start_point.Y + dy * text_width);
        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {
            //製作非矩形視窗
            //Region的用法
            this.FormBorderStyle = FormBorderStyle.None;
            GraphicsPath gp = new GraphicsPath();
            Rectangle rect = new Rectangle(new Point(0, 0), new Size(this.Width, this.Height));
            gp.AddEllipse(rect);
            //gp.AddEllipse(60, 80, 400, 300);
            Region r = new Region(gp);
            this.Region = r;

            //this.Region = new Region(gp); //same

        }

        private void button11_Click(object sender, EventArgs e)
        {
            //畫圓角矩形
            Bitmap bitmap1 = new Bitmap(640, 480);
            Graphics g = Graphics.FromImage(bitmap1);
            g.FillRectangle(Brushes.Pink, new Rectangle(0, 0, 600, 400));
            FillRoundRectangle(g, Brushes.Plum, new Rectangle(100, 100, 100, 100), 8);
            DrawRoundRectangle(g, Pens.Yellow, new Rectangle(100, 100, 100, 100), 8);
            //bm.Save(Response.OutputStream, ImageFormat.Jpeg);
            string filename = Application.StartupPath + "\\bmp_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bitmap1.Save(filename, ImageFormat.Bmp);
            pictureBox1.Image = bitmap1;
            g.Dispose();
            //bitmap1.Dispose();
        }

        public static void DrawRoundRectangle(Graphics g, Pen pen, Rectangle rect, int cornerRadius)
        {
            using (GraphicsPath path = CreateRoundedRectanglePath(rect, cornerRadius))
            {
                g.DrawPath(pen, path);
            }
        }

        public static void FillRoundRectangle(Graphics g, Brush brush, Rectangle rect, int cornerRadius)
        {
            using (GraphicsPath path = CreateRoundedRectanglePath(rect, cornerRadius))
            {
                g.FillPath(brush, path);
            }
        }

        internal static GraphicsPath CreateRoundedRectanglePath(Rectangle rect, int cornerRadius)
        {
            GraphicsPath roundedRect = new GraphicsPath();
            roundedRect.AddArc(rect.X, rect.Y, cornerRadius * 2, cornerRadius * 2, 180, 90);
            roundedRect.AddLine(rect.X + cornerRadius, rect.Y, rect.Right - cornerRadius * 2, rect.Y);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y, cornerRadius * 2, cornerRadius * 2, 270, 90);
            roundedRect.AddLine(rect.Right, rect.Y + cornerRadius * 2, rect.Right, rect.Y + rect.Height - cornerRadius * 2);
            roundedRect.AddArc(rect.X + rect.Width - cornerRadius * 2, rect.Y + rect.Height - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 0, 90);
            roundedRect.AddLine(rect.Right - cornerRadius * 2, rect.Bottom, rect.X + cornerRadius * 2, rect.Bottom);
            roundedRect.AddArc(rect.X, rect.Bottom - cornerRadius * 2, cornerRadius * 2, cornerRadius * 2, 90, 90);
            roundedRect.AddLine(rect.X, rect.Bottom - cornerRadius * 2, rect.X, rect.Y + cornerRadius * 2);
            roundedRect.CloseFigure();
            return roundedRect;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //不規則圖形裁剪圖片

            string filename = @"C:\______test_files\picture1.jpg";
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename, false);
            int W = bitmap1.Width;
            int H = bitmap1.Height;

            GraphicsPath path = new GraphicsPath();

            Point[] p = {
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
            path.AddLines(p);

            Bitmap bitmap2 = null;
            BitmapCrop(bitmap1, path, out bitmap2);
            pictureBox1.Image = bitmap2;
        }

        /// <summary>
        /// 圖片截圖
        /// </summary>
        /// <param name="bitmap">原圖</param>
        /// <param name="path">裁剪路徑</param>
        /// <param name="outputBitmap">輸出圖</param>
        /// <returns></returns>
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

        private GraphicsPath CreateRound(Rectangle rectangle, int r)
        {
            int l = 2 * r;
            // 把圆角矩形分成八段直线、弧的组合，依次加到路径中 
            GraphicsPath gp = new GraphicsPath();
            gp.AddLine(new Point(rectangle.X + r, rectangle.Y), new Point(rectangle.Right - r, rectangle.Y));
            gp.AddArc(new Rectangle(rectangle.Right - l, rectangle.Y, l, l), 270F, 90F);
            gp.AddLine(new Point(rectangle.Right, rectangle.Y + r), new Point(rectangle.Right, rectangle.Bottom - r));
            gp.AddArc(new Rectangle(rectangle.Right - l, rectangle.Bottom - l, l, l), 0F, 90F);
            gp.AddLine(new Point(rectangle.Right - r, rectangle.Bottom), new Point(rectangle.X + r, rectangle.Bottom));
            gp.AddArc(new Rectangle(rectangle.X, rectangle.Bottom - l, l, l), 90F, 90F);
            gp.AddLine(new Point(rectangle.X, rectangle.Bottom - r), new Point(rectangle.X, rectangle.Y + r));
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
            this.Region = null;
            SetWindowRegion();
        }

        public void SetWindowRegion()
        {
            GraphicsPath FormPath;
            FormPath = new GraphicsPath();
            Rectangle rect = new Rectangle(0, 22, this.Width, this.Height - 22);//this.Left-10,this.Top-10,this.Width-10,this.Height-10);                
            FormPath = GetRoundedRectPath(rect, 30);
            this.Region = new Region(FormPath);
        }

        private GraphicsPath GetRoundedRectPath(Rectangle rect, int radius)
        {
            int diameter = radius;
            Rectangle arcRect = new Rectangle(rect.Location, new Size(diameter, diameter));
            GraphicsPath path = new GraphicsPath();
            //   左上角  
            path.AddArc(arcRect, 180, 90);
            //   右上角  
            arcRect.X = rect.Right - diameter;
            path.AddArc(arcRect, 270, 90);
            //   右下角  
            arcRect.Y = rect.Bottom - diameter;
            path.AddArc(arcRect, 0, 90);
            //   左下角  
            arcRect.X = rect.Left;
            path.AddArc(arcRect, 90, 90);
            path.CloseFigure();
            return path;
        }
    }
}

