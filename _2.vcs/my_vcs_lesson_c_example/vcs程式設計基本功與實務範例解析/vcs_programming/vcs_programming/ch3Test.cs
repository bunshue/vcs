using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_programming
{
    public partial class ch3Test : Form
    {
        public ch3Test()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            char c = 'A';
            int i = 'A';

            lblOutput.Text = "字元變數c是" + c;
            lblOutput.Text = lblOutput.Text + "\n字元A的內碼是" + i;

            i = 'B';
            lblOutput.Text = lblOutput.Text + "\n字元B的內碼是" + i;

            c = '\u0041'; //16進位,2個Bytes
            lblOutput.Text = lblOutput.Text + "\nUniCode 0041的字元是" + c;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int a = 5, b = 10;

            lblOutput.Text = "交換前 a = " + a + ", b = " + b;
            //a = b;
            //b = a;
            int temp = a;
            a = b;
            b = temp;
            lblOutput.Text = lblOutput.Text + "\n交換後 a = " + a + ", b = " + b;

        }
    }
}
