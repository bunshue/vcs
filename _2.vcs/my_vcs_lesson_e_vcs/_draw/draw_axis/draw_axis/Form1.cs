using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;
using System.Drawing.Drawing2D;

//C# 使用GDI畫坐標圖(支持負值)

namespace draw_axis
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        Point getNewPoint(Point p, Point pZero, int bx, int by)
        {
            Point myp = new Point();
            myp.X = pZero.X + p.X / bx;
            if (p.Y > 0)
                myp.Y = pZero.Y - Math.Abs(p.Y / by);
            else
                myp.Y = pZero.Y + Math.Abs(p.Y / by);
            return myp;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap = new Bitmap(this.Width, this.Height, PixelFormat.Format24bppRgb);
            Graphics g = Graphics.FromImage(bitmap);
            //Graphics g = this.CreateGraphics();
            g.Clear(Color.White);
            Font font = new Font(Font.Name, 11);
            SolidBrush brush = new SolidBrush(Color.Black);
            Pen pen = new Pen(Color.Black);
            pen.EndCap = LineCap.ArrowAnchor;
            pen.DashStyle = DashStyle.Solid;
            //坐标轴
            Point pCenter = new Point(300, 260);
            g.DrawLine(pen, new Point(pCenter.X - 200, pCenter.Y), new Point(pCenter.X + 200, pCenter.Y));//x
            g.DrawLine(pen, new Point(pCenter.X, pCenter.Y + 200), new Point(pCenter.X, pCenter.Y - 200));//y            
            //轴标格
            int iX = 30;
            for (int i = 0; i < 5; i++)
            {
                //零點向左
                g.DrawLine(Pens.Black, new Point(pCenter.X - iX * i, pCenter.Y), new Point(pCenter.X - iX * i, pCenter.Y - 4));//x
                g.DrawString((-i).ToString(), font, brush, new PointF(pCenter.X - iX * i, pCenter.Y));

                //零點向右
                g.DrawLine(Pens.Black, new Point(pCenter.X + iX * i, pCenter.Y), new Point(pCenter.X + iX * i, pCenter.Y - 4));//x
                g.DrawString(i.ToString(), font, brush, new PointF(pCenter.X + iX * i, pCenter.Y));

                //零點向上
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y - iX * i), new Point(pCenter.X + 4, pCenter.Y - iX * i));//y
                g.DrawString(i.ToString(), font, brush, new PointF(pCenter.X, pCenter.Y - iX * i));

                //零點向下
                g.DrawLine(Pens.Black, new Point(pCenter.X, pCenter.Y + iX * i), new Point(pCenter.X + 4, pCenter.Y + iX * i));//y
                g.DrawString((-i).ToString(), font, brush, new PointF(pCenter.X, pCenter.Y + iX * i));
            }

            StringFormat sf = new StringFormat();
            sf.Alignment = StringAlignment.Far;
            g.DrawString("x", font, brush, new PointF(pCenter.X + 200, pCenter.Y));
            g.DrawString("y", font, brush, new PointF(pCenter.X, pCenter.Y - 200));
            g.DrawString("0", font, brush, new PointF(pCenter.X, pCenter.Y));
            //定义比例尺
            int BX = 4;
            int BY = 4;
            Point new1 = getNewPoint(new Point(200, 300), pCenter, BX, BY);
            Point new2 = getNewPoint(new Point(-300, 400), pCenter, BX, BY);
            Point new3 = getNewPoint(new Point(-400, -500), pCenter, BX, BY);
            Point new4 = getNewPoint(new Point(500, -300), pCenter, BX, BY);
            //g.DrawLine(Pens.Black, pCenter, new1);
            g.DrawArc(Pens.Black, new1.X, new1.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p1", font, brush, new PointF(new1.X, new1.Y));
            g.DrawArc(Pens.Black, new2.X, new2.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p2", font, brush, new PointF(new2.X, new2.Y));
            g.DrawArc(Pens.Black, new3.X, new3.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p3", font, brush, new PointF(new3.X, new3.Y));
            g.DrawArc(Pens.Black, new4.X, new4.Y, 1, 1, 45.0F, 360.0F);
            g.DrawString("p4", font, brush, new PointF(new4.X, new4.Y));
            g.DrawLine(Pens.Black, new1, new2);
            g.DrawLine(Pens.Black, new2, new3);
            g.DrawLine(Pens.Black, new3, new4);
            g.DrawLine(Pens.Black, new4, new1);
            //bitmap.Save("c:\\aaa.bmp");
            g.Dispose();

            pictureBox1.Image = bitmap;
        }


    }
}
