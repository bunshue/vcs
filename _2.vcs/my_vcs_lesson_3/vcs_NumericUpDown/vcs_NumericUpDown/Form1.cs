using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NumericUpDown
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

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "目前數量 : " + numericUpDown1.Value + "\n";
        }

        private void bt_plus_Click(object sender, EventArgs e)
        {
            numericUpDown1.UpButton();
        }

        private void bt_minus_Click(object sender, EventArgs e)
        {
            numericUpDown1.DownButton();
        }
    }
}
