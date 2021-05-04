using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Linq;
using System.Windows.Forms;

namespace BuildNumber
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (Char)Keys.Return)
            {
                if (textBox1.Text.Length > 8)
                {
                    textBox1.Text = textBox1.Text.Substring(0, 8);
                }
                else
                {
                    int j = 8 - textBox1.Text.Length;
                    for (int i = 0; i < j; i++)
                    {
                        textBox1.Text = "0" + textBox1.Text;
                    }
                }
            }
        }
    }
}