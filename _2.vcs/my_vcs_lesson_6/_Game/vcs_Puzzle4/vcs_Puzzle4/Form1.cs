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
            dx = 200 + 5;
            dy = 60 + 5;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button5.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 10);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Size = new Size(W, H);

            int pbx_w = 320;
            int pbx_h = 320;
            pictureBox4.Size = new Size(pbx_w, pbx_h);
            pictureBox4.Location = new Point(x_st + dx * 2, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 385);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(950, 770);
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

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            print_puzzle_array(puzzle_array);
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }


        byte[] EmptyFont = {
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
};
        byte[] Walking0 = {
0x0c,0x00,0x1e,0x00,0x0c,0x00,0x06,0x00,0x07,0xc0,0x07,0x20,0x0b,0x10,0x11,0x80,
0x01,0x80,0x01,0x40,0x02,0x20,0x04,0x10,0x1c,0x08,0x00,0x08,0x00,0x00,0x00,0x00,
};
        byte[] Walking1 = {
0x0c,0x00,0x1e,0x00,0x0c,0x00,0x06,0x00,0x07,0xc0,0x07,0x20,0x0b,0x10,0x11,0x80,
0x01,0x80,0x01,0x40,0x01,0x30,0x02,0x08,0x04,0x08,0x38,0x08,0x00,0x10,0x00,0x00,
};
        byte[] Walking2 = {
0x0c,0x00,0x1e,0x00,0x0c,0x00,0x06,0x00,0x03,0x80,0x03,0x40,0x07,0x20,0x09,0xa0,
0x01,0x80,0x01,0x40,0x01,0x40,0x02,0x20,0x02,0x10,0x0e,0x30,0x00,0x00,0x00,0x00,
};
        byte[] Walking3 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x03,0x00,0x03,0x80,0x03,0x40,0x01,0xa0,0x01,0xa0,
0x02,0xc0,0x01,0xc0,0x02,0x40,0x04,0x30,0x03,0x08,0x01,0x08,0x07,0x00,0x00,0x00,
};
        byte[] Walking4 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x03,0x00,0x03,0x80,0x03,0x40,0x01,0xa0,0x01,0xa0,
0x02,0xc0,0x01,0xc0,0x02,0x40,0x02,0x20,0x01,0x90,0x00,0xb0,0x03,0x80,0x00,0x00,
};
        byte[] Walking5 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x02,0x00,0x03,0x00,0x03,0x80,0x01,0xc0,0x01,0xc0,
0x00,0xc0,0x00,0xc0,0x01,0x60,0x00,0xa0,0x00,0xe0,0x00,0x20,0x00,0xe0,0x00,0x00,
};
        byte[] Walking6 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x03,0x00,0x03,0x80,0x01,0x40,0x03,0xa0,0x03,0xa0,
0x00,0xc0,0x00,0xc0,0x01,0x80,0x02,0x40,0x01,0x30,0x03,0x08,0x00,0x38,0x00,0x00,
};

        private void button4_Click(object sender, EventArgs e)
        {
            //測試小綠人
            int W = 320;
            int H = 320;
            int w = 20;
            int h = 20;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.LightGray);

            //測試小綠人
            byte[] man = Walking0;
            int len = man.Length;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            int yy;
            for (yy = 0; yy < len / 2; yy++)
            {
                //richTextBox1.Text += "第 " + yy.ToString() + " 行\t" + man[yy * 2].ToString("X2") + " " + man[yy * 2 + 1].ToString("X2") + "\n";
                int aa = man[yy * 2] * 256 + man[yy * 2 + 1];
                for (int xx = 0; xx < 16; xx++)
                {
                    if (((aa >> (15 - xx)) & 0x01) == 0x01)
                    {
                        g.FillEllipse(new SolidBrush(Color.Lime), w * xx, h * yy, w, h);
                        //g.FillRectangle(new SolidBrush(Color.Red), w * xx, h * yy, w, h);
                    }
                    else
                    {
                        g.FillEllipse(new SolidBrush(Color.White), w * xx, h * yy, w, h);
                        //g.FillRectangle(new SolidBrush(Color.White), w * xx, h * yy, w, h);
                    }
                }
            }
            pictureBox4.Image = bitmap1;
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
    }
}
