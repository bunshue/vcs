using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ClockingPlayImplement
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
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
            this.Hide();
            this.ShowInTaskbar = false;//不在任务栏显现
          
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (this.openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                this.textBox1.Text = this.openFileDialog1.FileName;
            }
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            if (this.axWindowsMediaPlayer1.status != "正在播放")
            {
                this.timer2.Enabled = false;
                MessageBox.Show("本次播放以完成，谢谢使用！！！");
                
            }
        }
    }
}