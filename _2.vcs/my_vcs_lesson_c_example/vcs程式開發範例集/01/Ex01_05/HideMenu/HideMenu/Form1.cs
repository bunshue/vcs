using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace HideMenu
{
    public partial class Form1 : Form
    {
        int i = 2;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.設置密碼ToolStripMenuItem.Visible = false;
            this.添加用戶ToolStripMenuItem.Visible = false;
            this.忘記密碼ToolStripMenuItem.Visible = false;
            this.修改密碼ToolStripMenuItem.Visible = false;
            this.員工錄入ToolStripMenuItem.Visible = false;
        }

        private void toolStripSeparator1_Click(object sender, EventArgs e)
        {

        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            switch (i)
            {
                case 1:
                    this.設置密碼ToolStripMenuItem.Visible = false;
                    this.添加用戶ToolStripMenuItem.Visible = false;
                    this.忘記密碼ToolStripMenuItem.Visible = false;
                    this.修改密碼ToolStripMenuItem.Visible = false;
                    this.員工錄入ToolStripMenuItem.Visible = false;
                    i = 2;
                    this.操作ToolStripMenuItem.ShowDropDown();
                    break;

                case 2:
                    this.設置密碼ToolStripMenuItem.Visible = true;
                    this.添加用戶ToolStripMenuItem.Visible = true;
                    this.忘記密碼ToolStripMenuItem.Visible = true;
                    this.修改密碼ToolStripMenuItem.Visible = true;
                    this.員工錄入ToolStripMenuItem.Visible = true;
                    i = 1;
                    this.操作ToolStripMenuItem.ShowDropDown();
                    break;
            }
        }
    }
}