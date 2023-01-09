using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Clock1
{
    public partial class Form1 : Form
    {

        int flag_operation_mode = MODE_0;

        private const int MODE_0 = 0x00;   //時間模式
        private const int MODE_1 = 0x01;   //碼表模式
        private const int MODE_2 = 0x02;   //離開
        private const int MODE_3 = 0x03;   //
        private const int MODE_4 = 0x04;   //
        private const int MODE_5 = 0x05;   //最上層切換

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE
        private const int W = 200;
        private const int H = 100;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            //string dt = DateTime.Now.ToString("yyyyMMdd_HHmmss");
            //string dt = DateTime.Now.ToString();
            //string dt = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
            string dt = DateTime.Now.ToString("HH:mm:ss");
            Graphics g = e.Graphics;

            Brush b = new SolidBrush(Color.Blue);
            Font f = new Font("標楷體", 20, FontStyle.Bold);
            Pen p = new Pen(Brushes.Blue, 5);

            g.DrawRectangle(p, 0, 0, W, H);
            g.DrawString(dt, f, b, 10, 10);

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            this.Invalidate();
        }

        private void Form1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "(" + e.X.ToString() + ", " + e.Y.ToString() + ") ";
            int xx = e.X;
            int yy = e.Y;
            if (yy < H / 2) //上排
            {
                if (xx < W / 3) //左
                {
                    richTextBox1.Text += "零";
                    flag_operation_mode = MODE_0;
                }
                else if (xx < W * 2 / 3) //中
                {
                    richTextBox1.Text += "一";
                    flag_operation_mode = MODE_1;

                }
                else  //右
                {
                    richTextBox1.Text += "二";
                    flag_operation_mode = MODE_2;
                    Application.Exit();
                }
            }
            else   //下排
            {
                if (xx < W / 3) //左
                {
                    richTextBox1.Text += "三";
                    flag_operation_mode = MODE_3;
                }
                else if (xx < W * 2 / 3) //中
                {
                    richTextBox1.Text += "四";
                    flag_operation_mode = MODE_4;

                }
                else  //右
                {
                    richTextBox1.Text += "五";
                    flag_operation_mode = MODE_5;
                    if (this.TopMost == false)
                        this.TopMost = true;
                    else
                        this.TopMost = false;
                }

            }



        }
    }
}
