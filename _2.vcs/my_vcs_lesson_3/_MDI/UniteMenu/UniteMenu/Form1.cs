using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace UniteMenu
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void 打開自窗體ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Form2 f = new Form2();
            f.MdiParent = this;
            f.Show();
            f.Resize += new EventHandler(f_Resize);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        void f_Resize(object sender, EventArgs e)
        {
            Form2 f = (Form2)sender;
            ToolStripMenuItem item = new ToolStripMenuItem();
            for (int i = 0; i < f.contextMenuStrip2.Items.Count; )
            {
                item.DropDownItems.Add(f.contextMenuStrip2.Items[i]);
            }
            this.contextMenuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            item});
        }

        private void menu1ToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void menu1ToolStripMenuItem6_Click(object sender, EventArgs e)
        {

        }

        private void 幫助HToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void toolStripSeparator4_Click(object sender, EventArgs e)
        {

        }
    }
}