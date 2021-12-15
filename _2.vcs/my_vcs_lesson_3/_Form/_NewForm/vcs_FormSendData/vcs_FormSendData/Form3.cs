using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData
{
    public partial class Form3 : Form
    {
        private Form1 frm1;

        //public Form3() old, 要改成可以接收參數
        public Form3(Form1 form)
        {
            InitializeComponent();
            frm1 = form;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            frm1.button6.BackColor = Color.Blue;
            //this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            frm1.button6.BackColor = Color.Red;
            //this.Close();
        }

        int cnt = 0;
        private void button3_Click(object sender, EventArgs e)
        {
            frm1.richTextBox1.Text += "Form3送資料給Form1的richTextBox1  " + (cnt++).ToString() + "\n";
        }
    }
}

