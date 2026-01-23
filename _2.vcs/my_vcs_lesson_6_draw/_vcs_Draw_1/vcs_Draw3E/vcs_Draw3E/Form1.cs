using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D; //for CompositingQuality, SmoothingMode //提供畫高級二維，矢量圖形功能
//using System.Drawing.Drawing2D; //for SmoothingMode, PixelOffsetMode
//using System.Drawing.Text;      //for TextRenderingHint
//using System.IO;                //for File

namespace vcs_Draw3E
{
    public partial class Form1 : Form
    {
        int W = 250;
        int H = 250;

        float Tension0 = 0; // 張力 0 ~ 1
        float Tension = 0; // 張力 0 ~ 1
        float Tension_D = 0.05f; // 張力增減值

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
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new System.Drawing.Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            x_st = 20;
            y_st = 20;
            dx = 160;
            dy = 50;

            pictureBox0.Size = new Size(W, H);
            pictureBox1.Size = new Size(W, H);
            pictureBox2.Size = new Size(W, H);
            pictureBox3.Size = new Size(W, H);
            pictureBox4.Size = new Size(W, H);
            pictureBox5.Size = new Size(W, H);
            pictureBox6.Size = new Size(W, H);
            pictureBox7.Size = new Size(W, H);
            pictureBox8.Size = new Size(W, H);
            pictureBox9.Size = new Size(W, H);
            pictureBox10.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox11.Size = new Size(W, H);
            pictureBox12.Size = new Size(W, H);
            pictureBox13.Size = new Size(W, H);
            pictureBox14.Size = new Size(W, H);

            x_st = 10;
            y_st = 30;
            dx = W + 40;
            dy = H + 50;

            pictureBox0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            pictureBox2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            pictureBox3.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            pictureBox4.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            pictureBox5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            pictureBox6.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            pictureBox7.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            pictureBox8.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            pictureBox9.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            pictureBox10.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            pictureBox11.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            pictureBox12.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            pictureBox13.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            pictureBox14.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            int dd = 26;
            label0.Location = new Point(x_st + dx * 0, y_st + dy * 0 - dd);
            label1.Location = new Point(x_st + dx * 1, y_st + dy * 0 - dd);
            label2.Location = new Point(x_st + dx * 2, y_st + dy * 0 - dd);
            label3.Location = new Point(x_st + dx * 3, y_st + dy * 0 - dd);
            label4.Location = new Point(x_st + dx * 4, y_st + dy * 0 - dd);
            label5.Location = new Point(x_st + dx * 0, y_st + dy * 1 - dd);
            label6.Location = new Point(x_st + dx * 1, y_st + dy * 1 - dd);
            label7.Location = new Point(x_st + dx * 2, y_st + dy * 1 - dd);
            label8.Location = new Point(x_st + dx * 3, y_st + dy * 1 - dd);
            label9.Location = new Point(x_st + dx * 4, y_st + dy * 1 - dd);
            label10.Location = new Point(x_st + dx * 0, y_st + dy * 2 - dd);
            label11.Location = new Point(x_st + dx * 1, y_st + dy * 2 - dd);
            label12.Location = new Point(x_st + dx * 2, y_st + dy * 2 - dd);
            label13.Location = new Point(x_st + dx * 3, y_st + dy * 2 - dd);
            label14.Location = new Point(x_st + dx * 4, y_st + dy * 2 - dd);
            label0.Text = "畫曲線 DrawCurve";
            label1.Text = "畫曲線 DrawCurve 跳動";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            label6.Text = "";
            label7.Text = "";
            label8.Text = "";
            label9.Text = "";
            label10.Text = "";
            label11.Text = "";
            label12.Text = "";
            label13.Text = "";
            label14.Text = "";

            richTextBox1.Size = new Size(W, H * 3 + 100);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1740, 940);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        // Force all threads to end.
        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            Environment.Exit(0);
        }

        private void pictureBox0_Paint(object sender, PaintEventArgs e)
        {
            label0.Text = "DrawCurve： 張力 = " + Tension0.ToString();

            int Cx = 60;  // 基準點
            int Cy = 100;
            int D = 40; // 偏移值

            Point[] pt = new Point[4]; // 定義 四個點
            pt[0] = new Point(Cx - D, Cy + D);
            pt[1] = new Point(Cx - D, Cy - D);
            pt[2] = new Point(Cx + D, Cy - D);
            pt[3] = new Point(Cx + D, Cy + D);

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.DrawCurve(Pens.Black, pt, Tension0);  // 曲線的繪出

            for (int i = 0; i < pt.Length; i++) // 控制點的繪出
            {
                e.Graphics.DrawEllipse(Pens.Black, pt[i].X - 2, pt[i].Y - 2, 4, 4);
            }

            //------------------------------------------------------------  # 60個

            //this.Text = "畫封閉的曲線  DrawClosedCurve： 張力 = " + Tension0.ToString();
            //int Cx = 300;  // 基準點
            //int Cy = 200;
            Cx += 120;

            //int D = 60; // 偏移值

            //Point[] pt = new Point[4]; // 定義 四個點
            pt[0] = new Point(Cx - D, Cy + D);
            pt[1] = new Point(Cx - D, Cy - D);
            pt[2] = new Point(Cx + D, Cy - D);
            pt[3] = new Point(Cx + D, Cy + D);

            e.Graphics.SmoothingMode = System.Drawing.Drawing2D.SmoothingMode.AntiAlias;
            e.Graphics.DrawClosedCurve(Pens.Black, pt, Tension0, System.Drawing.Drawing2D.FillMode.Alternate);  // 曲線的繪出

            for (int i = 0; i < pt.Length; i++) // 控制點的繪出
            {
                e.Graphics.DrawEllipse(Pens.Black, pt[i].X - 2, pt[i].Y - 2, 4, 4);
            }
        }

        private void timer0_Tick(object sender, EventArgs e)
        {
            Tension0 += 0.1f;
            if (Tension0 > 1.0)
            {
                Tension0 = 0;
            }
            this.pictureBox0.Invalidate();
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Point[] pt = new Point[3]; // 定義 三個點
            pt[0] = new Point(30, this.pictureBox1.ClientSize.Height / 2);
            //pt[1] = new Point(300, 100);
            pt[2] = new Point(this.pictureBox1.ClientSize.Width - 30, this.pictureBox1.ClientSize.Height / 2);

            for (int i = 0; i < this.pictureBox1.ClientSize.Height; i = i + 10)
            {
                pt[1] = new Point(this.pictureBox1.ClientSize.Width / 2, i);
                e.Graphics.DrawCurve(Pens.Black, pt, Tension); // 曲線的繪出
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Tension = Tension + Tension_D; // 調整張力
            if (Tension >= 2 || Tension <= -1)
            {
                Tension_D = -Tension_D;
            }
            this.pictureBox1.Invalidate();
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

        int x_st = 0;
        int y_st = 0;
        private void pictureBox2_Paint(object sender, PaintEventArgs e)
        {
            int W = 1024;
            int H = 256;
            int i;

            // Create pens.
            Pen redPen = new Pen(Color.Red, 4);
            Point[] curvePoints = new Point[W];    //一維陣列內有 W 個Point

            //畫紅色的分布
            for (i = 0; i < W; i++)
            {
                y_st = 256 * 1 - (int)(128 * (sind(x_st + i) + 1));
                //curvePoints[i].X = x_st;
                //curvePoints[i].Y = y_st;
                //richTextBox1.Text += y_st.ToString() + " ";
                //curvePoints[i].Y = 2 * i;

                if (y_st > 255)
                    y_st = 255;
                else if (y_st < 0)
                    y_st = 0;
                Pen p = new Pen(Color.Red, 1);
                p.Color = Color.FromArgb(y_st, y_st, y_st);
                e.Graphics.DrawLine(p, i, 0, i, 256);
            }
            //e.Graphics.DrawLines(redPen, curvePoints);   //畫直線
            x_st -= 5;

            for (i = 0; i < W; i++)
            {
                //richTextBox1.Text += c
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            pictureBox2.Invalidate();
        }

        private void pictureBox3_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer3_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox4_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer4_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox5_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer5_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox6_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer6_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox7_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer7_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox8_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer8_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox9_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer9_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox10_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer10_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox11_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer11_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox12_Paint(object sender, PaintEventArgs e)
        {

        }

        private void timer12_Tick(object sender, EventArgs e)
        {
        }

        private void pictureBox13_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer13_Tick(object sender, EventArgs e)
        {
        }


        private void pictureBox14_Paint(object sender, PaintEventArgs e)
        {
        }

        private void timer14_Tick(object sender, EventArgs e)
        {
        }





        //6060

        private int RetrievRandomCorners(int minCorners, int maxCorners)
        {
            return new Random(Guid.NewGuid().GetHashCode()).Next(minCorners, maxCorners);
        }

        void draw_random_pattern(int type, int minCorners, int maxCorners, PictureBox pbox)
        {
            int width = pbox.Width;
            int height = pbox.Height;
            int numX = 10;
            int numY = 10;
            float perX = width * 1f / numX;
            float perY = height * 1f / numY;
            Bitmap bitmap1 = new Bitmap(width, height);
            Graphics g = Graphics.FromImage(bitmap1);

            g.CompositingQuality = CompositingQuality.HighQuality;
            g.SmoothingMode = SmoothingMode.HighQuality;
            g.InterpolationMode = InterpolationMode.HighQualityBicubic;

            g.FillRectangle(Brushes.Black, new Rectangle(0, 0, width, height));

            int lastCorners = minCorners;
            for (int i = 0; i < numX; i++)
            {
                for (int j = 0; j < numY; j++)
                {
                    long tick = DateTime.Now.Ticks;
                    Random random = new Random((int)(tick & 0xffffffff) | (int)(tick >> 32));
                    int corners = random.Next(minCorners, maxCorners);
                    if (Math.Abs(corners - lastCorners) < (maxCorners - minCorners) / 2)
                    {
                        corners = RetrievRandomCorners(minCorners, maxCorners);
                    }
                    lastCorners = corners;

                    if (type == 0)
                    {
                        //this.Text = "竹葉";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 1.4f), (int)(perX * 0.009f), corners);
                        g.FillClosedCurve(Brushes.Green, points, FillMode.Winding);
                    }
                    else if (type == 1)
                    {
                        //this.Text = "長葉草";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.88f), (int)(perX * 0.01f), corners);
                        g.FillClosedCurve(Brushes.Green, points, FillMode.Winding);
                    }
                    else if (type == 2)
                    {
                        //this.Text = "雜亂石頭";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.4f), (int)(perX * 0.396f), corners);
                        g.FillClosedCurve(Brushes.Gray, points, FillMode.Winding);
                    }
                    else if (type == 3)
                    {
                        //this.Text = "天上繁星";
                        PointF[] points = Stone.CreateStone(new Point((int)(perX * j), (int)(perY * i)), (int)(perX * 0.18f), (int)(perX * 0.06f), corners);
                        g.FillClosedCurve(Brushes.White, points, FillMode.Winding);
                    }
                    else
                    {
                        //this.Text = "未選取";
                        return;
                    }
                }
            }
            pbox.Image = bitmap1;
        }

        void draw_random_pattern0()
        {
            //this.Text = "竹葉";
            int type = 0;
            int minCorners = 3;
            int maxCorners = 4;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox5);
        }

        void draw_random_pattern1()
        {
            //this.Text = "長葉草";
            int type = 1;
            int minCorners = 20;
            int maxCorners = 38;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox6);
        }

        void draw_random_pattern2()
        {
            //this.Text = "雜亂石頭";
            int type = 2;
            int minCorners = 3;
            int maxCorners = 4;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox7);
        }

        void draw_random_pattern3()
        {
            //this.Text = "天上繁星";
            int type = 3;
            int minCorners = 3;
            int maxCorners = 4;

            draw_random_pattern(type, minCorners, maxCorners, pictureBox8);
        }

        private void timer_random_pattern_Tick(object sender, EventArgs e)
        {
            //模擬雜亂無章的現實場景
            draw_random_pattern0();
            draw_random_pattern1();
            draw_random_pattern2();
            draw_random_pattern3();
        }

    }


    public static class Stone
    {
        public static PointF[] CreateStone(Point center, int outerRadius, int inner_radius, int arms)
        {
            int center_x = center.X;
            int center_y = center.Y;
            PointF[] points = new PointF[arms * 2];
            double offset = Math.PI / 2;
            double arc = 2 * Math.PI / arms;
            double half = arc / 2;
            double angle = 0;
            for (int i = 0; i < arms; i++)
            {
                Random randomOuter = new Random((int)DateTime.Now.Ticks);
                outerRadius = outerRadius - randomOuter.Next((int)(inner_radius * 0.06 * new Random().Next(-20, 20) / 30d), (int)(inner_radius * 0.08));
                //outerRadius = outerRadius - randomOuter.Next((int)(inner_radius * 0.16 * new Random().Next(-20, 20) / 30d), (int)(inner_radius * 0.18));
                Random randomInner = new Random(Guid.NewGuid().GetHashCode());
                inner_radius = inner_radius + randomInner.Next((int)(inner_radius * 0.02 * new Random().Next(-100, 100) / 150d), (int)(inner_radius * 0.08));
                //inner_radius = inner_radius + randomInner.Next((int)(inner_radius * 0.02 * new Random().Next(-100, 100) / 150d), (int)(inner_radius * 0.22));

                if (inner_radius > outerRadius)
                {
                    int temp = outerRadius;
                    outerRadius = inner_radius;
                    inner_radius = temp;
                }
                double angleTemp = arc * randomInner.Next(-5, 5) / 10d;
                angle = i * arc;
                angle += angleTemp;
                points[i * 2].X = (float)(center_x + Math.Cos(angle - offset) * outerRadius);
                points[i * 2].Y = (float)(center_y + Math.Sin(angle - offset) * outerRadius);
                points[i * 2 + 1].X = (float)(center_x + Math.Cos(angle + half - offset) * inner_radius);
                points[i * 2 + 1].Y = (float)(center_y + Math.Sin(angle + half - offset) * inner_radius);
            }
            return points;
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


