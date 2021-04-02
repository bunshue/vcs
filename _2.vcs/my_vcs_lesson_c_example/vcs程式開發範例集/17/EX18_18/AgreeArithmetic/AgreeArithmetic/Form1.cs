using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace AgreeArithmetic
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();//清空ListBox控制元件
            int p = 0, n = 0, a = 1, b = 1;//定義變數
            try
            {
                p = Convert.ToInt32(textBox1.Text);//將字符型轉換成數值型
            }
            catch//出現錯誤
            {
                MessageBox.Show("請輸入數值型數據");//彈出提示框
                textBox1.Text = "15";
                return;
            }
            for (n = 1; n <= p; n++)//對輸入的數值進行搜尋
            {
                listBox1.Items.Add(a.ToString());//輸出數值
                listBox1.Items.Add(b.ToString());//輸出數值
                a = a + b;//取得前兩個數的和
                b = a + b;//取得前兩個數的和
            }
        }
    }
}
