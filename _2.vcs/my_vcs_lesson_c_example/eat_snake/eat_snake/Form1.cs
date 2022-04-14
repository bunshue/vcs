using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Threading.Tasks;

namespace eat_snake
{
    public partial class Form1 : Form
    {
        cube s;
        Graphics g;
        Random xz = new Random();
        Random yz = new Random();
        int direct = 3;//方向参数 初始化向右
        int sum = 0;//总分
        int socre = 0;//加分

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label3.Text =   "規則：\n" +
                            "1.紅色果實加一分，身長加一，移動速度增加一個單位\n" +
                            "2.紫色果實加二分，身長加二，移動速度增加兩個單位\n" +
                            "3.金色果實加三分，身長加二，移動速度增加三個單位\n" +
                            "4.身體碰到自己或者邊界遊戲結束\n" +
                            "5.不允許向反方向移動，例如前進時不允許通過s鍵向後移動\n" +
                            "6.ASWD控制移動\n";

            textBox1.Text = "0";
            textBox2.Text = "0:0";
        }

        private int[] Get_Pos()
        {
            int[] pos = new int[2];
            int cube_x = 0;
            int cube_y = 0;
            while (true)
            {
                cube_x = xz.Next(0, 35);
                cube_y = yz.Next(0, 24);
                pos[0] = 11 + cube_x * 10;
                pos[1] = 28 + cube_y * 10;
                if (s.Createfood(pos[0], pos[1], 1)) break;
            }
            return pos;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (button1.Text == "start")
            {
                button1.Text = "end";
                timer1.Interval = 200;
                g = this.CreateGraphics();
                g.DrawRectangle(new Pen(Color.Black, 1), 9, 26, 348, 238);
                g.FillRectangle(new SolidBrush(Color.White), 11, 28, 345, 235);
                s = new cube(11, 28, g);
                s.next(3, ref socre);
                s.next(3, ref socre);
                this.Get_Pos();
                direct = 3;
                step = 3;
                timer1.Enabled = true;
                timer2.Enabled = true;
            }
            else
            {
                button1.Text = "start";
                g.FillRectangle(new SolidBrush(Color.White), 11, 25, 340, 235);
                s = new cube(11, 28, g);
                s.next(3, ref socre);
                s.next(3, ref socre);
                s.end();
                direct = 3;
                textBox1.Text = "0";
                sum = 0;
                socre = 0;
            }
        }

        int step = 3;
        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar == 'a' || e.KeyChar == 'A') && direct != 3) step = 2;
            else if ((e.KeyChar == 'd' || e.KeyChar == 'D') && direct != 2) step = 3;
            else if ((e.KeyChar == 'w' || e.KeyChar == 'W') && direct != 0) step = 1;
            else if ((e.KeyChar == 's' || e.KeyChar == 'S') && direct != 1) step = 0;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            bool res = true;
            direct = step;
            res = s.next(direct, ref socre);
            if (socre != 0)
            {
                sum += socre;
                timer1.Interval = 200 - sum * 2;
                textBox1.Text = sum.ToString();
            }
            if (res == false)
            {
                timer1.Enabled = false;
                MessageBox.Show("Game over!");
                button1_Click(null, null);
                timer1.Interval = 200;
                return;
            }
            s.move();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (button2.Text == "pause")
            {
                button2.Text = "back";
                timer1.Stop();
            }
            else
            {
                button2.Text = "pause";
                timer1.Start();
            }
        }

        int cec = 0;
        private void timer2_Tick(object sender, EventArgs e)
        {
            cec++;
            int min = cec / 60;
            int sec = cec % 60;
            textBox2.Text = min.ToString() + ":" + sec.ToString();
        }
    }
}
