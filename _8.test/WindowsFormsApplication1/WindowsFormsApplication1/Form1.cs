using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;


        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int r = 200;
            int x;
            int y;
            int degree;
            int i = 0;
            for(degree = 0; degree < 360; degree += 10)
            {
                i++;
                x = r + (int)(r * Math.Cos(degree * Math.PI / 180));
                y = r + (int)(r * Math.Sin(degree * Math.PI / 180));
                richTextBox1.Text += "x(" + i.ToString() + ")=" + x.ToString() + ";";
                richTextBox1.Text += "y(" + i.ToString() + ")=" + y.ToString() + ";\n";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int sec = DateTime.Now.Second;
            int ms = DateTime.Now.Millisecond;
            //richTextBox1.Text += "sec = " + sec.ToString() + ", ms = " + ms.ToString() + "\n";

            int r = 200;
            int x;
            int y;
            //int degree = (sec - 15) * 6;
            //int degree = ms % 360;  // (sec - 15) * 6;
            int degree = (sec * 1000 + ms) % 360;  // (sec - 15) * 6;
            int i = 0;
            //for (degree = 0; degree < 360; degree += 10)
            {
                i++;
                x = 250 + (int)(r * Math.Cos(degree * Math.PI / 180));
                y = 250 + (int)(r * Math.Sin(degree * Math.PI / 180));
                //richTextBox1.Text += "x(" + i.ToString() + ")=" + x.ToString() + ";";
                //richTextBox1.Text += "y(" + i.ToString() + ")=" + y.ToString() + ";\n";
            }

            g.Clear(Color.Pink);

            Point point1a = new Point(250, 250);
            Point point2a = new Point(x, y);
            g.DrawLine(p, point1a, point2a);     // Draw line to screen.

            //在指定位置畫上一圖
            // Create image.
            Image newImage = Image.FromFile(@"C:\______test_vcs\reuse.bmp");
            //Image newImage = Resource1.doraemon;

            // Create coordinates for upper-left corner of image.

            // Draw image to screen.
            g.DrawImage(newImage, x - newImage.Width / 2, y - newImage.Height / 2);

        
        
        
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int sec = DateTime.Now.Second;
            int ms = DateTime.Now.Millisecond;
            richTextBox1.Text += "sec = " + sec.ToString() + ", ms = " + ms.ToString() + "\n";

            int r = 200;
            int x;
            int y;
            int degree = sec * 6;
            int i = 0;
            //for (degree = 0; degree < 360; degree += 10)
            {
                i++;
                x = r + (int)(r * Math.Cos(degree * Math.PI / 180));
                y = r + (int)(r * Math.Sin(degree * Math.PI / 180));
                richTextBox1.Text += "x(" + i.ToString() + ")=" + x.ToString() + ";";
                richTextBox1.Text += "y(" + i.ToString() + ")=" + y.ToString() + ";\n";
            }

            Point point1a = new Point(200, 200);
            Point point2a = new Point(x, y);
            g.DrawLine(p, point1a, point2a);     // Draw line to screen.



        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            g = panel1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。

            g.Clear(Color.Red);             //useless??
            panel1.BackColor = Color.Pink;

        }

    }
}
