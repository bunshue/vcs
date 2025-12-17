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
        int[,] puzzle_array;//二維陣列
        int pbx_W = 800;
        int pbx_H = 480;
        int box_w = 100;
        int box_h = 100;
        int M = 8;
        int N = 3;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            puzzle_array = new int[N, M];

            int i;
            int j;
            for (j = 0; j < N; j++)
            {
                for (i = 0; i < M; i++)
                {
                    puzzle_array[j, i] = 0;
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

            label0.Location = new Point(x_st + dx * 0, y_st + dy * 7 + 60);
            tb_num_m.Location = new Point(x_st + dx * 0 + 50, y_st + dy * 7 + 60);
            label1.Location = new Point(x_st + dx * 0 + 140, y_st + dy * 7 + 60);
            tb_num_n.Location = new Point(x_st + dx * 0 + 140 + 50, y_st + dy * 7 + 60);
            tb_num_m.Text = M.ToString();
            tb_num_n.Text = N.ToString();
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 7 + 100);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 8 + 100);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 9 + 100);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 10 + 100);
            button4.Location = new Point(x_st + dx * 1, y_st + dy * 7 + 100);
            button5.Location = new Point(x_st + dx * 1, y_st + dy * 8 + 100);
            button6.Location = new Point(x_st + dx * 1, y_st + dy * 9 + 100);
            button7.Location = new Point(x_st + dx * 1, y_st + dy * 10 + 100);

            pictureBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            pictureBox1.Size = new Size(pbx_W, pbx_H);
            pictureBox1.BackColor = Color.Pink;

            int pbx_w = 320;
            int pbx_h = 320;
            pictureBox4.Size = new Size(pbx_w, pbx_h);
            pictureBox4.Location = new Point(x_st + dx * 4, y_st + dy * 0);

            richTextBox1.Size = new Size(500, 385);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1370, 880);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void print_puzzle_array(int[,] puzzle_array)
        {
            int i;
            int j;
            richTextBox1.Text += "aaaaaaa = {\n";
            for (j = 0; j < N; j++)
            {
                richTextBox1.Text += "{ ";
                for (i = 0; i < M; i++)
                {
                    if (i == (M - 1))
                        richTextBox1.Text += puzzle_array[j, i];
                    else
                        richTextBox1.Text += puzzle_array[j, i] + ", ";
                }
                richTextBox1.Text += "},\n";
            }
            richTextBox1.Text += "};\n";
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
            int W = box_w * M;
            int H = box_h * N;
            if (e.X >= W)
                return;
            if (e.Y >= H)
                return;

            int x = e.X / box_w;
            int y = e.Y / box_h;

            if (puzzle_array[y, x] == 0)
            {
                puzzle_array[y, x] = 1;
            }
            else
            {
                puzzle_array[y, x] = 0;
            }
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
            int W = box_w * M;
            int H = box_h * N;
            int i;
            int j;

            //畫垂直線
            for (i = 0; i < W; i += box_w)
            {
                e.Graphics.DrawLine(Pens.Red, i, 0, i, H);
            }

            //畫水平線
            for (j = 0; j < H; j += box_h)
            {
                e.Graphics.DrawLine(Pens.Green, 0, j, W, j);
            }

            Color c = Color.Black;

            for (j = 0; j < N; j++)
            {
                for (i = 0; i < M; i++)
                {
                    if (puzzle_array[j, i] == 0)
                    {
                        c = Color.Black;
                    }
                    else
                    {
                        c = Color.White;
                    }
                    //drawBox(i, j, w, h, c);
                    SolidBrush sb = new SolidBrush(c);
                    e.Graphics.FillRectangle(sb, box_w * i, box_h * j, box_w - 1, box_h - 1);
                }
            }

            //Pen p = new Pen(Color.Red, 20);
            //e.Graphics.DrawRectangle(p, 0, 0, W, H);

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
            int m = 0;
            bool conversionSuccessful = int.TryParse(tb_num_m.Text, out m);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "M = " + m.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
                richTextBox1.Text += "取得M失敗\n";
            }
            int n = 0;
            conversionSuccessful = int.TryParse(tb_num_n.Text, out n);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "N = " + n.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "int.TryParse 失敗\n";
                richTextBox1.Text += "取得N失敗\n";
            }

            if ((m <= 0) || (n <= 0))
            {
                richTextBox1.Text += "M = " + m.ToString() + ", N = " + n.ToString() + "\n";
                richTextBox1.Text += "M  或  N 不合法\n";
            }

            M = m;
            N = n;

            int ww = 5 * (pbx_W / M / 5);
            int hh = 5 * (pbx_H / N / 5);
            box_w = Math.Min(ww, hh);
            box_h = Math.Min(ww, hh);

            puzzle_array = new int[N, M];

            int i;
            int j;
            for (j = 0; j < N; j++)
            {
                for (i = 0; i < M; i++)
                {
                    puzzle_array[j, i] = 0;
                }
            }

            //建立圖片框陣列
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
            pictureBox1.Invalidate();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //刪除圖片框陣列
            pictureBox1.MouseDown -= new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove -= new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp -= new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint -= new PaintEventHandler(pictureBox1_Paint);
            pictureBox1.Invalidate();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //匯入陣列
            M = 16;
            N = 16;
            int ww = 5 * (pbx_W / M / 5);
            int hh = 5 * (pbx_H / N / 5);
            box_w = Math.Min(ww, hh);
            box_h = Math.Min(ww, hh);

            puzzle_array = new int[N, M];
            /*
            puzzle_array = new int[,] {
            { 0, 1, 0, 1, 0, 1, 0, 1 }, { 1, 0, 1, 0, 1, 0, 1, 0}, { 0, 1, 0, 1, 0, 1, 0, 1 }, { 1, 0, 1, 0, 1, 0, 1, 0 },
            { 0, 1, 0, 1, 0, 1, 0, 1 }, { 1, 0, 1, 0, 1, 0, 1, 0}, { 0, 1, 0, 1, 0, 1, 0, 1 }, { 1, 0, 1, 0, 1, 0, 1, 0 }
            };
            */

            puzzle_array = new int[,] {
            { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0 },
            { 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 },
            { 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 },
            { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 },
            };

            //建立圖片框陣列
            pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
            pictureBox1.MouseMove += new MouseEventHandler(pictureBox1_MouseMove);
            pictureBox1.MouseUp += new MouseEventHandler(pictureBox1_MouseUp);
            pictureBox1.Paint += new PaintEventHandler(pictureBox1_Paint);
            pictureBox1.Invalidate();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //匯出陣列
            print_puzzle_array(puzzle_array);
        }

        byte[] Step0 = {
0x0c,0x00,0x1e,0x00,0x0c,0x00,0x06,0x00,0x07,0xc0,0x07,0x20,0x0b,0x10,0x11,0x80,
0x01,0x80,0x01,0x40,0x02,0x20,0x04,0x10,0x1c,0x08,0x00,0x08,0x00,0x00,0x00,0x00,
};
        byte[] Step1 = {
0x0c,0x00,0x1e,0x00,0x0c,0x00,0x06,0x00,0x07,0xc0,0x07,0x20,0x0b,0x10,0x11,0x80,
0x01,0x80,0x01,0x40,0x01,0x30,0x02,0x08,0x04,0x08,0x38,0x08,0x00,0x10,0x00,0x00,
};
        byte[] Step2 = {
0x0c,0x00,0x1e,0x00,0x0c,0x00,0x06,0x00,0x03,0x80,0x03,0x40,0x07,0x20,0x09,0xa0,
0x01,0x80,0x01,0x40,0x01,0x40,0x02,0x20,0x02,0x10,0x0e,0x30,0x00,0x00,0x00,0x00,
};
        byte[] Step3 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x03,0x00,0x03,0x80,0x03,0x40,0x01,0xa0,0x01,0xa0,
0x02,0xc0,0x01,0xc0,0x02,0x40,0x04,0x30,0x03,0x08,0x01,0x08,0x07,0x00,0x00,0x00,
};
        byte[] Step4 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x03,0x00,0x03,0x80,0x03,0x40,0x01,0xa0,0x01,0xa0,
0x02,0xc0,0x01,0xc0,0x02,0x40,0x02,0x20,0x01,0x90,0x00,0xb0,0x03,0x80,0x00,0x00,
};
        byte[] Step5 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x02,0x00,0x03,0x00,0x03,0x80,0x01,0xc0,0x01,0xc0,
0x00,0xc0,0x00,0xc0,0x01,0x60,0x00,0xa0,0x00,0xe0,0x00,0x20,0x00,0xe0,0x00,0x00,
};
        byte[] Step6 = {
0x06,0x00,0x0f,0x00,0x06,0x00,0x03,0x00,0x03,0x80,0x01,0x40,0x03,0xa0,0x03,0xa0,
0x00,0xc0,0x00,0xc0,0x01,0x80,0x02,0x40,0x01,0x30,0x03,0x08,0x00,0x38,0x00,0x00,
};
        byte[] Step7 = {
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
};
        int step = 0;
        private void button4_Click(object sender, EventArgs e)
        {
            //測試小綠人1
            int W = 320;
            int H = 320;
            int w = 20;
            int h = 20;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);    //以記憶體圖像 bitmap1 建立 記憶體畫布g
            g.Clear(Color.LightGray);

            //測試小綠人
            byte[] man = Step0;

            if (step == 0)
            {
                richTextBox1.Text += "Step0\n";
                man = Step0;
            }
            else if (step == 1)
            {
                richTextBox1.Text += "Step1\n";
                man = Step1;
            }
            else if (step == 2)
            {
                richTextBox1.Text += "Step2\n";
                man = Step2;
            }
            else if (step == 3)
            {
                richTextBox1.Text += "Step3\n";
                man = Step3;
            }
            else if (step == 4)
            {
                richTextBox1.Text += "Step4\n";
                man = Step4;
            }
            else if (step == 5)
            {
                richTextBox1.Text += "Step5\n";
                man = Step5;
            }
            else if (step == 6)
            {
                richTextBox1.Text += "Step6\n";
                man = Step6;
            }
            else
            {
                richTextBox1.Text += "Step7\n";
                man = Step7;
            }
            step++;
            if (step > 7)
                step = 0;

            int len = man.Length;
            //richTextBox1.Text += "len = " + len.ToString() + "\n";

            int yy;
            for (yy = 0; yy < len / 2; yy++)
            {
                //richTextBox1.Text += "第 " + yy.ToString() + " 行\t" + man[yy * 2].ToString("X2") + " " + man[yy * 2 + 1].ToString("X2") + "\n";
                int aa = man[yy * 2] * 256 + man[yy * 2 + 1];
                richTextBox1.Text += "{ ";
                for (int xx = 0; xx < 16; xx++)
                {
                    if (((aa >> (15 - xx)) & 0x01) == 0x01)
                    {
                        g.FillEllipse(new SolidBrush(Color.Lime), w * xx, h * yy, w, h);
                        //g.FillRectangle(new SolidBrush(Color.Red), w * xx, h * yy, w, h);
                        if (xx == 15)
                            richTextBox1.Text += "1";
                        else
                            richTextBox1.Text += "1, ";
                    }
                    else
                    {
                        g.FillEllipse(new SolidBrush(Color.White), w * xx, h * yy, w, h);
                        //g.FillRectangle(new SolidBrush(Color.White), w * xx, h * yy, w, h);
                        richTextBox1.Text += "0, ";
                    }
                }
                richTextBox1.Text += "},\n";
            }
            pictureBox4.Image = bitmap1;
        }


        int[,] pattern0 = new int[,]
        {
        {0,1,1,0,0,0,0,0,0,0},
        {1,1,1,1,0,0,0,0,0,0},
        {0,1,1,0,0,0,0,0,0,0},
        {0,0,1,1,0,0,0,0,0,0},
        {0,0,1,1,1,1,0,0,0,0},
        {0,0,1,1,1,0,1,0,0,0},
        {0,1,0,1,1,0,1,0,0,0},
        {1,0,0,1,1,0,0,0,0,0},
        {0,0,0,1,1,1,0,0,0,0},
        {0,0,0,1,0,1,0,0,0,0},
        {0,0,1,0,0,0,1,1,0,0},
        {0,0,1,0,0,0,0,0,1,1},
        {0,0,1,0,0,0,0,0,0,1},
        {1,1,0,0,0,0,0,0,1,0}
        };

        int[,] pattern1 = new int[,]
        {
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,1,1},
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,0,0},
        {0,0,0,0,1,1,1,1,0,0},
        {0,0,0,1,0,1,1,1,0,0},
        {0,0,0,1,0,1,1,0,1,0},
        {0,0,0,0,0,1,1,0,0,1},
        {0,0,0,0,1,1,1,0,0,0},
        {0,0,0,0,1,0,1,0,0,0},
        {0,0,1,1,0,0,0,1,0,0},
        {1,1,0,0,0,0,0,1,0,0},
        {1,0,0,0,0,0,0,1,0,0},
        {0,1,0,0,0,0,0,0,1,1}
        };

        int[,] pattern2 = new int[,]
        {
        {0,1,1,0,0,0,0,0,0,0},
        {1,1,1,1,0,0,0,0,0,0},
        {0,1,1,0,0,0,0,0,0,0},
        {0,0,1,1,0,0,0,0,0,0},
        {0,0,1,1,1,1,0,0,0,0},
        {0,0,1,1,1,0,1,0,0,0},
        {0,1,0,1,1,0,1,0,0,0},
        {1,0,0,1,1,0,0,0,0,0},
        {0,0,0,1,1,1,0,0,0,0},
        {0,0,0,1,0,1,0,0,0,0},
        {0,0,1,0,0,0,1,1,0,0},
        {0,0,1,0,0,0,0,0,1,1},
        {0,0,1,0,0,0,0,0,0,1},
        {1,1,0,0,0,0,0,0,1,0}
        };

        int[,] pattern3 = new int[,]
        {
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,1,1},
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,0,0},
        {0,0,0,0,1,1,1,1,0,0},
        {0,0,0,1,0,1,1,1,0,0},
        {0,0,0,1,0,1,1,0,1,0},
        {0,0,0,0,0,1,1,0,0,1},
        {0,0,0,0,1,1,1,0,0,0},
        {0,0,0,0,1,0,1,0,0,0},
        {0,0,1,1,0,0,0,1,0,0},
        {1,1,0,0,0,0,0,1,0,0},
        {1,0,0,0,0,0,0,1,0,0},
        {0,1,0,0,0,0,0,0,1,1}
        };

        int[,] pattern4 = new int[,]
        {
        {0,1,1,0,0,0,0,0,0,0},
        {1,1,1,1,0,0,0,0,0,0},
        {0,1,1,0,0,0,0,0,0,0},
        {0,0,1,1,0,0,0,0,0,0},
        {0,0,1,1,1,1,0,0,0,0},
        {0,0,1,1,1,0,1,0,0,0},
        {0,1,0,1,1,0,1,0,0,0},
        {1,0,0,1,1,0,0,0,0,0},
        {0,0,0,1,1,1,0,0,0,0},
        {0,0,0,1,0,1,0,0,0,0},
        {0,0,1,0,0,0,1,1,0,0},
        {0,0,1,0,0,0,0,0,1,1},
        {0,0,1,0,0,0,0,0,0,1},
        {1,1,0,0,0,0,0,0,1,0}
        };

        int[,] pattern5 = new int[,]
        {
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,1,1},
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,0,0},
        {0,0,0,0,1,1,1,1,0,0},
        {0,0,0,1,0,1,1,1,0,0},
        {0,0,0,1,0,1,1,0,1,0},
        {0,0,0,0,0,1,1,0,0,1},
        {0,0,0,0,1,1,1,0,0,0},
        {0,0,0,0,1,0,1,0,0,0},
        {0,0,1,1,0,0,0,1,0,0},
        {1,1,0,0,0,0,0,1,0,0},
        {1,0,0,0,0,0,0,1,0,0},
        {0,1,0,0,0,0,0,0,1,1}
        };

        int[,] pattern6 = new int[,]
        {
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,1,1},
        {0,0,0,0,0,0,0,1,1,0},
        {0,0,0,0,0,0,1,1,0,0},
        {0,0,0,0,1,1,1,1,0,0},
        {0,0,0,1,0,1,1,1,0,0},
        {0,0,0,1,0,1,1,0,1,0},
        {0,0,0,0,0,1,1,0,0,1},
        {0,0,0,0,1,1,1,0,0,0},
        {0,0,0,0,1,0,1,0,0,0},
        {0,0,1,1,0,0,0,1,0,0},
        {1,1,0,0,0,0,0,1,0,0},
        {1,0,0,0,0,0,0,1,0,0},
        {0,1,0,0,0,0,0,0,1,1}
        };

        void draw_2d_pattern(int[,] pattern, int offset_x, int offset_y, int brick_size)
        {
            //richTextBox1.Text += "二維陣列內容\n";
            //PrintArray(pattern);

            int ROW = pattern.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = pattern.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int length = pattern.Length;//獲取整個二維陣列的長度，即所有元 的個數
            /*
            richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            richTextBox1.Text += "length = " + length.ToString() + "\n";
            */

            int x_st = 0;
            int y_st = 0;
            SolidBrush redBrush = new SolidBrush(Color.Red);
            SolidBrush blackBrush = new SolidBrush(Color.Black);

            for (int r = pattern.GetLowerBound(0); r <= pattern.GetUpperBound(0); r++)
            {
                for (int c = pattern.GetLowerBound(1); c <= pattern.GetUpperBound(1); c++)
                {
                    //richTextBox1.Text += pattern[r, c].ToString() + "\t";

                    //richTextBox1.Text += "(" + c.ToString() + ", " + r.ToString() + ")\t";
                    //g.DrawRectangle(Pens.Red, 100, 100, 200, 200);
                    x_st = offset_x + c * brick_size;
                    y_st = offset_y + r * brick_size;
                    if (pattern[r, c] == 1)
                    {
                        g.FillRectangle(redBrush, x_st, y_st, brick_size, brick_size);
                    }
                    else
                    {
                        g.FillRectangle(blackBrush, x_st, y_st, brick_size, brick_size);
                    }
                }
                //richTextBox1.Text += "\n";
            }
            //richTextBox1.Text += "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //測試小綠人2

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            Bitmap bitmap1 = new Bitmap(W, H);
            g = Graphics.FromImage(bitmap1);

            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            int x_st = 20;
            int y_st = 20;
            int dx = 170;
            int dy = 230;
            int brick_size = 15;
            draw_2d_pattern(pattern0, x_st + dx * 0, y_st + dy * 0, brick_size);
            draw_2d_pattern(pattern1, x_st + dx * 1, y_st + dy * 0, brick_size);
            draw_2d_pattern(pattern2, x_st + dx * 2, y_st + dy * 0, brick_size);
            draw_2d_pattern(pattern3, x_st + dx * 3, y_st + dy * 0, brick_size);
            draw_2d_pattern(pattern4, x_st + dx * 0, y_st + dy * 1, brick_size);
            draw_2d_pattern(pattern5, x_st + dx * 1, y_st + dy * 1, brick_size);
            draw_2d_pattern(pattern6, x_st + dx * 2, y_st + dy * 1, brick_size);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //測試數字 二維陣列

            int[,] num0 = new int[7, 3] {
            { 1, 1, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 1, 1 }
            };
            int[,] num1 = new int[7, 3] {
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 }
            };
            int[,] num2 = new int[7, 3] {
            { 1, 1, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 1, 1, 1 },
            { 1, 0, 0 },
            { 1, 0, 0 },
            { 1, 1, 1 }
            };
            int[,] num3 = new int[7, 3] {
            { 1, 1, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 1, 1, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 1, 1, 1 }
            };
            int[,] num4 = new int[7, 3] {
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 1, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 }
            };
            int[,] num5 = new int[7, 3] {
            { 1, 1, 1 },
            { 1, 0, 0 },
            { 1, 0, 0 },
            { 1, 1, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 1, 1, 1 }
            };
            int[,] num6 = new int[7, 3] {
            { 1, 1, 1 },
            { 1, 0, 0 },
            { 1, 0, 0 },
            { 1, 1, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 1, 1 }
            };
            int[,] num7 = new int[7, 3] {
            { 1, 1, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 }
            };
            int[,] num8 = new int[7, 3] {
            { 1, 1, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 1, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 1, 1 }
            };
            int[,] num9 = new int[7, 3] {
            { 1, 1, 1 },
            { 1, 0, 1 },
            { 1, 0, 1 },
            { 1, 1, 1 },
            { 0, 0, 1 },
            { 0, 0, 1 },
            { 1, 1, 1 }
            };






        }

        private void button7_Click(object sender, EventArgs e)
        {
            //測試2D陣列
            /*
            做一個 M X N 的二維陣列 column=8, row=3
            ROW	N
            COL	M
            [1 2 3 4 5 6 7 8]
            [1 2 3 4 5 6 7 8]
            [1 2 3 4 5 6 7 8]
            人 : 8 X 3陣列
            vcs要寫相反 puzzle_array(3, 8)
            */
            int[,] puzzle_array = new int[3, 8];    //Row = 3, Column = 8
            puzzle_array = new int[,] {
            {0, 1, 2, 3, 4, 5, 6, 7},
            {0, 1, 2, 3, 4, 5, 6, 7},
            {0, 1, 2, 3, 4, 5, 6, 7},
            };
            int ROW = puzzle_array.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = puzzle_array.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            int i;
            int j;
            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    //puzzle_array[j, i] = i * 10 + j;	//i j 相反
                    richTextBox1.Text += puzzle_array[j, i].ToString() + " ";
                }
                richTextBox1.Text += "\n";
            }
            richTextBox1.Text += "\n";
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




