using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.IO;
using System.Drawing.Imaging;
using System.Drawing.Drawing2D;
using System.Reflection;    //for Assembly
using System.Security.Cryptography; //for HashAlgorithm
using System.Diagnostics;   //for Process
using System.Threading;
using System.Text.RegularExpressions;
using System.Runtime.InteropServices;
using System.Collections;   //for Stack

//參考/加入參考 /COM/Microsoft Shell Controls and Automation
using Shell32;  //for Shell


namespace vcs_Mix06
{
    public partial class Form1 : Form
    {
        [DllImport("user32.dll")]
        public static extern bool GetCursorPos(out POINT lpPoint);

        [StructLayout(LayoutKind.Sequential)]
        public struct POINT
        {
            public int X;
            public int Y;
            public POINT(int x, int y)
            {
                this.X = x;
                this.Y = y;
            }
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
            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(0, 0);

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 185;
            dy = 85;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            label1.Location = new Point(x_st + dx * 3, y_st + dy * 0 + 10);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;

            int w = 0;
            int h = 0;

            richTextBox1.Location = new Point(x_st + dx * 7, y_st + dy * 0);
            w = this.ClientSize.Width - richTextBox1.Location.X - 10;   //border : 10
            h = this.ClientSize.Height - richTextBox1.Location.Y - 10;   //border : 10
            richTextBox1.Size = new Size(w, h);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bt_exit_setup();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void show_button_text(object sender)
        {
            richTextBox1.Text += ((Button)sender).Text + "\n";
        }

        private void button0_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        //#制作閃動的窗體
        private void button3_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            while (Visible) // 關閉窗體時，停止循環
            {
                for (int c = 0; c < 254 && Visible; c++)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c); // 此方法指定三個數字：red/green/blue.
                    Application.DoEvents(); // 此語句使操作系統能夠在程序之外執行其他操作。否則
                    // 程序將占用所有CPU周期
                    Thread.Sleep(3); // 此語句在循環中插入3毫秒的延遲。
                }
                for (int c = 254; c >= 0 && Visible; c--)
                {
                    this.BackColor = Color.FromArgb(c, 255 - c, c);
                    Application.DoEvents();
                    Thread.Sleep(3);
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button7_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button8_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button9_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button10_Click(object sender, EventArgs e)
        {
            show_button_text(sender);

        }

        private void button11_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            show_button_text(sender);
            //顯示Loading窗體
            LoadingControl pLoading = LoadingControl.getLoading();
            pLoading.SetExecuteMethod(method);
            pLoading.ShowDialog();
        }

        private void method()
        {
            LoadingControl pLoading = LoadingControl.getLoading();
            for (int i = 0; i < 10; i++)
            {
                pLoading.SetCaptionAndDescription("", "", "執行進度" + i.ToString() + "/10");

                //XXXXXXX

                Thread.Sleep(200);
            }
            LoadingControl.getLoading().CloseLoadingForm();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            POINT pt = new POINT();
            GetCursorPos(out pt);
            //label1.Text = "滑鼠位置 : (" + pt.X.ToString() + ", " + pt.Y.ToString() + ")";    same
            label1.Text = "滑鼠位置 : (" + string.Format("X:{0}, Y:{1}", pt.X, pt.Y) + ")";
        }
    }
}

