using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace vcs_MP3AlarmClock
{
    public partial class Form1 : Form
    {
        string filename = @"D:\vcs\astro\_DATA2\_mp3\陳盈潔_台語精選集6CD\disc3\01.南都夜曲.mp3";
        DateTime dt_new = new DateTime();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = filename;
            lb_date.Text = "";
            lb_time.Text = "";
            lb_mesg.Text = "";
            lb_result.Text = "";
            dt_new = DateTime.Now;
            bt_ack.Visible = false;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //監看時間是否到了
            richTextBox1.Text += ".";

            if (DateTime.Now.ToString() == dt_new.ToString())
            {
                richTextBox1.Text += "時間到了 關t1開t2\n";
                axWindowsMediaPlayer1.URL = textBox1.Text;
                axWindowsMediaPlayer1.Ctlcontrols.play();
                timer1.Enabled = false;
                this.TopMost = true;
                lb_mesg.Text = "時間到";
                bt_ack.Visible = true;
                this.Show();
            }
        }

        private void rb_CheckedChanged(object sender, EventArgs e)
        {
            if (rb1.Checked == true)    //現在
            {
                //lb_date.Visible = true;
                //lb_time.Visible = true;
                //timer_date.Enabled = true;

            }
            else if (rb2.Checked == true)   //設定
            {
                //lb_date.Visible = false;
                //lb_time.Visible = false;
                //timer_date.Enabled = false;

                nud_hh.Visible = true;
                nud_mm.Visible = true;
                nud_ss.Visible = true;

                nud_hh.Value = DateTime.Now.Hour;
                nud_mm.Value = DateTime.Now.Minute;
                nud_ss.Value = DateTime.Now.Second;


            }
            else if (rb3.Checked == true)   //之後
            {
                //lb_date.Visible = false;
                //lb_time.Visible = false;
                //timer_date.Enabled = false;

                nud_hh.Value = 0;
                nud_mm.Value = 10;
                nud_ss.Value = 0;

                int hh = (int)nud_hh.Value;
                int mm = (int)nud_mm.Value;
                int ss = (int)nud_ss.Value;

                DateTime dt = DateTime.Now;

                dt_new = dt.AddHours(hh).AddMinutes(mm).AddSeconds(ss);
                richTextBox1.Text += "設定時間為 : " + dt_new.ToString() + "\n";
                lb_result.Text = dt_new.ToString();
            }
            else    //其他
            {
                lb_date.Visible = false;
                lb_time.Visible = false;
                //timer_date.Enabled = false;

                richTextBox1.Text += "XXXXXX\n";
            }
        }

        private void timer_date_Tick(object sender, EventArgs e)
        {
            // Display the local time.
            DateTime now = DateTime.Now;
            lb_time.Text = now.ToLongTimeString();
            lb_date.Text = now.ToShortDateString();

        }

        private void nud_hhmmss_ValueChanged(object sender, EventArgs e)
        {
            lb_mesg.Text = "";
            bt_ack.Visible = false;
            if (rb1.Checked == true)    //現在
            {
                richTextBox1.Text += "XXXXXX\n";

            }
            else if (rb2.Checked == true)   //設定
            {
                int hh = (int)nud_hh.Value;
                int mm = (int)nud_mm.Value;
                int ss = (int)nud_ss.Value;

                DateTime dt = DateTime.Now;
                dt_new = new DateTime(dt.Year, dt.Month, dt.Day, hh, mm, ss);	//年月日時分秒毫秒

                if (dt_new < dt)
                {
                    richTextBox1.Text += "過去";
                    dt_new = dt_new.AddDays(1);

                }
                else
                {
                    richTextBox1.Text += "未來";
                }

                richTextBox1.Text += "設定時間為 : " + dt_new.ToString() + "\n";
                lb_result.Text = dt_new.ToString();

            }
            else if (rb3.Checked == true)   //之後
            {
                int hh = (int)nud_hh.Value;
                int mm = (int)nud_mm.Value;
                int ss = (int)nud_ss.Value;

                DateTime dt = DateTime.Now;

                dt_new = dt.AddHours(hh).AddMinutes(mm).AddSeconds(ss);
                //richTextBox1.Text += "設定時間為 : " + dt_new.ToString() + "\n";
                lb_result.Text = dt_new.ToString();
            }
            else    //其他
            {
                richTextBox1.Text += "XXXXXX\n";
            }
        }

        private void bt_ok_Click(object sender, EventArgs e)
        {
            if (rb1.Checked == true)    //現在
            {
                richTextBox1.Text += "XXXXXX\n";

            }
            else if (rb2.Checked == true)   //設定
            {
                timer1.Enabled = true;
                lb_mesg.Text = "已設定";
                richTextBox1.Text += "設定時間為 : " + dt_new.ToString() + "\n";
                this.Hide();
            }
            else if (rb3.Checked == true)   //之後
            {
                timer1.Enabled = true;
                lb_mesg.Text = "已設定";
                richTextBox1.Text += "設定時間為 : " + dt_new.ToString() + "\n";
                this.Hide();
            }
            else    //其他
            {
                richTextBox1.Text += "XXXXXX\n";
            }
        }

        private void bt_cancel_Click(object sender, EventArgs e)
        {

        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt_ack_Click(object sender, EventArgs e)
        {
            bt_ack.Visible = false;
            axWindowsMediaPlayer1.Ctlcontrols.stop();
            lb_mesg.Text = "";
            lb_result.Text = "";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //選檔
            openFileDialog1.Filter = "mp3 (*.mp3)|*.mp3|avi (*.avi)|*.avi|mp4 (*.mp4)|*.mp4";
            openFileDialog1.InitialDirectory = @"D:\vcs\astro\_DATA2\_mp3\";    //對話方塊的初始目錄
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //試聽
            if (button2.Text == "試聽")
            {
                button2.Text = "停止";
                axWindowsMediaPlayer1.URL = textBox1.Text;
                axWindowsMediaPlayer1.Ctlcontrols.play();
            }
            else
            {
                button2.Text = "試聽";
                axWindowsMediaPlayer1.Ctlcontrols.stop();
            }


        }
    }
}

