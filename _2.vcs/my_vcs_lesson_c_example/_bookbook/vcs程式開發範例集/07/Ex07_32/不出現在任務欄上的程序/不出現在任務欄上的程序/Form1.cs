using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 不出現在任務欄上的程序
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            Form1_Load(sender, e);
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            Form1_Load(sender, e);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            if (radioButton1.Checked)
                this.ShowInTaskbar = true;
            else
                this.ShowInTaskbar = false;
        }
    }
}