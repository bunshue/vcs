using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace DaffodilAccount
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //水仙花數的算法是一個三位數，每一位數的立方相加等於該數本身。
        private void button1_Click(object sender, EventArgs e)
        {
            int a = 0, b = 0, c = 0;//定義變數
            listBox1.Items.Clear();//清空listBox1控制元件
            for (int i = 100; i <= 1000; i++)//搜尋所有3位數
            {
                a = i / 100;//取得3位數中的第一個數
                Math.DivRem(i, 100, out b);//取得3位數中的後兩位數
                b = b / 10;//取得3位數中的第二位數
                Math.DivRem(i, 10, out c);//取得3位數中的第3位數
                a = a * a * a;//計算第一位數的立方
                b = b * b * b;//計算第二位數的立方
                c = c * c * c;//計算第3位數的立方
                if ((a + b + c) == i)//如果符合水仙花數
                    listBox1.Items.Add(i.ToString());//顯示目前3位數
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "水仙花數的算法是一個三位數，每一位數的立方相"+"\r"+"加等於該數本身。";
        }
    }
}
