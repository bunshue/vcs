using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Form7_FadeInFadeOut
{
    public partial class Form1 : Form
    {
        private int state;//淡入\淡出狀態

        private double inspeed;
        private double outspeed;

        public double InSpeed //淡入速度屬性（0---100）
        {
            get
            {
                return inspeed;
            }
            set
            {
                inspeed = value;
            }
        }

        public double OutSpeed //淡出速度屬性（0---100）
        {
            get
            {
                return outspeed;
            }
            set
            {
                outspeed = value;
            }
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            inspeed = 10;
            outspeed = 10;
            state = 0;  //啟動表單
            this.Opacity = 0;
            timer1.Enabled = true;
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (state >= 0) //啟動表單
            {
                this.Opacity += inspeed / 100;
                if (this.Opacity == 1)
                {
                    timer1.Enabled = false;
                }
            }
            else if (state < 0) //關閉表單
            {
                this.Opacity -= outspeed / 100;
                if (this.Opacity == 0)
                {
                    this.Close();
                    timer1.Enabled = false;
                }
            }
        }

        public void FormClose()//窗體關閉時，調用此函數實現淡出效果
        {
            state = -1; //關閉表單
            timer1.Enabled = true;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            FormClose();
        }
    }
}

