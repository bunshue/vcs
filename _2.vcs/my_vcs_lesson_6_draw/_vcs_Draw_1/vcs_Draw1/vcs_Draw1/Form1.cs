using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Drawing2D; //for GraphicsState
using System.Drawing.Text;      //for TextRenderingHint

namespace vcs_Draw1
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Font f;

        string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            this.ResizeRedraw = true;

            p = new Pen(Color.Red, 3);

            int W = 640;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            //------------------------------------------------------------  # 60個

            //畫 UAC

            pictureBox_uac.Image = UacStuff.GetUacShieldImage();
            // Add the shield to a button.
            UacStuff.AddShieldToButton(button29);
        }

        protected override void OnPaintBackground(PaintEventArgs e)
        {
            int x_st = this.ClientRectangle.X;
            int y_st = this.ClientRectangle.Y;
            int W = this.ClientRectangle.Width;
            int H = this.ClientRectangle.Height;

            e.Graphics.FillRectangle(new SolidBrush(Color.White), x_st, y_st, W, H);

            x_st = 50;
            y_st = H - 90;
            e.Graphics.DrawString("OnPaintBackground", new Font("標楷體", 30), new SolidBrush(Color.Red), x_st, y_st);
            e.Graphics.DrawRectangle(new Pen(Color.Green, 4), x_st, y_st, 370, 40);
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;
            int dd = 40;

            //button
            x_st = 1060;
            y_st = 40;
            dx = 200 + 5;
            dy = 60 + 5;

            pictureBox_uac.Location = new Point(40, y_st + dy * 12);

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

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            checkBox1.Location = new Point(x_st + dx * 2 - dd * 4, y_st + dy * 10);
            bt_eraser.Location = new Point(x_st + dx * 2 - dd * 2, y_st + dy * 10);
            bt_reset.Location = new Point(x_st + dx * 3 - dd * 3, y_st + dy * 10);
            bt_save.Location = new Point(x_st + dx * 4 - dd * 4, y_st + dy * 10);

            richTextBox1.Size = new Size(800, 280);
            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            pictureBox1.Size = new Size(640, 750);
            pictureBox1.Location = new Point(20, 20);

            pictureBox_count.Size = new Size(260, 50);
            pictureBox_count.Location = new Point(550, 990);

            panel1.Size = new Size(50, 50);
            panel1.Location = new Point(450, 990);
            panel1.BackColor = Color.Lime;

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

        private void DrawPoint(Graphics g, PointF pt, Color c_out, Color c_in, int radius)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c_out, 1);
            SolidBrush b = new SolidBrush(c_in);
            //Brush b = new Brush(c_in);

            // Draw the circle
            g.FillEllipse(b, pt.X - radius, pt.Y - radius, radius * 2, radius * 2);
            g.DrawEllipse(p, pt.X - radius, pt.Y - radius, radius * 2, radius * 2);
            //Dispose of the pen.
            p.Dispose();
        }

        // Draw a point.
        private void DrawPoint2(Graphics g, PointF pt, Brush brush, Pen pen)
        {
            const int RADIUS = 3;
            g.FillEllipse(brush, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
            g.DrawEllipse(pen, pt.X - RADIUS, pt.Y - RADIUS, 2 * RADIUS, 2 * RADIUS);
        }

        private void DrawCircle(Graphics g, PointF center, int radius, int linewidth, Color c)
        {
            // Create a new pen.
            //顏色、線寬分開寫
            //Pen p = new Pen(c);
            // Set the pen's width.
            //p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);
            richTextBox1.Text += "draw circle\n";
            // Draw the circle
            g.DrawEllipse(p, center.X - radius, center.Y - radius, radius * 2, radius * 2);
            //Dispose of the pen.
            p.Dispose();
        }

        private void FillCircle(Graphics g, PointF center, int radius, Color c)
        {
            SolidBrush sb = new SolidBrush(c);

            // Fill the circle
            g.FillEllipse(sb, new RectangleF(center.X - radius, center.Y - radius, radius * 2, radius * 2));

            //Dispose of the brush
            sb.Dispose();
        }

        private void DrawStar(Graphics g, PointF center, int radius, int linewidth, Color c)
        {
            // DrawStar

            // 顏色、線寬分開寫
            // Pen p = new Pen(c);
            // p.Width = linewidth;

            //顏色、線寬寫在一起
            Pen p = new Pen(c, linewidth);

            PointF[] pt = new PointF[6];    //一維陣列內有6個Point

            for (int i = 0; i < 6; i++)
            {
                int angle = -90 + 144 * i;
                pt[i].X = (int)(radius * Math.Cos(angle * Math.PI / 180));
                pt[i].Y = (int)(radius * Math.Sin(angle * Math.PI / 180));

                //richTextBox1.Text += "pt[" + i.ToString() + "].X " + pt[i].X.ToString() + "\t" + "pt[" + i.ToString() + "].Y " + pt[i].Y.ToString() + "\n";
                pt[i].X += center.X;
                pt[i].Y += center.Y;
            }
            g.DrawLines(new Pen(Brushes.Red, linewidth), pt);

            p.Dispose();
        }

        private void FillStar(Graphics g, PointF center, int radius, Color c)
        {
            // FillStar

            PointF[] pt1 = new PointF[5];    //一維陣列內有5個Point, 外圈
            PointF[] pt2 = new PointF[5];    //一維陣列內有5個Point, 內圈
            for (int i = 0; i < 5; i++)
            {
                int angle = -90 + 72 * i;
                pt1[i].X = (int)(radius * Math.Cos(angle * Math.PI / 180));
                pt1[i].Y = (int)(radius * Math.Sin(angle * Math.PI / 180));

                //richTextBox1.Text += "pt1[" + i.ToString() + "].X " + pt1[i].X.ToString() + "\t" + "pt1[" + i.ToString() + "].Y " + pt1[i].Y.ToString() + "\n";
                pt1[i].X += center.X;
                pt1[i].Y += center.Y;
            }

            double radius2;
            radius2 = (double)radius * Math.Sin(18 * Math.PI / 180) / Math.Sin(54 * Math.PI / 180);
            for (int i = 0; i < 5; i++)
            {
                int angle = 72 * i - 54;
                pt2[i].X = (int)(radius2 * Math.Cos(angle * Math.PI / 180));
                pt2[i].Y = (int)(radius2 * Math.Sin(angle * Math.PI / 180));

                //richTextBox1.Text += "pt2[" + i.ToString() + "].X " + pt2[i].X.ToString() + "\t" + "pt2[" + i.ToString() + "].Y " + pt2[i].Y.ToString() + "\n";
                pt2[i].X += center.X;
                pt2[i].Y += center.Y;
            }

            sb = new SolidBrush(c);

            PointF[] pt3 = new PointF[3];    //一維陣列內有3個Point
            pt3[0] = pt1[0];
            pt3[1] = pt2[1];
            pt3[2] = pt2[3];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[1];
            pt3[1] = pt2[2];
            pt3[2] = pt2[4];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[2];
            pt3[1] = pt2[3];
            pt3[2] = pt2[0];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[3];
            pt3[1] = pt2[4];
            pt3[2] = pt2[1];
            g.FillPolygon(sb, pt3);
            pt3[0] = pt1[4];
            pt3[1] = pt2[0];
            pt3[2] = pt2[2];
            g.FillPolygon(sb, pt3);
        }

        private void DrawGrid()
        {
            p = new Pen(Color.Navy, 1);
            for (int i = 0; i < 7; i++)
            {
                g.DrawLine(p, 0, i * 100, pictureBox1.ClientSize.Width - 1, i * 100);
            }
            for (int i = 0; i < 7; i++)
            {
                g.DrawLine(p, new Point(i * 100, 0), new Point(i * 100, pictureBox1.ClientSize.Height - 1));
            }
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            // 基本畫圖 0

            int W = 1100;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            p = new Pen(Color.Green, 3);
            sb = new SolidBrush(Color.Blue);
            f = new Font("Times New Roman", 14);

            Rectangle rec;
            Rectangle[] recs;

            int x_st = 20;
            int y_st = 20;
            int dx = 100;
            int dy = 80;
            int w = 80;
            int h = 60;

            //空長方形
            x_st = 20;
            y_st = 20;
            g.DrawString("DrawRectangle", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.DrawRectangle(p, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.DrawRectangle(p, rec);

            x_st += dx;
            g.DrawRectangle(new Pen(Color.Lime), new Rectangle(x_st, y_st, w, h));

            //填滿長方形
            x_st = W / 2;
            y_st = 20;
            g.DrawString("FillRectangle", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.FillRectangle(sb, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.FillRectangle(sb, rec);

            x_st += dx;
            g.FillRectangle(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));

            //空長方形多個
            x_st = 20;
            y_st = 20;
            y_st += dy;
            g.DrawString("DrawRectangles", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            recs = new Rectangle[4] {
	            new Rectangle(x_st + 0, y_st + 0, 50, 80),
	            new Rectangle(x_st + 60, y_st + 0, 80, 60),
	            new Rectangle(x_st + 60 + 90, y_st + 0, 100, 75),
	            new Rectangle(x_st + 60 + 90 + 110, y_st + 0, 50, 70)
            };
            g.DrawRectangles(p, recs);

            //填滿長方形多個
            x_st = W / 2;
            y_st = 20;
            y_st += dy;
            g.DrawString("FillRectangles", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            recs = new Rectangle[4] {
	            new Rectangle(x_st + 0, y_st + 0, 50, 80),
	            new Rectangle(x_st + 60, y_st + 0, 80, 60),
	            new Rectangle(x_st + 60 + 90, y_st + 0, 100, 75),
	            new Rectangle(x_st + 60 + 90 + 110, y_st + 0, 50, 70)
            };
            g.FillRectangles(sb, recs);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //空橢圓形
            x_st = 20;
            y_st = 20;
            y_st += dy * 2;
            g.DrawString("DrawEllipse", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.DrawEllipse(p, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.DrawEllipse(p, rec);

            x_st += dx;
            g.DrawEllipse(new Pen(Color.Lime), new Rectangle(x_st, y_st, w, h));

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //填滿橢圓形
            x_st = W / 2;
            y_st = 20;
            y_st += dy * 2;
            g.DrawString("FillEllipse", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;
            g.FillEllipse(sb, x_st, y_st, w, h);

            x_st += dx;
            rec = new Rectangle(x_st, y_st, w, h);
            g.FillEllipse(sb, rec);

            x_st += dx;
            g.FillEllipse(new SolidBrush(Color.Lime), new Rectangle(x_st, y_st, w, h));

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //空多邊形
            x_st = 20;
            y_st = 20;
            y_st += dy * 3;
            g.DrawString("DrawPolygon", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;

            Point[] points1 = new Point[3];
            points1[0] = new Point(x_st + 0, y_st + 0);
            points1[1] = new Point(x_st + 0, y_st + 50);
            points1[2] = new Point(x_st + 100, y_st + 50);
            g.DrawPolygon(p, points1);

            x_st += dx;
            Point[] points2 = { 
                new Point(x_st + 0, y_st + 0),
                new Point(x_st + 200, y_st + 20),
                new Point(x_st + 200, y_st + 60),
                new Point(x_st + 150, y_st + 20),
                new Point(x_st + 20, y_st + 60) };
            g.DrawPolygon(Pens.Red, points2);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //填滿多邊形
            x_st = W / 2;
            y_st = 20;
            y_st += dy * 3;
            g.DrawString("FillPolygon", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;

            Point[] points3 = new Point[3];
            points3[0] = new Point(x_st + 0, y_st + 0);
            points3[1] = new Point(x_st + 0, y_st + 50);
            points3[2] = new Point(x_st + 100, y_st + 50);
            g.FillPolygon(sb, points3);

            x_st += dx;
            Point[] points4 = { 
                new Point(x_st + 0, y_st + 0),
                new Point(x_st + 200, y_st + 20),
                new Point(x_st + 200, y_st + 60),
                new Point(x_st + 150, y_st + 20),
                new Point(x_st + 20, y_st + 60) };
            g.FillPolygon(new SolidBrush(Color.Red), points4);

            //空派形
            x_st = 20;
            y_st = 20;
            y_st += dy * 4;
            g.DrawString("DrawPie", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            g.DrawPie(p, x_st, y_st, w, h, 0, 30);

            x_st += dx;
            g.DrawPie(new Pen(Color.Red), new Rectangle(x_st, y_st, w, h), 180, 30);

            x_st += dx / 2;
            g.DrawPie(p, x_st, y_st, w, h, 0, -30);

            x_st += dx;
            g.DrawPie(p, x_st, y_st - 20, w, w, 40, 280);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //填滿派形
            x_st = W / 2;
            y_st = 20;
            y_st += dy * 4;
            g.DrawString("FillPie", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            g.FillPie(sb, x_st, y_st, w, h, 0, 30);

            x_st += dx;
            g.FillPie(new SolidBrush(Color.Red), new Rectangle(x_st, y_st, w, h), 180, 30);

            x_st += dx / 2;
            g.FillPie(sb, x_st, y_st, w, h, 0, -30);

            x_st += dx;
            g.FillPie(sb, x_st, y_st - 20, w, w, 40, 280);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫分佈餅圖
            x_st = W - 180;
            y_st = H - 180;
            int r = 100;
            Brush bb = new SolidBrush(Color.Navy);
            g.FillPie(bb, x_st, y_st, r, r, 0, 90);
            //畫個Pie，顏色是Pink,位置的x、y在50，大小為r*r，角度為從0度開始，畫90度

            bb = new SolidBrush(Color.Green);
            g.FillPie(bb, x_st, y_st, r, r, 90, 135);
            //畫個Pie，顏色是Green,位置大小同上，角度為接著從90度開始，畫135度

            bb = new SolidBrush(Color.Purple);
            g.FillPie(bb, x_st, y_st, r, r, 225, 135);
            //畫個Pie，顏色是Purple,位置大小同上，角度為接著從90+135=225度開始 畫135度
            //如此，這3個pie就會合成一個圓

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫直線
            x_st = 20;
            y_st = 20;
            y_st += dy * 5;
            g.DrawString("DrawLine", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            Point point1a = new Point(x_st, y_st);
            Point point2a = new Point(x_st + 100, y_st + 50);
            g.DrawLine(p, point1a, point2a);

            Point point3a = new Point(x_st, y_st + 50);
            Point point4a = new Point(x_st + 100, y_st);
            g.DrawLine(p, point3a, point4a);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫直線連線與曲線
            x_st += dx * 3 / 2;

            g.DrawString("DrawLines", f, new SolidBrush(Color.Red), new PointF(x_st, y_st));
            g.DrawString("DrawCurve", f, new SolidBrush(Color.Green), new PointF(x_st, y_st + 50));

            x_st += dx;
            // Create points that define curve.
            Point point0 = new Point(x_st + 0, y_st + 0);
            Point point1 = new Point(x_st + 50, y_st + 150);
            Point point2 = new Point(x_st + 100, y_st - 50);
            Point point3 = new Point(x_st + 150, y_st + 120);
            Point point4 = new Point(x_st + 200, y_st - 20);
            Point point5 = new Point(x_st + 250, y_st + 150);
            Point point6 = new Point(x_st + 300, y_st - 20);
            Point point7 = new Point(x_st + 350, y_st + 50);
            Point point8 = new Point(x_st + 400, y_st + 0);
            Point point9 = new Point(x_st + 450, y_st + 150);
            Point point10 = new Point(x_st + 500, y_st + 0);
            Point point11 = new Point(x_st + 550, y_st + 150);
            Point point12 = new Point(x_st + 600, y_st + 50);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12 };

            Pen redPen = new Pen(Color.Red, 3); // Create pens.
            g.DrawLines(redPen, curvePoints);   //畫直線

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.
            g.DrawCurve(greenPen, curvePoints); //畫曲線

            x_st = 670;
            y_st = 530;
            g.DrawString("Sine", f, new SolidBrush(Color.Red), new PointF(x_st, y_st));

            /*
            Point[] pts = new Point[90];
            double yy;
            int i;
            for (i = 0; i < 90; i++)
            {
                yy = Math.Sin(Math.PI * i * 4 / 180) * 50;
                pts[i].X = x_st + (int)i * 1;
                pts[i].Y = y_st + (int)yy;
                //richTextBox1.Text += "x= " + pts[i].X.ToString() + " y = " + pts[i].Y.ToString() + "\n";
            }
            p = new Pen(Color.Navy, 3);
            g.DrawCurve(p, pts);
            */

            //畫三角函數
            int omega = 60;  //angular frequency
            Point[] pts = new Point[360 / omega + 1];    //一維Point陣列內有100個Point
            int i;
            int amplitude = 50;
            for (i = 0; i <= 360 / omega; i++)
            {
                pts[i].X = x_st + i * omega / 3;
                pts[i].Y = y_st - (int)(amplitude * Math.Sin(i * omega * Math.PI / 180));   //Y反相
                g.FillEllipse(Brushes.Black, pts[i].X - 3, pts[i].Y - 3, 6, 6); //畫點
            }
            g.DrawLines(new Pen(Brushes.Red, 1), pts);      //畫直線, 直接把Point陣列畫出來
            g.DrawCurve(new Pen(Brushes.Blue, 1), pts);     //畫曲線, 直接把Point陣列畫出來

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //各種連線
            x_st = 50;
            y_st = 20;
            y_st += dy * 6;
            w = 100;
            h = 100;

            Point[] pa = { new Point(x_st, y_st), new Point(x_st, y_st + h), new Point(x_st + w, y_st + h), new Point(x_st + w, y_st), new Point(x_st + w * 2, y_st), new Point(x_st + w * 2, y_st + h), new Point(x_st + w * 3, y_st + h / 2) };

            p = new Pen(Color.Red, 5);
            g.DrawLines(p, pa);  //陣列的連線

            p = new Pen(Color.LightCoral, 1);
            for (float k = 0; k < 1.5; k += 0.4F)
            {
                g.DrawCurve(p, pa, k);  //DrawCurve 加上 屈度
            }

            p = new Pen(Color.Red, 1);
            g.DrawCurve(p, pa);     ////DrawCurve 預設屈度

            p = new Pen(Color.Yellow, 1);
            g.DrawClosedCurve(p, pa);       //頭尾相連 加上 屈度

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫弧線
            x_st = 20;
            y_st = 20;
            y_st += dy * 8;
            g.DrawString("DrawArc", f, sb, new PointF(x_st, y_st));

            y_st -= dy / 2;

            x_st += dx * 1;
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, x_st, y_st, 150, 100);
            g.DrawArc(new Pen(Color.Blue, 10), new Rectangle(x_st, y_st, 150, 100), 0, 135);

            x_st += dx * 2;
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, x_st, y_st, 150, 100);
            p = new Pen(Color.Blue, 10);
            p.EndCap = LineCap.ArrowAnchor;
            g.DrawArc(p, x_st, y_st, 150, 100, 0, 135);

            x_st += dx * 2;
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, x_st, y_st, 150, 100);
            p = new Pen(Color.Blue, 10);
            p.EndCap = LineCap.ArrowAnchor;
            g.DrawArc(p, x_st, y_st, 150, 100, 0, -135);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫字
            // Create string to draw.
            String drawString = "各種畫圖範例";

            Font drawFont = new Font("標楷體", 36, FontStyle.Italic | FontStyle.Underline | FontStyle.Strikeout);
            SolidBrush drawBrush = new SolidBrush(Color.Navy);

            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(W - 400, H - 70);

            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);

            drawPoint = new PointF(W - 400, H - 70 - 50);
            g.DrawString(drawString, new Font("標楷體", 24, FontStyle.Bold | FontStyle.Italic), new SolidBrush(Color.Navy), drawPoint);
            //畫字就比較簡單了，會產生一個標楷體，24的大小，粗加斜，顏色為bb，位置在drawPoint

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //貼圖
            g.DrawString("貼圖", new Font("標楷體", 20), new SolidBrush(Color.Blue), new PointF(W - 80, 30));
            Bitmap bmp = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__pic\_ball\red-ball-icon.png");
            for (y_st = 60; y_st < H; y_st += 80)
            {
                g.DrawImage(bmp, W - 75, y_st);
            }

            // 剛好等寬畫滿邊框
            p = new Pen(Color.Green, 10);
            g.DrawRectangle(p, 0 + p.Width / 2, 0 + p.Width / 2, bitmap1.Width - p.Width, bitmap1.Height - p.Width);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //基本畫圖 1

            int W = 1100;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            sb = new SolidBrush(Color.Blue);
            p = new Pen(Color.Green, 3);
            f = new Font("Times New Roman", 14);

            //Rectangle rec;
            //Rectangle[] recs;

            int x_st = 20;
            int y_st = 20;
            int dx = 100;
            int dy = 80;
            int w = 80;
            int h = 60;

            //貝茲線
            x_st = 20;
            y_st = 20;
            g.DrawString("DrawBezierAAAA", f, sb, new PointF(x_st, y_st));

            x_st += dx;
            x_st += dx / 2;

            Point[] points = new Point[4];
            points[0] = new Point(x_st + 0, y_st + 0);
            points[1] = new Point(x_st + 0, y_st + h);
            points[2] = new Point(x_st + w * 2, y_st + h);
            points[3] = new Point(x_st + w * 2, y_st + 0);

            g.DrawBezier(new Pen(Color.Black), points[0], points[1], points[2], points[3]);
            g.DrawLines(Pens.Red, points);

            for (int i = 0; i < 4; i++)
            {
                points[i] = new Point(points[i].X + dx * 2, points[i].Y);
            }
            g.DrawBeziers(new Pen(Color.Black), points);
            g.DrawLines(Pens.Red, points);

            //畫貝茲線
            p = new Pen(Color.Red, 5);
            x_st = 550;
            y_st = 0;
            float startX = x_st + 50.0F;
            float startY = y_st + 80.0F;
            float controlX1 = x_st + 150.0F;
            float controlY1 = y_st + 20.0F;
            float controlX2 = x_st + 230.0F;
            float controlY2 = y_st + 50.0F;
            float endX = x_st + 190.0F;
            float endY = y_st + 80.0F;
            g.DrawBezier(p, startX, startY, controlX1, controlY1, controlX2, controlY2, endX, endY);
            //4個Point點分別表示起始點、第一個控制點、第二個控制點和結束點。

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫多個Rectangles
            x_st = 20;
            y_st = 20;
            y_st += dy * 2;
            g.DrawString("畫多個Rectangles", f, sb, new PointF(x_st, y_st - 25));

            Rectangle[] R = new Rectangle[15];
            for (int i = 0; i < R.Length; i++)
            {
                //R[i] = new Rectangle(0 + 30 * i, 0 + 30 * i);
                R[i] = new Rectangle(x_st + i * 10, y_st + i * 5, i * 30, i * 15);
            }
            g.DrawRectangles(new Pen(Brushes.Red, 2), R);

            //一次畫一群長方形
            int hwidth = 50;
            int x_center = 150;
            int y_center = 400;
            //Pen pen = new Pen(Pens.Red);
            Pen pen = new Pen(Color.Blue, 1);
            Rectangle[] R1 = new Rectangle[25];
            for (int i = 0; i <= 24; i++)
            {
                R1[i] = new Rectangle(x_center - hwidth, y_center - hwidth, 2 * hwidth, 2 * hwidth);
                y_center += 4;
                hwidth += 2;
            }
            g.DrawRectangles(pen, R1);

            //pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button2_Click(object sender, EventArgs e)
        {
            int W = 1100;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            //畫點圓形星形

            Font f = new Font("標楷體", 16);
            SolidBrush sb = new SolidBrush(Color.Blue);
            Point pt = new Point();
            int xx = 0;
            int yy = 0;

            for (int size = 1; size <= 10; size++)
            {
                xx = 40;
                yy = 42 * size;
                pt = new Point(xx, yy);
                g.DrawString(size.ToString(), f, sb, pt);

                xx = 80;
                pt = new Point(xx, yy);
                DrawPoint(g, pt, Color.Red, Color.Pink, 10);

                xx = 120;
                yy = 42 * size;
                pt = new Point(xx, yy);
                g.DrawString(size.ToString(), f, sb, pt);

                xx = 160;
                pt = new Point(xx, yy);
                DrawPoint2(g, pt, Brushes.LightBlue, Pens.Blue);

                xx = 200;
                pt = new Point(xx, yy);
                DrawPoint2(g, pt, Brushes.HotPink, Pens.Red);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "畫一些空心圓\n";

            int radius = 60;
            int linewidth = 10;
            pt = new Point();

            pt = new Point(300, 60);
            DrawCircle(g, pt, radius, linewidth, Color.Red);

            pt = new Point(380, 120);
            DrawCircle(g, pt, radius, linewidth, Color.Green);

            pt = new Point(460, 180);
            DrawCircle(g, pt, radius, linewidth, Color.Blue);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "畫一些實心圓\n";

            radius = 60;
            pt = new Point();

            pt = new Point(300, 60 + 160);
            FillCircle(g, pt, radius, Color.Red);

            pt = new Point(380, 120 + 160);
            FillCircle(g, pt, radius, Color.Green);

            pt = new Point(460, 180 + 160);
            FillCircle(g, pt, radius, Color.Blue);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "空心星形\n";

            radius = 80;
            linewidth = 5;
            Point center = new Point(300, 400);
            DrawStar(g, center, radius, linewidth, Color.Red);

            richTextBox1.Text += "實心星形\n";

            radius = 80;
            center = new Point(500, 400);
            FillStar(g, center, radius, Color.Red);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫多邊形與五角星星

            Point[] pts = new Point[5];  // 五個點
            W = 200;
            H = 200;
            int Cx = W / 2 + 450;  // 中心點
            int Cy = H / 2;
            int D = (int)(Math.Min(W, H) / 2) - 10; // 半徑
            double Theta = -Math.PI / 2.0; // 角度

            int i;
            for (i = 0; i < 5; i++)
            {
                pts[i].X = Cx + (int)(D * Math.Cos(Theta));
                pts[i].Y = Cy + (int)(D * Math.Sin(Theta));
                Theta += Math.PI * 2.0 / 5.0;  // 五邊形
                //Theta += 2 * Math.PI * 2.0 / 5.0; // 五角星星
            }
            g.DrawPolygon(Pens.Black, pts);  // 繪出多邊形

            for (i = 0; i < 5; i++)
            {
                pts[i].X = Cx + (int)(D * Math.Cos(Theta));
                pts[i].Y = Cy + (int)(D * Math.Sin(Theta));
                //Theta += Math.PI * 2.0 / 5.0;  // 五邊形
                Theta += 2 * Math.PI * 2.0 / 5.0; // 五角星星
            }
            g.DrawPolygon(Pens.Red, pts);  // 繪出多邊形

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //畫笑臉
            int x_st = 530;
            int y_st = 220;
            DrawSmileImage(g, x_st, y_st);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //寫字

            f = new Font("Brush Script MT", 24, FontStyle.Italic);
            Brush b = new SolidBrush(Color.White);
            Brush bb = new SolidBrush(Color.Red);
            string ct = "輸出文字";

            x_st = 530 + 100;
            y_st = 220;

            g.DrawString(ct, f, b, x_st, y_st);
            g.DrawString(ct, f, bb, x_st - 1, y_st - 1);
            g.DrawString(ct, f, bb, x_st - 1, y_st + 1);
            g.DrawString(ct, f, bb, x_st + 1, y_st - 1);
            g.DrawString(ct, f, bb, x_st + 1, y_st + 1);
            g.DrawString(ct, f, b, x_st, y_st);


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //半透明筆刷

            //　寫文字的筆刷，透明度為100,藍色
            b = new SolidBrush(Color.FromArgb(100, Color.Blue));

            x_st = 20;
            y_st = 480;

            for (i = 0; i < 10; i += 2)
            {
                g.DrawString("群曜醫電", new Font("標楷體", 80), b, x_st + i, y_st + i);
            }
            //重疊部分 筆色加深

            pictureBox1.Image = bitmap1;
        }

        private void DrawSmileImage(Graphics g, int x_st, int y_st)
        {
            Rectangle rect;

            rect = new Rectangle(x_st + 10, y_st + 10, 80, 80);
            g.FillEllipse(Brushes.LightGreen, rect);
            g.DrawEllipse(Pens.Green, rect);

            rect = new Rectangle(x_st + 40, y_st + 40, 20, 30);
            g.FillEllipse(Brushes.LightBlue, rect);
            g.DrawEllipse(Pens.Blue, rect);

            rect = new Rectangle(x_st + 25, y_st + 30, 50, 50);
            g.DrawArc(Pens.Red, rect, 20, 140);

            rect = new Rectangle(x_st + 25, y_st + 25, 15, 20);
            g.FillEllipse(Brushes.White, rect);
            g.DrawEllipse(Pens.Black, rect);
            rect = new Rectangle(x_st + 30, y_st + 30, 10, 10);
            g.FillEllipse(Brushes.Black, rect);

            rect = new Rectangle(x_st + 60, y_st + 25, 15, 20);
            g.FillEllipse(Brushes.White, rect);
            g.DrawEllipse(Pens.Black, rect);
            rect = new Rectangle(x_st + 65, y_st + 30, 10, 10);
            g.FillEllipse(Brushes.Black, rect);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //箭頭 虛線 LineCap

            //自定義直線箭頭大小
            Bitmap bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);

            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            AdjustableArrowCap lineCap = new AdjustableArrowCap(6, 6, true);
            Pen RedPen = new Pen(Color.Red, 2);
            RedPen.CustomEndCap = lineCap;

            g.DrawLine(RedPen, 100, 100, 300, 300);

            //畫虛線
            Control P = (Control)sender;
            Pen pen = new Pen(Color.FromArgb(255, 0, 0), 5);
            pen.DashStyle = DashStyle.Custom;//虛線的樣式
            pen.DashPattern = new float[] { 2, 2 };//設置虛線中實點和空白區域之間的間隔
            //g.DrawLine(pen, 0, 0, 0, P.Height - 1);
            g.DrawRectangle(pen, 50, 50, 300, 300);

            //#畫虛線
            Pen p = new Pen(Color.Red, 5);
            p.DashStyle = DashStyle.Custom;//虛線的樣式
            p.DashPattern = new float[] { 2, 2 };//設置虛線中實點和空白區域之間的間隔
            g.DrawLine(p, 0, 0, this.pictureBox1.Width - 1, this.pictureBox1.Height - 1);

            //虛線樣式
            Pen dash_pen = new Pen(Color.Red);
            dash_pen.DashStyle = DashStyle.Custom;
            dash_pen.DashPattern = new float[] { 4, 4 };
            g.DrawLine(dash_pen, 100, 300, 300, 100);

            //畫箭頭
            Pen myPen2 = new Pen(Color.Blue, 20);
            myPen2.EndCap = LineCap.ArrowAnchor;
            g.DrawLine(myPen2, 20, 400, 300, 400); // 繪製箭形直線

            /*
            PenStyle = new Pen(foreColor);
            PenStyle.Width = (int)numericUpDown1.Value;
            PenStyle.StartCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            PenStyle.Color = foreColor;

            //PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Bevel;
            PenStyle.LineJoin = System.Drawing.Drawing2D.LineJoin.Round;
            */

            //繪製虛線，可設定Pen的DashStyle屬性為Dash,Dot,DashDot或者DashDotDot等
            //改變直線端點的形狀，可以設定StartCap和EndCap屬性

            //blackPen.StartCap=LineCap.ArrowAnchor;

            //箭頭的畫法

            //Pen p = new Pen(Color.Red, 0);
            p.EndCap = LineCap.ArrowAnchor;

            pictureBox1.Image = bitmap1;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //透明色測試
            richTextBox1.Text += "R = " + Color.Transparent.R.ToString() + "\n";
            richTextBox1.Text += "G = " + Color.Transparent.G.ToString() + "\n";
            richTextBox1.Text += "B = " + Color.Transparent.B.ToString() + "\n";
            richTextBox1.Text += "A = " + Color.Transparent.A.ToString() + "\n";
            richTextBox1.Text += "A2 = " + Color.Red.A.ToString() + "\n";

            Bitmap bitmap1 = (Bitmap)Image.FromFile(filename);	//Image.FromFile出來的是Image格式
            g = Graphics.FromImage(bitmap1);

            //清空畫布並用透明色填充
            //g.Clear(Color.Transparent);  // 填上透明色

            Color c1 = Color.FromArgb(255, 255, 0, 0);
            SolidBrush sb1 = new SolidBrush(c1);
            g.FillRectangle(sb1, 50, 50, 100, 100);

            Color c2 = Color.FromArgb(255, 0, 255, 0);
            SolidBrush sb2 = new SolidBrush(c2);
            g.FillRectangle(sb2, 100, 50, 100, 100);

            Color c3 = Color.FromArgb(255, 255, 0, 0);
            SolidBrush sb3 = new SolidBrush(c3);
            g.FillRectangle(sb3, 50, 200, 100, 100);

            Color c4 = Color.FromArgb(128, 0, 255, 0);
            SolidBrush sb4 = new SolidBrush(c4);
            g.FillRectangle(sb4, 100, 200, 100, 100);

            //g.FillRectangle(Brushes.Blue, 00, 320, 600, 50);
            //g.FillRectangle(Brushes.Blue, 00, 420, 600, 50);
            /*
            int i;
            int w = 40;
            for (i = 0; i < 13; i++)
            {
            Color c5 = Color.FromArgb(255, 20 * i, 0, 0);
            SolidBrush sb5 = new SolidBrush(c5);
            g.FillRectangle(sb5, 50 + w * i, 300, w, 100);

            }
            for (i = 0; i < 13; i++)
            {
            Color c5 = Color.FromArgb(20 * i, 255, 0, 0);
            SolidBrush sb5 = new SolidBrush(c5);
            g.FillRectangle(sb5, 50 + w * i, 400, w, 100);

            }
            */

            Color c6 = Color.FromArgb(200, 255, 255, 255);
            SolidBrush sb5 = new SolidBrush(c6);
            g.FillRectangle(sb5, 300, 100, 100, 100);

            //g.DrawString("格子裏", new Font("黑體", 20), new SolidBrush(c6), 200, 100);
            g.DrawString("格子裏", new Font("黑體", 20), new SolidBrush(Color.Black), 200, 100);

            g.DrawRectangle(Pens.Red, 100, 100, 100, 100);

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button5_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(600, 500);

            int i;
            int xx;
            int yy;
            int W = 600;
            int H = 500;
            byte[,] rgb = new byte[30, 3];

            for (i = 0; i < 30; i++)
            {
                int rrr;
                int ggg;
                int bbb;

                rrr = (i % 27) / 9;
                ggg = ((i % 27) % 9) / 3;
                bbb = (i % 27) % 3;

                if (rrr == 0)
                    rrr = 0;
                else
                    rrr = (byte)(128 * rrr - 1);
                if (ggg == 0)
                    ggg = 0;
                else
                    ggg = (byte)(128 * ggg - 1);
                if (bbb == 0)
                    bbb = 0;
                else
                    bbb = (byte)(128 * bbb - 1);

                if (rrr > 255)
                    rrr = 255;
                if (ggg > 255)
                    ggg = 255;
                if (bbb > 255)
                    bbb = 255;

                rgb[i, 0] = (byte)rrr;
                rgb[i, 1] = (byte)ggg;
                rgb[i, 2] = (byte)bbb;
            }
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += rgb[i, 0].ToString("X2") + " " + rgb[i, 1].ToString("X2") + " " + rgb[i, 2].ToString("X2");
                if ((i % 4) == 3)
                {
                    richTextBox1.Text += "\n";
                }
                else if ((i % 2) == 1)
                {
                    richTextBox1.Text += "   ";
                }
                else
                    richTextBox1.Text += "  ";
            }
            richTextBox1.Text += "\n";
            for (i = 0; i < 30; i++)
            {
                richTextBox1.Text += (((rgb[i, 0] + 1) / 128) << 8 | ((rgb[i, 1] + 1) / 128) << 4 | ((rgb[i, 2] + 1) / 128)).ToString("X3");
                if ((i % 6) == 5)
                {
                    richTextBox1.Text += "\n";
                }
                else
                    richTextBox1.Text += "  ";
            }
            richTextBox1.Text += "\n";
            pictureBox1.Size = new Size(W, H);
            bitmap1 = new Bitmap(W, H);

            byte aa = 255;
            byte rr = 0;
            byte gg = 0;
            byte bb = 0;
            for (yy = 0; yy < H; yy++)
            {
                for (xx = 0; xx < W; xx++)
                {
                    /*
                    if ((xx % 100) == 0)
                    {
                        if ((yy % 100) == 0)
                        {
                            int rrr = random.Next(3);
                            int ggg = random.Next(3);
                            int bbb = random.Next(3);

                            if (rrr == 0)
                                rr = 0;
                            else
                                rr = (byte)(128 * rrr - 1);

                            if (ggg == 0)
                                ggg = 0;
                            else
                                gg = (byte)(128 * ggg - 1);

                            if (bbb == 0)
                                bb = 0;
                            else
                                bb = (byte)(128 * bbb - 1);

                            richTextBox1.Text += "rrr = " + rrr.ToString() + " ggg = " + ggg.ToString() + " bbb = " + bbb.ToString() + "\t";
                            richTextBox1.Text += "xx = " + xx.ToString() + " yy = " + yy.ToString() + " rr = " + rr.ToString() + " gg = " + gg.ToString() + " bb = " + bb.ToString() + "\n";
                        
                        }
                    }
                    */

                    //Color p = Color.FromName("SlateBlue");
                    /*
                    Color p ;
                    p.A = (byte)(xx % 255);
                    p.R = (byte)(xx % 127 + 127);
                    p.G = (byte)(xx % 127);
                    p.B = (byte)(xx % 63);
                    */

                    //獲取像素的ＲＧＢ顏色值
                    //srcColor = srcBitmap.GetPixel(x, y);
                    //byte temp = (byte)(srcColor.R * .299 + srcColor.G * .587 + srcColor.B * .114);

                    //byte temp = (byte)((byte)(xx % 255) + (byte)(xx % 127 + 127) + (byte)(xx % 63));

                    //設置像素的ＲＧＢ顏色值
                    rr = (byte)rgb[xx / 100 + (yy / 100) * 6, 0];
                    gg = (byte)rgb[xx / 100 + (yy / 100) * 6, 1];
                    bb = (byte)rgb[xx / 100 + (yy / 100) * 6, 2];
                    bitmap1.SetPixel(xx, yy, Color.FromArgb(aa, rr, gg, bb));
                }
            }
            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button6_Click(object sender, EventArgs e)
        {
            //MeasureString

            Bitmap bitmap1 = new Bitmap(640, 480);

            Graphics g = Graphics.FromImage(bitmap1);//用指定的Bitmap實例化Graphics

            Font f = new Font("標楷體", 30);

            pictureBox1.Image = bitmap1;

            string text = "標楷體";
            SizeF size = g.MeasureString(text, f);  // 對文字進行測量
            g.DrawString(text, f, Brushes.Blue, 100, 100);
            g.DrawRectangle(Pens.Red, 100, 100, size.Width, size.Height);

            //------------------------------------------------------------  # 60個

            //表單底部畫字 ST
            // Transform. 縮放+旋轉+平移
            g.ScaleTransform(1.5f, 1.5f, MatrixOrder.Append);
            g.RotateTransform(25, MatrixOrder.Append);
            g.TranslateTransform(80, 30, MatrixOrder.Append);

            int x_st = 160;
            int y_st = 0;

            // See how big the text will be when drawn.
            string the_text = "群曜醫電\n股份有限公司";
            SizeF text_size = g.MeasureString(the_text, f);

            g.SmoothingMode = SmoothingMode.AntiAlias;

            g.DrawRectangle(new Pen(Color.Red, 3), x_st, y_st, text_size.Width, text_size.Height);

            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            g.DrawString(the_text, f, Brushes.Brown, x_st, y_st);

            //表單底部畫字 SP
        }

        //------------------------------------------------------------  # 60個

        private void button7_Click(object sender, EventArgs e)
        {
            //透明的畫筆與塗刷

            //透明的畫筆與塗刷

            //半透明畫筆 alpha = 64
            Pen p = new Pen(Color.FromArgb(64, 0, 255, 0), 40); // 透明的畫筆

            //半透明筆刷 alpha = 64
            SolidBrush sb = new SolidBrush(Color.FromArgb(64, 0, 0, 255)); // 透明的塗刷

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            Image image1 = Image.FromFile(filename);

            Rectangle rect = new Rectangle(0, 0, image1.Width, image1.Height);
            g.Clear(Color.Pink);
            g.DrawImage(image1, rect); // 呈現原圖
            g.DrawLine(p, 0, 100, image1.Width, 100); // 畫出透明的直線
            int Cx = this.pictureBox1.ClientSize.Width / 2; // 視窗客戶區 正中心
            int Cy = this.pictureBox1.ClientSize.Height / 2;
            g.FillEllipse(sb, Cx - 100, Cy - 100, 200, 200); // 繪畫出透明的圓形

            pictureBox1.Image = bitmap1;

        }

        //------------------------------------------------------------  # 60個

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button9_Click(object sender, EventArgs e)
        {
            //畫格線
            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            draw_grid(g);
            pictureBox1.Image = bitmap1;

            //------------------------------------------------------------  # 60個

            PaintImage(g);

            //------------------------------------------------------------  # 60個

            //多點之間的線段
            Pen pen = new Pen(Color.Blue, 2);

            //定義一個陣列有三個點
            //分別為(10,10)、(20,20)、(30,30)
            Point[] points =
            {
                new Point(100, 100),
                new Point(200, 50),
                new Point(300, 200)
            };
            g.DrawLines(pen, points);

            //------------------------------------------------------------  # 60個

            //用GDI+畫圖

            //Graphics g = this.pictureBox1.CreateGraphics();
            g.FillRectangle(Brushes.White, this.ClientRectangle);
            for (int i = 1; i <= 7; ++i)
            {
                //在窗體上面畫出橙色的矩形
                Rectangle r = new Rectangle(i * 40 - 15, 0, 15, this.ClientRectangle.Height);
                g.FillRectangle(Brushes.Orange, r);
            }
            //在內存中創建一個Bitmap並設置CompositingMode
            Bitmap bmp = new Bitmap(260, 260, PixelFormat.Format32bppArgb);
            Graphics gBmp = Graphics.FromImage(bmp);
            gBmp.CompositingMode = CompositingMode.SourceCopy;

            // 創建一個帶有Alpha的紅色區域
            // 並將其畫在內存的位圖裏面
            SolidBrush sb = new SolidBrush(Color.FromArgb(0x60, 0xff, 0, 0));
            gBmp.FillEllipse(sb, 70, 70, 160, 160);
            // 創建一個帶有Alpha的綠色區域
            Color green = Color.FromArgb(0x40, 0, 0xff, 0);
            Brush greenBrush = new SolidBrush(green);
            gBmp.FillRectangle(greenBrush, 10, 10, 140, 140);

            //在窗體上面畫出位圖 now draw the bitmap on our window
            g.DrawImage(bmp, 20, 20, bmp.Width, bmp.Height);

            // 清理資源
            bmp.Dispose();
            gBmp.Dispose();
            sb.Dispose();
            greenBrush.Dispose();
        }

        private void PaintImage(Graphics g)
        {
            //绘图
            GraphicsPath path = new GraphicsPath(
                new Point[]
                {
                    new Point(100,60),new Point(350,200),new Point(105,225),new Point(190,ClientRectangle.Bottom),
                    new Point(50,ClientRectangle.Bottom),new Point(50,180)
                },
                new byte[]
                {
                    (byte)PathPointType.Start,
                    (byte)PathPointType.Bezier,
                    (byte)PathPointType.Bezier,
                    (byte)PathPointType.Bezier,
                    (byte)PathPointType.Line,
                    (byte)PathPointType.Line
                }
                );
            PathGradientBrush pgb = new PathGradientBrush(path);

            pgb.SurroundColors = new Color[]
            {
                Color.Green, Color.Yellow, Color.Red, Color.Blue, Color.Orange, Color.LightBlue
            };
            g.FillPath(pgb, path);
            g.DrawBeziers(
                new Pen(new SolidBrush(Color.Green), 2),
                new Point[]
                {
                    new Point(220, 100),
                    new Point(250, 180),
                    new Point(300, 70),
                    new Point(350, 150)
                }
                );
            g.DrawArc(new Pen(new SolidBrush(Color.Blue), 5), new Rectangle(new Point(250, 170), new Size(60, 60)), 0, 235);
        }

        //------------------------------------------------------------  # 60個

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "反鋸齒功能\n";

            richTextBox1.Text += "開啟一個 800 X 600 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = 800;
            pictureBox1.Height = 600;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            Font f = new Font("標楷體", 20);
            SolidBrush sb = new SolidBrush(Color.Purple);

            Pen p = new Pen(Color.Red, 10);

            Point p1 = new Point(10, 100);
            Point p2 = new Point(590, 160);
            g.DrawLine(p, p1, p2);
            g.DrawString("反鋸齒功能\t關閉", f, sb, new PointF(170, 70));

            g.SmoothingMode = SmoothingMode.AntiAlias;  //反鋸齒功能

            Point p3 = new Point(10, 100 + 100);
            Point p4 = new Point(590, 100 + 160);
            g.DrawLine(p, p3, p4);
            g.DrawString("反鋸齒功能\t打開", f, sb, new PointF(170, 170));

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "有 無 Smoothing 比較\n";
            f = new Font("Times New Roman", 16);
            // Draw without smoothing.
            int x = 30, y = 240;
            g.TextRenderingHint = TextRenderingHint.SingleBitPerPixelGridFit;
            g.DrawString("無 Smoothing", f, Brushes.Blue, x, y);
            y += 50;
            g.DrawImage(Properties.Resources.Smiley100x100, x, y, 50, 50);
            y += 100;
            g.DrawEllipse(Pens.Red, x, y, 100, 50);

            // Draw with smoothing.
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            g.InterpolationMode = InterpolationMode.High;

            x = 180;
            y = 240;
            g.DrawString("有 Smoothing", f, Brushes.Blue, x, y);
            y += 50;
            g.DrawImage(Properties.Resources.Smiley100x100, x, y, 50, 50);
            y += 100;
            g.DrawEllipse(Pens.Red, x, y, 100, 50);

            //畫示意圖
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_material\AntiAlias.jpg";
            //讀檔 至 Image 影像
            Image img = Image.FromFile(filename); // 產生一個Image物件
            //畫出來
            g.DrawImage(img, 300, 380, img.Width / 2, img.Height / 2);

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button11_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";
            pictureBox1.Size = new Size(W, H);

            SolidBrush sb = new SolidBrush(Color.Purple);
            Font f = new Font("標楷體", 30);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            //g.DrawRectangle(p, 0, 0, bitmap1.Width - 1, bitmap1.Height - 1);
            //g.DrawRectangle(p, 100, 100, bitmap1.Width - 1 - 200, bitmap1.Height - 1 - 200);

            p = new Pen(Color.Purple, 5);

            /*
            g.DrawLine(p, 0, bitmap1.Height / 2, bitmap1.Width - 1, bitmap1.Height / 2);
            g.DrawLine(p, bitmap1.Width / 2, 0, bitmap1.Width / 2, bitmap1.Height - 1);
            g.DrawString("Sugar", f, sb, new PointF(bitmap1.Width - 75, bitmap1.Height / 2 - 35));
            g.DrawString("Sugar", f, sb, new PointF(bitmap1.Width - 75, bitmap1.Height / 1 - 35));
            */

            g.DrawString("在圖上寫字", f, sb, new PointF(300, 30));

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //小圖貼到大圖上

            Bitmap bitmap2 = new Bitmap(@"D:\_git\vcs\_1.data\______test_files1\__RW\_png\vcs_ReadWrite_PNG.png");
            //將小圖貼到大圖上
            g.DrawImage(bitmap2, 5, 5);

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button12_Click(object sender, EventArgs e)
        {
            //繪圖圖形的Contains功能
            Graphics g = this.pictureBox1.CreateGraphics();
            g.DrawRectangle(Pens.Red, 100, 100, 150, 150);
            Rectangle rec = new Rectangle(100, 100, 150, 150);
            Point pt1 = new Point(180, 180);
            Point pt2 = new Point(280, 280);
            g.FillEllipse(Brushes.Green, pt1.X, pt1.Y, 20, 20);
            g.FillEllipse(Brushes.Red, pt2.X, pt2.Y, 20, 20);

            if (rec.Contains(pt1))
            {
                richTextBox1.Text += "pt1 在 rec 之內\n";
            }
            else
            {
                richTextBox1.Text += "pt1 在 rec 之外\n";
            }

            if (rec.Contains(pt2))
            {
                richTextBox1.Text += "pt2 在 rec 之內\n";
            }
            else
            {
                richTextBox1.Text += "pt2 在 rec 之外\n";
            }
        }

        //------------------------------------------------------------  # 60個

        private void button13_Click(object sender, EventArgs e)
        {
            //圓形和矩形
            List<Rectangle> Circles = new List<Rectangle>();

            Circles.Clear();

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            for (int i = 20; i < 250; i += 20)
            {
                int x_st = W / 2;
                int y_st = H / 2;
                int r = i;
                Rectangle rect = new Rectangle(x_st - r / 2, y_st - r / 2, r, r);
                Circles.Add(rect);
            }

            richTextBox1.Text += Circles.Count.ToString() + "\n";

            foreach (Rectangle rect in Circles)
            {
                richTextBox1.Text += rect.ToString() + "\n";
            }

            Graphics g = this.pictureBox1.CreateGraphics();
            g.SmoothingMode = SmoothingMode.AntiAlias;

            foreach (Rectangle rect in Circles)
            {
                g.DrawEllipse(Pens.Blue, rect);
                g.DrawRectangle(Pens.Red, rect);
            }
        }

        //------------------------------------------------------------  # 60個

        private void button14_Click(object sender, EventArgs e)
        {
            //星級饗宴創意台菜

            int W = 1100;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            Color c1 = Color.FromArgb(255, 1, 85, 69);
            g.Clear(c1);

            Pen p = new Pen(Color.FromArgb(255, 227, 194, 149), 7);

            int dd = 180 * 2 / 3;
            //for (int y = (int)(120 * 1.732 * 1 / 4); y <= H; y += (int)(120 * 1.732 * 2 / 3))
            for (int y = (int)(20 * 1.732) + 20; y <= H; y += (int)(60 * 1.732))
            {
                g.DrawLine(p, 0, y, W, y);
            }

            for (int x = -dd * 5; x <= W + dd * 5; x += dd)
            {
                Point px1 = new Point(x, 0);
                Point px2 = new Point(x + (int)(H / 1.732), H);
                g.DrawLine(p, px1, px2);

                px2 = new Point(x - (int)(H / 1.732), H);
                g.DrawLine(p, px1, px2);
            }
        }

        //------------------------------------------------------------  # 60個

        private void button15_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\step2.png";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap2;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            pictureBox1.Size = new Size(W, H);
            pictureBox1.Image = bitmap1;

            SolidBrush sb = new SolidBrush(Color.Blue);
            Font f = new Font("標楷體", 16);
            sb = new SolidBrush(Color.Red);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            //g.FillRectangle(sb, 75, 75, 200, 75);

            //g.DrawString("內視鏡時效已過", f, sb, new PointF(70.0F, 110.0F));
            //g.DrawString("請更換", f, sb, new PointF(240.0F, 200.0F));

            //g.DrawString("內視鏡時效已過", f, sb, new PointF(120.0F, 70.0F));
            //g.DrawString("請更換", f, sb, new PointF(270.0F, 160.0F));
            //g.DrawString("相機非全新且不同", f, sb, new PointF(90.0F, 250.0F));

            f = new Font("標楷體", 24);
            g.DrawString("主機電池失效", f, sb, new PointF(60.0F, 90.0F));
            g.DrawString("請更換與校時", f, sb, new PointF(60.0F, 200.0F));

            //f = new Font("標楷體", 12);
            //g.DrawString("(使用<30分，累計關機>30分)", f, sb, new PointF(40.0F, 290.0F));

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button16_Click(object sender, EventArgs e)
        {
            string filename = @"D:\_git\vcs\_1.data\______test_files1\_image_processing\sample.png";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            bitmap1 = new Bitmap(filename);
            //pictureBox1.Image = bitmap2;

            int W = bitmap1.Width;
            int H = bitmap1.Height;
            richTextBox1.Text += "W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";
            pictureBox1.Size = new Size(W, H);
            pictureBox1.Image = bitmap1;

            int LAYER0_WIDTH = 1920;
            //int LAYER0_HEIGHT = 1080;
            int LAYER1_WIDTH = 1216;
            int LAYER1_HEIGHT = 912;
            //int LAYER2_WIDTH = 640;
            //int LAYER2_HEIGHT = 480;
            //int LAYER3_WIDTH = 1920;
            //int LAYER3_HEIGHT = 1080;
            int BORDER_X = 16;
            int BORDER_Y = 16;

            int LAYER1_START_X = (LAYER0_WIDTH - LAYER1_WIDTH - BORDER_X);
            int LAYER1_START_Y = BORDER_Y;

            //int WIDTH1 = 150;		//for ID NO, NAME
            //int WIDTH2 = 370;		//for Doraemon, 9/3/2112
            //int WIDTH3 = 430;		//for SN : 2DCF-XXXXXX
            //int WIDTH4 = 180;
            //int WIDTH5 = 80;	//for Sun, Mon
            int THICK1 = 40;

            int x;
            int y;
            SolidBrush sb;
            Font f;
            sb = new SolidBrush(Color.Black);
            f = new Font("Times New Roman", 20);
            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g

            g.FillRectangle(sb, 0, 0, 500, 800);

            //在指定位置畫上一圖
            // Create image.
            //Image newImage = Image.FromFile(@"D:\_git\vcs\_1.data\______test_files1\step3.png");

            filename = @"D:\_git\vcs\_1.data\______test_files1\step3.png";
            richTextBox1.Text += "開啟檔案: " + filename + ", 並顯示之\n";

            Bitmap bitmap3 = new Bitmap(filename);

            richTextBox1.Text += "W = " + bitmap3.Width.ToString() + " H = " + bitmap3.Height.ToString() + "\n";

            // Create coordinates for upper-left corner of image.
            int dx = 228;
            int dy = 264;

            // Draw image to screen.
            g.DrawImage(bitmap3, LAYER1_START_X + dx, LAYER1_START_Y + dy, bitmap3.Width, bitmap3.Height);

            sb = new SolidBrush(Color.White);

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 0;
            g.DrawString("ID NO:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 1;
            g.DrawString("NAME:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 3;
            g.DrawString("SEX:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 4;
            g.DrawString("AGE:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 5;
            g.DrawString("Birthday:", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 7;
            g.DrawString("12/28/2018 Fri", f, sb, new PointF(x, y));

            x = BORDER_X;
            y = BORDER_Y + THICK1 * 8;
            g.DrawString("16:33:32", f, sb, new PointF(x, y));

            p = new Pen(Color.Gray, 5);

            g.DrawRectangle(p, LAYER1_START_X, LAYER1_START_Y, LAYER1_WIDTH - 1, LAYER1_HEIGHT - 1);

            p = new Pen(Color.Blue, 5);

            int R = 170;

            Point[] myPointArray = { 
                new Point(LAYER1_START_X + R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + R),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X + R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X, BORDER_Y + R)
                                   };
            g.DrawPolygon(p, myPointArray);  // 繪出多邊形

            p = new Pen(Color.Red, 5);

            R = 250;

            Point[] myPointArray2 = { 
                new Point(LAYER1_START_X + R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + R),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X + R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X, BORDER_Y + R)
                                   };
            g.DrawPolygon(p, myPointArray2);  // 繪出多邊形

            //------------------------------------------------------------  # 60個

            p = new Pen(Color.Red, 5);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y, R * 2, R * 2, 180, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y, R * 2, R * 2, 270, 90);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 90, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 0, 90);

            //------------------------------------------------------------  # 60個

            R = 350;
            p = new Pen(Color.Yellow, 5);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y, R * 2, R * 2, 180, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y, R * 2, R * 2, 270, 90);
            g.DrawArc(p, LAYER1_START_X, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 90, 90);
            g.DrawArc(p, LAYER1_START_X + LAYER1_WIDTH - R * 2, LAYER1_START_Y + LAYER1_HEIGHT - R * 2, R * 2, R * 2, 0, 90);

            //------------------------------------------------------------  # 60個

            Point[] myPointArray3 = { 
                new Point(LAYER1_START_X + R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + R),
                new Point(LAYER1_START_X + LAYER1_WIDTH, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X + LAYER1_WIDTH - R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X + R, BORDER_Y + LAYER1_HEIGHT),
                new Point(LAYER1_START_X, BORDER_Y + LAYER1_HEIGHT - R),
                new Point(LAYER1_START_X, BORDER_Y + R)
                                   };
            g.DrawPolygon(p, myPointArray3);  // 繪出多邊形

            //SolidBrush sb;
            //Font f;
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 20);

            g.DrawString("0          170    200    250", f, sb, new PointF(LAYER1_START_X - 10, BORDER_Y + LAYER1_HEIGHT + 15));

            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        private void button17_Click(object sender, EventArgs e)
        {
            //StringFormat

            //畫格線
            bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
            Graphics g = Graphics.FromImage(bitmap1);
            draw_grid(g);
            pictureBox1.Image = bitmap1;

            //------------------------------------------------------------  # 60個

            Font f = new Font("標楷體", 24);

            StringFormat string_format = new StringFormat();

            //橫書
            //無參數的 預設 橫向列印
            g.DrawString("預設為橫向書寫, 字在線下", f, Brushes.Green, 200, 100);

            //直書
            string_format.FormatFlags = StringFormatFlags.DirectionVertical;  // 文字會垂直對齊
            //string_format.FormatFlags = StringFormatFlags.NoClip;
            g.DrawString("直向書寫, 字在線右", f, Brushes.Green, 200, 100, string_format);

            //string_format.Trimming = StringTrimming.None;
            //string_format.FormatFlags = StringFormatFlags.MeasureTrailingSpaces;

            g.FillEllipse(Brushes.Red, 200 - 10, 100 - 10, 20, 20);

            //------------------------------------------------------------  # 60個

            //重設StringFormat
            string_format = new StringFormat();

            //文字在線位置 + 置中/向左/向右

            int x_st = 100;
            int y_st = 400;
            int dx = 200;
            int dy = 100;

            string_format.LineAlignment = StringAlignment.Far;  // 字在線上
            string_format.Alignment = StringAlignment.Center;
            g.DrawString("字在線上", f, Brushes.Black, x_st + dx * 0, y_st + dy * 0, string_format);
            string_format.Alignment = StringAlignment.Center;
            g.DrawString("位置置中", f, Brushes.Black, x_st + dx * 0, y_st + dy * 1, string_format);
            string_format.Alignment = StringAlignment.Far;
            g.DrawString("向右寫", f, Brushes.Black, x_st + dx * 0, y_st + dy * 2, string_format);
            string_format.Alignment = StringAlignment.Near;
            g.DrawString("向右寫", f, Brushes.Black, x_st + dx * 0, y_st + dy * 3, string_format);

            //------------------------------------------------------------  # 60個

            string_format.LineAlignment = StringAlignment.Center;  // 字在線中
            string_format.Alignment = StringAlignment.Center;
            g.DrawString("字在線中", f, Brushes.Black, x_st + dx * 1, y_st + dy * 0, string_format);
            string_format.Alignment = StringAlignment.Center;
            g.DrawString("位置置中", f, Brushes.Black, x_st + dx * 1, y_st + dy * 1, string_format);
            string_format.Alignment = StringAlignment.Far;
            g.DrawString("向右寫", f, Brushes.Black, x_st + dx * 1, y_st + dy * 2, string_format);
            string_format.Alignment = StringAlignment.Near;
            g.DrawString("向右寫", f, Brushes.Black, x_st + dx * 1, y_st + dy * 3, string_format);

            //------------------------------------------------------------  # 60個

            string_format.LineAlignment = StringAlignment.Near;  // 字在線下
            string_format.Alignment = StringAlignment.Center;
            g.DrawString("字在線下", f, Brushes.Black, x_st + dx * 2, y_st + dy * 0, string_format);
            string_format.Alignment = StringAlignment.Center;
            g.DrawString("位置置中", f, Brushes.Black, x_st + dx * 2, y_st + dy * 1, string_format);
            string_format.Alignment = StringAlignment.Far;
            g.DrawString("向右寫", f, Brushes.Black, x_st + dx * 2, y_st + dy * 2, string_format);
            string_format.Alignment = StringAlignment.Near;
            g.DrawString("向右寫", f, Brushes.Black, x_st + dx * 2, y_st + dy * 3, string_format);

            for (int i = 0; i < 4; i++)
            {
                int xx = x_st + dx * 0;
                int yy = y_st + dy * i;
                g.FillEllipse(Brushes.Red, xx - 10, yy - 10, 20, 20);
            }

            for (int i = 0; i < 4; i++)
            {
                int xx = x_st + dx * 1;
                int yy = y_st + dy * i;
                g.FillEllipse(Brushes.Green, xx - 10, yy - 10, 20, 20);

            }

            for (int i = 0; i < 4; i++)
            {
                int xx = x_st + dx * 2;
                int yy = y_st + dy * i;
                g.FillEllipse(Brushes.Blue, xx - 10, yy - 10, 20, 20);
            }
        }

        //------------------------------------------------------------  # 60個

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //Rectangle的交集與聯集

            Graphics g = pictureBox1.CreateGraphics();

            //Rectangle 的 Union
            Rectangle rec1 = new Rectangle(100, 10, 200, 200);
            Rectangle rec2 = new Rectangle(150, 100, 200, 200);
            Rectangle rec3 = new Rectangle(30, 150, 200, 200);
            g.DrawRectangle(Pens.Red, rec1);
            g.DrawRectangle(Pens.Green, rec2);
            g.DrawRectangle(Pens.Blue, rec3);

            Rectangle new_rect = Rectangle.Union(rec1, rec2);
            new_rect = Rectangle.Union(new_rect, rec3);
            g.DrawRectangle(Pens.Magenta, new_rect);

            //------------------------------------------------------------  # 60個

            int x_st = 30;
            int y_st = 30 + 400;

            Rectangle rect1 = new Rectangle(x_st, y_st, 150, 150);
            g.FillRectangle(Brushes.Green, rect1); //綠色矩形區塊 固定 畫綠色

            x_st = 120;
            y_st = 120 + 400;

            Rectangle rect2 = new Rectangle(x_st, y_st, 150, 150);
            g.FillRectangle(Brushes.Red, rect2); //紅色矩形區塊 依滑鼠位置變化 畫紅色

            Rectangle union = Rectangle.Union(rect1, rect2); //聯集區域
            g.DrawRectangle(Pens.Black, union);                   //聯集 畫 黑色框

            Rectangle intersect = Rectangle.Intersect(rect1, rect2); //交集區域
            g.FillRectangle(Brushes.Yellow, intersect);    //交集 畫黃色
        }

        //------------------------------------------------------------  # 60個

        private void bt_clear_Click(object sender, EventArgs e)
        {
            //另法
            //bitmap1 = null;
            //pictureBox1.Image = null;

            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        void reset_bitmap1(int W, int H)
        {
            // 初始化畫布

            richTextBox1.Text += "建立一個 " + W.ToString() + " X " + H.ToString() + " 的空畫布\n";
            //指定畫布大小
            pictureBox1.Width = W;
            pictureBox1.Height = H;
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);

            g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);
            pictureBox1.Image = bitmap1;
            return;
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        int show_position = 1;
        private void button24_Click(object sender, EventArgs e)
        {
            string text = "牡丹亭";
            Font f = new Font("標楷體", 24, FontStyle.Bold);
            Image image2 = new Bitmap(filename);
            int Var_FontSize = (int)f.Size;//取得字體大小
            bool Var_isSetFont = false;//判斷目前文字是否超出圖片的大小
            int Var_W = image2.Width;//取得圖片的寬度
            int Var_H = image2.Height;//取得圖片的高度
            int Var_StrX = 0;//記錄文字的X位置
            int Var_StrY = 0;//記錄文字的Y位置

            Bitmap bitmap1 = new Bitmap(Var_W, Var_H);//實例化Image類
            Bitmap bitmap2 = new Bitmap(image2);//實例化Image類
            Graphics g = Graphics.FromImage(bitmap1);//用指定的Bitmap實例化Graphics
            Graphics g2 = Graphics.FromImage(image2);//用指定的Bitmap實例化Graphics
            SizeF Var_Size = new SizeF(Var_W, Var_H);//實例化SizeF類
            Font tem_Font = f;//取得文字的設定文字
            g.Clear(Color.White);//清空圖片
            while (Var_isSetFont == false)//如果文字超出圖片的大小
            {
                //設定文字的文字
                tem_Font = new Font(f.Name, Var_FontSize, f.Bold ? FontStyle.Bold : FontStyle.Regular);
                Var_Size = g.MeasureString(text, tem_Font);//對文字進行測量
                if (Var_Size.Width < bitmap1.Width - 10)//如果文字的寬度沒有超出圖片
                {
                    if (Var_Size.Height < bitmap1.Height - 10)//如果文字的高度沒有超出圖片
                    {
                        Var_isSetFont = true;//不減小文字的大小
                    }
                }
                else
                {
                    Var_FontSize = Var_FontSize - 1;//文字的字體大小減1
                }
            }
            switch (show_position)//選擇文字的顯示位置
            {
                case 1://右下角
                    richTextBox1.Text += "右下角\n";
                    Var_StrX = (int)(bitmap1.Width - Var_Size.Width - 3);//設定文字的X座標值
                    Var_StrY = (int)(bitmap1.Height - Var_Size.Height);//設定文字的Y座標值
                    break;
                case 2://右上角
                    richTextBox1.Text += "右上角\n";
                    Var_StrX = (int)(bitmap1.Width - Var_Size.Width - 3);
                    Var_StrY = 1;
                    break;
                case 3://左下角
                    richTextBox1.Text += "左下角\n";
                    Var_StrX = 1;
                    Var_StrY = (int)(bitmap1.Height - Var_Size.Height);
                    break;
                case 4://左上角
                    richTextBox1.Text += "左上角\n";
                    Var_StrX = 1;
                    Var_StrY = 1;
                    break;
                case 5://頂局中
                    richTextBox1.Text += "上中\n";
                    Var_StrX = (int)(bitmap1.Width - Var_Size.Width - 2) / 2;
                    Var_StrY = 1;
                    break;
                case 6://底局中
                    richTextBox1.Text += "下中\n";
                    Var_StrX = (int)(bitmap1.Width - Var_Size.Width - 2) / 2;
                    Var_StrY = (int)(bitmap1.Height - Var_Size.Height);
                    break;
            }
            g.DrawString(text, tem_Font, new SolidBrush(Color.Black), Var_StrX, Var_StrY);//繪製前景色為黑色的文字

            int tem_Become = 40;//設定文字的變色深度
            //搜尋圖片的所有象素
            for (int x = 1; x < bitmap1.Width; x++)
            {
                for (int y = 1; y < bitmap1.Height; y++)
                {
                    int tem_a, tem_r, tem_g, tem_b, tem_r1, tem_g1, tem_b1;//定義變數
                    if (bitmap1.GetPixel(x, y).ToArgb() == Color.Black.ToArgb())//如果目前象素的顏色為黑色
                    {
                        tem_a = bitmap2.GetPixel(x, y).A;//取得目前象素的alpha份量值
                        tem_r = bitmap2.GetPixel(x, y).R;//取得目前象素的R色值
                        tem_g = bitmap2.GetPixel(x, y).G;//取得目前象素的G色值
                        tem_b = bitmap2.GetPixel(x, y).B;//取得目前象素的B色值
                        tem_r1 = tem_r;//臨時儲存R色值
                        tem_g1 = tem_g;//臨時儲存G色值
                        tem_b1 = tem_b;//臨時儲存B色值
                        //根據加深後的圖片背景顯示文字
                        if (tem_b + tem_Become < 255)//如果B色值加上目前深度小於255
                        {
                            tem_b = tem_b + 255;//B色值加上深度值
                        }
                        if (tem_g + tem_Become < 255)
                        {
                            tem_g = tem_g + 255;
                        }
                        if (tem_r + tem_Become < 255)
                        {
                            tem_r = tem_r + 255;
                        }
                        if (tem_r1 - tem_Become > 0)//如果B色值加上目前深度大於0
                        {
                            tem_r1 = tem_r1 - tem_Become;//B色值減去深度值
                        }
                        if (tem_g1 - tem_Become > 0)
                        {
                            tem_g1 = tem_g1 - tem_Become;
                        }
                        if (tem_b1 - tem_Become > 0)
                        {
                            tem_b1 = tem_b1 - tem_Become;
                        }
                        g2.DrawEllipse(new Pen(new SolidBrush(Color.Black)), x, y + 1, 3, 3);//繪製文字的陰影
                        //以深後的圖片背景顯示文字
                        g2.DrawEllipse(new Pen(new SolidBrush(Color.FromArgb(tem_a, tem_r1, tem_g1, tem_b1))), x, y, 1, 1);
                    }
                }
            }
            pictureBox1.Image = image2;

            show_position++;  //設定文字的顯示位置
            if (show_position > 6)
            {
                show_position = 1;
            }
        }

        //------------------------------------------------------------  # 60個

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //DrawPoint

            List<PointF> points = new List<PointF>();

            int i;
            Random r = new Random();

            Graphics g = pictureBox1.CreateGraphics();				//實例化pictureBox1控件的Graphics類
            g.Clear(Color.White);

            for (i = 0; i < 14; i++)
            {
                points.Add(new PointF(30 * i, r.Next(400)));
            }

            if (points.Count > 1)
            {
                Pen p = new Pen(Color.Red);
                g.DrawLines(p, points.ToArray());   //List轉Array
            }

            foreach (PointF point in points)
            {
                const float radius = 4;
                g.DrawEllipse(Pens.Red, point.X - radius, point.Y - radius, 2 * radius, 2 * radius);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //DrawCurve

            Pen p1 = new Pen(Color.Red, 2);
            Pen p2 = new Pen(Color.Green, 2);
            Pen p3 = new Pen(Color.Blue, 2);
            Pen p4 = new Pen(Color.Gold, 2);
            Pen p5 = new Pen(Color.Black, 2);
            int x_st = 0;
            int y_st = 250;
            Point pt1 = new Point(x_st + 100, y_st + 0);
            Point pt2 = new Point(x_st + 200, y_st + 0);
            Point pt3 = new Point(x_st + 300, y_st + 100);
            Point pt4 = new Point(x_st + 200, y_st + 200);
            Point pt5 = new Point(x_st + 100, y_st + 200);
            Point pt6 = new Point(x_st + 0, y_st + 100);
            Point[] pts = { pt1, pt2, pt3, pt4, pt5, pt6 };
            g.DrawCurve(p1, pts, 1.0F); //使用tension
            g.DrawCurve(p2, pts);   //不使用tension
            g.DrawPolygon(p3, pts);

            g.DrawLines(p4, pts);
        }

        private void button27_Click(object sender, EventArgs e)
        {
            //DrawLines 直接使用 List
            List<PointF> points = new List<PointF>();

            // Make the Bitmap.
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            Bitmap bm = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bm);
            g.SmoothingMode = SmoothingMode.AntiAlias;  //反鋸齒

            Pen p = new Pen(Color.Blue, 1);

            // Loop over x values to generate points.
            for (float x = 0; x < W; x += 5)
            {
                float y = (float)(H / 2 * Math.Sin(x / 25)) + H / 2;
                points.Add(new PointF(x, y));
            }

            if (points.Count > 1)
            {
                for (int i = 0; i < points.Count; i++)
                {
                    points[i] = new PointF(points[i].X, H - points[i].Y);
                }
                g.DrawLines(p, points.ToArray());
            }
            pictureBox1.Image = bm;
        }

        //------------------------------------------------------------  # 60個

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //畫表單邊框

            Rectangle rect = new Rectangle(20, 20, this.ClientSize.Width - 40, this.ClientSize.Height - 40);

            Pen p = new Pen(Color.Red, 20);
            e.Graphics.DrawRectangle(p, rect);

            p.Color = Color.Lime;
            p.Width = 10;
            e.Graphics.DrawRectangle(p, rect.X, rect.Y, rect.Width, rect.Height);

            p.Color = Color.Blue;
            p.Width = 1;
            e.Graphics.DrawRectangle(p, rect);
        }

        //------------------------------------------------------------  # 60個

        private void button28_Click(object sender, EventArgs e)
        {
            //畫出Windows內建的系統圖示

            int W = 640;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            int x_st = 50;
            int y_st = 50;
            int dx = 130;
            int dy = 50;
            DrawIconSample(g, x_st + dx * 0, y_st + dy * 0, SystemIcons.Application, "Application");
            DrawIconSample(g, x_st + dx * 1, y_st + dy * 0, SystemIcons.Asterisk, "Asterisk");
            DrawIconSample(g, x_st + dx * 2, y_st + dy * 0, SystemIcons.Error, "Error");
            DrawIconSample(g, x_st + dx * 3, y_st + dy * 0, SystemIcons.Exclamation, "Exclamation");
            DrawIconSample(g, x_st + dx * 0, y_st + dy * 1, SystemIcons.Hand, "Hand");
            DrawIconSample(g, x_st + dx * 1, y_st + dy * 1, SystemIcons.Information, "Information");
            DrawIconSample(g, x_st + dx * 2, y_st + dy * 1, SystemIcons.Question, "Question");
            DrawIconSample(g, x_st + dx * 3, y_st + dy * 1, SystemIcons.Shield, "Shield");
            DrawIconSample(g, x_st + dx * 0, y_st + dy * 2, SystemIcons.Warning, "Warning");
            DrawIconSample(g, x_st + dx * 1, y_st + dy * 2, SystemIcons.WinLogo, "WinLogo");

            pictureBox1.Image = bitmap1;
        }

        private void DrawIconSample(Graphics g, int x_st, int y_st, Icon ico, string ico_name)
        {
            g.DrawIconUnstretched(ico, new Rectangle(x_st, y_st, ico.Width, ico.Height));
            g.DrawString(ico_name, this.Font, Brushes.Black, x_st + ico.Width + 5, y_st);
        }

        //------------------------------------------------------------  # 60個

        private void button29_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "就是 Button 上的 UAC圖示\n";
        }

        //------------------------------------------------------------  # 60個

        private void button30_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button31_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(640, 750);
            pictureBox1.Location = new Point(20, 20);

            int W = 640;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            SolidBrush sb = new SolidBrush(Color.FromArgb(0x30, 0xff, 0, 0));

            for (int i = 0; i < 400; i += 30)
            {
                g.FillRectangle(sb, i, 0, 200, 200);
                g.DrawRectangle(Pens.Black, i, 0, 200, 200);
            }

            //若使用下行, 則透明色不累加
            g.CompositingMode = CompositingMode.SourceCopy;

            for (int i = 0; i < 400; i += 30)
            {
                g.FillRectangle(sb, i, 220, 200, 200);
                g.DrawRectangle(Pens.Black, i, 220, 200, 200);
            }
            pictureBox1.Image = bitmap1;
        }

        //------------------------------------------------------------  # 60個

        //在線的上下畫字
        private void button32_Click(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(640, 750);
            pictureBox1.Location = new Point(20, 20);

            Graphics g = pictureBox1.CreateGraphics();
            g.TextRenderingHint = TextRenderingHint.AntiAliasGridFit;
            g.SmoothingMode = SmoothingMode.AntiAlias;
            g.InterpolationMode = InterpolationMode.High;

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int border = 100;

            PointF point_st = new PointF(border, border);
            PointF point_sp = new PointF(W - border, border);
            DrawOnSegment(g, point_st, point_sp, "1在線上畫字(true) ", true);   // 在線上畫字(true)
            DrawOnSegment(g, point_st, point_sp, "1在線下畫字(false)", false);  // 在線下畫字(false)

            point_st = new PointF(W - border, border);
            point_sp = new PointF(W - border, H - border);
            DrawOnSegment(g, point_st, point_sp, "2在線上畫字(true) ", true);   // 在線上畫字(true)
            DrawOnSegment(g, point_st, point_sp, "2在線下畫字(false)", false);  // 在線下畫字(false)

            point_st = new PointF(W - border, H - border);
            point_sp = new PointF(border, H - border);
            DrawOnSegment(g, point_st, point_sp, "3在線上畫字(true) ", true);   // 在線上畫字(true)
            DrawOnSegment(g, point_st, point_sp, "3在線下畫字(false)", false);  // 在線下畫字(false)

            point_st = new PointF(border, H - border);
            point_sp = new PointF(border, border);
            DrawOnSegment(g, point_st, point_sp, "4在線上畫字(true) ", true);   // 在線上畫字(true)
            DrawOnSegment(g, point_st, point_sp, "4在線下畫字(false)", false);  // 在線下畫字(false)
        }

        // Draw some text.
        private void DrawOnSegment(Graphics g, PointF start_point, PointF end_point, string txt, bool text_above_segment)
        {
            int first_ch = 0;
            g.DrawLine(Pens.Green, start_point, end_point);

            Brush brush = Brushes.Red;
            Font f = new Font("標楷體", 18);

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
                if (g.MeasureString(test_string, f).Width > dist)
                {
                    // This is one too many characters.
                    last_ch--;
                    richTextBox1.Text += "字串太長了, 畫到此\n";
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
            GraphicsState state = g.Save();
            if (text_above_segment)
            {
                g.TranslateTransform(0, -g.MeasureString(chars_that_fit, f).Height, MatrixOrder.Append);
            }

            float angle = (float)(180 * Math.Atan2(dy, dx) / Math.PI);
            g.RotateTransform(angle, MatrixOrder.Append);
            g.TranslateTransform(start_point.X, start_point.Y, MatrixOrder.Append);

            // Draw the characters that fit.
            g.DrawString(chars_that_fit, f, brush, 0, 0);

            // Restore the saved state.
            g.Restore(state);

            // Update first_ch and start_point.
            first_ch = last_ch + 1;
            float text_width = g.MeasureString(chars_that_fit, f).Width;
            start_point = new PointF(start_point.X + dx * text_width, start_point.Y + dy * text_width);
        }

        //------------------------------------------------------------  # 60個

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button35_Click(object sender, EventArgs e)
        {
            //為此Button畫陰影
            int len = 7;    //陰影長度
            Graphics g = this.CreateGraphics();
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button35.Left - i;
                p1.Y = button35.Top + button35.Height + i;
                Point p2 = new Point();
                p2.X = button35.Left + button35.Width + i;
                p2.Y = button35.Top + button35.Height + i;
                g.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button35.Left + button35.Width + i;
                p1.Y = button35.Top - i;
                Point p2 = new Point();
                p2.X = button35.Left + button35.Width + i;
                p2.Y = button35.Top + button35.Height + i;
                g.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
        }

        private void button36_Click(object sender, EventArgs e)
        {
            //為此Button畫投影
            int len = 7;    //投影長度
            Graphics g = this.CreateGraphics();
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button36.Left - i;
                p1.Y = button36.Top;
                Point p2 = new Point();
                p2.X = button36.Left + i;
                p2.Y = button36.Top + button36.Height + i;
                g.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
            for (int i = 0; i < len; i++)
            {
                Point p1 = new Point();
                p1.X = button36.Left - i;
                p1.Y = button36.Top - i;
                Point p2 = new Point();
                p2.X = button36.Left + button36.Width + i;
                p2.Y = button36.Top + i;
                g.DrawLine(new Pen(Color.Black, 1), p1, p2);
            }
        }

        private void button37_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

            int w = button37.ClientSize.Width;
            int h = button37.ClientSize.Height;
            g = ((Button)sender).CreateGraphics();
            g.DrawEllipse(p, 0, 0, w - 1, h - 1);

            //在Button上畫圖
            richTextBox1.Text += "在Button上畫圖, 要加上button_Paint()\n";

            ((Button)sender).Paint += new PaintEventHandler(button_Paint);
        }

        private void button_Paint(object sender, PaintEventArgs e)
        {
            int W = button37.Width;
            int H = button37.Height;
            //e.Graphics.FillRectangle(new SolidBrush(Color.White), x_st, y_st, W, H);
            e.Graphics.FillRectangle(new SolidBrush(Color.Pink), 0, 0, W, H);

            Pen p = new Pen(Color.Red, 6);
            e.Graphics.DrawRectangle(p, 0, 0, W - 0, H - 0);

            e.Graphics.DrawString("在Button上畫圖", new Font("標楷體", 11), new SolidBrush(Color.Blue), 5, 15);
        }

        private void button38_Click(object sender, EventArgs e)
        {
            //在控件上畫東西

            //先畫 button38
            Graphics g = button38.CreateGraphics();
            Pen p = new Pen(Color.ForestGreen, 4.0F);
            p.DashStyle = DashStyle.DashDotDot;

            Rectangle theRectangle = button38.ClientRectangle;
            theRectangle.Inflate(-2, -2);
            g.DrawRectangle(p, theRectangle);
            g.DrawRectangle(p, 10, 10, button38.Width - 20, button38.Height - 20);
            g.Dispose();
            p.Dispose();

            //再畫 richTextBox1
            g = richTextBox1.CreateGraphics();
            p = new Pen(Color.ForestGreen, 4.0F);
            p.DashStyle = DashStyle.DashDotDot;

            theRectangle = richTextBox1.ClientRectangle;
            theRectangle.Inflate(-2, -2);
            g.DrawRectangle(p, theRectangle);
            g.DrawRectangle(p, 10, 10, richTextBox1.Width - 20, richTextBox1.Height - 20);
            g.Dispose();
            p.Dispose();
        }

        //------------------------------------------------------------  # 60個

        private void button39_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        bool flag_eraser = false;
        private void bt_eraser_Click(object sender, EventArgs e)
        {
            if (flag_eraser == true)
            {
                flag_eraser = false;
                bt_eraser.BackColor = BackColor;
            }
            else
            {
                flag_eraser = true;
                bt_eraser.BackColor = Color.Red;
            }
        }

        private void bt_reset_Click(object sender, EventArgs e)
        {
            int W = 640;
            int H = 750;
            reset_bitmap1(W, H);  // 初始化畫布

            bitmap1 = null;
            pictureBox1.Image = null;
            richTextBox1.Clear();
        }

        private void bt_save_Click(object sender, EventArgs e)
        {
            save_image_to_drive();
        }

        void save_image_to_drive()
        {
            if (bitmap1 != null)
            {
                string filename = Application.StartupPath + "\\IMG_" + DateTime.Now.ToString("yyyyMMdd_HHmmss");
                String filename1 = filename + ".jpg";
                String filename2 = filename + ".bmp";
                String filename3 = filename + ".png";

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

        int flag_mouse_down = 0;    //給erase用
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = 1;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if ((flag_eraser == true) && (flag_mouse_down == 1))
            {
                sb = new SolidBrush(BackColor);
                g.FillEllipse(sb, e.X - 10, e.Y - 10, 20, 20);
                pictureBox1.Image = bitmap1;
            }
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = 0;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Pen pen = new Pen(Color.Red, 10);
            //Rectangle rect = SelectionRectangle(true);
            e.Graphics.DrawRectangle(pen, 0, 0, pictureBox1.Size.Width, pictureBox1.Size.Height);

            pen.Color = Color.Green;
            pen.DashPattern = new float[] { 5, 5 };
            e.Graphics.DrawRectangle(pen, 5, 5, pictureBox1.Size.Width - 10, pictureBox1.Size.Height - 10);
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void timer_progress_Tick(object sender, EventArgs e)
        {
            //畫進度表
            pictureBox_count.Invalidate();
        }

        int count = 0;
        private void pictureBox_count_Paint(object sender, PaintEventArgs e)
        {
            int border = 10;    //10 percent
            int W = pictureBox_count.ClientSize.Width;
            int H = pictureBox_count.ClientSize.Height;
            int x_st = W * border / 100;
            int y_st = H * border / 100;
            int w = W * (100 - border * 2) / 100;
            int h = H * (100 - border * 2) / 100;

            int i = 0;
            int width = 0;

            e.Graphics.Clear(Color.Pink);
            if (count == 0)
            {
            }
            else if (count <= 10)
            {
                width = w / 10;
                for (i = 0; i < count; i++)
                {
                    e.Graphics.FillRectangle(Brushes.Red, x_st + width * i, y_st, width, h);
                    e.Graphics.DrawRectangle(Pens.DarkRed, x_st + width * i, y_st, width, h);
                }
            }
            else
            {
                count = 0;
            }
            count++;
        }

        //------------------------------------------------------------  # 60個

        private void checkBox1_CheckedChanged(object sender, EventArgs e)
        {
            //g.Clear(Color.White);
            if (checkBox1.Checked == true)
            {
                bitmap1 = new Bitmap(pictureBox1.ClientSize.Width, pictureBox1.ClientSize.Height);
                Graphics g = Graphics.FromImage(bitmap1);
                draw_grid(g);
                pictureBox1.Image = bitmap1;
            }
        }

        public void draw_grid(Graphics g)
        {
            int i;
            int rows = pictureBox1.ClientSize.Height / 100;
            int cols = pictureBox1.ClientSize.Width / 100;
            p = new Pen(Color.Navy, 1);
            for (i = 0; i <= rows; i++)
            {
                g.DrawLine(p, 0, i * 100, pictureBox1.ClientSize.Width - 1, i * 100);
            }
            for (i = 0; i <= cols; i++)
            {
                g.DrawLine(p, new Point(i * 100, 0), new Point(i * 100, pictureBox1.ClientSize.Height - 1));
            }
        }

        //------------------------------------------------------------  # 60個
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*
bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0xff, 0x00, 0x00));
bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x00, 0xff, 0x00));
bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0x00, 0x00, 0xff));

bitmap1.SetPixel(xx, yy, Color.FromArgb(0xFF, (rr) % 256, (gg) % 256, (bb) % 256));
bitmap1.SetPixel(xx, yy, Color.FromArgb(30, 0x11, 0x33, 0x55));
bitmap1.SetPixel(xx, yy, Color.FromArgb(255, 0, 0, 0));

Color p = bitmap1.GetPixel(xx, yy);
//richTextBox1.Text += p.ToString() + " ";
richTextBox1.Text += p.A.ToString("X2") + p.R.ToString("X2") + p.G.ToString("X2") + p.B.ToString("X2") + " ";

//------------------------------------------------------------  # 60個

Font設定字型及樣式
new Font(this.Font, FontStyle.Italic),
                
//Graphics.DrawImage (Image, Rectangle, Rectangle, GraphicsUnit)
//四個參數分別是     來源影像 目標區域  來源區域      單位

string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
//讀檔 至 Image 影像
Image image = Image.FromFile(filename); // 產生一個Image物件
//旋轉
image.RotateFlip(RotateFlipType.Rotate90FlipNone); // 影像旋轉90度
//畫出來
g.DrawImage(image, 10, 50, image.Width, image.Height);
//              貼上的位置      貼上的大小 放大縮小用

//製作縮圖
int w = 100;	//預縮放的圖的寬度
Image imgThumbnail = image1.GetThumbnailImage(w, (int)(w * image1.Height / image1.Width), null, (IntPtr)0);

//------------------------------------------------------------  # 60個

Pen的屬性主要有: Color(顏色), DashCap(短劃線終點形狀), DashStyle(虛線樣式), EndCap(線尾形狀), StartCap(線頭形狀), Width(粗細) 等.

void ctx.drawImage(image, dx, dy);
void ctx.drawImage(image, dx, dy, dWidth, dHeight);
void ctx.drawImage(image, sx, sy, sWidth, sHeight, dx, dy, dWidth, dHeight);

//------------------------------------------------------------  # 60個

繪製圖形物件的方法

Graphics類別GDI+提供下列方法來繪製上述清單中的項目： 

DrawLines
DrawCurve
DrawClosedCurve

//------------------------------------------------------------  # 60個

建立畫布

Graphics 畫布物件變數;
畫布物件變數 = 控制項名稱.CreateGraphics();

例如：在表單上建立畫布g：
Graphics g = this.CreateGraphics();

例如：在圖片方塊pictureBox1上建立畫布g：
Graphics g = pictureBox1.CreateGraphics();

畫筆Pen物件

Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);
Pen p = new Pen(Color.Blue, 5);
p.Color = Color.Red;
p.Width = 2;

Pen 畫筆 = new Pen(畫筆顏色, 畫筆粗細);

//------------------------------------------------------------  # 60個

Pen只有一類
Brush有四類

Pen用於告訴Graphics如何繪製線條
Brush用於填充區域

Point的用法
Point b = new Point(20,10);
Point a = new Point();
a.X = 20;
a.Y = 10;

//------------------------------------------------------------  # 60個

本文將介紹在．Net中如何使用代碼畫圖表，就像用MS Excel產生的圖表一樣。也可以畫像DataGrid一樣的表格。
在．Net中，微軟給我們提供了畫圖類（System.Drawing.Imaging），在該類中畫圖的準系統都有。
比如：直線、折線、矩形、多邊形、橢圓形、扇形、曲線等等，因此一般的圖形都可以直接通過代碼畫出來。
接下來介紹一些畫圖函數：

Bitmap bitmap1 = new Bitmap(500, 500)　//定義映像大小；
bitmap1.Save(Stream,ImageCodecInfo) //將映像儲存到指定的輸出資料流；
Graphics g //定義或建立GDI繪圖對像；
PointF pt　//定義二維平面中x,y座標；
DrawString(text, f, Brush, PonitF) //用指定的Brush和Font對像在指定的矩形或點繪製指定的字串；
DrawLine(Pen, Ponit, Ponit) //用指定的筆(Pen)對像繪製指定兩點之間直線；
DrawPolygon(Pen, Ponit[]) //用指定的筆(Pen)對像繪製指定多邊形，比如三角形，四邊形等等；
FillPolygon(Brush, Ponit[]) //用指定的刷子(Brush)對像填充指定的多邊形；
DrawEllipse(Pen, x, y, Width, Height) //用指定的筆繪製一個邊框定義的橢圓；
FillEllipse(Brush, x, y, Width, Height) //用指定的刷子填充一個邊框定義的橢圓；
DrawRectangle(Pen, x, y, Width, Height) //用指定的筆繪製一個指定座標點、寬度、高度的矩形；
DrawPie(Pen, x, y, Width, Height, startAngle, sweepAngle) //用指定的筆繪製一個指定座標點、寬度、高度以及兩條射線組成的扇形；

//------------------------------------------------------------  # 60個

//影像的寬高可以是負的, 做倒影鏡射
string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";

Bitmap bitmap1 = new Bitmap(filename);

int Cx = this.pictureBox1.ClientSize.Width  / 2;  // 視窗客戶區 正中心
int Cy = this.pictureBox1.ClientSize.Height / 2;

int W = bitmap1.Width;
int H = bitmap1.Height;

g.DrawImage(bitmap1, Cx, Cy,  W / 2,  H / 2);
g.DrawImage(bitmap1, Cx, Cy, -W / 2,  H / 2);
g.DrawImage(bitmap1, Cx, Cy,  W / 2, -H / 2);
g.DrawImage(bitmap1, Cx, Cy, -W / 2, -H / 2);
*/


/*
            StringFormat string_format = new StringFormat();
            string_format.Alignment = StringAlignment.Near;
            string_format.LineAlignment = StringAlignment.Near;
            string_format.Trimming = StringTrimming.None;
            string_format.FormatFlags = StringFormatFlags.MeasureTrailingSpaces;

            g.TextRenderingHint = TextRenderingHint.AntiAlias;
*/


//f = new Font("Times New Roman", 40, FontStyle.Regular, GraphicsUnit.Pixel);

