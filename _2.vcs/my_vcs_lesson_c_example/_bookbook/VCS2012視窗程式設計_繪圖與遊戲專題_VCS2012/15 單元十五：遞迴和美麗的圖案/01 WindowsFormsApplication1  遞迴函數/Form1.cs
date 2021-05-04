using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int k = Convert.ToInt32(textBox1.Text);  // 字串 轉為 整數

            long sol = 1; // 最後的階乘答案
            for (int i = k; i >= 1; i--) // k!
                sol = sol * i;

            label1.Text = sol.ToString(); // 整數 轉為 字串 
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int k = Convert.ToInt32(textBox1.Text);  // 字串 轉為 整數
            long sol = factorial(k); // 使用 遞迴函數

            label1.Text = sol.ToString(); // 整數 轉為 字串 
        }

        long factorial(int k) // Recursive 遞迴函數  k!
        {
            if (k > 1)
                return k * factorial(k - 1); // k! = k * (k-1)!
            else
                return 1; // 1! = 1
        }
    }
}