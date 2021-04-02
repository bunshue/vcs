using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 取得系統啟動後經過的時間
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            textBox1.Text = (Environment.TickCount / 1000).ToString() + "秒";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.Text = (Environment.TickCount / 1000).ToString() + "秒";
        }
    }
}
