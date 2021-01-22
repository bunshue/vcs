using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


/*  1P模式和2P模式
 *  1P模式為與電腦對戰  1P模式可選先攻後攻
 *  必為1P為O  2P為X
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 * 
 */



namespace vcs_Tictactoe2
{
    public partial class Form1 : Form
    {
        //一維List for int
        List<int> steps = new List<int>();
        List<int> select_steps_a = new List<int>();
        List<int> select_steps_b = new List<int>();
        List<int> select_steps_c = new List<int>();

        Graphics g;
        Graphics g2;
        Pen p;
        SolidBrush sb;
        Bitmap bitmap1;
        Bitmap bitmap2;

        bool flag_release_mode = false; 

        bool isRunning;
        int current_user = PLAYER_1P;
        int play_mode = MODE_1PLAYER;

        private const int PLAYER_1P = 0x00;
        private const int PLAYER_2P = 0x01;

        private const int MODE_1PLAYER = 0x00;
        private const int MODE_2PLAYER = 0x01;

        public Form1()
        {
            InitializeComponent();

            p = new Pen(Color.Green, 3);
            sb = new SolidBrush(Color.Pink);

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            bitmap2 = new Bitmap(pictureBox2.Width, pictureBox2.Height);
            g2 = Graphics.FromImage(bitmap2);
            g2.Clear(Color.White);
            pictureBox2.Image = bitmap2;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int w = W / 3;
            int h = H / 3;

            g.DrawLine(p, w, 0, w, H);
            g.DrawLine(p, w * 2, 0, w * 2, H);
            g.DrawLine(p, 0, h, W, h);
            g.DrawLine(p, 0, h * 2, W, h * 2);

            label2.Text = "";
            isRunning = false;

            button4.Enabled = true;
            button5.Enabled = false;
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx = 80;
            int dy = 60;

            x_st = 500;
            y_st = 10;
            groupBox2.Location = new Point(x_st, y_st);

            y_st += (dy + 10);
            groupBox1.Location = new Point(x_st, y_st);

            if (flag_release_mode == true)
            {
                y_st += (dy + 20);
                label2.Location = new Point(x_st, y_st);

                x_st = 500;
                y_st = 300;

                button4.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                button5.Location = new Point(x_st + dx * 0, y_st + dy * 1);

                button1.Visible = false;
                button6.Visible = false;
                button2.Visible = false;
                button7.Visible = false;

                richTextBox1.Visible = false;
                button3.Visible = false;
                this.Size = new Size(this.Size.Width - 280, this.Size.Height);
            }
            else
            {   //debug
                x_st = 700;
                y_st = 20;
                button4.Location = new Point(x_st + dx * 0, y_st + dy * 0);
                button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
                button6.Location = new Point(x_st + dx * 2, y_st + dy * 0);

                button5.Location = new Point(x_st + dx * 0, y_st + dy * 1);
                button2.Location = new Point(x_st + dx * 1, y_st + dy * 1);
                button7.Location = new Point(x_st + dx * 2, y_st + dy * 1);

                button1.Visible = true;
                button6.Visible = true;
                button2.Visible = true;
                button7.Visible = true;

                x_st -= 100;
                y_st += (dy / 2);
                pictureBox2.Location = new Point(x_st, y_st);
            }

            return;
        }

        void draw_win(int current, int N)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int w = W / 3;
            int h = H / 3;
            int x_st = 0;
            int y_st = 0;
            int dd = 10;

            if (N == 1)
            {
                x_st = dd;
                y_st = dd;
            }
            else if (N == 2)
            {
                x_st = w + dd;
                y_st = dd;
            }
            else if (N == 3)
            {
                x_st = w * 2 + dd;
                y_st = dd;
            }
            else if (N == 4)
            {
                x_st = dd;
                y_st = h + dd;
            }
            else if (N == 5)
            {
                x_st = w + dd;
                y_st = h + dd;
            }
            else if (N == 6)
            {
                x_st = w * 2 + dd;
                y_st = h + dd;
            }
            else if (N == 7)
            {
                x_st = dd;
                y_st = h * 2 + dd;
            }
            else if (N == 8)
            {
                x_st = w + dd;
                y_st = h * 2 + dd;
            }
            else if (N == 9)
            {
                x_st = w * 2 + dd;
                y_st = h * 2 + dd;
            }

            //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
            //richTextBox1.Text += "w = " + (w - dd * 2).ToString() + ", h = " + (h - dd * 2).ToString() + "\n";

            //richTextBox1.Text += "CCCCC\tcurrent_user = " + current.ToString() + "\n";

            if (current == 0)
            {
                sb = new SolidBrush(Color.Lime);
                g.FillRectangle(sb, x_st, y_st, w - dd * 2, h - dd * 2);
            }
            else
            {
                sb = new SolidBrush(Color.Pink);
                g.FillRectangle(sb, x_st, y_st, w - dd * 2, h - dd * 2);
            }
            pictureBox1.Image = bitmap1;


        }

        void draw_item(int current, int N)
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int w = W / 3;
            int h = H / 3;
            int x_st = 0;
            int y_st = 0;
            int dd = 10;

            if (N == 1)
            {
                x_st = dd;
                y_st = dd;
            }
            else if (N == 2)
            {
                x_st = w + dd;
                y_st = dd;
            }
            else if (N == 3)
            {
                x_st = w * 2 + dd;
                y_st = dd;
            }
            else if (N == 4)
            {
                x_st = dd;
                y_st = h + dd;
            }
            else if (N == 5)
            {
                x_st = w + dd;
                y_st = h + dd;
            }
            else if (N == 6)
            {
                x_st = w * 2 + dd;
                y_st = h + dd;
            }
            else if (N == 7)
            {
                x_st = dd;
                y_st = h * 2 + dd;
            }
            else if (N == 8)
            {
                x_st = w + dd;
                y_st = h * 2 + dd;
            }
            else if (N == 9)
            {
                x_st = w * 2 + dd;
                y_st = h * 2 + dd;
            }

            //richTextBox1.Text += "x_st = " + x_st.ToString() + ", y_st = " + y_st.ToString() + "\n";
            //richTextBox1.Text += "w = " + (w - dd * 2).ToString() + ", h = " + (h - dd * 2).ToString() + "\n";

            //richTextBox1.Text += "CCCCC\tcurrent_user = " + current.ToString() + "\n";

            if (current == 0)
            {
                sb = new SolidBrush(Color.Lime);
                //g.FillRectangle(sb, x_st, y_st, w - dd * 2, h - dd * 2);

                p = new Pen(Color.Lime, 3);
                g.DrawEllipse(p, x_st, y_st, w - dd * 2, h - dd * 2);
            }
            else
            {
                sb = new SolidBrush(Color.Pink);
                //g.FillRectangle(sb, x_st, y_st, w - dd * 2, h - dd * 2);

                p = new Pen(Color.Pink, 3);
                //g.DrawEllipse(p, x_st, y_st, w - dd * 2, h - dd * 2);
                g.DrawLine(p, x_st, y_st, x_st + w - dd * 2, y_st + h - dd * 2);
                g.DrawLine(p, x_st + w - dd * 2, y_st, x_st, y_st + h - dd * 2);


            }
            pictureBox1.Image = bitmap1;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            reset_steps();
        }

        void reset_steps()
        {
            int i;
            //int tmp;
            Random r = new Random();

            steps.Clear();
            select_steps_a.Clear();
            select_steps_b.Clear();

            for (i = 0; i < 9; i++)
            {
                steps.Add(i + 1);
                //steps.Add(new string[] { i.ToString(), ('A' + i).ToString() });
            }

            //show_steps(steps);

            /*  打亂分布
            for (i = 0; i < steps.Count; i++)
            {
                int n = r.Next(steps.Count);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = steps[i];
                steps[i] = steps[n];
                steps[n] = tmp;
            }
            */
            show_steps(steps);
        }

        void show_steps(List<int> steps)
        {
            int i;

            if (steps.Count > 0)
            {
                richTextBox1.Text += "剩餘步數 " + steps.Count.ToString() + " 步, 分別是:\t";
                for (i = 0; i < steps.Count; i++)
                {
                    richTextBox1.Text += steps[i].ToString() + "  ";
                }
                richTextBox1.Text += "\n";
            }

            if (select_steps_a.Count > 0)
            {
                richTextBox1.Text += "先攻方已走步數 " + select_steps_a.Count.ToString() + " 步, 分別是:\t";
                for (i = 0; i < select_steps_a.Count; i++)
                {
                    richTextBox1.Text += select_steps_a[i].ToString() + "  ";
                }
                richTextBox1.Text += "\n";
            }

            if (select_steps_b.Count > 0)
            {
                richTextBox1.Text += "後攻方已走步數 " + select_steps_b.Count.ToString() + " 步, 分別是:\t";
                for (i = 0; i < select_steps_b.Count; i++)
                {
                    richTextBox1.Text += select_steps_b[i].ToString() + "  ";
                }
                richTextBox1.Text += "\n";
            }
        }

        void remove_item(int N)
        {
            int i;
            if (steps.Count > 0)
            {
                for (i = 0; i < steps.Count; i++)
                {
                    if (N == steps[i])
                    {
                        richTextBox1.Text += "取得在index = " + i.ToString() + ",\t移除之\n";
                        steps.RemoveAt(i);
                        break;
                    }
                }
            }

            //revert color on N

        }

        int check_select_steps_a()
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int w = W / 3;
            int h = H / 3;
            int x_st = -1;
            int y_st = -1;
            int x_sp = -1;
            int y_sp = -1;

            if ((select_steps_a.Contains(1) == true) && (select_steps_a.Contains(2) == true) && (select_steps_a.Contains(3) == true))
            {
                richTextBox1.Text += "row 1 OK\n";
                x_st = 0;
                y_st = h / 2;
                x_sp = W;
                y_sp = h / 2;
            }
            else if ((select_steps_a.Contains(4) == true) && (select_steps_a.Contains(5) == true) && (select_steps_a.Contains(6) == true))
            {
                richTextBox1.Text += "row 2 OK\n";
                x_st = 0;
                y_st = h + h / 2;
                x_sp = W;
                y_sp = h + h / 2;
            }
            else if ((select_steps_a.Contains(7) == true) && (select_steps_a.Contains(8) == true) && (select_steps_a.Contains(9) == true))
            {
                richTextBox1.Text += "row 3 OK\n";
                x_st = 0;
                y_st = h * 2 + h / 2;
                x_sp = W;
                y_sp = h * 2 + h / 2;
            }
            else if ((select_steps_a.Contains(1) == true) && (select_steps_a.Contains(4) == true) && (select_steps_a.Contains(7) == true))
            {
                richTextBox1.Text += "column 1 OK\n";
                x_st = w / 2;
                y_st = 0;
                x_sp = w / 2;
                y_sp = H;
            }
            else if ((select_steps_a.Contains(2) == true) && (select_steps_a.Contains(5) == true) && (select_steps_a.Contains(8) == true))
            {
                richTextBox1.Text += "column 2 OK\n";
                x_st = w + w / 2;
                y_st = 0;
                x_sp = w + w / 2;
                y_sp = H;
            }
            else if ((select_steps_a.Contains(3) == true) && (select_steps_a.Contains(6) == true) && (select_steps_a.Contains(9) == true))
            {
                richTextBox1.Text += "column 3 OK\n";
                x_st = w * 2 + w / 2;
                y_st = 0;
                x_sp = w * 2 + w / 2;
                y_sp = H;
            }
            else if ((select_steps_a.Contains(1) == true) && (select_steps_a.Contains(5) == true) && (select_steps_a.Contains(9) == true))
            {
                richTextBox1.Text += "cross 1 OK\n";
                x_st = 0;
                y_st = 0;
                x_sp = W;
                y_sp = H;
            }
            else if ((select_steps_a.Contains(3) == true) && (select_steps_a.Contains(5) == true) && (select_steps_a.Contains(7) == true))
            {
                richTextBox1.Text += "cross 2 OK\n";
                x_st = W;
                y_st = 0;
                x_sp = 0;
                y_sp = H;
            }
            if ((x_st == -1) || (y_st == -1) || (x_sp == -1) || (y_sp == -1))
                return 0;

            p = new Pen(Color.Red, 5);
            g.DrawLine(p, x_st, y_st, x_sp, y_sp);

            return 1;
        }

        int check_select_steps_b()
        {
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int w = W / 3;
            int h = H / 3;
            int x_st = -1;
            int y_st = -1;
            int x_sp = -1;
            int y_sp = -1;

            if ((select_steps_b.Contains(1) == true) && (select_steps_b.Contains(2) == true) && (select_steps_b.Contains(3) == true))
            {
                richTextBox1.Text += "row 1 OK\n";
                x_st = 0;
                y_st = h / 2;
                x_sp = W;
                y_sp = h / 2;
            }
            else if ((select_steps_b.Contains(4) == true) && (select_steps_b.Contains(5) == true) && (select_steps_b.Contains(6) == true))
            {
                richTextBox1.Text += "row 2 OK\n";
                x_st = 0;
                y_st = h + h / 2;
                x_sp = W;
                y_sp = h + h / 2;
            }
            else if ((select_steps_b.Contains(7) == true) && (select_steps_b.Contains(8) == true) && (select_steps_b.Contains(9) == true))
            {
                richTextBox1.Text += "row 3 OK\n";
                x_st = 0;
                y_st = h * 2 + h / 2;
                x_sp = W;
                y_sp = h * 2 + h / 2;
            }
            else if ((select_steps_b.Contains(1) == true) && (select_steps_b.Contains(4) == true) && (select_steps_b.Contains(7) == true))
            {
                richTextBox1.Text += "column 1 OK\n";
                x_st = w / 2;
                y_st = 0;
                x_sp = w / 2;
                y_sp = H;
            }
            else if ((select_steps_b.Contains(2) == true) && (select_steps_b.Contains(5) == true) && (select_steps_b.Contains(8) == true))
            {
                richTextBox1.Text += "column 2 OK\n";
                x_st = w + w / 2;
                y_st = 0;
                x_sp = w + w / 2;
                y_sp = H;
            }
            else if ((select_steps_b.Contains(3) == true) && (select_steps_b.Contains(6) == true) && (select_steps_b.Contains(9) == true))
            {
                richTextBox1.Text += "column 3 OK\n";
                x_st = w * 2 + w / 2;
                y_st = 0;
                x_sp = w * 2 + w / 2;
                y_sp = H;
            }
            else if ((select_steps_b.Contains(1) == true) && (select_steps_b.Contains(5) == true) && (select_steps_b.Contains(9) == true))
            {
                richTextBox1.Text += "cross 1 OK\n";
                x_st = 0;
                y_st = 0;
                x_sp = W;
                y_sp = H;
            }
            else if ((select_steps_b.Contains(3) == true) && (select_steps_b.Contains(5) == true) && (select_steps_b.Contains(7) == true))
            {
                richTextBox1.Text += "cross 2 OK\n";
                x_st = W;
                y_st = 0;
                x_sp = 0;
                y_sp = H;
            }
            if ((x_st == -1) || (y_st == -1) || (x_sp == -1) || (y_sp == -1))
                return 0;

            p = new Pen(Color.Red, 5);
            g.DrawLine(p, x_st, y_st, x_sp, y_sp);

            return 1;
        }

        int check_select_steps_c(List<int> select_steps)
        {
            int got_line = 0;

            if ((select_steps.Contains(1) == true) && (select_steps.Contains(2) == true) && (select_steps.Contains(3) == true))
            {
                richTextBox1.Text += "row 1 OK\n";
                got_line = 1;
            }
            else if ((select_steps.Contains(4) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(6) == true))
            {
                richTextBox1.Text += "row 2 OK\n";
                got_line = 1;
            }
            else if ((select_steps.Contains(7) == true) && (select_steps.Contains(8) == true) && (select_steps.Contains(9) == true))
            {
                richTextBox1.Text += "row 3 OK\n";
                got_line = 1;
            }
            else if ((select_steps.Contains(1) == true) && (select_steps.Contains(4) == true) && (select_steps.Contains(7) == true))
            {
                richTextBox1.Text += "column 1 OK\n";
                got_line = 1;
            }
            else if ((select_steps.Contains(2) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(8) == true))
            {
                richTextBox1.Text += "column 2 OK\n";
                got_line = 1;
            }
            else if ((select_steps.Contains(3) == true) && (select_steps.Contains(6) == true) && (select_steps.Contains(9) == true))
            {
                richTextBox1.Text += "column 3 OK\n";
                got_line = 1;
            }
            else if ((select_steps.Contains(1) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(9) == true))
            {
                richTextBox1.Text += "cross 1 OK\n";
                got_line = 1;
            }
            else if ((select_steps.Contains(3) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(7) == true))
            {
                richTextBox1.Text += "cross 2 OK\n";
                got_line = 1;
            }
            return got_line;
        }


        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            this.Text = "目前滑鼠在Form1上的位置：" + e.X + " : " + e.Y;

            if (isRunning == false)
                return;

            int N = 0;
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int x = e.X;
            int y = e.Y;
            int w = W / 3;
            int h = H / 3;
            int dd = 10;
            int result;

            if ((x < dd) || (y < dd) || (x >= (W - dd)) || (y >= (H - dd)))
                return;

            if (y < (h - dd))
            {
                if (x < (w - dd))
                {
                    //richTextBox1.Text += "左上\n";
                    N = 1;
                }
                else if (x < (w * 2 - dd))
                {
                    //richTextBox1.Text += "中上\n";
                    N = 2;
                }
                else
                {
                    //richTextBox1.Text += "右上\n";
                    N = 3;
                }
            }
            else if (y < (h * 2 - dd))
            {
                if (x < (w - dd))
                {
                    //richTextBox1.Text += "左中\n";
                    N = 4;
                }
                else if (x < (w * 2 - dd))
                {
                    //richTextBox1.Text += "中中\n";
                    N = 5;
                }
                else
                {
                    //richTextBox1.Text += "右中\n";
                    N = 6;
                }
            }
            else
            {
                if (x < (w - dd))
                {
                    //richTextBox1.Text += "左下\n";
                    N = 7;
                }
                else if (x < (w * 2 - dd))
                {
                    //richTextBox1.Text += "中下\n";
                    N = 8;
                }
                else
                {
                    //richTextBox1.Text += "右下\n";
                    N = 9;
                }
            }

            //richTextBox1.Text += "取得 N = " + N.ToString() + "\n";

            if (current_user == 0)
            {
                if (select_steps_b.Contains(N) == true)
                {
                    richTextBox1.Text += "別人已經走過, 重來\n";
                    return;
                }

                if (select_steps_a.Contains(N) == false)
                {
                    select_steps_a.Add(N);
                    draw_item(current_user, N);
                    remove_item(N);
                    result = check_select_steps_a();

                    if (result == 1)
                    {
                        richTextBox1.Text += "勝負已分\t1P勝";

                        SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(30, 0, 255, 0));
                        g.FillRectangle(semiTransBrush, new Rectangle(0, 0, pictureBox1.Width, pictureBox1.Height));
                        button5.Text = "重玩";

                        draw_result("1P勝");

                        isRunning = false;
                    }
                    else
                    {
                        richTextBox1.Text += "共走了 " + (select_steps_a.Count + select_steps_b.Count).ToString() + " 步\t";
                        richTextBox1.Text += "PC方共走了 " + select_steps_a.Count.ToString() + " 步\n";

                        if ((select_steps_a.Count + select_steps_b.Count) >= 9)
                        {
                            richTextBox1.Text += "平手\n";
                            draw_result("平手");

                            button5.Text = "重玩";
                            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(30, 0, 0, 255));
                            g.FillRectangle(semiTransBrush, new Rectangle(0, 0, pictureBox1.Width, pictureBox1.Height));
                            isRunning = false;
                            return;
                        }

                        current_user = 1 - current_user;
                        if (play_mode == MODE_1PLAYER)
                        {
                            label2.Text = "輪到 PC, 電選\n";
                            button6_Click(sender, e);
                        }
                        else
                            label2.Text = "輪到 2P";
                        draw_user(current_user);
                    }
                }
            }
            else
            {
                if (select_steps_a.Contains(N) == true)
                {
                    richTextBox1.Text += "別人已經走過, 重來\n";
                    return;
                }

                if (select_steps_b.Contains(N) == false)
                {
                    select_steps_b.Add(N);

                    draw_item(current_user, N);
                    remove_item(N);
                    result = check_select_steps_b();

                    if (result == 1)
                    {

                        SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(30, 255, 0, 0));
                        g.FillRectangle(semiTransBrush, new Rectangle(0, 0, pictureBox1.Width, pictureBox1.Height));

                        button5.Text = "重玩";

                        if (play_mode == MODE_1PLAYER)
                        {
                            draw_result("PC勝");
                            richTextBox1.Text += "勝負已分\tPC勝";
                        }
                        else
                        {
                            draw_result("2P勝");
                            richTextBox1.Text += "勝負已分\t2P勝";
                        }

                        /*
                        if (radioButton1.Checked == true)
                        {
                            if ((select_steps_a.Count % 2) == 0)
                                label2.Text = "PC勝";
                            else
                                label2.Text = "USER勝";
                        }
                        else
                        {
                            if ((select_steps_a.Count % 2) == 0)
                                label2.Text = "USER勝";
                            else
                                label2.Text = "PC勝";
                        }
                        */
                        isRunning = false;
                    }
                    else
                    {
                        richTextBox1.Text += "共走了 " + (select_steps_a.Count + select_steps_b.Count).ToString() + " 步\t";
                        richTextBox1.Text += "1P 方共走了 " + select_steps_b.Count.ToString() + " 步\n";

                        if ((select_steps_a.Count + select_steps_b.Count) >= 9)
                        {
                            richTextBox1.Text += "平手\n";
                            button5.Text = "重玩";
                            SolidBrush semiTransBrush = new SolidBrush(Color.FromArgb(30, 0, 0, 255));
                            g.FillRectangle(semiTransBrush, new Rectangle(0, 0, pictureBox1.Width, pictureBox1.Height));
                            isRunning = false;
                            return;
                        }

                        current_user = 1 - current_user;
                        label2.Text = "輪到 1P";
                        draw_user(current_user);
                    }
                }
            }
        }

        void draw_user(int current_user)
        {
            int W = pictureBox2.Width;
            int H = pictureBox2.Height;
            int x_st = 0;
            int y_st = 0;
            int dd = 3;
            g2.Clear(Color.White);

            if (current_user == PLAYER_1P)
            {
                p = new Pen(Color.Lime, 3);
                g2.DrawEllipse(p, x_st + dd, y_st + dd, W - dd * 2, H - dd * 2);


            }
            else   //PLAYER_2P
            {
                p = new Pen(Color.Pink, 3);
                g2.DrawLine(p, x_st + dd, y_st + dd, x_st + W - dd * 2, y_st + H - dd * 2);
                g2.DrawLine(p, x_st + W - dd, y_st + dd, x_st + dd, y_st + H - dd * 2);
            }
            pictureBox2.Image = bitmap2;
        }

        void draw_result(string str)
        {
            Font f = new Font("標楷體", 120);
            int tmp_width = 0;
            int tmp_height = 0;
            tmp_width = g.MeasureString(str, f).ToSize().Width;
            tmp_height = g.MeasureString(str, f).ToSize().Height;
            //richTextBox1.Text += "tmp_width = " + tmp_width.ToString() + "  tmp_height = " + tmp_height.ToString() + "\n";
            sb = new SolidBrush(Color.Purple);
            g.DrawString(str, f, sb, new PointF((pictureBox1.Width - tmp_width) / 2, (pictureBox1.Height - tmp_height) / 2));

            pictureBox2.Image = bitmap2;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            reset_steps();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_steps(steps);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
                richTextBox1.Text += "先攻";
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton2.Checked == true)
                richTextBox1.Text += "後攻";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            isRunning = true;
            reset_steps();

            //新建圖檔, 初始化畫布
            bitmap1 = new Bitmap(pictureBox1.Width, pictureBox1.Height);
            g = Graphics.FromImage(bitmap1);
            g.Clear(Color.White);
            pictureBox1.Image = bitmap1;

            richTextBox1.Text += "已新建圖檔\n";
            richTextBox1.Text += "畫布大小 : W = " + bitmap1.Width.ToString() + " H = " + bitmap1.Height.ToString() + "\n";

            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int w = W / 3;
            int h = H / 3;

            p = new Pen(Color.Green, 3);
            g.DrawLine(p, w, 0, w, H);
            g.DrawLine(p, w * 2, 0, w * 2, H);
            g.DrawLine(p, 0, h, W, h);
            g.DrawLine(p, 0, h * 2, W, h * 2);

            button4.Enabled = false;
            button5.Enabled = true;
            groupBox1.Enabled = false;
            groupBox2.Enabled = false;

            if (radioButton1.Checked == true)
            {
                current_user = PLAYER_1P;
            }
            else
            {
                current_user = PLAYER_2P;
            }

            if (current_user == PLAYER_1P)
            {
                label2.Text = "輪到 1P";
            }
            else
            {
                if (play_mode == MODE_1PLAYER)
                    label2.Text = "輪到 PC";
                else
                    label2.Text = "輪到 2P";
            }
            draw_user(current_user);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            if (button5.Text == "重玩")
            {
                button4_Click(sender, e);
                button5.Text = "放棄";
            }
            else
            {
                isRunning = false;
                button4.Enabled = true;
                button5.Enabled = false;
                groupBox1.Enabled = true;
                groupBox2.Enabled = true;
                label2.Text = "";
                button5.Text = "放棄";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            if (isRunning == false)
                return;

            if (current_user == PLAYER_1P)
            {
                richTextBox1.Text += "目前輪到 1P\n";
            }
            else    //PLAYER_2P
            {
                if (play_mode == MODE_1PLAYER)
                {
                    richTextBox1.Text += "目前輪到 PC\t自動走步\n";

                    int i;

                    if (steps.Count > 0)
                    {
                        richTextBox1.Text += "pc目前可走步數 " + steps.Count.ToString() + " 步, 分別是:\t";
                        for (i = 0; i < steps.Count; i++)
                        {
                            richTextBox1.Text += steps[i].ToString() + "  ";
                        }
                        richTextBox1.Text += "\n";
                    }

                    if (select_steps_b.Count > 0)
                    {
                        richTextBox1.Text += "目前後攻方已走步數 " + select_steps_b.Count.ToString() + " 步, 分別是:\t";
                        for (i = 0; i < select_steps_b.Count; i++)
                        {
                            richTextBox1.Text += select_steps_b[i].ToString() + "  ";
                        }
                        richTextBox1.Text += "\n";
                    }

                    int win = 0;
                    //1. 檢查每一步，若必能贏，就直接下
                    if (steps.Count > 0)
                    {
                        richTextBox1.Text += "bb目前可走步數 " + steps.Count.ToString() + " 步, 分別測試:\n";
                        for (i = 0; i < steps.Count; i++)
                        {
                            //richTextBox1.Text += "測試項目 " + steps[i].ToString() + "\n";
                            select_steps_c.Clear();
                            int j;
                            for (j = 0; j < select_steps_b.Count; j++)
                            {
                                select_steps_c.Add(select_steps_b[j]);
                            }
                            select_steps_c.Add(steps[i]);

                            win = check_select_steps_c(select_steps_c);
                            if (win == 1)
                            {
                                richTextBox1.Text += "下了 " + steps[i].ToString() + " 這步，立刻可贏\n";
                                draw_win(current_user, steps[i]);
                                break;
                            }


                        }
                        richTextBox1.Text += "\n";


                    
                    }


                    //2. 檢查每一步，若下了之後，給對方贏的機會，則刪除

                    //3. 檢查每一步，下了之後，有兩勝以上機會，就直接下

                    //4. 檢查每一步，若有一勝機會，任選其一
                    //4. 檢查每一步，任選其一，盡量選邊角







                else
                    richTextBox1.Text += "目前輪到 2P\n";

                }









            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            draw_win(0, 5);

            draw_win(1, 7);

        }

        private void rb_1p_CheckedChanged(object sender, EventArgs e)
        {
            if (rb_1p.Checked == true)
            {
                groupBox1.Visible = true;
                play_mode = MODE_1PLAYER;
            }

            if (rb_2p.Checked == true)
            {
                groupBox1.Visible = false;
                play_mode = MODE_2PLAYER;
                richTextBox1.Text += "1 play_mode = " + play_mode.ToString() + "\n";

            }
        }

    }
}
