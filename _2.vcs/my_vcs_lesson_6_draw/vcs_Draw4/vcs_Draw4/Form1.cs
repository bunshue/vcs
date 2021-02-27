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
            p = new Pen(Color.Red, 10);     // 設定畫筆為藍色、粗細為 10 點。
            sb = new SolidBrush(Color.Blue);
            f = new Font("標楷體", 16);

            g.Clear(Color.Red);             //useless??
            pictureBox1.BackColor = Color.Pink;
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

        private void button13_Click(object sender, EventArgs e)
        {
            p = new Pen(Color.Red, 5);
            g.DrawEllipse(p, 100, 100, 300, 200);

            p = new Pen(Color.Blue, 10);
            p.EndCap = System.Drawing.Drawing2D.LineCap.ArrowAnchor;
            g.DrawArc(p, 100, 100, 300, 200, 0, 135);

            g.DrawArc(p, 300, 300, 100, 100, 0, -135);

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

        int flag_mouse_down = 0;    //給erase用
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
