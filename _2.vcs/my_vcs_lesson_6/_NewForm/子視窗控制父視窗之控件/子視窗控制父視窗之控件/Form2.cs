using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 子視窗控制父視窗之控件
{
    public partial class Form2 : Form
    {
        private Form1 frm1;
        public Form2(Form1 form)
        {
            InitializeComponent();
            frm1 = form;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            frm1.button1.BackColor = Color.Green;
            this.Close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            frm1.button1.BackColor = Color.Red;
            this.Close();

        }
    }
}
