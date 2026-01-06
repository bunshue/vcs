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
            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = new Bitmap(filename);

            /*
            // 使用 ContextMenuStrip 方法一, 使用設定
            //在 Form1 使用 ContextMenuStrip
            this.ContextMenuStrip = contextMenuStrip1;
            //在 pictureBox1 使用 ContextMenuStrip
            this.pictureBox1.ContextMenuStrip = contextMenuStrip2;
            */

            // 使用 ContextMenuStrip 方法二, 使用設定 XXXX_MouseDown / XXXX_MouseClick
            this.MouseDown += new MouseEventHandler(Form1_MouseDown);
            this.pictureBox1.MouseDown += new MouseEventHandler(pictureBox1_MouseDown);
        }

        void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                richTextBox1.Text += "按 表單 MouseDown\n";
                // 參數一為被綁定的控件
                // 參數二為彈出式菜單的顯示位置(0,0與被綁定控件的原點重合)
                contextMenuStrip1.Show(this, e.Location);//顯示ContextMenu
            }
        }

        void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right)
            {
                richTextBox1.Text += "按 pictureBox1 MouseDown\n";
                // 參數一為被綁定的控件
                // 參數二為彈出式菜單的顯示位置(0,0與被綁定控件的原點重合)
                contextMenuStrip2.Show(this, e.Location);//顯示ContextMenu
            }           
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

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "按 Button Click\n";
            // 參數一為被綁定的控件
            // 參數二為彈出式菜單的顯示位置(0,0與被綁定控件的原點重合)
            contextMenuStrip1.Show(button1, new Point(0, button1.Height + 5));
        }
    }
}

