using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NotifyIcon_ContextMenuStrip
{
    public partial class Form1 : Form
    {
        private Icon icon = new Icon(@"C:\_git\vcs\_2.vcs\______test_files\_material\ims.ico");

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //目前無法依選項動作
            contextMenuStrip1.Items.Add("恢復");
            contextMenuStrip1.ItemClicked += recoverToolStripMenuItem_Click;

            contextMenuStrip1.Items.Add("離開");
            contextMenuStrip1.ItemClicked += exitToolStripMenuItem_Click;

            contextMenuStrip1.Visible = true;

            notifyIcon1.ContextMenuStrip = contextMenuStrip1;
            notifyIcon1.Text = "製作TrayIcon";    //設置系統托盤顯示文字
            notifyIcon1.Visible = true;

            notifyIcon1.Icon = icon;



            this.WindowState = FormWindowState.Minimized;
            this.Visible = false;
            this.notifyIcon1.Visible = true;
        }

        private void recoverToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Visible = true;
            this.WindowState = FormWindowState.Normal;
            notifyIcon1.Visible = false;

        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            //Application.Exit();
        }

    }
}
