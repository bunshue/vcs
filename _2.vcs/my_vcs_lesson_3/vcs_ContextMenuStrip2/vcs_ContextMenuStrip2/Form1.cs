using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ContextMenuStrip2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            label1.Text =
            "在不同控件上按滑鼠右鍵, 出現不同右鍵選單\n\n" +
            "1. 在表單空白處按右鍵, 出現右鍵選單\n" +
            "2. 在pictureBox處按右鍵, 出現右鍵選單\n\n" +
            "加入 ContextMenuStrip\n" +
            "點選屬性/Items/打開集合/MenuItem 按加入\n" +
            "修改Text 及 事件\n";
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right) //檢查滑鼠右鍵
            {
                contextMenuStrip1.Show(this, e.Location); //顯示ContextMenu
                return;
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right) //檢查滑鼠右鍵
            {
                contextMenuStrip2.Show(this.pictureBox1, e.Location); //顯示ContextMenu
                return;
            }
        }

        private void toolStripMenuItem_Click(object sender, EventArgs e)
        {
            //richTextBox1.Text += "Text : " + ((ToolStripMenuItem)sender).Text + "\n";

            richTextBox1.Text += "aaa\n";
        }
    }
}
