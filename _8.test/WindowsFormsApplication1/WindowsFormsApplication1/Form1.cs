using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace WindowsFormsApplication1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            label1.Text = "";
        }

        int cnt = 0;
        private void richTextBox1_TextChanged(object sender, EventArgs e)
        {
            if (richTextBox1.Text.Length > 0)
            {
                label1.Text = "序號 : " + richTextBox1.Text + "\nlen = " + richTextBox1.Text.Length.ToString();
                cnt = 0;
                timer1.Enabled = true;
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            if (cnt == 5)
            {
                richTextBox1.Clear();
                timer1.Enabled = false;
                label1.Text = "";
            }
        }


    }
}
