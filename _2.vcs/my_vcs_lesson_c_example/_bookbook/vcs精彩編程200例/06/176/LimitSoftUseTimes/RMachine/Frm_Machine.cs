using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using ClassLibrary1;

namespace RMachine
{
    public partial class Frm_Machine : Form
    {
        SoftReg softreg = new SoftReg();//实例化公共类对象

        public Frm_Machine()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            {
                MessageBox.Show("机器码输入不能为空！", "警告", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
            else
            {
                textBox2.Text = softreg.getRNum();
                richTextBox1.Text += textBox2.Text + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void Frm_Machine_Load(object sender, EventArgs e)
        {
            textBox1.Text = "12345";
        }
    }
}
