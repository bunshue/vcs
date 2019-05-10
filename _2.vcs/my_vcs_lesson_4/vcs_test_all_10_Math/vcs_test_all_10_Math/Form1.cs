using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_10_Math
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "pi = " + Math.PI.ToString() + "\n";
            richTextBox1.Text += "e = " + Math.E.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int r = 5;
            int value = -5;
            int aa = 123;
            int bb = 456;

            richTextBox1.Text += "圓面積 = " + (Math.PI * Math.Pow(r, 2)).ToString() + "\n";
            richTextBox1.Text += "-5的絕對值 = " + (Math.Abs(value)).ToString() + "\n";
            richTextBox1.Text += "兩者取大 = " + (Math.Max(aa, bb)).ToString() + "\n";
            richTextBox1.Text += "兩者取小 = " + (Math.Min(aa, bb)).ToString() + "\n";

            float result = 0;
            int a = 11;
            int b = 3;
            int c = 0;
            result = (float)a / b;
            richTextBox1.Text += "result = " + result.ToString() + "\n";
            c = (int)Math.Round(result);
            richTextBox1.Text += "四捨五入c = " + c.ToString() + "\n";
            c = (int)Math.Floor(result);
            richTextBox1.Text += "無條件捨去c = " + c.ToString() + "\n";
            c = (int)Math.Ceiling(result);
            richTextBox1.Text += "無條件進位c = " + c.ToString() + "\n";
        
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "未完成\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Random r = new Random();
            string result1 = "";
            string result2 = "";
            string result3 = "";
            string result4 = "";
            for (int i = 0; i < 5; i++)
            {
                result1 += r.Next().ToString() + " ";
                result2 += r.Next(10).ToString() + " ";
                result3 += r.Next(10, 20).ToString() + " ";
                result4 += r.NextDouble().ToString() + " ";
            }
            richTextBox1.Text += "取>=0的亂數值：" + result1 + "\n";
            richTextBox1.Text += "取0~10的亂數值：" + result2 + "\n";
            richTextBox1.Text += "取10~20的亂數值：" + result3 + "\n";
            richTextBox1.Text += "取0.0~1.0的亂數值：" + result4 + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "未完成\n";
        }
    }
}
