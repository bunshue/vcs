using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Max2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //Max自定方法顯示兩數的最大值
        private void Max(int n1, int n2)
        {
            label1.Text += n1.ToString() + "和" + n2.ToString() + "的最大值為：" + (n1 > n2 ? n1 : n2).ToString() + "\n\n";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text = "";
            Max(1, 10);     //呼叫Max方法顯示1、10兩數的最大值
            Max(12, -5);    //呼叫Max方法顯示12、-5兩數的最大值
        }
    }
}
