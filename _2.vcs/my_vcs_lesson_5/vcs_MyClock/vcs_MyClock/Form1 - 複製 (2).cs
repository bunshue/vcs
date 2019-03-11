using System;
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

        int flag_clock_mode = 0;
        int total_count_down_sec = 0;
        System.DateTime time_stop;
        System.DateTime time_start;
        System.DateTime time_pause_start;
        System.DateTime time_pause_stop;

        int status = 0;
        System.DateTime time_sp;
        System.DateTime time_st;
        TimeSpan time_diff;
        TimeSpan time_diff_total;

        //TimeSpan ts3 = time_pause_stop - time_pause_start;

        private void Form1_Load(object sender, EventArgs e)
        {
            digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            label1.Text = "";
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
            if (flag_clock_mode == 0)
            {
                digitalDisplayControl1.DigitText = DateTime.Now.ToString("HH:mm:ss");
            }
            else if (flag_clock_mode == 1)
            {
                if (time_stop <= dt_now)
                {
                    button1.Text = "時間到";
                    this.TopMost = true;
                    //timer1.Enabled = false;
                    flag_clock_mode = 2;
                    //digitalDisplayControl1.BackColor = Color.Red;
                    this.BackColor = Color.Red;
                    this.WindowState = FormWindowState.Normal;
                    digitalDisplayControl1.DigitColor = Color.Purple;
                    label1.Text = "";
                }
                else
                {
                    TimeSpan ts1 = time_stop - dt_now;
                    int remain1 = Convert.ToInt32(ts1.TotalSeconds);
                    int remain2;
                    int hh;
                    int mm;
                    int ss;
                    hh = remain1 / 3600;
                    mm = (remain1 % 3600) / 60;
                    ss = remain1 % 60;
                    remain2 = hh * 10000 + mm * 100 + ss;
                    digitalDisplayControl1.DigitText = remain2.ToString("00:00:00");
                    label1.Text = dt_now.ToString();
                }
            }
            else if (flag_clock_mode == 3)
            {
                TimeSpan ts2 = dt_now - time_start;
                TimeSpan ts3 = time_pause_stop - time_pause_start;
                int count1 = Convert.ToInt32(ts2.TotalSeconds) - Convert.ToInt32(ts3.TotalSeconds);
                //richTextBox1.Text += count1.ToString() + " ";
                richTextBox1.Text += Convert.ToInt32(ts3.TotalSeconds).ToString() + " ";
                int count2;
                int hh;
                int mm;
                int ss;
                hh = count1 / 3600;
                mm = (count1 % 3600) / 60;
                ss = count1 % 60;
                count2 = hh * 10000 + mm * 100 + ss;
                digitalDisplayControl1.DigitText = count2.ToString("00:00:00");
                label1.Text = dt_now.ToString();

            }
            else if (flag_clock_mode == 4)
            {
                label1.Text = dt_now.ToString();
            }
            else if (flag_clock_mode == 5)
            {
                digitalDisplayControl1.DigitText = "00:00:00";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (flag_clock_mode == 0)
            {
                flag_clock_mode = 1;
                button1.Text = "倒數中";
                button2.Text = "正數";
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
            }
            else if ((flag_clock_mode == 1) || (flag_clock_mode == 2))
            {
                flag_clock_mode = 0;
                button1.Text = "倒數";
                button2.Text = "正數";
                button1.BackColor = System.Drawing.SystemColors.Control;
                this.TopMost = false;
                //digitalDisplayControl1.BackColor = Color.Transparent;
                //this.BackColor = System.Drawing.SystemColors.Control;
                this.BackColor = default(Color);
                digitalDisplayControl1.DigitColor = Color.Purple;
            }
            else
            {
                button2.Text = "取消正數";
                flag_clock_mode = 0;
            }
            richTextBox1.Text += "mode = " + flag_clock_mode.ToString() + "\n";
        }

        private void button2_Click_1(object sender, EventArgs e)
        {
            if ((flag_clock_mode == 0) || (flag_clock_mode == 5))
            {
                flag_clock_mode = 3;
                time_start = DateTime.Now;
                button2.Text = "正數中";
                time_pause_stop = time_pause_start;
            }
            else if (flag_clock_mode == 3)
            {
                flag_clock_mode = 4;
                button2.Text = "正數暫停";
                time_pause_start = DateTime.Now;
            }
            else if (flag_clock_mode == 4)
            {
                flag_clock_mode = 3;
                button2.Text = "正數中";
                time_pause_stop = DateTime.Now;
            }
            richTextBox1.Text += "st = " + time_pause_start.ToString() + " sp = " + time_pause_stop.ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (flag_clock_mode < 3)
            { 
            
            }
            else if (flag_clock_mode == 4)
            {
                flag_clock_mode = 5;
                button2.Text = "正數歸零";
            }
            else
            {
                flag_clock_mode = 3;
                time_start = DateTime.Now;
                time_pause_stop = time_pause_start;
            }
        }
        /*
        System.DateTime time_sp;
        System.DateTime time_st;
        TimeSpan time_diff;
        TimeSpan time_diff_total;
        */

		/*
        private void button4_Click(object sender, EventArgs e)
        {
            if (status == 0)
            {
                status = 1;
                time_st = DateTime.Now;
                richTextBox1.Text += "ST ";
            
            }
            else if (status == 1)
            {
                status = 0;
                time_sp = DateTime.Now;
                time_diff = time_sp - time_st;
                time_diff_total += time_diff;
                richTextBox1.Text += "SP diff = " + Convert.ToInt32(time_diff.TotalSeconds).ToString() + " diff_total = " + Convert.ToInt32(time_diff_total.TotalSeconds).ToString() + "\n";
            
            }


        }
		*/
    }
}

