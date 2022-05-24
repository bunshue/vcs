using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_FormSendData2
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

        private void Form1_Activated(object sender, EventArgs e)
        {
            this.textBox1.Focus();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string data = this.textBox1.Text.Trim();

            if (string.IsNullOrEmpty(data))
            {
                MessageBox.Show("資料不能空白，請重新輸入");
                return;
            }


            Form2 f2 = new Form2(data);
            //f2.Show();
            //this.Hide();//隱藏窗體

            //子表單關閉時 回傳給父表單訊息
            if (f2.ShowDialog() == DialogResult.OK)
            {
                richTextBox1.Text += "子表單回傳 OK\n";
            }
            else
            {
                richTextBox1.Text += "子表單回傳 Cancel\n";
            }
        }
    }
}
