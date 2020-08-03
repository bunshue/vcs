using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_OXGame
{
    public partial class Form1 : Form
    {
        //一維List for int
        List<int> steps = new List<int>();
        List<int> select_steps = new List<int>();
        //int N;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            reset_steps();
        }

        void reset_steps()
        {
            int i;
            int tmp;
            Random r = new Random();

            steps.Clear();
            select_steps.Clear();

            for (i = 0; i < 9; i++)
            {
                steps.Add(i + 1);
                //steps.Add(new string[] { i.ToString(), ('A' + i).ToString() });
            }

            //show_steps(steps);

            for (i = 0; i < steps.Count; i++)
            {
                int n = r.Next(steps.Count);
                //richTextBox1.Text += "第" + i.ToString() + "項和第" + n.ToString() + "項交換\n";
                tmp = steps[i];
                steps[i] = steps[n];
                steps[n] = tmp;
            }
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

            if (select_steps.Count > 0)
            {
                richTextBox1.Text += "已走步數 " + select_steps.Count.ToString() + " 步, 分別是:\t";
                for (i = 0; i < select_steps.Count; i++)
                {
                    richTextBox1.Text += select_steps[i].ToString() + "  ";
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

        void check_select_steps()
        {
            /*
            int i;

            if (select_steps.Count > 0)
            {
                richTextBox1.Text += "已走步數 " + select_steps.Count.ToString() + " 步, 分別是:\t";
                for (i = 0; i < select_steps.Count; i++)
                {
                    richTextBox1.Text += select_steps[i].ToString() + "  ";
                }
                richTextBox1.Text += "\n";
            }
            */
            if ((select_steps.Contains(1) == true) && (select_steps.Contains(2) == true) && (select_steps.Contains(3) == true))
            {
                richTextBox1.Text += "row 1 OK\n";
            }
            else if ((select_steps.Contains(4) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(6) == true))
            {
                richTextBox1.Text += "row 2 OK\n";
            }
            else if ((select_steps.Contains(7) == true) && (select_steps.Contains(8) == true) && (select_steps.Contains(9) == true))
            {
                richTextBox1.Text += "row 3 OK\n";
            }
            else if ((select_steps.Contains(1) == true) && (select_steps.Contains(4) == true) && (select_steps.Contains(7) == true))
            {
                richTextBox1.Text += "column 1 OK\n";
            }
            else if ((select_steps.Contains(2) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(8) == true))
            {
                richTextBox1.Text += "column 2 OK\n";
            }
            else if ((select_steps.Contains(3) == true) && (select_steps.Contains(6) == true) && (select_steps.Contains(9) == true))
            {
                richTextBox1.Text += "column 3 OK\n";
            }
            else if ((select_steps.Contains(1) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(9) == true))
            {
                richTextBox1.Text += "cross 1 OK\n";
            }
            else if ((select_steps.Contains(3) == true) && (select_steps.Contains(5) == true) && (select_steps.Contains(7) == true))
            {
                richTextBox1.Text += "cross 2 OK\n";
            }



        }



        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            this.Text = "目前滑鼠在Form1上的位置：" + e.X + " : " + e.Y;
            int N = 0;
            int W = pictureBox1.Width;
            int H = pictureBox1.Height;
            int x = e.X;
            int y = e.Y;
            int w = W / 3;
            int h = H / 3;
            int dd = 10;

            if ((x < dd) || (y < dd) || (x >= (W - dd)) || (y >= (H - dd)))
                return;

            if (y < (h - dd))
            {
                if (x < (w - dd))
                {
                    richTextBox1.Text += "左上\n";
                    N = 1;
                }
                else if (x < (w * 2 - dd))
                {
                    richTextBox1.Text += "中上\n";
                    N = 2;
                }
                else
                {
                    richTextBox1.Text += "右上\n";
                    N = 3;
                }
            }
            else if (y < (h * 2 - dd))
            {
                if (x < (w - dd))
                {
                    richTextBox1.Text += "左中\n";
                    N = 4;
                }
                else if (x < (w * 2 - dd))
                {
                    richTextBox1.Text += "中中\n";
                    N = 5;
                }
                else
                {
                    richTextBox1.Text += "右中\n";
                    N = 6;
                }
            }
            else
            {
                if (x < (w - dd))
                {
                    richTextBox1.Text += "左下\n";
                    N = 7;
                }
                else if (x < (w * 2 - dd))
                {
                    richTextBox1.Text += "中下\n";
                    N = 8;
                }
                else
                {
                    richTextBox1.Text += "右下\n";
                    N = 9;
                }
            }

            richTextBox1.Text += "取得 N = " + N.ToString() + "\n";

            remove_item(N);
            select_steps.Add(N);
            check_select_steps();


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

    }
}
