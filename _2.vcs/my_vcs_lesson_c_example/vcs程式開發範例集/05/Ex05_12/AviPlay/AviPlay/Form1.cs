using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace AviPlay
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //this.axAnimation1.AutoPlay = true;
            this.axAnimation1.Open(Application.StartupPath + "//clock.avi");
            
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                this.axAnimation1.Stop();
                object start = this.textBox1.Text;
                object end = this.textBox2.Text;
                object time = 20;
                this.axAnimation1.Play(time, start, end);
            }
            catch(Exception ey)
            {
                MessageBox.Show("請輸入正確幀數，本程序將關閉！！！");
                Application.Exit();
            } 
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.axAnimation1.Play();
        }
    }
}