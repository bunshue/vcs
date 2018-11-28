using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//using System.Net.NetworkInformation;
//using System.Net.Sockets;
//using System.Net;

using System.Runtime.InteropServices;   //for dll

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("wininet.dll", EntryPoint = "InternetGetConnectedState")]
        public extern static bool InternetGetConnectedState(out int conState, int reder);

        private void button1_Click(object sender, EventArgs e)
        {
            Point b = new Point(500, 200);
            Point a = new Point();
            a.X = 123;
            a.Y = 234;
            Graphics g;
            g = this.CreateGraphics();
            Pen p;
            p = new Pen(Color.Red, 10);

            Point c = new Point(124, 234);
            
            g.DrawLine(p, a, c);
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            this.Text = "當前滑鼠位置為(" + e.X + "，" + e.Y + ")";
        }

        public bool IsConnectedToInternet()
        {
            int Desc = 0;
            return InternetGetConnectedState(out  Desc, 0);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (IsConnectedToInternet())
                MessageBox.Show("網路OK", "AAAA");
            else
                MessageBox.Show("無網路", "BBBB");

        }

        private void button3_Click(object sender, EventArgs e)
        {
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

            Graphics g = this.CreateGraphics();
            Brush b1 = new SolidBrush(Color.Red);
            Brush b2 = new SolidBrush(Color.Green);
            Brush b3 = new SolidBrush(Color.Blue);
            Brush b4 = new SolidBrush(Color.Yellow);

            g.FillPie(b1, 100, 50, 250, 250, 0, angle1);
            g.FillPie(b2, 100, 50, 250, 250, angle1, angle2);
            g.FillPie(b3, 100, 50, 250, 250, angle1 + angle2, angle3);
            g.FillPie(b4, 100, 50, 250, 250, angle1 + angle2 + angle3, angle4);

            Brush b = new SolidBrush(Color.LimeGreen);
            Font f = new Font("標楷體", 20);
            g.DrawString("各種勢力分佈圖", f, b, 20, 20);

        }

        private void button4_Click(object sender, EventArgs e)
        {
            int intLocation, intHeight;//定义两个int型的变量intLocation、intHeight 
            intLocation = this.ClientRectangle.Location.Y;//为变量intLocation赋值
            intHeight = this.ClientRectangle.Height / 200;//为变量intHeight赋值

            Graphics g = this.CreateGraphics();

            for (int i = 255; i >= 0; i--)
            {
                Color color = new Color();
                color = Color.FromArgb(1, i, 100);
                SolidBrush SBrush = new SolidBrush(color);
                Pen p = new Pen(SBrush, 1);
                g.DrawLine(p, 400, 50 + i, 500, 50 + i);


            }

        }

        private void button5_Click(object sender, EventArgs e)
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
            Graphics g = this.CreateGraphics();
            Pen p = new Pen(Color.Red, 5);
            g.DrawCurve(p, aaa);



        }
    }
}
