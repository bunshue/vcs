using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
表單的按鍵響應
this.KeyPress += new KeyPressEventHandler(Form1_KeyPress);
this.KeyPreview = true;
*/

namespace vcs_Form4_KeyPreview
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.KeyPreview = true;

            this.KeyPress += new KeyPressEventHandler(Form1_KeyPress);
        }

        private void Form1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Escape)
            {
                richTextBox1.Text += "Esc\n";
                Application.Exit();
            }
            else
            {
                richTextBox1.Text += "你按了 : " + e.KeyChar + "\n";

            }
        }
    }
}

