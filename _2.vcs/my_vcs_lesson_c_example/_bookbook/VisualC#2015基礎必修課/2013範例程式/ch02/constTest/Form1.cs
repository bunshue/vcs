using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace constTest
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            const double  PI = 3.14;   // 宣告PI為常數名稱
            int radius;
            radius = 100;
            label1.Text = "1. 圓周率: " + PI;
            label2.Text = "2. 半  徑: " + radius + "公分";
            label3.Text = "3. 圓周長: " + 2 * PI * radius + "公分";
            label4.Text = "4. 圓面積: " + PI * radius * radius + "平方公分";
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void label3_Click(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
