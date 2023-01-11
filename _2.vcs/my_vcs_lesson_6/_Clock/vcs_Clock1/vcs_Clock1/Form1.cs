using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_Clock1
{
    public partial class Form1 : Form
    {
        bool flag_debug = false;
        int flag_operation_mode = MODE_0;

        private const int MODE_0 = 0x00;   //時間模式
        private const int MODE_1 = 0x01;   //碼表模式
        private const int MODE_2 = 0x02;   //離開
        private const int MODE_3 = 0x03;   //大螢幕
        private const int MODE_4 = 0x04;   //倒數計時
        private const int MODE_5 = 0x05;   //最上層切換

        int flag_stopwatch_mode = -1;
        private const int MODE_1a = 0x00;   //碼表模式a, 歸零, 等待開始
        private const int MODE_1b = 0x01;   //碼表模式b, 開始計數
        private const int MODE_1c = 0x02;   //碼表模式c, 暫停

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
            this.FormBorderStyle = FormBorderStyle.None;

            if (flag_debug == false)
            {
                this.Size = new Size(W, H);
            }
            else
            {

            }

            int ScreenWidth = Screen.PrimaryScreen.Bounds.Width;
            int ScreenHeight = Screen.PrimaryScreen.Bounds.Height;

            //設定執行後的表單起始位置
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point(ScreenWidth - this.Width, ScreenHeight - 40 - this.Height);
        }

        //Form1 initial location
        private const int FORM1_DEFAULT_POSITION_X = 600 - 10;
        private const int FORM1_DEFAULT_POSITION_Y = 700;
        int form1_position_x_old = FORM1_DEFAULT_POSITION_X;
        int form1_position_y_old = FORM1_DEFAULT_POSITION_Y;
        bool flag_form1_mouse_down = false;

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            flag_form1_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            form1_position_x_old = e.X;
            form1_position_y_old = e.Y;
        }

        private void Form1_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_form1_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - form1_position_x_old;
                int dy = e.Y - form1_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);
            }
        }

        private void Form1_MouseUp(object sender, MouseEventArgs e)
        {
            flag_form1_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - form1_position_x_old;
            int dy = e.Y - form1_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);
        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            int linewidth = 6;
            Graphics g = e.Graphics;
            Brush b = new SolidBrush(Color.Blue);
            Font f = new Font("標楷體", 20, FontStyle.Bold);
            Pen p = new Pen(Brushes.Blue, linewidth);

            if ((flag_operation_mode == MODE_0) || (flag_operation_mode == MODE_3) || (flag_operation_mode == MODE_5))
            {
                //string dt = DateTime.Now.ToString("yyyyMMdd_HHmmss");
                //string dt = DateTime.Now.ToString();
                //string dt = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");
                string dt = DateTime.Now.ToString("HH:mm:ss");

                g.DrawRectangle(p, linewidth / 2, linewidth / 2, W - linewidth, H - linewidth);
                g.DrawString(dt, f, b, 10, 10);

            }
            else if (flag_operation_mode == MODE_1)
            {
                g.DrawRectangle(p, linewidth / 2, linewidth / 2, W - linewidth, H - linewidth);
                g.DrawString(stopwatch_text, f, b, 10, 10);


            }
        }

        private void timer_clock_Tick(object sender, EventArgs e)
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
                    richTextBox1.Text += "零 時間模式";
                    timer_clock.Enabled = true;
                    timer_stopwatch.Enabled = false;
                    timer_countdown.Enabled = false;
                    flag_operation_mode = MODE_0;
                    this.Invalidate();
                }
                else if (xx < W * 2 / 3) //中
                {
                    richTextBox1.Text += "一 碼表模式";
                    timer_clock.Enabled = false;
                    timer_stopwatch.Enabled = false;
                    timer_countdown.Enabled = false;
                    flag_operation_mode = MODE_1;

                    do_stopwatch();
                }
                else  //右
                {
                    richTextBox1.Text += "二 離開";
                    flag_operation_mode = MODE_2;
                    Application.Exit();
                }
            }
            else   //下排
            {
                if (xx < W / 3) //左
                {
                    richTextBox1.Text += "三 大螢幕";
                    flag_operation_mode = MODE_3;
                }
                else if (xx < W * 2 / 3) //中
                {
                    richTextBox1.Text += "四 倒數計時";
                    flag_operation_mode = MODE_4;

                }
                else  //右
                {
                    richTextBox1.Text += "五 最上層切換";
                    flag_operation_mode = MODE_5;
                    if (this.TopMost == false)
                        this.TopMost = true;
                    else
                        this.TopMost = false;
                }
            }

            if (flag_operation_mode != MODE_1)
            {
                flag_stopwatch_mode = -1;
            }
        }

        void do_stopwatch()
        {
            if (flag_stopwatch_mode == -1)
            {
                flag_stopwatch_mode = MODE_1a;  //歸零, 等待開始
                richTextBox1.Text += "歸零, 等待開始\n";
                stopwatch_text = "00:00:00.0";
                this.Invalidate();
            }
            else if (flag_stopwatch_mode == MODE_1a)
            {
                flag_stopwatch_mode = MODE_1b;  //開始計數
                richTextBox1.Text += "開始計數\n";
                timer_stopwatch.Enabled = true;
                StartTime = DateTime.Now;
            }
            else if (flag_stopwatch_mode == MODE_1b)
            {
                flag_stopwatch_mode = MODE_1c;  //暫停
                richTextBox1.Text += "暫停\n";
                timer_stopwatch.Enabled = false;
            }
            else if (flag_stopwatch_mode == MODE_1c)
            {
                flag_stopwatch_mode = MODE_1a;  //歸零, 等待開始
                richTextBox1.Text += "歸零, 等待開始\n";
                stopwatch_text = "00:00:00.0";
                this.Invalidate();
            }
            else
            {
                richTextBox1.Text += "XXXXXXXXXXXXXXXXXXXXXXXX\n";

            }

        }

        private DateTime StartTime;
        string stopwatch_text = "";
        private void timer_stopwatch_Tick(object sender, EventArgs e)
        {
            //碼表
            TimeSpan elapsed = DateTime.Now - StartTime;

            stopwatch_text = "";
            // Start with the days if greater than 0.
            if (elapsed.Days > 0)
            {
                stopwatch_text += elapsed.Days.ToString() + ".";
            }

            // Convert milliseconds into tenths of seconds.
            int tenths = elapsed.Milliseconds / 100;

            // Compose the rest of the elapsed time.
            stopwatch_text +=
                elapsed.Hours.ToString("00") + ":" +
                elapsed.Minutes.ToString("00") + ":" +
                elapsed.Seconds.ToString("00") + "." +
                tenths.ToString("0");
            this.Invalidate();
        }

        private void timer_countdown_Tick(object sender, EventArgs e)
        {
            //倒數計時

        }



    }
}
