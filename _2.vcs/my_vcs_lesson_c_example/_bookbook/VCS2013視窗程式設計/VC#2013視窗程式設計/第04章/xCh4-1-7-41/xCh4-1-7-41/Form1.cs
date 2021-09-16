using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_7_41
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double stdHeight = 0;
            if (radioButton1.Checked)
                stdHeight = (double.Parse(textBox1.Text) - 80) * 0.7;
            else
                stdHeight = (double.Parse(textBox1.Text) - 70) * 0.6;

            double min = stdHeight * 0.9;
            double max = stdHeight * 1.1;
            double nowHeight = double.Parse(textBox2.Text.ToString());
            string normalOrNot = (nowHeight >= min & nowHeight <= max 
                ? "標準" 
                : "要注意喔");

            string msg = "您的標準體重應該是：" + stdHeight.ToString()
                +"\n您目前的體重是："+normalOrNot;
            MessageBox.Show(msg);
        }
    }
}
