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
            label3.Text = "操作員 : Admin / Admin\n系統管理員 : Mr / Mrsoft";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox1.Text == "")
            {
                MessageBox.Show("請輸入帳號");
                return;
            }
            else if (textBox2.Text == "")
            {
                MessageBox.Show("請輸入密碼");
                return;
            }
            else if (textBox1.Text == "Admin" && textBox2.Text == "Admin")
            {
                //Form_Main的6個button的Modifiers要改成Public
                form_main.Show();
                form_main.button1.Visible = false;
                form_main.button4.Visible = false;
                form_main.Text = form_main.Text + "    " + "操作員:" + textBox1.Text;
                this.Hide();
            }
            else if (textBox1.Text == "Mr" && textBox2.Text == "Mrsoft")
            {
                form_main.Show();
                form_main.Text = form_main.Text + "    " + "系統管理員:" + textBox2.Text;
                this.Hide();
            }
            else
            {
                MessageBox.Show("帳號或密碼錯誤");
                textBox1.Text = "";
                textBox2.Text = "";
                textBox1.Focus();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            DialogResult bb = MessageBox.Show("是否要退出登錄？", "退出登錄", MessageBoxButtons.YesNo);
            if (Convert.ToString(bb) == "Yes")
            {
                Application.Exit();
            }
        }
    }
}


