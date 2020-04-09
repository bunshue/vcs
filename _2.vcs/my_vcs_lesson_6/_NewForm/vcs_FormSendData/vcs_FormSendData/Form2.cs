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
    public partial class Form2 : Form
    {
        private string form2_data;

        public string SetupForm2Data
        {
            set
            {
                form2_data = value;
            }
        }

        public void setForm2Value()
        {
            this.richTextBox1.Text += "子得到信息 : " + form2_data + "\n";
        }

        public Form2()
        {
            InitializeComponent();
            button_ok.DialogResult = System.Windows.Forms.DialogResult.OK;//設定button_ok為OK
            button_cancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;//設定button_cancel為Cancel
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

        private void button1_Click(object sender, EventArgs e)
        {
            Form1 parentForm = (Form1)this.Owner;
            parentForm.SetupForm1Data = "子告訴父一件事~~~~~~~";
            parentForm.setForm1Value();
        }


    }
}
