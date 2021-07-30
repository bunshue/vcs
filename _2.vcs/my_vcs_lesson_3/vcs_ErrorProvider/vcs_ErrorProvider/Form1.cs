using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ErrorProvider
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        string strA = null;
        string strB = null;

        private void textBox1_Validating(object sender, CancelEventArgs e)
        {
            //驗證帳號

            if (textBox1.Text != "mr")
            {
                errorProvider1.SetError(textBox1, "登錄名錯誤");
            }
            else
            {
                errorProvider1.SetError(textBox1, "");
                strB = textBox1.Text;
            }
        }

        private void textBox2_Validating(object sender, CancelEventArgs e)
        {
            //驗證密碼
            if (textBox2.Text != "mrsoft")//判斷輸入是否正確
            {
                errorProvider2.SetError(textBox2, "密碼確誤");
            }
            else
            {
                errorProvider2.SetError(textBox2, "");
                strA = textBox2.Text;
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (strB != null && strA != null)
            {
                MessageBox.Show("登錄成功");
            }
            else
            {
                MessageBox.Show("輸入用戶名和密碼");
            }

        }
    }
}
