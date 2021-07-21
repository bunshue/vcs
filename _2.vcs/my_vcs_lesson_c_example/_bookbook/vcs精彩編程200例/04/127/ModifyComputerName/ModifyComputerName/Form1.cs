using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic.Devices;
using System.Runtime.InteropServices;

namespace ModifyComputerName
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("kernel32.dll")]
        private static extern int SetComputerName(string ipComputerName);//重写API函数

        private void Frm_Main_Load(object sender, EventArgs e)
        {
            Computer computer = new Computer();//创建计算机对象
            textBox1.Text = computer.Name;//显示计算机名称
            richTextBox1.Text += "原計算機名 : " + computer.Name + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox2.Text == "")//判断计算机名称是否为空
            {
                MessageBox.Show("计算机名称不能为空！");
            }
            else
            {
                richTextBox1.Text += "偽執行 計算機名稱修改, 須重啟計算機使之生效\n";
                //SetComputerName(textBox2.Text);//修改計算機名稱
            }
        }
    }
}
