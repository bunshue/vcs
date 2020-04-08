using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 父子視窗傳值問題
{
    public partial class Form2 : Form
    {
        private string string1;

        public string Msg
        {
            set { string1 = value; }
        }

        public void setValue()
        {
            this.richTextBox1.Text += "子得到信息 : " + string1 + "\n";
        }

        public Form2()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            // point the Form2's owner to Form1
            Form1 parentForm = (Form1)this.Owner;
            parentForm.MsgFromChild = "按了按鍵1";
            //this.close();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Application.Exit();
            //this.Close();
            this.Hide();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // point the Form2's owner to Form1
            Form1 parentForm = (Form1)this.Owner;
            parentForm.MsgFromChild = "按了按鍵1";
            //this.close();
        }
    }
}
