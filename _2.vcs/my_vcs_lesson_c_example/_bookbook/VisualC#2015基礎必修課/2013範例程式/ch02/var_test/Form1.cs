using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace var_test
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num1;
            num1 = 20;
            label1.Text = num1.ToString();      // 顯示 20
            float num2;
            num2 = 123456789;
            label2.Text = num2.ToString();   		 // 顯示 1.234568E+08
            string str1;
            str1 = "哈囉！";
            string name = "Mr. White";
            label3.Text = str1 + name;        // 顯示 “哈囉!  Mr. White“
            label4.Text = DateTime.Now.ToString(); // 顯示目前的完整日期時間
        }
    }
}
