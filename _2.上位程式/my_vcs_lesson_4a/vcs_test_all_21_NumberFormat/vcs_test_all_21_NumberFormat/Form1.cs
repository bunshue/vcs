using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_21_NumberFormat
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        int value = 12345;
        double value2 = 123.456;
        double value3 = 1234.5678;
        private void button1_Click(object sender, EventArgs e)
        {
            textBox1.Text = value.ToString("D");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            textBox1.Text = value.ToString("D8");
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox1.Text = value.ToString("X");
        }

        private void button4_Click(object sender, EventArgs e)
        {
            textBox1.Text = value.ToString("X8");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            textBox1.Text = value2.ToString("F4");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#0.0");         //格式化，小數點後留1位
        }

        private void button7_Click(object sender, EventArgs e)
        {
            textBox1.Text = value3.ToString("#00000.000");   //格式化，小數點前5位，小數點後留3位四捨五入
        }
    }
}
