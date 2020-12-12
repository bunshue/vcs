using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ToolStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void toolStripButton_Click(object sender, EventArgs e)
        {
            ToolStripButton btn = sender as ToolStripButton;
            richTextBox1.Text += "你按了\t" + btn.Name + " " + btn.Text + "\n";

        }
    }
}
