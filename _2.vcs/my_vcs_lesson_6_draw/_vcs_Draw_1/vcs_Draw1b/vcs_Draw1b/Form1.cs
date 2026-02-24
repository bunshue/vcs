using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Drawing2D;

namespace vcs_Draw1b
{
    public partial class Form1 : Form
    {
        private Pen myPen = new Pen(Color.Black, 1);
        private Graphics g;

        private double[] x = new double[10];
        private double[] y = new double[10];

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.BackColor = Color.White;
            g = this.CreateGraphics();
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            double x_center = 100;
            double y_center = 100;
            double radius = 100;

            for (int i = 0; i <= 9; i++)
            {
                x[i] = x_center + radius * Math.Sin(36 * i * Math.PI / 180.0);
                y[i] = y_center + radius * Math.Cos(36 * i * Math.PI / 180);
            }

            for (int i = 0; i <= 9; i++)
            {
                for (int j = 0; j <= 9; j++)
                {
                    g.DrawLine(myPen, (int)x[i], (int)y[i], (int)x[j], (int)y[j]);
                }
            }

            //------------------------------------------------------------  # 60個

            double xx;
            double yy;
            Point[] p = new Point[100];

            x_center = 300;
            y_center = 100;
            radius = 100;

            for (int i = 0; i <= 99; i++)
            {
                xx = x_center + radius * Math.Sin(36 * i * Math.PI / 180);
                yy = y_center + radius * Math.Cos(36 * i * Math.PI / 180);
                p[i] = new Point((int)xx, (int)yy);
                radius -= 1;
            }
            g.DrawLines(myPen, p);

            //------------------------------------------------------------  # 60個

            x_center = 80;
            y_center = 280;
            int hwidth = 50;
            int hheight = 40;
            for (int i = 0; i <= 20; i++)
            {
                g.DrawRectangle(myPen, (int)x_center - hwidth, (int)y_center - hheight, 2 * hwidth, 2 * hheight);
                x_center += 4;
                y_center += 4;
                hwidth += 2;
                hheight += 2;
            }

            //------------------------------------------------------------  # 60個

            x_center = 350;
            y_center = 200;
            hwidth = 50;
            Rectangle[] R = new Rectangle[25];
            for (int i = 0; i <= 24; i++)
            {
                R[i] = new Rectangle((int)x_center - hwidth, (int)y_center - hwidth, 2 * hwidth, 2 * hwidth);
                y_center += 4;
                hwidth += 2;
            }
            g.DrawRectangles(myPen, R);

            //------------------------------------------------------------  # 60個

            x_center = 500;
            y_center = 10;
            hwidth = 10;
            for (int i = 0; i <= 40; i++)
            {
                g.DrawEllipse(myPen, (int)x_center - hwidth, (int)y_center - hwidth, 2 * hwidth, 2 * hwidth);
                y_center += 4;
                hwidth += 2;
            }

            //------------------------------------------------------------  # 60個

            x_center = 650;
            y_center = 50;
            hwidth = 50;
            hheight = 40;
            for (int i = 0; i < +29; i++)
            {
                g.DrawArc(myPen, (int)x_center - hwidth, (int)y_center - hheight, 2 * hwidth, 2 * hheight, 0, -180);
                x_center += 4;
                y_center += 4;
                hwidth += 2;
                hheight += 2;
            }

            //------------------------------------------------------------  # 60個

            HatchBrush hatchBrush1;
            Single p1, p2, p3;

            p1 = 180;
            p2 = 125;
            p3 = 160;
            hatchBrush1 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.White, Color.Red);
            g.FillRectangle(hatchBrush1, 70, 250 - p1, 30, p1);
            hatchBrush1 = new HatchBrush(HatchStyle.DarkUpwardDiagonal, Color.White, Color.Blue);
            g.FillRectangle(hatchBrush1, 120, 250 - p2, 30, p2);
            hatchBrush1 = new HatchBrush(HatchStyle.DiagonalCross, Color.White, Color.Green);
            g.FillRectangle(hatchBrush1, 170, 250 - p3, 30, p3);
            g.DrawLine(new Pen(Color.Black, 2), new Point(10, 250), new Point(280, 250));

            //------------------------------------------------------------  # 60個

            HatchBrush hatchBrush2;
            Font myFont;
            hatchBrush2 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.Black, Color.Red);
            myFont = new Font("Arial", 25, FontStyle.Bold);
            g.DrawString("Visual Studio", myFont, hatchBrush2, new PointF(20, 10));
            hatchBrush2 = new HatchBrush(HatchStyle.DarkUpwardDiagonal, Color.Black, Color.Blue);
            myFont = new Font("Garamond", 16, FontStyle.Strikeout);
            g.DrawString("Visual Studio I love it.", myFont, hatchBrush2, new PointF(10, 60));
            hatchBrush2 = new HatchBrush(HatchStyle.DashedDownwardDiagonal, Color.Black, Color.Green);
            myFont = new Font("Broadway", 22, FontStyle.Underline);
            g.DrawString(".NET Framework", myFont, hatchBrush2, new PointF(30, 100));

            //------------------------------------------------------------  # 60個

            Rectangle R2;
            LinearGradientBrush lgb2;

            R2 = new Rectangle(20, 50, 80, 80);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);
            R2 = new Rectangle(120, 70, 50, 50);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);
            R2 = new Rectangle(190, 85, 30, 30);
            lgb2 = new LinearGradientBrush(R2, Color.Green, Color.Yellow, -45);
            g.FillPie(lgb2, R2, 30, 300);

            //------------------------------------------------------------  # 60個

            TextureBrush textureBrush1;
            Image img = Image.FromFile(@"../../006.jpg");
            //呼叫DrawImage()方法從表單左上角繪製圖片
            g.DrawImage(img, 0, 0);
            textureBrush1 = new TextureBrush(img, WrapMode.TileFlipXY);
            g.FillRectangle(textureBrush1, 0, 0, this.Size.Width, this.Size.Height);

            //------------------------------------------------------------  # 60個

            TextureBrush textureBrush2;
            Rectangle sR, dR;
            img = Image.FromFile(@"../../005.jpg");
            //呼叫DrawImage()方法從表單左上角繪製圖片
            g.DrawImage(img, 0, 0);
            sR = new Rectangle(400, 80, 400, 400);
            dR = new Rectangle(0, 0, this.Size.Width, this.Size.Height);
            textureBrush2 = new TextureBrush(img, WrapMode.TileFlipXY);
            g.DrawImage(img, dR, sR, GraphicsUnit.Pixel);

            //------------------------------------------------------------  # 60個

            img = Image.FromFile(@"../../007.jpg");
            //呼叫DrawImage()方法從表單左上角繪製圖片
            g.DrawImageUnscaled(img, 10, 10);
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



