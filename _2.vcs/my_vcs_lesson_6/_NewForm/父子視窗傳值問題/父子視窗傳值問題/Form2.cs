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
            parentForm.MsgFromChild = "Msg from child-form success";
            //this.close();
        }
    }
}
