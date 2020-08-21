using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;     //for GraphicsPath

namespace vcs_Draw4
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Font f;

        bool flag_eraser = false;

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
            pictureBox1.BackColor = Color.Pink;
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
            g.Clear(BackColor);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Pen bluePen = new Pen(Color.Blue, 3);// Create pens.

            Point point1a = new Point(0, 0);
            Point point2a = new Point(600, 400);
            g.DrawLine(bluePen, point1a, point2a);     // Draw line to screen.

            Point point3a = new Point(300, 400);
            Point point4a = new Point(600, 0);
            g.DrawLine(bluePen, point3a, point4a);     // Draw line to screen.

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


            // Create string to draw.
            String drawString = "江山如畫一時多少豪傑";

            // Create font and brush.
            Font drawFont = new Font("標楷體", 36, FontStyle.Italic|FontStyle.Underline|FontStyle.Strikeout);
            SolidBrush drawBrush = new SolidBrush(Color.Black);

            // Create point for upper-left corner of drawing.
            PointF drawPoint = new PointF(50.0F, 250.0F);

            // Draw string to screen.
            g.DrawString(drawString, drawFont, drawBrush, drawPoint);

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

        private void button17_Click(object sender, EventArgs e)
        {
            g.DrawBezier(p, 0, 0, 40, 20, 200, 450, 500, 300);
        }

        private void button32_Click(object sender, EventArgs e)
        {
            Point[] pt = new Point[360];    //一維陣列內有360個Point
            int angle;
            int amplitude = 100;
            for (angle = 0; angle < 360; angle += 1)
            {
                pt[angle].X = angle;
                pt[angle].Y = 300 - (int)(amplitude * Math.Sin(angle * 3 * Math.PI / 180));

            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt);

        }

        private void button29_Click(object sender, EventArgs e)
        {
            Point[] arrayPoint = new Point[20];
            p = new Pen(Color.Blue, 5);
            double zz;

            for (int i = 0; i < 20; i++)
            {
                zz = Math.Sin(Math.PI * i * 30 / 180) * 200 + 200;
                arrayPoint[i].X = i * 20;
                arrayPoint[i].Y = (int)zz;
            }
            g.DrawLines(p, arrayPoint);

        }

        private void button30_Click(object sender, EventArgs e)
        {

            // 以紅色繪正弦波
            //Graphics g = this.CreateGraphics();
            //Pen p = new Pen(Color.Red, 2);
            int h = 100;
            int y1 = 100;
            double angle, y;
            float tmpy, tmpx;
            for (double x = 0; x <= 360; x++)
            {
                angle = x / 180 * Math.PI;
                y = Convert.ToDouble(y1) + Math.Sin(angle) * h;
                tmpx = Convert.ToSingle(x);
                tmpy = Convert.ToSingle(y);
                g.DrawEllipse(p, tmpx, tmpy, 1, 1); //繪製紅色圓點
            }

            g.DrawEllipse(p, 260, 260, 100, 100); //繪製紅色圓點

            SolidBrush sb = new SolidBrush(Color.Green);
            g.FillEllipse(sb, 360, 360, 100, 100); //繪製紅色圓點

        }

        private void button31_Click(object sender, EventArgs e)
        {
            int[] x = new int[10];
            double[] y = new double[10];
            int[] yy = new int[10];
            //int x[10] = 0;
            //float y[10] = 0;
            for (int i = 0; i < 10; i++)
            {
                x[i] = i * 40;
                y[i] = Math.Sin(x[i] * Math.PI / 180) * 200 + 200;
                yy[i] = (int)y[i];
                richTextBox1.Text += x[i].ToString() + "\t" + y[i].ToString() + "\n";
            }

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.

            // Create points that define curve.
            Point point0 = new Point(x[0], yy[0]);
            Point point1 = new Point(x[1], yy[1]);
            Point point2 = new Point(x[2], yy[2]);
            Point point3 = new Point(x[3], yy[3]);
            Point point4 = new Point(x[4], yy[4]);
            Point point5 = new Point(x[5], yy[5]);
            Point point6 = new Point(x[6], yy[6]);
            Point point7 = new Point(x[7], yy[7]);
            Point point8 = new Point(x[8], yy[8]);
            Point point9 = new Point(x[9], yy[9]);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9 };

            g.DrawCurve(greenPen, curvePoints); //畫曲線
            g.DrawLines(greenPen, curvePoints);   //畫直線

        }

        private void button28_Click(object sender, EventArgs e)
        {
            Point[] pt = new Point[360];    //一維陣列內有360個Point
            int angle;
            int amplitude = 100;
            for (angle = 0; angle < 360; angle += 1)
            {
                pt[angle].X = angle;
                pt[angle].Y = (int)(amplitude * Math.Sin(angle * 3 * Math.PI / 180)) + amplitude;

            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt);

        }

        private void button25_Click(object sender, EventArgs e)
        {

            //畫曲線
            Point[] pts = new Point[5];
            pts[0].X = 10;
            pts[0].Y = 10;
            pts[1].X = 20;
            pts[1].Y = 60;
            pts[2].X = 30;
            pts[2].Y = 10;
            pts[3].X = 40;
            pts[3].Y = 60;
            pts[4].X = 50;
            pts[4].Y = 10;
            g.DrawCurve(new Pen(Color.Black), pts);

        }

        private void button24_Click(object sender, EventArgs e)
        {



            //畫多個Rectangles
            Rectangle[] R = new Rectangle[25];
            int i;
            for (i = 0; i <= 24; i++)
            {
                //R[i] = new Rectangle(0 + 30 * i, 0 + 30 * i);
                R[i] = new Rectangle(i * 10, i * 5, i * 30, i * 15);
            }
            g.DrawRectangles(new Pen(Brushes.Red, 3), R);


        }

        private void button34_Click(object sender, EventArgs e)
        {
            // Create points that define curve.
            Point point0 = new Point(0, 400);
            Point point1 = new Point(50, 350);
            Point point2 = new Point(100, 400);
            Point point3 = new Point(150, 250);
            Point point4 = new Point(200, 200);
            Point point5 = new Point(250, 150);
            Point point6 = new Point(300, 100);
            Point point7 = new Point(350, 50);
            Point point8 = new Point(400, 0);
            Point point9 = new Point(450, 200);
            Point point10 = new Point(500, 400);
            Point point11 = new Point(550, 300);
            Point point12 = new Point(600, 100);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12 };

            Pen redPen = new Pen(Color.Red, 3); // Create pens.
            g.DrawLines(redPen, curvePoints);   //畫直線

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.
            g.DrawCurve(greenPen, curvePoints); //畫曲線
        }

        private void button39_Click(object sender, EventArgs e)
        {
            double[] xx = new double[20];
            double[] yy = new double[20];

            for (int i = 0; i < 20; i++)
            {
                xx[i] = i * 30;
                yy[i] = Math.Sin(i) * 200 + 200;
                //yy[i] = 100;
            }

            // Create points that define curve.
            Point point0 = new Point((int)xx[0], pictureBox1.Height - (int)yy[0]);
            Point point1 = new Point((int)xx[1], pictureBox1.Height - (int)yy[1]);
            Point point2 = new Point((int)xx[2], pictureBox1.Height - (int)yy[2]);
            Point point3 = new Point((int)xx[3], pictureBox1.Height - (int)yy[3]);
            Point point4 = new Point((int)xx[4], pictureBox1.Height - (int)yy[4]);
            Point point5 = new Point((int)xx[5], pictureBox1.Height - (int)yy[5]);
            Point point6 = new Point((int)xx[6], pictureBox1.Height - (int)yy[6]);
            Point point7 = new Point((int)xx[7], pictureBox1.Height - (int)yy[7]);
            Point point8 = new Point((int)xx[8], pictureBox1.Height - (int)yy[8]);
            Point point9 = new Point((int)xx[9], pictureBox1.Height - (int)yy[9]);
            Point point10 = new Point((int)xx[10], pictureBox1.Height - (int)yy[10]);
            Point point11 = new Point((int)xx[11], pictureBox1.Height - (int)yy[11]);
            Point point12 = new Point((int)xx[12], pictureBox1.Height - (int)yy[12]);
            Point point13 = new Point((int)xx[13], pictureBox1.Height - (int)yy[13]);
            Point point14 = new Point((int)xx[14], pictureBox1.Height - (int)yy[14]);
            Point point15 = new Point((int)xx[15], pictureBox1.Height - (int)yy[15]);
            Point point16 = new Point((int)xx[16], pictureBox1.Height - (int)yy[16]);
            Point point17 = new Point((int)xx[17], pictureBox1.Height - (int)yy[17]);
            Point point18 = new Point((int)xx[18], pictureBox1.Height - (int)yy[18]);
            Point point19 = new Point((int)xx[19], pictureBox1.Height - (int)yy[19]);

            Point[] curvePoints = { point0, point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11, point12, point13, point14, point15, point16, point17, point18, point19 };

            Pen redPen = new Pen(Color.Red, 3); // Create pens.
            g.DrawLines(redPen, curvePoints);   //畫直線

            Pen greenPen = new Pen(Color.Green, 3); // Create pens.
            g.DrawCurve(greenPen, curvePoints); //畫曲線


        }

        private void button42_Click(object sender, EventArgs e)
        {
            if (flag_eraser == true)
            {
                flag_eraser = false;
                button42.BackColor = BackColor;
            }
            else
            {
                flag_eraser = true;
                button42.BackColor = Color.Red;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            label1.Text = "(" + Control.MousePosition.X.ToString() + ", " + Control.MousePosition.Y.ToString() + ")";
            if (flag_mouse_down == 1)
            {
                label2.Text = "1";
                sb = new SolidBrush(Color.White);
                //g.FillEllipse(sb, Control.MousePosition.X, Control.MousePosition.Y, Control.MousePosition.X + 10, Control.MousePosition.Y + 10);


        }
            else
                label2.Text = "0";
        }

        int flag_mouse_down = 0;
        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_mouse_down = 1;
        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_mouse_down = 0;
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {
            if ((flag_eraser == true) && (flag_mouse_down == 1))
            {
                sb = new SolidBrush(Color.White);
                g.FillEllipse(sb, e.X - 5, e.Y - 5, 10, 10);
            }
        }

        private void button43_Click(object sender, EventArgs e)
        {
            //DrawRoundRect(100, 100, 300, 200, 20);

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

        private void button44_Click(object sender, EventArgs e)
        {
            GraphicsPath myGraphicsPath = new GraphicsPath();
            myGraphicsPath.AddLine(0, 0, 300, 200);
            myGraphicsPath.AddEllipse(100, 100, 20, 40);
            myGraphicsPath.AddBezier(130, 160, 170, 160, 150, 130, 300, 110);
            g.DrawPath(p, myGraphicsPath);
        }

        private void button45_Click(object sender, EventArgs e)
        {
            GraphicsPath myGraphicsPath = new GraphicsPath();

            Point[] myPointArray = {
new Point(5, 30), 
new Point(20, 40), 
new Point(50, 30)};

            FontFamily myFontFamily = new FontFamily("Times New Roman");
            PointF myPointF = new PointF(50, 20);
            StringFormat myStringFormat = new StringFormat();

            myGraphicsPath.AddArc(0, 0, 30, 20, -90, 180);
            myGraphicsPath.StartFigure();
            myGraphicsPath.AddCurve(myPointArray);
            myGraphicsPath.AddString("a string in a path", myFontFamily,
               0, 24, myPointF, myStringFormat);
            myGraphicsPath.AddPie(230, 10, 40, 40, 40, 110);
            g.DrawPath(p, myGraphicsPath);
        }

        private void button46_Click(object sender, EventArgs e)
        {
            // Create a GraphicsPath object.
            GraphicsPath myPath = new GraphicsPath();
            // Set up all the string parameters.
            string stringText = "Sample Text";
            FontFamily family = new FontFamily("Arial");
            int fontStyle = (int)FontStyle.Italic;
            int emSize = 26;
            Point origin = new Point(20, 20);
            StringFormat format = StringFormat.GenericDefault;
            // Add the string to the path.
            myPath.AddString(stringText,
              family,
              fontStyle,
              emSize,
              origin,
              format);
            //Draw the path to the screen.
            g.FillPath(Brushes.Black, myPath);
        }

    }
}
