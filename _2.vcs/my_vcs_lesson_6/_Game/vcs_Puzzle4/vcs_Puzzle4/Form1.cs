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
        int[,] puzzle_array;//二維陣列
        int pbx_W = 1200;
        int pbx_H = 500;
        int box_w = 100;
        int box_h = 100;
        int M = 8;
        int N = 3;
        int i;
        int j;
        int step = 0;
        bool flag_create_picture_array = false;
        SolidBrush whiteBrush = new SolidBrush(Color.White);
        SolidBrush blackBrush = new SolidBrush(Color.Black);
        SolidBrush greenBrush = new SolidBrush(Color.Lime);
        SolidBrush pale_blackBrush = new SolidBrush(Color.FromArgb(41, 47, 43));
        SolidBrush pale_greenBrush = new SolidBrush(Color.FromArgb(90, 230, 134));
        Color dark_black = Color.FromArgb(36, 38, 35);

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            puzzle_array = new int[N, M];

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

            richTextBox1.Size = new Size(790, 295);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 7 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1250, 880);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void print_puzzle_array(int[,] array2d)
        {
            richTextBox1.Text += "aaaaaaa = {\n";
            for (j = 0; j < N; j++)
            {
                richTextBox1.Text += "{ ";
                for (i = 0; i < M; i++)
                {
                    if (i == (M - 1))
                        richTextBox1.Text += array2d[j, i];
                    else
                        richTextBox1.Text += array2d[j, i] + ", ";
                }
                richTextBox1.Text += "},\n";
            }
            richTextBox1.Text += "};\n";
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

            e.Graphics.Clear(Color.LightGray);

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

            for (j = 0; j < N; j++)
            {
                for (i = 0; i < M; i++)
                {
                    if (puzzle_array[j, i] == 0)
                    {
                        //e.Graphics.FillEllipse(blackBrush, box_w * i, box_h * j, box_w - 1, box_h - 1);
                        e.Graphics.FillRectangle(blackBrush, box_w * i, box_h * j, box_w - 1, box_h - 1);
                    }
                    else
                    {
                        //e.Graphics.FillEllipse(greenBrush, box_w * i, box_h * j, box_w - 1, box_h - 1);
                        e.Graphics.FillRectangle(whiteBrush, box_w * i, box_h * j, box_w - 1, box_h - 1);
                    }
                }
            }
        }

        private void button0_Click(object sender, EventArgs e)
        {
            if (flag_create_picture_array == true)
            {
                richTextBox1.Text += "已建立圖片框陣列，應先刪除\n";
                return;
            }

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
                return;
            }

            M = m;
            N = n;

            int ww = 5 * (pbx_W / M / 5);
            int hh = 5 * (pbx_H / N / 5);
            box_w = Math.Min(ww, hh);
            box_h = Math.Min(ww, hh);

            puzzle_array = new int[N, M];

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

            flag_create_picture_array = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_create_picture_array == true)
            {
                richTextBox1.Text += "刪除圖片框陣列\n";
                pictureBox1.MouseDown -= new MouseEventHandler(pictureBox1_MouseDown);
                pictureBox1.MouseMove -= new MouseEventHandler(pictureBox1_MouseMove);
                pictureBox1.MouseUp -= new MouseEventHandler(pictureBox1_MouseUp);
                pictureBox1.Paint -= new PaintEventHandler(pictureBox1_Paint);
                pictureBox1.Invalidate();
                flag_create_picture_array = false;
            }
            else
            {
                richTextBox1.Text += "無須 刪除圖片框陣列\n";
            }
            pictureBox1.Image = null;
        }

        private void button2_Click(object sender, EventArgs e)
        {
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //匯出陣列
            print_puzzle_array(puzzle_array);
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

        void draw_array2d(Graphics g, int[,] array2d, int x_st, int y_st, int box_w, int box_h)
        {
            int ROW = array2d.GetUpperBound(0) + 1;//獲取指定維度的上限，在 上一個1就是列數
            int COL = array2d.GetLength(1);//獲取指定維中的元 個數，這裡也就是列數了。（1表示的是第二維，0是第一維）
            //int length = array2d.Length;//獲取整個二維陣列的長度，即所有元 的個數
            //richTextBox1.Text += "ROW = " + ROW.ToString() + "\n";
            //richTextBox1.Text += "COL = " + COL.ToString() + "\n";
            //richTextBox1.Text += "length = " + length.ToString() + "\n";

            int W = box_w * COL;
            int H = box_h * ROW;

            //畫垂直線
            for (i = 0; i < W; i += box_w)
            {
                g.DrawLine(Pens.Red, x_st + i, y_st + 0, x_st + i, y_st + H);
            }

            //畫水平線
            for (j = 0; j < H; j += box_h)
            {
                g.DrawLine(Pens.Green, x_st + 0, y_st + j, x_st + W, y_st + j);
            }

            for (j = 0; j < ROW; j++)
            {
                for (i = 0; i < COL; i++)
                {
                    if (array2d[j, i] == 0)
                    {
                        g.FillRectangle(blackBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                        //g.FillEllipse(greenBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                    }
                    else
                    {
                        g.FillRectangle(whiteBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                        //g.FillEllipse(whiteBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                    }
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (flag_create_picture_array == true)
            {
                button1.PerformClick();
            }

            int[,] array2d;//二維陣列
            if (step == 0)
            {
                array2d = pattern0;
            }
            else if (step == 1)
            {
                array2d = pattern1;
            }
            else if (step == 2)
            {
                array2d = pattern2;
            }
            else if (step == 3)
            {
                array2d = pattern3;
            }
            else if (step == 4)
            {
                array2d = pattern4;
            }
            else if (step == 5)
            {
                array2d = pattern5;
            }
            else if (step == 6)
            {
                array2d = pattern6;
            }
            else
            {
                array2d = pattern0;
            }
            step++;
            if (step > 6)
                step = 0;

            //測試小綠人1
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.LightGray);
            pictureBox1.Image = bitmap1;

            int x_st = 200;
            int y_st = 10;
            box_w = 30;
            box_h = 30;
            draw_array2d(g, array2d, x_st, y_st, box_w, box_h);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (flag_create_picture_array == true)
            {
                button1.PerformClick();
            }

            int[,] array2d;//二維陣列
            if (step == 0)
            {
                array2d = greenman_step0;
            }
            else if (step == 1)
            {
                array2d = greenman_step1;
            }
            else if (step == 2)
            {
                array2d = greenman_step2;
            }
            else if (step == 3)
            {
                array2d = greenman_step3;
            }
            else if (step == 4)
            {
                array2d = greenman_step4;
            }
            else if (step == 5)
            {
                array2d = greenman_step5;
            }
            else if (step == 6)
            {
                array2d = greenman_step6;
            }
            else
            {
                array2d = greenman_step7;
            }
            step++;
            if (step > 7)
                step = 0;

            //測試小綠人2
            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;
            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.LightGray);
            pictureBox1.Image = bitmap1;

            int x_st = 200;
            int y_st = 10;
            box_w = 30;
            box_h = 30;
            draw_array2d(g, array2d, x_st, y_st, box_w, box_h);
        }

        int[,] comma = new int[7, 1] {
            { 0 },
            { 1 },
            { 0 },
            { 0 },
            { 0 },
            { 1 },
            { 0 }
            };

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

        void drawNumber(Graphics g, int num, int x_st, int y_st, int box_w, int box_h)
        {
            int M = 3;
            int N = 7;
            int W = box_w * M;
            int H = box_h * N;

            int[,] array2d = new int[N, M];//二維陣列

            if (num == 10)
            {
                M = 1;
            }

            if (num == 0)
            {
                array2d = num0;
            }
            else if (num == 1)
            {
                array2d = num1;
            }
            else if (num == 2)
            {
                array2d = num2;
            }
            else if (num == 3)
            {
                array2d = num3;
            }
            else if (num == 4)
            {
                array2d = num4;
            }
            else if (num == 5)
            {
                array2d = num5;
            }
            else if (num == 6)
            {
                array2d = num6;
            }
            else if (num == 7)
            {
                array2d = num7;
            }
            else if (num == 8)
            {
                array2d = num8;
            }
            else if (num == 9)
            {
                array2d = num9;
            }
            else if (num == 10)
            {
                array2d = comma;
            }
            else
            {
                array2d = num0;
            }

            for (j = 0; j < N; j++)
            {
                for (i = 0; i < M; i++)
                {
                    if (array2d[j, i] == 0)
                    {
                        //g.FillEllipse(pale_blackBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                        g.FillRectangle(pale_blackBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                    }
                    else
                    {
                        //g.FillEllipse(pale_greenBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                        g.FillRectangle(pale_greenBrush, x_st + box_w * i, y_st + box_h * j, box_w - 1, box_h - 1);
                    }
                }
            }

            //畫垂直線
            for (i = 0; i < W; i += box_w)
            {
                g.DrawLine(new Pen(dark_black, 4), x_st + i, y_st + 0, x_st + i, y_st + H);
            }

            //畫水平線
            for (j = 0; j < H; j += box_h)
            {
                g.DrawLine(new Pen(dark_black, 4), x_st + 0, y_st + j, x_st + W, y_st + j);
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (flag_create_picture_array == true)
            {
                button1.PerformClick();
            }

            //測試數字 二維陣列

            int W = pictureBox1.ClientSize.Width;
            int H = pictureBox1.ClientSize.Height;

            Bitmap bitmap1 = new Bitmap(W, H);
            Graphics g = Graphics.FromImage(bitmap1);
            g.Clear(Color.FromArgb(50, 50, 50));
            pictureBox1.Image = bitmap1;

            int x_st = 0;
            int y_st = 0;
            int num = 0;
            box_w = 42;
            box_h = 42;

            x_st = 0;
            y_st = 0;
            num = 1;
            drawNumber(g, num, x_st, y_st, box_w, box_h);

            x_st += box_w * 4;
            num = 2;
            drawNumber(g, num, x_st, y_st, box_w, box_h);

            x_st += box_w * 4;
            num = 10;
            drawNumber(g, num, x_st, y_st, box_w, box_h);

            x_st += box_w * 2;
            num = 3;
            drawNumber(g, num, x_st, y_st, box_w, box_h);

            x_st += box_w * 4;
            num = 4;
            drawNumber(g, num, x_st, y_st, box_w, box_h);

            x_st += box_w * 4;
            num = 10;
            drawNumber(g, num, x_st, y_st, box_w, box_h);

            x_st += box_w * 2;
            num = 5;
            drawNumber(g, num, x_st, y_st, box_w, box_h);

            x_st += box_w * 4;
            num = 6;
            drawNumber(g, num, x_st, y_st, box_w, box_h);
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        int[,] greenman_step0 = new int[,] {
        { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0},
        { 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
        { 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };

        int[,] greenman_step1 = new int[,] {
        { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0},
        { 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };

        int[,] greenman_step2 = new int[,] {
        { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };

        int[,] greenman_step3 = new int[,] {
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };

        int[,] greenman_step4 = new int[,] {
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };

        int[,] greenman_step5 = new int[,] {
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };

        int[,] greenman_step6 = new int[,] {
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };

        int[,] greenman_step7 = new int[,] {
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        };
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


