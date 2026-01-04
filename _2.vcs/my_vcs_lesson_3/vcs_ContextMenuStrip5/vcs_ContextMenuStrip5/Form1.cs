using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ContextMenuStrip5
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.ContextMenuStrip = contextMenuStrip1;
        }

        private void ToolStripMenuItem_AA_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem item = sender as ToolStripMenuItem;

            richTextBox1.Text += "你按了右鍵選單的 AAAA 裡面的 : " + item.Text + "\n";
        }

        private void ToolStripMenuItem_B_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了右鍵選單的 BBBB\n";
            ToolStripMenuItem_B.Checked = !ToolStripMenuItem_B.Checked;
        }

        private void ToolStripMenuItem_C_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了右鍵選單的 CCCC\n";
            ToolStripMenuItem_C.Checked = !ToolStripMenuItem_C.Checked;
        }

        private void ToolStripMenuItem_Exit_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
