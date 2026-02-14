using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace TheEntryOfControl
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

        protected override void OnKeyPress(KeyPressEventArgs e)
        {
            if (e.KeyChar == 13)
            {
                this.SelectNextControl(this.ActiveControl, true, true, true, true);
            }
            base.OnKeyPress(e);
        }

        private void textBox5_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar != 8 && !char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }

        private void textBox5_KeyUp(object sender, KeyEventArgs e)
        {
            if (textBox5.Text.Length == 2)
            {
                int age = Convert.ToInt32(textBox5.Text);
                if (age < 8 || age > 18)
                {
                    MessageBox.Show("學生年齡應在8－18週歲之間", "信息提示");
                    textBox5.Text = "";
                    textBox5.SelectAll();
                    textBox5.Focus();
                }
            }
        }

        private void textBox7_KeyPress(object sender, KeyPressEventArgs e)
        {
            if ((e.KeyChar != 65 && e.KeyChar != 66) && (e.KeyChar != 79 && e.KeyChar != 8))
            {
                MessageBox.Show("血型請輸入<A,AB,O,B>");
                e.Handled = true;
            }
        }

        private void textBox7_KeyDown(object sender, KeyEventArgs e)
        {
            //MessageBox.Show(e.KeyValue.ToString());
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (textBox7.Text == "")
            {
                MessageBox.Show("請輸入血型");
            }
            else
            {
                MessageBox.Show("輸入成功");
            }
        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {
        }
    }
}
