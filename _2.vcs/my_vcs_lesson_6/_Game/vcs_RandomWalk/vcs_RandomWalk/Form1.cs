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
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        int sel = 0;
        int sel_old = -1;
        private void timer1_Tick(object sender, EventArgs e)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;

            int x_max = W / dd;
            int y_max = H / dd;

            while (true)
            {
                Random r = new Random();
                sel = r.Next(4);
                //sel = GetNextStep();
                richTextBox1.Text += sel.ToString() + " ";

                if (sel_old == 0)
                {
                    if (sel == 2)
                    {
                        continue;
                    }
                }
                else if (sel_old == 1)
                {
                    if (sel == 3)
                    {
                        continue;
                    }
                }
                else if (sel_old == 2)
                {
                    if (sel == 0)
                    {
                        continue;
                    }
                }
                else if (sel_old == 3)
                {
                    if (sel == 1)
                    {
                        continue;
                    }
                }

                if (sel_old == 0)
                {
                    if (sel == 0)
                    {
                        continue;
                    }
                }
                else if (sel_old == 1)
                {
                    if (sel == 1)
                    {
                        continue;
                    }
                }
                else if (sel_old == 2)
                {
                    if (sel == 2)
                    {
                        continue;
                    }
                }
                else if (sel_old == 3)
                {
                    if (sel == 3)
                    {
                        continue;
                    }
                }

                sel_old = sel;

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
                break;
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


            int nx = 12;
            int ny = 12;
            int border = 0;
            int dx = (W - border * 2) / nx;
            int dy = (H - border * 2) / ny;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p1 = new Pen(Color.Gray, 5);
            Pen p2 = new Pen(Color.Red, 1);

            e.Graphics.DrawRectangle(p2, 0, 0, W - 1, H - 1);

            int i;
            for (i = 0; i <= ny; i++)
            {
                e.Graphics.DrawLine(p1, border + 0, border + dy * i, W - border, border + dy * i);
            }

            for (i = 0; i <= ny; i++)
            {
                e.Graphics.DrawLine(p1, border + dx * i, border, border + dx * i, H - border);
            }

            /*
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            Pen p1 = new Pen(Color.Gray, 5);
            Pen p2 = new Pen(Color.Red, 1);

            e.Graphics.DrawRectangle(p2, 0, 0, W - 1, H - 1);

            int i;
            for (i = 0; i < W; i += dd)
            {
                e.Graphics.DrawLine(p1, i, 0, i, H);
            }
            for (i = 0; i < H; i += dd)
            {
                e.Graphics.DrawLine(p1, 0, i, W, i);

            }
            */


            if (len < 2)
                return;

            //richTextBox1.Text += "A";
            e.Graphics.DrawLines(new Pen(Color.Lime, 8), Points.ToArray());
            e.Graphics.DrawLine(new Pen(Color.Red, 5), Points[Points.Count - 2], Points[Points.Count - 1]);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (timer2.Enabled == false)
            {
                timer2.Enabled = true;
            }
            else
            {
                timer2.Enabled = false;

            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            Random r = new Random();
            sel = r.Next(4);
            richTextBox1.Text += sel.ToString() + " ";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得亂數的方法
            int[] rs = new int[1000];

            for (int i = 0; i < 1000; i++)
                rs[i] = GetNextStep();

            richTextBox1.Text += "方法二, 取得亂數 : ";
            for (int i = 0; i < 1000; i++)
            {
                richTextBox1.Text += rs[i].ToString() + " ";

            }
            richTextBox1.Text += "\t可取得亂數\n";
        }

        //定義一個自增的數字作為種子
        private static int _RandomSeed = (int)DateTime.Now.Ticks;
        private int GetNextStep()
        {
            if (_RandomSeed == int.MaxValue)
            {
                _RandomSeed = 1;
            }

            Random r = new Random(_RandomSeed++);
            return r.Next(0, 4);
        }
    }
}

