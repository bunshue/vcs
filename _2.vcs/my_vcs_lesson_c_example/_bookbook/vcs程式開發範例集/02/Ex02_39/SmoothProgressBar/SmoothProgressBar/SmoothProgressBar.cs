using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using WindowsFormsControlLibrary;

namespace SmoothProgressBar
{
    public partial class SmoothProgressBar : Form
    {
        public SmoothProgressBar()
        {
            InitializeComponent();
        }

        private void SmoothProgressBar_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (this.smoothProgressBar1.Value > 0) //當smoothProgressBar1控件的當前值大於0時
            {
                this.smoothProgressBar1.Value--;//設置smoothProgressBar1控件的當前值遞減
                this.smoothProgressBar2.Value++;//設置smoothProgressBar2控件的當前值遞增
            }
            else//當smoothProgressBar1控件的當前值小於0時
            {
                this.timer1.Enabled = false;//使Timer組件處於不可用狀態
            }
        }

        private void StartOrStop_Click(object sender, EventArgs e)
        {
            this.smoothProgressBar1.Value = 100;//設置smoothProgressBar1的值為100
            this.smoothProgressBar2.Value = 0;//設置smoothProgressBar2的值為0

            this.timer1.Interval = 1;//設置Timer組件的Tick事件的時間間隔
            this.timer1.Enabled = true;//設置Timer組件為可用狀態
        }
    }
}
