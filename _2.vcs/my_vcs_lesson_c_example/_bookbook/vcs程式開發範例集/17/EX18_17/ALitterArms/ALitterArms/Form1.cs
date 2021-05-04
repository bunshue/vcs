using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace ALitterArms
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int a = 0, b = 0, c = 0;//定義變數
            for (int i = 1; i < 100; i++)//搜尋
            {
                Math.DivRem(i, 3, out a);//3行一列時取余
                Math.DivRem(i, 5, out b);//5行一列時取余
                Math.DivRem(i, 7, out c);//7行一列時取余
                if (a == 1 && b == 0 && c == 5)//如果3種方式的餘數符合要求
                {
                    textBox1.Text = i.ToString();//顯示人數
                    return;
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label2.Text = "韓信點兵是一道古代數學題，內容是：韓信具有" + "\r" + "兵不足百人，三人一行排列多一個，七人一行" + "\r" + "排列少兩個，五人一行排列正好。";
        }
    }
}
