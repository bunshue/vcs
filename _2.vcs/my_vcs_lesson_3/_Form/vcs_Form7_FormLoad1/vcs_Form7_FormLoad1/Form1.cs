using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form7_FormLoad1
{
    public partial class Form1 : Form
    {
        private bool showing = true;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //窗體顯示特效
            Opacity = 0.0; //窗體透明度為0

            timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            double d = 0.10;
            if (showing)
            {
                if (Opacity + d >= 1.0)
                {
                    Opacity = 1.0;
                    timer1.Stop();
                    label1.Text += ", 啟動完成";
                }
                else
                {
                    Opacity += d;
                }
            }
            else
            {
                if (Opacity - d <= 0.0)
                {
                    Opacity = 0.0;
                    timer1.Stop();
                }
                else
                {
                    Opacity -= d;
                }
            }
        }
    }
}

