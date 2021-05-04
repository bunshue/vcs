﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void colorOption1_Click(object sender, EventArgs e)
        {
            clockText.ForeColor = Color.Black;
        }
        private void colorOption2_Click(object sender, EventArgs e)
        {
            clockText.ForeColor = Color.Red;
        }
        private void colorOption3_Click(object sender, EventArgs e)
        {
            clockText.ForeColor = Color.Blue;
        }

        private void startButton_Click(object sender, EventArgs e)
        {
            if (timeOption1.Checked)
                clockText.Text = "300";
            else if (timeOption2.Checked)
                clockText.Text = "180";
            else if (timeOption3.Checked)
                clockText.Text = "60";
            else{
                MessageBox.Show("您尚未選定倒數的時間長短");
                clockText.Text = "0";
            }

            timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            int oldTime = Int32.Parse(clockText.Text);

            if (oldTime == 0){
                timer1.Enabled = false;
                MessageBox.Show("倒數計時結束!!!");
            }
            else{
                int newTime = --oldTime;
                clockText.Text = newTime.ToString();

                if (timeOption1.Checked)
                    progressBar1.Value = (300 - newTime) * 100 / 300;
                else if (timeOption2.Checked)
                    progressBar1.Value = (180 - newTime) * 100 / 180;
                else if (timeOption3.Checked)
                    progressBar1.Value = (60 - newTime) * 100 / 60;
            }
        }


    }
}
