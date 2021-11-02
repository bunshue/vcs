using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Xml;
using System.Text.RegularExpressions;
using System.Management;
using System.IO;
using Shell32;
using System.Runtime.InteropServices;

namespace test6
{
    public partial class Form1 : Form
    {
        //實現控件中捕獲按鍵 只要補上這個函數就好
        protected override bool ProcessCmdKey(ref Message msg, Keys keyData)
        {
            const int WM_KEYDOWN = 0x100;
            const int WM_SYSKEYDOWN = 0x104;
            if ((msg.Msg == WM_KEYDOWN) || (msg.Msg == WM_SYSKEYDOWN))
            {
                switch (keyData)
                {
                    case Keys.Down:
                        this.Text = "向下鍵已經被捕捉";
                        break;
                    case Keys.Up:
                        this.Text = "向上鍵已經被捕捉";
                        break;
                    case Keys.Left:
                        this.Text = "向左鍵已經被捕捉";
                        break;
                    case Keys.Right:
                        this.Text = "向右鍵已經被捕捉";
                        break;
                    case Keys.Home:
                        this.Text = "Home 鍵已經被捕捉";
                        break;
                    case Keys.End:
                        this.Text = "End 鍵已經被捕捉";
                        break;
                }
            }
            return base.ProcessCmdKey(ref msg, keyData);
        }


        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
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
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //模擬MSN窗體抖動1

            int rand = 50;
            int recordx = this.Left;　//保存原來窗體的左上角的x坐標
            int recordy = this.Top;　//保存原來窗體的左上角的y坐標

            Random random = new Random();

            for (int i = 0; i < 100; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }

                this.Left = recordx;　//還原原始窗體的左上角的x坐標
                this.Top = recordy;　//還原原始窗體的左上角的y坐標
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //模擬MSN窗體抖動2

            int rand = 10;
            int recordx = this.Left;
            int recordy = this.Top;
            Random random = new Random();
            for (int i = 0; i < 50; i++)
            {
                int x = random.Next(rand);
                int y = random.Next(rand);
                if (x % 2 == 0)
                {
                    this.Left = this.Left + x;
                }
                else
                {
                    this.Left = this.Left - x;
                }
                if (y % 2 == 0)
                {
                    this.Top = this.Top + y;
                }
                else
                {
                    this.Top = this.Top - y;
                }
                System.Threading.Thread.Sleep(1);
            }
            this.Left = recordx;
            this.Top = recordy;
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

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

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

    }
}

