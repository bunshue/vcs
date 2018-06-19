using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace my_vcs_18_跑馬燈
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string g_str = "王昌齡 出塞 秦時明月漢時關，萬里長征人未還。但使龍城飛將在，不教胡馬度陰山。";
        private void timer1_Tick(object sender, EventArgs e)
        {
            string temp = g_str.Substring(0, 1);
            g_str = g_str.Substring(1, g_str.Length - 1) + temp;
            label1.Text = g_str;
        }
    }
}
