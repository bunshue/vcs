using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Test_Notifier
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Minimized;
        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            if (cnt == 10)
            {
                this.WindowState = FormWindowState.Normal;
                this.TopMost = true;
                cnt = 0;

                richTextBox1.Text += "Here 1111\n";
            }
            else if (cnt == 15)
            {
                if (this.WindowState == FormWindowState.Minimized)
                {
                    this.WindowState = FormWindowState.Normal;
                    this.TopMost = true;
                    cnt = 0;
                    richTextBox1.Text += "Here 2222\n";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.TopMost = false;
            this.WindowState = FormWindowState.Minimized;
            cnt = 0;

        }
    }
}
