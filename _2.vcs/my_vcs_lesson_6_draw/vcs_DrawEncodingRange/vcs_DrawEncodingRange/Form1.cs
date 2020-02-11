using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DrawEncodingRange
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void DrawXY()//画X轴Y轴
        {
            Graphics g = this.panel1.CreateGraphics();
            System.Drawing.Point px1 = new System.Drawing.Point(this.panel1.Width * 10 / 100, this.panel1.Height * 90 / 100);
            System.Drawing.Point px2 = new System.Drawing.Point(this.panel1.Width * 90 / 100, this.panel1.Height * 90 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), px1, px2);
            System.Drawing.Point py1 = new System.Drawing.Point(this.panel1.Width * 10 / 100, this.panel1.Height * 90 / 100);
            System.Drawing.Point py2 = new System.Drawing.Point(this.panel1.Width * 10 / 100, this.panel1.Height * 10 / 100);
            g.DrawLine(new Pen(Brushes.Black, 5), py1, py2);
            g.Dispose();
        }

        //畫各種編碼的區間
        private void button1_Click(object sender, EventArgs e)
        {
            int xx;
            int yy;
            int dd = 20;
            int allow = 0;

            richTextBox1.Text += "W = " + this.panel1.Width.ToString() + " H = " + this.panel1.Height.ToString() + "\n";

            Graphics g = panel1.CreateGraphics();
            g.Clear(Color.White);
            //DrawXY();

            Point[] pt1 = new Point[656];    //一維陣列內有360個Point
            yy = 200;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt1[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0xA1) && ((xx / 256) <= 0xE7)) && (((xx % 256) >= 0xA1) && ((xx % 256) <= 0xFE)))
                {
                    pt1[xx / 100].Y = yy - 100 + dd;
                    allow++;
                }
                else
                    //pt1[xx / 100].Y = 300 - 100;
                    pt1[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Red, 3), pt1);
            g.DrawString("GB2313", new Font("標楷體", 30), new SolidBrush(Color.Red), new PointF(20, yy - 80));
            richTextBox1.Text += "e1 allow = " + allow.ToString() + "\n";



            Point[] pt2 = new Point[656];    //一維陣列內有360個Point
            yy = 300;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt2[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0x81) && ((xx / 256) <= 0xFE)) && ((((xx % 256) >= 0x40) && ((xx % 256) <= 0x7E)) || (((xx % 256) >= 0x80) && ((xx % 256) <= 0xFE))))
                {
                    pt2[xx / 100].Y = yy - 100 + dd;
                    allow++;
                    //pt1[xx / 100].Y = 300 - 100;
                }
                else
                    //pt1[xx / 100].Y = 300 - 100;
                    pt2[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Green, 3), pt2);
            g.DrawString("GBK", new Font("標楷體", 30), new SolidBrush(Color.Green), new PointF(20, yy - 80));
            richTextBox1.Text += "e2 allow = " + allow.ToString() + "\n";

            Point[] pt3 = new Point[656];    //一維陣列內有360個Point
            yy = 400;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt3[xx / 100].X = xx / 100;
                if ((((xx / 256) >= 0x81) && ((xx / 256) <= 0xFE)) && ((((xx % 256) >= 0x40) && ((xx % 256) <= 0x7E)) || (((xx % 256) >= 0xA1) && ((xx % 256) <= 0xFE))))
                {
                    pt3[xx / 100].Y = yy - 100 + dd;
                    allow++;
                    //pt1[xx / 100].Y = 300 - 100;
                }
                else
                    //pt1[xx / 100].Y = 300 - 100;
                    pt3[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Blue, 3), pt3);
            g.DrawString("GB2313", new Font("Big5", 30), new SolidBrush(Color.Blue), new PointF(20, yy - 80));
            richTextBox1.Text += "e3 allow = " + allow.ToString() + "\n";


            Point[] pt4 = new Point[656];    //一維陣列內有360個Point
            yy = 500;
            allow = 0;
            for (xx = 0; xx <= 65535; xx++)
            {
                pt4[xx / 100].X = xx / 100;
                if ((xx > 0x4e00) && (xx < 0x9fbf))
                {
                    pt4[xx / 100].Y = yy - 100 + dd;
                    allow++;
                }
                else
                    pt4[xx / 100].Y = yy - dd;


            }
            g.DrawLines(new Pen(Brushes.Yellow, 3), pt4);
            g.DrawString("Unicode", new Font("標楷體", 30), new SolidBrush(Color.Yellow), new PointF(20, yy - 80));
            richTextBox1.Text += "e4 allow = " + allow.ToString() + "\n";


        }
    }
}
