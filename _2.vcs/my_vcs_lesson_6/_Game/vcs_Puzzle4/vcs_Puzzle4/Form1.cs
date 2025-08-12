using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Puzzle4
{
    public partial class Form1 : Form
    {
        Graphics g;
        //二維陣列
        int[,] puzzle_array = new int[8, 8];
        int W = 400;
        int H = 400;

        int w = 50;
        int h = 50;

        public Form1()
        {
            InitializeComponent();
        }

        void print_puzzle_array(int[,] puzzle_array)
        {
            int i;
            int j;
            for (j = 0; j < 8; j++)
            {
                for (i = 0; i < 8; i++)
                {
                    richTextBox1.Text += puzzle_array[i, j] + " ";
                }
                richTextBox1.Text += "\n";
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            int i;
            int j;
            for (j = 0; j < 8; j++)
            {
                for (i = 0; i < 8; i++)
                {
                    puzzle_array[i, j] = 0;
                }
            }
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 140;
            dy = 70;

            //button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 5-50, y_st + dy * 0);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Size = new Size(W, H);

            richTextBox1.Size = new Size(200, 900);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(800, 600);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void drawBox(int i, int j, int w, int h, Color c)
        {
            Font f;
            SolidBrush sb = new SolidBrush(c);
            g.FillRectangle(sb, w * i, h * j, w - 1, h - 1);

            //sb = new SolidBrush(Color.Black);
            sb = new SolidBrush(Color.FromArgb(255 - c.R, 255 - c.G, 255 - c.B));

            f = new Font("標楷體", 12);
            g.DrawString(c.Name, f, sb, new PointF(w * i, h * j + h / 3));
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            //richTextBox1.Text += "取得 : (" + e.X.ToString() +", "+ e.Y.ToString() + ")\n";
            int x = e.X / w;
            int y = e.Y / h;

            if (puzzle_array[x, y] == 0)
                puzzle_array[x, y] = 1;
            else
                puzzle_array[x, y] = 0;

            this.pictureBox1.Invalidate();
        }

        private void pictureBox1_MouseMove(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_MouseUp(object sender, MouseEventArgs e)
        {

        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            int i;
            int j;

            //畫垂直線
            for (i = 0; i < W; i += w)
            {
                e.Graphics.DrawLine(Pens.Red, i, 0, i, H);
            }

            //畫水平線
            for (j = 0; j < H; j += h)
            {
                e.Graphics.DrawLine(Pens.Green, 0, j, W, j);
            }

            Color c = Color.Black;

            for (j = 0; j < 8; j++)
            {
                for (i = 0; i < 8; i++)
                {
                    if (puzzle_array[i, j] == 0)
                    {
                        c = Color.Black;
                    }
                    else
                    {
                        c = Color.White;
                    }
                    //drawBox(i, j, w, h, c);
                    SolidBrush sb = new SolidBrush(c);
                    e.Graphics.FillRectangle(sb, w * i, h * j, w - 1, h - 1);
                }
            }

            /*
            foreach (int argb in Properties.Settings.Default.Argbs)
            {
                Color color = Color.FromArgb(argb);
                richTextBox1.Text += "get color " + color.ToString() + "\n";
                using (SolidBrush br = new SolidBrush(color))
                {
                    e.Graphics.FillRectangle(br, x, y,
                        PatchWidth, PatchHeight);
                }
                x += PatchWidth + PatchMargin;
                if (x > max_x)
                {
                    x = 0;
                    y += PatchHeight + PatchMargin;
                }
            }
            */

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            print_puzzle_array(puzzle_array);
        }
    }
}
