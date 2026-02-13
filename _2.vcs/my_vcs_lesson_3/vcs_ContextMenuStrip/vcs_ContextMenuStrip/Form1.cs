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

namespace vcs_ContextMenuStrip
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

            string filename = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
            pictureBox1.Image = new Bitmap(filename);

            label_description.Text =
                "在不同控件上按滑鼠右鍵, 出現不同右鍵選單\n\n" +
                "1. 在表單空白處按右鍵, 出現右鍵選單\n" +
                "2. 在pictureBox處按右鍵, 出現右鍵選單\n\n" +
                "加入 ContextMenuStrip\n" +
                "點選屬性/Items/打開集合/MenuItem 按加入\n" +
                "修改Text 及 事件\n\n" +
                "設定寫在xxxx_MouseDown裡面\n\n";

            richTextBox1.Text += "RTB加右鍵選單\nRTB加右鍵選單\nRTB加右鍵選單\n";
            richTextBox1.ContextMenuStrip = contextMenuStrip3;

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

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            richTextBox1.Size = new Size(270, 620);
            richTextBox1.Location = new Point(930, 10);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1250, 680);
            this.Text = "vcs_ContextMenuStrip";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void Form1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right) //檢查滑鼠右鍵
            {
                richTextBox1.Text += "按 表單 MouseDown\n";
                // 參數一為被綁定的控件
                // 參數二為彈出式菜單的顯示位置(0,0與被綁定控件的原點重合)
                contextMenuStrip1.Show(this, e.Location);//顯示ContextMenu
                return;
            }
        }

        private void pictureBox1_MouseDown(object sender, MouseEventArgs e)
        {
            if (e.Button == MouseButtons.Right) //檢查滑鼠右鍵
            {
                richTextBox1.Text += "按 pictureBox1 MouseDown\n";
                // 參數一為被綁定的控件
                // 參數二為彈出式菜單的顯示位置(0,0與被綁定控件的原點重合)
                //contextMenuStrip2.Show(this, e.Location);//顯示ContextMenu
                contextMenuStrip2.Show(this.pictureBox1, e.Location); //顯示ContextMenu
                return;
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
            toolStripMenuItem1.Checked = !toolStripMenuItem1.Checked;
            richTextBox1.Text += "你按了\t" + toolStripMenuItem1.Text + "\n";
        }

        private void toolStripMenuItem2_Click(object sender, EventArgs e)
        {
            toolStripMenuItem2.Checked = !toolStripMenuItem2.Checked;
            richTextBox1.Text += "你按了\t" + toolStripMenuItem2.Text + "\n";
        }

        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            toolStripMenuItem3.Checked = !toolStripMenuItem3.Checked;
            richTextBox1.Text += "你按了\t" + toolStripMenuItem3.Text + "\n";
        }

        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            toolStripMenuItem4.Checked = !toolStripMenuItem4.Checked;
            richTextBox1.Text += "你按了\t" + toolStripMenuItem4.Text + "\n";
        }

        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            toolStripMenuItem5.Checked = !toolStripMenuItem5.Checked;
            richTextBox1.Text += "你按了\t" + toolStripMenuItem5.Text + "\n";
        }

        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {
            toolStripMenuItem6.Checked = !toolStripMenuItem6.Checked;
            richTextBox1.Text += "你按了\t" + toolStripMenuItem6.Text + "\n";
        }

        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            toolStripMenuItem7.Checked = !toolStripMenuItem7.Checked;
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

        private void 剪下ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Cut();
        }

        private void 複製ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Copy();
        }

        private void 貼上ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Paste();
        }
    }
}
