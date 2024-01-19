using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Stopwatch

namespace vcs_MyToolbox
{
    public partial class Form_Clock : Form
    {
        Stopwatch sw = new Stopwatch();

        private const int _MODE_CLOCK = 0;  //一般
        private const int _MODE_STOPWATCH = 1;  //正數、碼表、stopwatch
        private const int _MODE_TIMER = 2;  //倒數
        private const int _MODE_ALARM = 3;  //鬧鐘

        //一般
        private const int _MODE_CLOCK_STATE_0 = 0;  //一般

        //正數
        private const int _MODE_STOPWATCH_STATE_0 = 0;  //正數準備中
        private const int _MODE_STOPWATCH_STATE_1 = 1;  //正數中、正數繼續
        private const int _MODE_STOPWATCH_STATE_2 = 2;  //正數暫停
        private const int _MODE_STOPWATCH_STATE_3 = 3;  //正數暫停歸零中

        //倒數
        private const int _MODE_TIMER_STATE_0 = 0;  //倒數準備中
        private const int _MODE_TIMER_STATE_1 = 1;  //倒數中
        private const int _MODE_TIMER_STATE_2 = 2;  //倒數暫停
        private const int _MODE_TIMER_STATE_3 = 3;  //倒數時間到

        //鬧鐘
        private const int _MODE_ALARM_STATE_0 = 0;  //鬧鐘準備中、時間到
        private const int _MODE_ALARM_STATE_1 = 1;  //鬧鐘開始
        //private const int _MODE_ALARM_STATE_2 = 2;  //鬧鐘時間到

        int flag_mode = _MODE_CLOCK;    //0:時鐘、1:正數、2:倒數、3:鬧鐘
        int flag_state = _MODE_CLOCK_STATE_0;

        int total_count_down_sec = 0;
        DateTime time_stop;
        DateTime time_pause_start;
        DateTime time_pause_stop;

        DateTime alarm_target;

        //int status = 0;
        System.DateTime time_sp;
        System.DateTime time_st;
        TimeSpan time_diff;
        TimeSpan time_diff_total;

        Label lb_main_mesg1 = new Label();
        int timer_display_show_main_mesg_count = 0;
        int timer_display_show_main_mesg_count_target = 0;

        private const int S_OK = 0;     //system return OK
        private const int S_FALSE = 1;     //system return FALSE


        public Form_Clock()
        {
            InitializeComponent();
        }

        private void Form_Clock_Load(object sender, EventArgs e)
        {
            show_item_location();

            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            this.Size = new Size(600, 200);

            lb_main_mesg1.Text = "AAAAAAA";
            lb_main_mesg1.Font = new Font("標楷體", 20);
            lb_main_mesg1.ForeColor = Color.Red;
            //lb_main_mesg1.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            lb_main_mesg1.Location = new Point(digitalDisplayControl1.Location.X, digitalDisplayControl1.Location.Y + digitalDisplayControl1.Height + 10);
            lb_main_mesg1.AutoSize = true;
            this.Controls.Add(lb_main_mesg1);     // 將控件加入表單

            groupBox2.Visible = false;

            this.FormBorderStyle = FormBorderStyle.None;
            //離開按鈕的寫法
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

        private void timer1_Tick(object sender, EventArgs e)
        {
            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
        }

        private void radioButton_CheckedChanged(object sender, EventArgs e)
        {
            if (radioButton1.Checked == true)
            {
                this.Text = "時鐘";
                flag_mode = _MODE_CLOCK;
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
                timer_clock.Enabled = true;
                timer_stopwatch.Enabled = false;
            }
            else if (radioButton2.Checked == true)
            {
                this.Text = "碼表";
                show_main_message1("碼表", S_OK, 30);

                flag_mode = _MODE_STOPWATCH;
                flag_state = _MODE_STOPWATCH_STATE_0;
                digitalDisplayControl1.DigitText = "00:00:00.00";

                groupBox2.Visible = true;
                this.Size = new Size(600, 320);

                timer_clock.Enabled = false;
            }
            else if (radioButton3.Checked == true)
            {
                this.Text = "倒數";
                show_main_message1("倒數", S_OK, 30);

                flag_mode = _MODE_CLOCK;
            }
            else
            {
                this.Text = "XXXXX";
                show_main_message1("XXXXX", S_OK, 30);

                flag_mode = _MODE_TIMER;
            }
        }

        void show_main_message1(string mesg, int number, int timeout)
        {
            lb_main_mesg1.Text = mesg;
            //playSound(number);

            timer_display_show_main_mesg_count = 0;
            timer_display_show_main_mesg_count_target = timeout;   //timeout in 0.1 sec
            timer_display.Enabled = true;
        }

        private void timer_display_Tick(object sender, EventArgs e)
        {
            if (timer_display_show_main_mesg_count < timer_display_show_main_mesg_count_target)      //display main message timeout
            {
                timer_display_show_main_mesg_count++;
                if (timer_display_show_main_mesg_count >= timer_display_show_main_mesg_count_target)
                {
                    lb_main_mesg1.Text = "";
                }
            }
        }

        bool flag_form_clock_mouse_down = false;
        //form_clock initial location
        private const int PB3_DEFAULT_POSITION_X = 600 - 10;
        private const int PB3_DEFAULT_POSITION_Y = 700;
        int form_clock_position_x_old = PB3_DEFAULT_POSITION_X;
        int form_clock_position_y_old = PB3_DEFAULT_POSITION_Y;

        private void Form_Clock_MouseDown(object sender, MouseEventArgs e)
        {
            flag_form_clock_mouse_down = true;
            //richTextBox1.Text += "Down : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            form_clock_position_x_old = e.X;
            form_clock_position_y_old = e.Y;

        }

        private void Form_Clock_MouseMove(object sender, MouseEventArgs e)
        {
            if (flag_form_clock_mouse_down == true)
            {
                //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
                int dx = e.X - form_clock_position_x_old;
                int dy = e.Y - form_clock_position_y_old;

                //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
                this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);
            }

        }

        private void Form_Clock_MouseUp(object sender, MouseEventArgs e)
        {
            flag_form_clock_mouse_down = false;
            //richTextBox1.Text += "Up : (" + e.X.ToString() + ", " + e.Y.ToString() + ")\n";
            int dx = e.X - form_clock_position_x_old;
            int dy = e.Y - form_clock_position_y_old;

            //richTextBox1.Text += "dx, dy : (" + dx.ToString() + ", " + dy.ToString() + ")\n";
            this.Location = new Point(this.Location.X + dx, this.Location.Y + dy);

        }

        private void digitalDisplayControl1_DoubleClick(object sender, EventArgs e)
        {
            Application.Exit();                             //關閉視窗
        }

        private void Form_Clock_Paint(object sender, PaintEventArgs e)
        {
            e.Graphics.DrawRectangle(Pens.Red, 0, 0, this.Width - 1, this.Height - 1);
        }

        private void bt_stopwatch_1_Click(object sender, EventArgs e)
        {
            //stopwatch play-pause
            if ((flag_mode == _MODE_STOPWATCH) && ((flag_state == _MODE_STOPWATCH_STATE_0) || (flag_state == _MODE_STOPWATCH_STATE_3)))
            {
                sw.Start();
                flag_state = _MODE_STOPWATCH_STATE_1;
                show_main_message1("正數中", S_OK, 30);
            }
            else if ((flag_mode == _MODE_STOPWATCH) && ((flag_state == _MODE_STOPWATCH_STATE_1) || (flag_state == _MODE_STOPWATCH_STATE_3)))
            {
                sw.Stop();
                flag_state = _MODE_STOPWATCH_STATE_2;
                show_main_message1("正數暫停", S_OK, 30);
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_2))
            {
                sw.Start();
                flag_state = _MODE_STOPWATCH_STATE_1;
                show_main_message1("正數繼續", S_OK, 30);
            }
            //richTextBox1.Text += "b17, flag_state = " + flag_state.ToString() + "\n";
        }

        private void bt_stopwatch_2_Click(object sender, EventArgs e)
        {
            //stopwatch stop
            if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_0))
            {
                //開始準備中、暫停中、停止中按停止，把數字歸零
                flag_mode = _MODE_STOPWATCH;
                flag_state = _MODE_STOPWATCH_STATE_0;
                digitalDisplayControl1.DigitText = "00:00:00.00";
                show_main_message1("歸零", S_OK, 30);
                sw.Reset();
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_1))
            {
                //正數中按停止，數字停止
                flag_mode = _MODE_STOPWATCH;
                flag_state = _MODE_STOPWATCH_STATE_0;
                show_main_message1("正數停止", S_OK, 30);
                sw.Stop();
            }
            else if ((flag_mode == _MODE_STOPWATCH) && (flag_state == _MODE_STOPWATCH_STATE_2))
            {
                //暫停中、停止中按停止，把數字歸零
                flag_mode = _MODE_STOPWATCH;
                flag_state = _MODE_STOPWATCH_STATE_0;
                digitalDisplayControl1.DigitText = "00:00:00.00";
                show_main_message1("歸零", S_OK, 30);
                sw.Reset();
            }
        }

        private void bt_stopwatch_3_Click(object sender, EventArgs e)
        {
            //stopwatch reset
            if (sw.IsRunning == true)
            {
                sw.Restart();
                digitalDisplayControl1.DigitText = "00:00:00.00";
                show_main_message1("正數重數", S_OK, 30);
            }
            else
            {
                sw.Reset();
                digitalDisplayControl1.DigitText = "00:00:00.00";
                show_main_message1("歸零", S_OK, 30);
            }
        }
    }
}
