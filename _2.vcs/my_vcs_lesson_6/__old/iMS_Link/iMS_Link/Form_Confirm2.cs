using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace iMS_Link
{
    public partial class Form_Confirm2 : Form
    {
        public Form_Confirm2()
        {
            InitializeComponent();
        }

        private void Form_Confirm2_Load(object sender, EventArgs e)
        {
            textBox1.Clear();
            textBox1.Focus();
        }

        private void bt_ok_Click(object sender, EventArgs e)
        {
            Form1 f1 = (Form1)this.Owner;
            f1.SetupForm1Data = textBox1.Text;
            f1.setForm1Value();
            this.DialogResult = DialogResult.Ignore;
        }

        private void bt_cancel_Click(object sender, EventArgs e)
        {
            Form1 f1 = (Form1)this.Owner;
            this.DialogResult = DialogResult.Cancel;
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)13)
            {
                bt_ok_Click(sender, e);
            }
        }
    }
}
