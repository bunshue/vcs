using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Drawing.Imaging;   //for ImageFormat

namespace vcs_Draw3
{
    public partial class Form1 : Form
    {
        Graphics g;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;

        public Form1()
        {
            InitializeComponent();

            show_item_location();
            pictureBox1.SizeMode = PictureBoxSizeMode.AutoSize;
        }


        private void Form1_Load(object sender, EventArgs e)
        {
            g = panel1.CreateGraphics();
            p = new Pen(Color.Red, 10);     // 設定畫筆為紅色、粗細為 10 點。

            g.Clear(Color.Red);             //useless??
            panel1.BackColor = Color.Pink;

        }


        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 800;
            y_st = 10;
            dx = 120;
            dy = 50;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            button3.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            button6.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button8.Location = new Point(x_st + dx * 2, y_st + dy * 2);

            button9.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button11.Location = new Point(x_st + dx * 2, y_st + dy * 3);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button15.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 5);

            button18.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 6);

            button21.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 8);

            richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            richTextBox1.Size = new Size(richTextBox1.Size.Width, this.Height - richTextBox1.Location.Y - 50);

            pictureBox1.Location = new Point(10, 10);
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        private void button20_Click(object sender, EventArgs e)
        {

        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {

        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {

        }

        private void button26_Click(object sender, EventArgs e)
        {

        }


        double degree = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int r = 150;
            int x;
            int y;
            degree += 0.1;
            x = r + (int)(r * Math.Cos(degree * Math.PI / 180));
            y = r + (int)(r * Math.Sin(degree * Math.PI / 180));

            g.Clear(Color.Pink);

            Point point1a = new Point(r, r);
            Point point2a = new Point(x, y);
            g.DrawLine(p, point1a, point2a);     // Draw line to screen.


        }

        int cnt = 0;
        private void timer2_Tick(object sender, EventArgs e)
        {
            cnt++;

            if ((cnt % 4) == 0)
            {
                p0.BackColor = Color.Blue;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 1)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Blue;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 2)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Blue;
                p3.BackColor = Color.Gray;
            }
            else if ((cnt % 4) == 3)
            {
                p0.BackColor = Color.Gray;
                p1.BackColor = Color.Gray;
                p2.BackColor = Color.Gray;
                p3.BackColor = Color.Blue;
            }
        }





    }
}
