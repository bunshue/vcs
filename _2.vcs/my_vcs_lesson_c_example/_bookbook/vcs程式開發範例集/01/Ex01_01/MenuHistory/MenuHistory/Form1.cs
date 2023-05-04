using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace MenuHistory
{
    public partial class Form1 : Form
    {
        string filename = @"C:\______test_files1\__RW\_ini\Menu.ini";

        public Form1()
        {
            InitializeComponent();
        }

        private void 打開ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            openFileDialog1.FileName = "";
            this.openFileDialog1.ShowDialog();
            StreamWriter s = new StreamWriter(filename, true);
            s.WriteLine(openFileDialog1.FileName);
            s.Flush();
            s.Close();
            ShowWindows(openFileDialog1.FileName);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            StreamReader sr = new StreamReader(filename);
            int i = this.文件ToolStripMenuItem.DropDownItems.Count - 2;
            while (sr.Peek() >= 0)
            {
                ToolStripMenuItem menuitem = new ToolStripMenuItem(sr.ReadLine());
                this.文件ToolStripMenuItem.DropDownItems.Insert(i, menuitem);
                i++;
                menuitem.Click += new EventHandler(menuitem_Click);
            }
            sr.Close();
        }

        private void menuitem_Click(object sender, EventArgs e)
        {
            ToolStripMenuItem menu = (ToolStripMenuItem)sender;
            ShowWindows(menu.Text);
        }
        public void ShowWindows(string fileName)
        {
            Image p = Image.FromFile(fileName);
            Form f = new Form();
            f.MdiParent = this;
            f.BackgroundImage = p;
            f.Show();
        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}


