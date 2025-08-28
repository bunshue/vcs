using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_RandomWalk2
{
    public partial class Form1 : Form
    {
        private const int N = 4;
        private const int L = 100;

        int x = 0;
        int y = 0;
        int x_old = 0;
        int y_old = 0;

        int W = L * N;
        int H = L * N;
        List<Point> points = new List<Point>();
        int[] array_row = new int[N * (N + 1)];
        int[] array_col = new int[N * (N + 1)];
        int array_row_len = 0;
        int array_col_len = 0;
        int total_steps = 0;
        int offset_x = 10;
        int offset_y = 10;
        int direction = 0;  //0: 向右, 1: 向下, 2: 向左, 3: 向上, 
        int direction_old = 0;

        bool flag_game_end = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Size = new Size(L * N + 50, L * N + 50);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            init_mouse_setting();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void init_mouse_setting()
        {
            total_steps = 0;
            this.Text = total_steps.ToString();

            x = (N / 2) * L;
            y = (N / 2) * L;
            x_old = x;
            y_old = y;

            int i;
            array_row_len = array_row.Length;
            array_col_len = array_col.Length;

            for (i = 0; i < array_row_len; i++)
            {
                array_row[i] = 0;
            }
            for (i = 0; i < array_col_len; i++)
            {
                array_col[i] = 0;
            }

            points.Clear();
            points.Add(new Point(x + offset_x, y + offset_y));
            flag_game_end = false;
            //timer1.Enabled = true;
        }

        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            string filename = string.Empty;
            if (direction == 0)
            {
                filename = @"D:\_git\vcs\_2.vcs\______test_files1\__pic\_car\car_potato.right.jpg";
            }
            else if (direction == 1)
            {
                filename = @"D:\_git\vcs\_2.vcs\______test_files1\__pic\_car\car_potato.down.jpg";
            }
            else if (direction == 2)
            {
                filename = @"D:\_git\vcs\_2.vcs\______test_files1\__pic\_car\car_potato.left.jpg";
            }
            else if (direction == 3)
            {
                filename = @"D:\_git\vcs\_2.vcs\______test_files1\__pic\_car\car_potato.up.jpg";
            }
            else
            {
                filename = @"D:\_git\vcs\_2.vcs\______test_files1\__pic\_car\car_potato.right.jpg";
            }

            GraphicsUnit units = GraphicsUnit.Pixel;
            Bitmap bmp;

            bmp = new Bitmap(filename);

            Pen p;

            if (flag_game_end == false)
            {
                p = new Pen(Color.Green, 5);
            }
            else
            {
                p = new Pen(Color.Red, 5);
            }

            if (points.Count > 1)
            {
                e.Graphics.DrawLines(p, points.ToArray());
            }

            int r = 40;
            e.Graphics.FillEllipse(Brushes.Red, x - r / 2 + offset_x, y - r / 2 + offset_y, r, r);

            int mouse_size_width = 40;
            int mouse_size_height = 40;

            int ww = mouse_size_width;
            int hh = mouse_size_height;

            ww = hh * bmp.Width / bmp.Height;   //符合比例
            Rectangle destRect1 = new Rectangle(x - r / 2 + offset_x, y - r / 2 + offset_y, ww, hh);
            e.Graphics.DrawImage(bmp, destRect1, 0, 0, bmp.Width, bmp.Height, units);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            Random r = new Random();

            int result = r.Next(4);
            if (result == 0)
            {
                //向右
                richTextBox1.Text += "欲向右\t";
                x += L;
            }
            else if (result == 1)
            {
                //向下
                richTextBox1.Text += "欲向下\t";
                y += L;
            }
            else if (result == 2)
            {
                //向左
                richTextBox1.Text += "欲向左\t";
                x -= L;
            }
            else if (result == 3)
            {
                //向上
                richTextBox1.Text += "欲向上\t";
                y -= L;
            }
            else
            {
                richTextBox1.Text += "xxxxx\n";
            }
            if (x < 0)
                x = 0;
            if (y < 0)
                y = 0;
            if (x > W)
                x = W;
            if (y > H)
                y = H;

            //richTextBox1.Text += "\nx_old = " + x_old.ToString() + " y_old = " + y_old.ToString() + "\tx = " + x.ToString() + " y = " + y.ToString() + "\n";

            if ((x == x_old) && (y == y_old))
            {
                richTextBox1.Text += "未移動\n\n";

                timer1_Tick(sender, e);
            }
            else
            {
                int ix = 0;
                int iy = 0;
                int index = 0;
                ix = x_old / L;
                iy = y_old / L;

                bool flag_skip = false;
                if (x > x_old)  //向右
                {
                    ix = x_old / L;
                    index = ix + N * iy;
                    if (array_row[index] == 1)
                    {
                        richTextBox1.Text += "已走過 向右\n\n";
                        flag_skip = true;
                    }
                    else
                    {
                        richTextBox1.Text += "向右\n";
                        direction = 0;
                        total_steps++;
                        array_row[index] = 1;
                    }
                }
                else if (y > y_old)  //向下
                {
                    iy = y_old / L;
                    index = N * ix + iy;
                    if (array_col[index] == 1)
                    {
                        richTextBox1.Text += "已走過 向下\n\n";
                        flag_skip = true;
                    }
                    else
                    {
                        richTextBox1.Text += "向下\n";
                        direction = 1;
                        total_steps++;
                        array_col[index] = 1;
                    }
                }
                else if (x < x_old)  //向左
                {
                    ix = x / L;
                    index = ix + N * iy;
                    if (array_row[index] == 1)
                    {
                        richTextBox1.Text += "已走過 向左\n\n";
                        flag_skip = true;
                    }
                    else
                    {
                        richTextBox1.Text += "向左\n";
                        direction = 2;
                        total_steps++;
                        array_row[index] = 1;
                    }
                }
                else if (y < y_old)  //向上
                {
                    iy = y / L;
                    index = N * ix + iy;
                    if (array_col[index] == 1)
                    {
                        richTextBox1.Text += "已走過 向上\n\n";
                        flag_skip = true;
                    }
                    else
                    {
                        richTextBox1.Text += "向上\n";
                        direction = 3;
                        total_steps++;
                        array_col[index] = 1;
                    }
                }

                if (flag_skip == false)
                {
                    this.Text = total_steps.ToString();
                    x_old = x;
                    y_old = y;

                    richTextBox1.Text += "x = " + x.ToString() + ", y = " + y.ToString() + "\t" + "px = " + (x / L).ToString() + ", py = " + (y / L).ToString() + "\n";
                    points.Add(new Point(x + offset_x, y + offset_y));

                    result = check_available_movements();
                    if (result > 0)
                    {
                        richTextBox1.Text += "還有路可走\t" + result.ToString() + "\n\n";
                    }
                    else
                    {
                        richTextBox1.Text += "無路可走\n";
                        this.Text = "無路可走";
                        timer1.Enabled = false;
                        flag_game_end = true;
                    }
                    this.pictureBox1.Invalidate();
                }
                else
                {
                    x = x_old;
                    y = y_old;
                    timer1_Tick(sender, e);
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;

            int i;
            array_row_len = array_row.Length;
            array_col_len = array_col.Length;

            richTextBox1.Text += "row:\n";
            for (i = 0; i < array_row_len; i++)
            {
                richTextBox1.Text += array_row[i].ToString();
                if ((i % N) == (N - 1))
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "col:\n";
            for (i = 0; i < array_col_len; i++)
            {
                richTextBox1.Text += array_col[i].ToString() + " ";
                if ((i % N) == (N - 1))
                    richTextBox1.Text += "\n";
                else
                    richTextBox1.Text += " ";

            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "目前位置\tx = " + x.ToString() + ", y = " + y.ToString() + "\t" + "px = " + (x / L).ToString() + ", py = " + (y / L).ToString() + "\n";

            int result = check_available_movements();
            if (result > 0)
            {
                richTextBox1.Text += "還有路可走\t" + result.ToString() + "\n\n";
            }
            else
            {
                richTextBox1.Text += "無路可走\n";
                this.Text = "無路可走";
                timer1.Enabled = false;
                flag_game_end = true;
            }
        }

        int check_available_movements()
        {
            richTextBox1.Text += "目前位置\tx = " + x.ToString() + ", y = " + y.ToString() + "\t" + "px = " + (x / L).ToString() + ", py = " + (y / L).ToString() + "\n";

            int ix = 0;
            int iy = 0;
            int index = 0;
            ix = x / L;
            iy = y / L;

            int available_movements = 0;
            if ((x + L) <= W)
            {
                richTextBox1.Text += "可向右\t";
                ix = x / L;
                iy = y / L;
                index = ix + N * iy;
                if (array_row[index] == 1)
                {
                    richTextBox1.Text += "已走過 向右\n";
                }
                else
                {
                    richTextBox1.Text += "未走過 向右\n";
                    available_movements++;
                }
            }
            if ((y + L) <= H)
            {
                richTextBox1.Text += "可向下\t";
                ix = x / L;
                iy = y / L;
                index = N * ix + iy;
                if (array_col[index] == 1)
                {
                    richTextBox1.Text += "已走過 向下\n";
                }
                else
                {
                    richTextBox1.Text += "未走過 向下\n";
                    available_movements++;
                }
            }
            if ((x - L) >= 0)
            {
                richTextBox1.Text += "可向左\t";
                ix = (x - L) / L;
                iy = y / L;
                index = ix + N * iy;
                if (array_row[index] == 1)
                {
                    richTextBox1.Text += "已走過 向左\n";
                }
                else
                {
                    richTextBox1.Text += "未走過 向左\n";
                    available_movements++;
                }
            }
            if ((y - L) >= 0)
            {
                richTextBox1.Text += "可向上\t";
                ix = x / L;
                iy = (y - L) / L;
                index = N * ix + iy;
                if (array_col[index] == 1)
                {
                    richTextBox1.Text += "已走過 向上\n";
                }
                else
                {
                    richTextBox1.Text += "未走過 向上\n";
                    available_movements++;
                }
            }
            return available_movements;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            timer1.Enabled = false;
            init_mouse_setting();
            this.pictureBox1.Invalidate();

            timer1.Enabled = true;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (flag_game_end == false)
            {
                timer1_Tick(sender, e);
            }
            else
            {
                richTextBox1.Text += "無路可走\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            timer1.Enabled = true;
        }
    }
}

