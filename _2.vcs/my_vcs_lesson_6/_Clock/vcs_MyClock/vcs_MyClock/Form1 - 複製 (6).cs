﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MyClock
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private const int _MODE_CLOCK = 0;  //一般
        private const int _MODE_COUNTR = 1;  //正數
        private const int _MODE_TIMER = 2;  //倒數
        private const int _MODE_ALARM = 3;  //鬧鐘

        //一般
        private const int _MODE_CLOCK_STATE_0 = 0;  //一般

        //正數
        private const int _MODE_COUNTR_STATE_0 = 0;  //正數準備中
        private const int _MODE_COUNTR_STATE_1 = 1;  //正數中、正數繼續
        private const int _MODE_COUNTR_STATE_2 = 2;  //正數暫停
        private const int _MODE_COUNTR_STATE_3 = 3;  //正數暫停歸零中

        //倒數
        private const int _MODE_TIMER_STATE_0 = 0;  //倒數準備中
        private const int _MODE_TIMER_STATE_1 = 1;  //倒數中
        private const int _MODE_TIMER_STATE_2 = 2;  //倒數暫停
        private const int _MODE_TIMER_STATE_3 = 3;  //倒數時間到

        //鬧鐘
        private const int _MODE_ALARM_STATE_0 = 0;  //鬧鐘

        int flag_mode = _MODE_CLOCK;    //0:時鐘、1:正數、2:倒數、3:鬧鐘
        int flag_state = _MODE_CLOCK_STATE_0;

        int total_count_down_sec = 0;
        System.DateTime time_stop;
        System.DateTime time_start;
        System.DateTime time_pause_start;
        System.DateTime time_pause_stop;

        //int status = 0;
        System.DateTime time_sp;
        System.DateTime time_st;
        TimeSpan time_diff;
        TimeSpan time_diff_total;

        private void Form1_Load(object sender, EventArgs e)
        {
            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            label1.Text = "";
            lb_mesg.Text = "";
            //this.FormBorderStyle = FormBorderStyle.None;
            time_pause_start = DateTime.Now;
            time_pause_stop = time_pause_start;

            time_st = DateTime.Now;
            time_sp = DateTime.Now;
            time_diff = time_sp - time_st;
            time_diff_total = time_diff;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt_now = DateTime.Now;
            if ((flag_mode == _MODE_CLOCK) && (flag_state == _MODE_CLOCK_STATE_0))
            {
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            }
            else if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_1))
            {
                if (time_stop <= dt_now)
                {
                    button1.Text = "時間到";
                    this.TopMost = true;
                    //timer1.Enabled = false;
                    flag_state = _MODE_TIMER_STATE_3;
                    //digitalDisplayControl1.BackColor = Color.Red;
                    this.BackColor = Color.Red;
                    this.WindowState = FormWindowState.Normal;
                    digitalDisplayControl1.DigitColor = Color.Purple;
                    digitalDisplayControl1.DigitText = "00.00";
                    label1.Text = "";
                }
                else
                {
                    TimeSpan ts1 = time_stop - dt_now;
                    double remain1 = Convert.ToDouble(ts1.TotalSeconds);
                    double remain2;
                    int hh;
                    int mm;
                    int ss;
                    double ms;
                    hh = (int)remain1 / 3600;
                    mm = (int)(remain1 % 3600) / 60;
                    ss = (int)remain1 % 60;
                    ms = remain1 % 1;
                    remain2 = hh * 10000 + mm * 100 + ss + ms;
                    if (remain1 > 3600)
                        digitalDisplayControl1.DigitText = remain2.ToString("00:00:00.00");
                    else if (remain1 > 60)
                        digitalDisplayControl1.DigitText = remain2.ToString("00:00.00");
                    else
                        digitalDisplayControl1.DigitText = remain2.ToString("00.00");

                    label1.Text = dt_now.ToString();
                }
            }
            else if ((flag_mode == _MODE_COUNTR) && (flag_state == _MODE_COUNTR_STATE_1))
            {
                TimeSpan ts2 = dt_now - time_start;
                double count1 = Convert.ToDouble(ts2.TotalSeconds) - Convert.ToDouble(time_diff_total.TotalSeconds);
                double count2;
                int hh;
                int mm;
                int ss;
                double ms;
                hh = (int)count1 / 3600;
                mm = (int)(count1 % 3600) / 60;
                ss = (int)count1 % 60;
                ms = count1 % 1;
                count2 = hh * 10000 + mm * 100 + ss + ms;
                if (count2 > 3600)
                    digitalDisplayControl1.DigitText = count2.ToString("00:00:00.00");
                else if (count2 > 60)
                    digitalDisplayControl1.DigitText = count2.ToString("00:00.00");
                else
                    digitalDisplayControl1.DigitText = count2.ToString("00.00");

                label1.Text = dt_now.ToString();

            }
            else if ((flag_mode == _MODE_COUNTR) && (flag_state == _MODE_COUNTR_STATE_2))
            {
                label1.Text = dt_now.ToString();
            }
            else if ((flag_mode == _MODE_COUNTR) && (flag_state == _MODE_COUNTR_STATE_3))
            {
                digitalDisplayControl1.DigitText = "00.00";
                label1.Text = dt_now.ToString();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_0))
            {
                flag_state = _MODE_TIMER_STATE_1;
                button1.Text = "倒數中";
                lb_mesg.Text = "正數";
                button1.BackColor = Color.Pink;
                digitalDisplayControl1.DigitColor = Color.Red;
                this.TopMost = false;
                int hh = (int)numericUpDown1.Value;
                int mm = (int)numericUpDown2.Value;
                int ss = (int)numericUpDown3.Value;
                total_count_down_sec = hh * 60 * 60 + mm * 60 + ss;
                //richTextBox1.Text += "total_count_down_sec = " + total_count_down_sec.ToString() + "\n";


                System.DateTime dt = System.DateTime.Now;
                //richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
                //richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

                //現在時間減分鐘寫法
                time_stop = dt.AddSeconds(total_count_down_sec);
                //richTextBox1.Text += "現在時間加" + total_count_down_sec.ToString() + "秒： " + time_stop.ToLongTimeString() + Environment.NewLine;
                //timer1.Enabled = true;
                label1.Text = dt.ToString();
                richTextBox1.Text += "1111111111\n";
            }
            else if ((flag_mode == _MODE_TIMER) && ((flag_state == _MODE_TIMER_STATE_1) || (flag_state == _MODE_TIMER_STATE_3)))
            {
                //倒數取消
                flag_state = _MODE_TIMER_STATE_0;
                button1.Text = "倒數";
                lb_mesg.Text = "正數";
                button1.BackColor = System.Drawing.SystemColors.Control;
                this.TopMost = false;
                //digitalDisplayControl1.BackColor = Color.Transparent;
                //this.BackColor = System.Drawing.SystemColors.Control;
                this.BackColor = default(Color);
                digitalDisplayControl1.DigitColor = Color.Purple;
                richTextBox1.Text += "2222222222\n";
            }
            else
            {
            }
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            flag_mode = _MODE_CLOCK;
            flag_state = _MODE_CLOCK_STATE_0;
            lb_mesg.Text = "時鐘模式";
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            flag_mode = _MODE_COUNTR;
            flag_state = _MODE_COUNTR_STATE_0;
            digitalDisplayControl1.DigitText = "00.00";
            lb_mesg.Text = "正數模式";
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            flag_mode = _MODE_TIMER;
            flag_state = _MODE_TIMER_STATE_0;
            digitalDisplayControl1.DigitText = "00.00";
            lb_mesg.Text = "倒數模式";
        }

        private void radioButton4_CheckedChanged(object sender, EventArgs e)
        {
            flag_mode = _MODE_ALARM;
            flag_state = _MODE_ALARM_STATE_0;
            //digitalDisplayControl1.DigitText = "00.00";
            lb_mesg.Text = "鬧鐘模式";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_0))
            {
                flag_state = _MODE_TIMER_STATE_1;
                button1.Text = "倒數中";
                lb_mesg.Text = "正數";
                button1.BackColor = Color.Pink;
                digitalDisplayControl1.DigitColor = Color.Red;
                this.TopMost = false;
                int hh = (int)numericUpDown1.Value;
                int mm = (int)numericUpDown2.Value;
                int ss = (int)numericUpDown3.Value;
                total_count_down_sec = hh * 60 * 60 + mm * 60 + ss;
                //richTextBox1.Text += "total_count_down_sec = " + total_count_down_sec.ToString() + "\n";


                System.DateTime dt = System.DateTime.Now;
                //richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
                //richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

                //現在時間減分鐘寫法
                time_stop = dt.AddSeconds(total_count_down_sec);
                //richTextBox1.Text += "現在時間加" + total_count_down_sec.ToString() + "秒： " + time_stop.ToLongTimeString() + Environment.NewLine;
                //timer1.Enabled = true;
                label1.Text = dt.ToString();
                richTextBox1.Text += "1111111111\n";
            }

        }

        private void button8_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_TIMER) && ((flag_state == _MODE_TIMER_STATE_1) || (flag_state == _MODE_TIMER_STATE_3)))
            {
                //倒數取消
                flag_state = _MODE_TIMER_STATE_0;
                button1.Text = "倒數";
                lb_mesg.Text = "倒數取消";
                button1.BackColor = System.Drawing.SystemColors.Control;
                this.TopMost = false;
                //digitalDisplayControl1.BackColor = Color.Transparent;
                //this.BackColor = System.Drawing.SystemColors.Control;
                this.BackColor = default(Color);
                digitalDisplayControl1.DigitColor = Color.Purple;
                richTextBox1.Text += "2222222222\n";
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_COUNTR) && ((flag_state == _MODE_COUNTR_STATE_0) || (flag_state == _MODE_COUNTR_STATE_3)))
            {
                flag_state = _MODE_COUNTR_STATE_1;
                time_start = DateTime.Now;
                lb_mesg.Text = "正數中";
                time_pause_stop = time_pause_start;
            }
            else if ((flag_mode == _MODE_COUNTR) && ((flag_state == _MODE_COUNTR_STATE_1) || (flag_state == _MODE_COUNTR_STATE_3)))
            {
                flag_state = _MODE_COUNTR_STATE_2;
                lb_mesg.Text = "正數暫停";
                time_pause_start = DateTime.Now;
                time_st = DateTime.Now;

            }
            else if ((flag_mode == _MODE_COUNTR) && (flag_state == _MODE_COUNTR_STATE_2))
            {
                flag_state = _MODE_COUNTR_STATE_1;
                lb_mesg.Text = "正數繼續";
                time_pause_stop = DateTime.Now;

                time_sp = DateTime.Now;
                time_diff = time_sp - time_st;
                time_diff_total += time_diff;
                //richTextBox1.Text += "SP diff = " + Convert.ToInt32(time_diff.TotalSeconds).ToString() + " diff_total = " + Convert.ToInt32(time_diff_total.TotalSeconds).ToString() + "\n";
            }
            richTextBox1.Text += "b17, flag_state = " + flag_state.ToString() + "\n";



        }

        private void button18_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_COUNTR) && (flag_state == _MODE_COUNTR_STATE_0))
            {
                //開始準備中、暫停中、停止中按停止，把數字歸零
                flag_mode = _MODE_COUNTR;
                flag_state = _MODE_COUNTR_STATE_0;
                digitalDisplayControl1.DigitText = "00.00";
                time_st = DateTime.Now;
                time_sp = DateTime.Now;
                time_diff = time_sp - time_st;
                time_diff_total = time_diff;
                time_pause_stop = time_pause_start;
            }
            else if ((flag_mode == _MODE_COUNTR) && (flag_state == _MODE_COUNTR_STATE_1))
            {
                //正數中按停止，數字停止
                flag_mode = _MODE_COUNTR;
                flag_state = _MODE_COUNTR_STATE_0;
                //digitalDisplayControl1.DigitText = "00.00";
                time_st = DateTime.Now;
                time_sp = DateTime.Now;
                time_diff = time_sp - time_st;
                time_diff_total = time_diff;
                time_pause_stop = time_pause_start;
            }
            else if ((flag_mode == _MODE_COUNTR) && (flag_state == _MODE_COUNTR_STATE_2))
            {
                //暫停中、停止中按停止，把數字歸零
                flag_mode = _MODE_COUNTR;
                flag_state = _MODE_COUNTR_STATE_0;
                digitalDisplayControl1.DigitText = "00.00";
                time_st = DateTime.Now;
                time_sp = DateTime.Now;
                time_diff = time_sp - time_st;
                time_diff_total = time_diff;
                time_pause_stop = time_pause_start;
            }

        }

        private void button3_Click(object sender, EventArgs e)
        {
            if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_0))
            {
                flag_state = _MODE_TIMER_STATE_1;   //倒數中
                button1.Text = "倒數中";
                lb_mesg.Text = "正數";
                button1.BackColor = Color.Pink;
                digitalDisplayControl1.DigitColor = Color.Red;
                this.TopMost = false;
                int hh = (int)numericUpDown1.Value;
                int mm = (int)numericUpDown2.Value;
                int ss = (int)numericUpDown3.Value;
                total_count_down_sec = hh * 60 * 60 + mm * 60 + ss;
                //richTextBox1.Text += "total_count_down_sec = " + total_count_down_sec.ToString() + "\n";


                System.DateTime dt = System.DateTime.Now;
                //richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
                //richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

                //現在時間減分鐘寫法
                time_stop = dt.AddSeconds(total_count_down_sec);
                //richTextBox1.Text += "現在時間加" + total_count_down_sec.ToString() + "秒： " + time_stop.ToLongTimeString() + Environment.NewLine;
                //timer1.Enabled = true;
                label1.Text = dt.ToString();
                richTextBox1.Text += "1111111111\n";
            }
            //else if ((flag_mode == _MODE_TIMER) && ((flag_state == _MODE_TIMER_STATE_1) || (flag_state == _MODE_TIMER_STATE_3)))
            else if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_1))
            {
                //倒數暫停
                flag_state = _MODE_TIMER_STATE_2;   //倒數暫停
                button1.Text = "倒數";
                lb_mesg.Text = "倒數暫停";
                button1.BackColor = System.Drawing.SystemColors.Control;
                this.TopMost = false;
                //digitalDisplayControl1.BackColor = Color.Transparent;
                //this.BackColor = System.Drawing.SystemColors.Control;
                this.BackColor = default(Color);
                digitalDisplayControl1.DigitColor = Color.Purple;
                richTextBox1.Text += "2222222222\n";
            }
            else if ((flag_mode == _MODE_TIMER) && (flag_state == _MODE_TIMER_STATE_2))
            {
                flag_state = _MODE_TIMER_STATE_1;   //繼續倒數中
                button1.Text = "倒數中";
                lb_mesg.Text = "繼續倒數中";
                button1.BackColor = Color.Pink;
                digitalDisplayControl1.DigitColor = Color.Red;
                this.TopMost = false;
                /*
                int hh = (int)numericUpDown1.Value;
                int mm = (int)numericUpDown2.Value;
                int ss = (int)numericUpDown3.Value;
                total_count_down_sec = hh * 60 * 60 + mm * 60 + ss;
                //richTextBox1.Text += "total_count_down_sec = " + total_count_down_sec.ToString() + "\n";


                System.DateTime dt = System.DateTime.Now;
                //richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
                //richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

                //現在時間減分鐘寫法
                time_stop = dt.AddSeconds(total_count_down_sec);
                //richTextBox1.Text += "現在時間加" + total_count_down_sec.ToString() + "秒： " + time_stop.ToLongTimeString() + Environment.NewLine;
                //timer1.Enabled = true;
                label1.Text = dt.ToString();
                richTextBox1.Text += "1111111111\n";
                */
            
            }

        }


    }
}
