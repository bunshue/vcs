using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
在 Form1 / pictureBox1 按右鍵測試ContextMenuStrip

加入 ContextMenuStrip
點選屬性/Items/打開集合/MenuItem 按加入
修改Text
*/

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
            //在 Form1 使用 ContextMenuStrip
            this.ContextMenuStrip = contextMenuStrip1;

            //在 pictureBox1 使用 ContextMenuStrip
            this.pictureBox1.ContextMenuStrip = contextMenuStrip2;
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

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem1.Text + "\n";
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem2.Text + "\n";
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem3.Text + "\n";
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem4.Text + "\n";
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem5.Text + "\n";
        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem6.Text + "\n";
        }

        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了\t" + toolStripMenuItem7.Text + "\n";
            this.Close();
        }
    }
}
