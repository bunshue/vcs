using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MenuStrip_ToolStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        void Create_File()
        {
            richTextBox1.Text += "建立新檔案\n";
        }

        void Open_File()
        {
            richTextBox1.Text += "開啟檔案\n";
        }

        void Save_File()
        {
            richTextBox1.Text += "儲存檔案\n";
        }
        
        private void toolStripButton1_Click(object sender, EventArgs e)
        {
            Create_File();
        }

        private void toolStripButton2_Click(object sender, EventArgs e)
        {
            Open_File();
        }

        private void toolStripButton3_Click(object sender, EventArgs e)
        {
            Save_File();
        }

        private void newToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Create_File();
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Open_File();
        }

        private void saveToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Save_File();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 結束程式\n";
        }

        private void selectAllToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectAll();
        }

        private void copyToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 Copy\n";
        }

        private void pasteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 Paste\n";
        }

        private void optionToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 Option\n";
        }

        private void helpToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 Help\n";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n";
            richTextBox1.Text += @"
MenuStrip選單項目加上底線快速鍵
menuStrip/屬性/Items/打開(集合)/點選MenuStrip下的ToolStripMenuItem/
Text項目 要加底線的字之前多一個& 例如 &File 則F下會有底線
DropDownItems/打開(集合)
Text項目 要加底線的字之前多一個& 例如 &Full Scale 則F下會有底線

MenuStrip選單項目加上快速鍵
menuStrip/屬性/Items/打開(集合)/點選MenuStrip下的ToolStripMenuItem/
DropDownItems/打開(集合)
選ShortcutKeys 例如Ctrl+F ShowShortcutKeys改為True";
            richTextBox1.Text += "\n";
        }

    }
}
