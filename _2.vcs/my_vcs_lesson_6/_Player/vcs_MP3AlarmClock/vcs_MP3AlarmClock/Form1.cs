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

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.textBox1.Text = filename;

            textBox2.Text = DateTime.Now.AddMinutes(2).ToShortTimeString();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            richTextBox1.Text += DateTime.Now.ToShortTimeString() + "\t" + this.textBox2.Text.Trim().ToString() + "\n";
            if (DateTime.Now.ToShortTimeString() == this.textBox2.Text.Trim().ToString())
            {
                this.axWindowsMediaPlayer1.URL = this.textBox1.Text;
                this.axWindowsMediaPlayer1.Ctlcontrols.play();
                this.timer1.Enabled = false;
                this.timer2.Enabled = true;
                this.timer2.Interval = 1000;
                this.Show();
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.timer1.Enabled = true;
            //this.Hide();
            //this.ShowInTaskbar = false;//不在任务栏显现

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (this.axWindowsMediaPlayer1.status != "正在播放")
            {
                this.timer2.Enabled = false;
                richTextBox1.Text += "時間到\n";
            }
        }
    }
}
