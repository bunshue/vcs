using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_test_all_11_Draw
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Font f;

        Point[] p_Array = { new Point(150, 50), new Point(100, 400), new Point(450, 400), new Point(400, 50) };

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = pictureBox1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 16);

            g.Clear(Color.Red);             //useless??
        }

        private void button1_Click(object sender, EventArgs e)
        {
            p = new Pen(Color.Green, 3);
            g.DrawRectangle(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);

            g.DrawRectangle(p, new Rectangle(100, 100, 400, 300));

            Rectangle r = new Rectangle(200, 200, 200, 100);
            g.DrawRectangle(p, r);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //g.Clear(Color.Yellow);
            g.Clear(BackColor);
            if (checkBox1.Checked == true)
                draw_grid();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            draw_grid();
            /*
            Point myStartPoint = new Point(400, 200);
            Point myEndPoint = new Point(120, 600);
            g.DrawLine(p, myStartPoint, myEndPoint);
            */
        }

        private void button4_Click(object sender, EventArgs e)
        {
            p = new Pen(Color.Green, 3);
            g.DrawEllipse(p, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);

            g.DrawEllipse(p, new Rectangle(100, 100, 400, 300));

            Rectangle r = new Rectangle(200, 200, 200, 100);
            g.DrawEllipse(p, r);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            draw_grid();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            Rectangle[] walls;
            walls = new Rectangle[4] {
	            new Rectangle(0, 0, 200, 100),
	            new Rectangle(200, 100, 200, 200),
	            new Rectangle(100, 400, 500, 200),
	            new Rectangle(300, 200, 300, 300)
            };
            g.DrawRectangles(p, walls);

        }

        private void button7_Click(object sender, EventArgs e)
        {
            Pen p = new Pen(Color.Black);
            Point[] points = new Point[3];
            points[0] = new Point(400, 0);
            points[1] = new Point(0, 500);
            points[2] = new Point(400, 500);
            g.DrawPolygon(p, points);

            Point[] myPointArray = { 
                new Point(0, 0),
                new Point(350, 30),
                new Point(430, 60),
                new Point(150, 120),
                new Point(20, 60) };
            g.DrawPolygon(p, myPointArray);

        }

        private void button8_Click(object sender, EventArgs e)
        {
            sb = new SolidBrush(Color.Red);
            g.FillRectangle(sb, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);

            sb = new SolidBrush(Color.Green);
            g.FillRectangle(sb, new Rectangle(100, 100, 400, 300));

            sb = new SolidBrush(Color.Blue);
            Rectangle r = new Rectangle(200, 200, 200, 100);
            g.FillRectangle(sb, r);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            g.DrawString("各種畫圖範例", f, sb, new PointF(150.0F, 150.0F));
            g.DrawString("各種畫圖範例", f, sb, 50.0F, 50.0F);
        }

        private void button10_Click(object sender, EventArgs e)
        {
            Point[] points = new Point[3];
            points[0] = new Point(400, 0);
            points[1] = new Point(0, 500);
            points[2] = new Point(400, 500);
            g.FillPolygon(sb, points);

            sb = new SolidBrush(Color.Red);
            g.FillPolygon(sb, p_Array);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            sb = new SolidBrush(Color.Red);
            g.FillEllipse(sb, 0, 0, pictureBox1.Width - 1, pictureBox1.Height - 1);

            sb = new SolidBrush(Color.Green);
            g.FillEllipse(sb, new Rectangle(100, 100, 400, 300));

            sb = new SolidBrush(Color.Blue);
            Rectangle r = new Rectangle(200, 200, 200, 100);
            g.FillEllipse(sb, r);

        }

        private void button12_Click(object sender, EventArgs e)
        {
            g.DrawPie(p, 300, 300, 200, 200, 0, 135);

            float total = 1234;
            float part1 = 222;
            float part2 = 345;
            float part3 = 456;
            float others;
            others = total - part1 - part2 - part3;
            float angle1 = 360 * part1 / total;
            float angle2 = 360 * part2 / total;
            float angle3 = 360 * part3 / total;
            float angle4 = 360 * others / total;
            richTextBox1.Text += "angle1 = " + angle1.ToString() + "\n";
            richTextBox1.Text += "angle2 = " + angle2.ToString() + "\n";
            richTextBox1.Text += "angle3 = " + angle3.ToString() + "\n";
            richTextBox1.Text += "angle4 = " + angle4.ToString() + "\n";

            p = new Pen(Color.Red, 10);
            g.DrawPie(p, 100, 50, 250, 250, 0, angle1);
            g.DrawPie(p, 100, 50, 250, 250, angle1, angle2);
            g.DrawPie(p, 100, 50, 250, 250, angle1 + angle2, angle3);
            g.DrawPie(p, 100, 50, 250, 250, angle1 + angle2 + angle3, angle4);

        }

        private void button13_Click(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, 100, 100, 300, 200);

            p = new Pen(Color.Blue, 10);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawArc(p, 100, 100, 300, 200, 0, 135);

            g.DrawArc(p, 300, 300, 100, 100, 0, -135);

        }

        private void button14_Click(object sender, EventArgs e)
        {
            g.FillPie(sb, 300, 300, 200, 200, 0, 135);

            float total = 1234;
            float part1 = 222;
            float part2 = 345;
            float part3 = 456;
            float others;
            others = total - part1 - part2 - part3;
            float angle1 = 360 * part1 / total;
            float angle2 = 360 * part2 / total;
            float angle3 = 360 * part3 / total;
            float angle4 = 360 * others / total;
            richTextBox1.Text += "angle1 = " + angle1.ToString() + "\n";
            richTextBox1.Text += "angle2 = " + angle2.ToString() + "\n";
            richTextBox1.Text += "angle3 = " + angle3.ToString() + "\n";
            richTextBox1.Text += "angle4 = " + angle4.ToString() + "\n";

            Brush b1 = new SolidBrush(Color.Red);
            Brush b2 = new SolidBrush(Color.Green);
            Brush b3 = new SolidBrush(Color.Blue);
            Brush b4 = new SolidBrush(Color.Yellow);

            g.FillPie(b1, 100, 50, 250, 250, 0, angle1);
            g.FillPie(b2, 100, 50, 250, 250, angle1, angle2);
            g.FillPie(b3, 100, 50, 250, 250, angle1 + angle2, angle3);
            g.FillPie(b4, 100, 50, 250, 250, angle1 + angle2 + angle3, angle4);




        }

        private void button15_Click(object sender, EventArgs e)
        {
            Point[] aaa = new Point[90];
            double yy;
            int i;
            for (i = 0; i < 90; i++)
            {
                //yy = Math.Sin(Math.PI * i * 10 / 180)* 100 + 100;
                yy = Math.Sin(Math.PI * i * 4 / 180) * 100 + 100;
                aaa[i].X = (int)i * 3;
                aaa[i].Y = 100 - (int)yy + 100;
                richTextBox1.Text += "x= " + aaa[i].X.ToString() + " y = " + aaa[i].Y.ToString() + "\n";
            }
            p = new Pen(Color.Red, 3);
            g.DrawCurve(p, aaa);

            p = new Pen(Color.Blue, 8);
            g.DrawLines(p, p_Array);

            p = new Pen(Color.Red, 3);
            for (float k = 0; k < 1.5; k += 0.4F)
            {
                g.DrawCurve(p, p_Array, k);
            }

            p = new Pen(Color.Green, 2);
            g.DrawClosedCurve(p, p_Array);

            p = new Pen(Color.Yellow, 1);
            g.DrawCurve(p, p_Array);

        }

        private void button16_Click(object sender, EventArgs e)
        {
            int yy = 20;
            int dy = 25;

            p.Width = 5;
            p.Color = Color.Blue;

            p.DashStyle = System.Drawing.Drawing2D.DashStyle.Custom;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dash;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDot;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.DashStyle = System.Drawing.Drawing2D.DashStyle.DashDotDot;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.DashStyle = System.Drawing.Drawing2D.DashStyle.Dot;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.DashStyle = System.Drawing.Drawing2D.DashStyle.Solid;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy * 2;
            p.EndCap = System.Drawing.Drawing2D.LineCap.AnchorMask;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.Custom;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.DiamondAnchor;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.Flat;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.NoAnchor;
            g.DrawLine(p, 20, yy, 300, yy);


            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.Round;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.RoundAnchor;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.Square;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.SquareAnchor;
            g.DrawLine(p, 20, yy, 300, yy);

            yy += dy;
            p.EndCap = System.Drawing.Drawing2D.LineCap.Triangle;
            g.DrawLine(p, 20, yy, 300, yy);

        }

        private void button17_Click(object sender, EventArgs e)
        {
            g.DrawBezier(p, 0, 0, 40, 20, 200, 450, 500, 300);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //純色筆刷
            SolidBrush sb = new SolidBrush(Color.LightGreen);
            g.FillEllipse(sb, 50, 50, 300, 100);

            //規劃筆刷
            HatchBrush hb = new HatchBrush(HatchStyle.Vertical, Color.Blue, Color.Green);
            g.FillEllipse(hb, 50, 150, 200, 100);

            hb = new HatchBrush(HatchStyle.Cross, Color.Blue, Color.Green);
            g.FillEllipse(hb, 250, 150, 200, 100);

            hb = new HatchBrush(HatchStyle.Wave, Color.Blue, Color.Green);
            g.FillEllipse(hb, 450, 150, 200, 100);

            //紋理筆刷
            Image myImage = Image.FromFile(@"D:\bear.jpg");
            TextureBrush tb = new TextureBrush(myImage);
            g.FillEllipse(tb, 50, 250, 300, 100);


            //漸層筆刷
            Rectangle r;
            LinearGradientBrush lgb;

            r = new Rectangle(50, 350, 300, 100);
            lgb = new LinearGradientBrush(
               r,
               Color.Blue,
               Color.Green,
               LinearGradientMode.Horizontal);
            g.FillEllipse(lgb, r);


            r = new Rectangle(50, 450, 300, 100);
            lgb = new LinearGradientBrush(
               r,
               Color.Blue,
               Color.Green,
               LinearGradientMode.BackwardDiagonal);
            g.FillEllipse(lgb, r);

        }

        public void draw_grid()
        {
            int i;
            p = new Pen(Color.Navy, 1);
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, 0, i * 100, pictureBox1.ClientSize.Width - 1, i * 100);
            }
            for (i = 0; i < 7; i++)
            {
                g.DrawLine(p, new Point(i * 100, 0), new Point(i * 100, pictureBox1.ClientSize.Height - 1));
            }
        }
    }
}
