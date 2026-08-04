using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_LoginSystem
{
    public partial class Form1 : Form
    {
        Form_Main form_main = new Form_Main();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //case 1

            //Form_Main的6個button的Modifiers要改成Public
            form_main.Show();
            form_main.button1.Visible = false;
            form_main.button4.Visible = false;
            form_main.Text = form_main.Text + "    " + "操作員";
            this.Hide();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //case 2

            //Form_Main的6個button的Modifiers要改成Public
            form_main.Show();
            form_main.Text = form_main.Text + "    " + "系統管理員";
            this.Hide();
        }
    }
}

