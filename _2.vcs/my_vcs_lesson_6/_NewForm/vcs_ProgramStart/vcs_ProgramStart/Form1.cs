using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ProgramStart
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            progressBar1.Minimum = 0;               //设定ProgressBar控件的最小值为0
            progressBar1.Maximum = 10;              //设定ProgressBar控件的最大值为10
            progressBar1.MarqueeAnimationSpeed = 100; //设定ProgressBar控件进度块在进度栏中移动的时间段
            Counter.Start();                       //启动计时器
        }

        private void Counter_Tick(object sender, EventArgs e)
        {
            this.Hide();                           //隐藏本窗体
            Form2 f2 = new Form2();  //实例化一个Form2对象
            f2.Show();                                 //显示窗体f2
            Counter.Stop();                                  //停止计时器

        }
    }
}
