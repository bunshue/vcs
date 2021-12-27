using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ContextMenuStrip3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void item1ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 item1\n";
        }

        private void item2ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 item2\n";
        }

        private void item3ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 item3\n";
        }

        private void item4ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 item4\n";
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            richTextBox1.Text += "按 表單 MOuseDown\n";
            // 參數一為被綁定的控件
            // 參數二為彈出式菜單的顯示位置(0,0與被綁定控件的原點重合)
            contextMenuStrip1.Show(this, e.Location);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "按 Button Click\n";
            // 參數一為被綁定的控件
            // 參數二為彈出式菜單的顯示位置(0,0與被綁定控件的原點重合)
            contextMenuStrip1.Show(button1, new Point(0, button1.Height + 5));
        }
    }
}

