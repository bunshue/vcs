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
            show_item_location();

            label1.Text =
            "在不同控件上按滑鼠右鍵, 出現不同右鍵選單\n\n" +
            "1. 在表單空白處按右鍵, 出現右鍵選單\n" +
            "2. 在pictureBox處按右鍵, 出現右鍵選單\n\n" +
            "加入 ContextMenuStrip\n" +
            "點選屬性/Items/打開集合/MenuItem 按加入\n" +
            "修改Text 及 事件\n\n" +
            "設定寫在xxxx_MouseDown裡面\n";
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //richTextBox1.Size = new Size(790, 295);
            //richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 7 + 60);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //this.Size = new Size(1250, 880);
            this.Text = "vcs_ContextMenuStrip2";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
