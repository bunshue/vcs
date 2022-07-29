using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RandomWalk
{
    public partial class Form1 : Form
    {
        private List<Point> Points = new List<Point>();
        int dd = 50;
        int pos_x = 0;
        int pos_y = 0;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (timer1.Enabled == false)
            {
                Points.Clear();
                Points.Add(new Point(6 * dd, 6 * dd));
                pos_x = 6;
                pos_y = 6;

                timer1.Enabled = true;
            }
            else
            {
                timer1.Enabled = false;

            }


        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            int x_max = W / dd;
            int y_max = H / dd;

            Random r = new Random();

            int sel = r.Next(4);
            if (sel == 0)
            {
                pos_y -= 1; //向上
            }
            else if (sel == 1)
            {
                pos_x += 1; //向右
            }
            else if (sel == 2)
            {
                pos_y += 1; //向下
            }
            else if (sel == 3)
            {
                pos_x -= 1; //向左
            }
            else
            {
                richTextBox1.Text += "XXXXXXX ";    //錯誤
            }

            Points.Add(new Point(pos_x * dd, pos_y * dd));

            pictureBox1.Invalidate();


            if ((pos_x <= 0) || (pos_x >= x_max) || (pos_y <= 0) || (pos_y >= y_max))
            {
                timer1.Enabled = false;
                richTextBox1.Text += "結束~~~~~~\n";

            }
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int len = Points.Count;

            if (len <= 0)
                return;

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int i;
            for (i = 0; i < W; i += dd)
            {
                e.Graphics.DrawLine(Pens.Gray, i, 0, i, H);
            }
            for (i = 0; i < H; i += dd)
            {
                e.Graphics.DrawLine(Pens.Gray, 0, i, W, i);

            }

            if (len < 2)
                return;

            //richTextBox1.Text += "A";
            e.Graphics.DrawLines(new Pen(Color.Lime, 8), Points.ToArray());
            e.Graphics.DrawLine(new Pen(Color.Red, 5), Points[Points.Count - 2], Points[Points.Count - 1]);

        }
    }
}
