using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            Graphics g = this.pictureBox1.CreateGraphics();
            GraphicsPath gp = new GraphicsPath();
            Pen p = new Pen(Color.Blue, 1);
            Point[] pts = { new Point(15, 30), new Point(30, 40), new Point(50, 30) };
            gp.AddArc(15, 20, 80, 50, 210, 120);
            gp.StartFigure();
            gp.AddCurve(pts);
            gp.AddString("圖形路徑", new FontFamily("標楷體"), (int)FontStyle.Underline, 50, new PointF(20, 50), new StringFormat());
            gp.AddPie(180, 20, 80, 50, 210, 120);
            g.DrawPath(p, gp);

        }

        private void button1_Click(object sender, EventArgs e)
        {

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



    }
}
