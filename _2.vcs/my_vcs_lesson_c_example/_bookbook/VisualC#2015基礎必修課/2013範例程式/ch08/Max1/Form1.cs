using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Max1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        //Max自定方法求兩數的最大值
        private int Max(int n1, int n2)
        {
            return (n1 > n2 ? n1 : n2);   //傳回兩數的最大值
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int m = 1; int n = 10;
            //呼叫Max方法求1、10兩數的最大值
            label1.Text = m.ToString() + "和" + n.ToString() + "的最大值為：" +
                       Max(m, n).ToString() + "\n\n";
            m = 12; n = -5;
            //呼叫Max方法求12、-5兩數的最大值
            label1.Text += m.ToString() + "和" + n.ToString() + "的最大值為：" +
                       Max(m, n).ToString();
        }
    }
}
