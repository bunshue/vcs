using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_MenuStripToolStrip
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        void Create_File()
        {
            richTextBox1.Text += "建立新檔案。\n";
        }

        void Open_File()
        {
            richTextBox1.Text += "開啟檔案。\n";
        }

        void Save_File()
        {
            richTextBox1.Text += "儲存檔案。\n";
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
            richTextBox1.Text += "結束程式";
        }

        private void selectAllToolStripMenuItem_Click(object sender, EventArgs e)
        {
            richTextBox1.SelectAll();
        }
    }
}
