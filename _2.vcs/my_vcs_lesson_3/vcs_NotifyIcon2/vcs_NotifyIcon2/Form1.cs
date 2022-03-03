using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NotifyIcon2
{
    public partial class Form1 : Form
    {
        private Icon icon = new Icon(@"C:\_git\vcs\_2.vcs\______test_files\_material\ims.ico");
        private NotifyIcon notifyIcon1;
        private ContextMenuStrip contextMenuStrip1;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            contextMenuStrip1 = new ContextMenuStrip();
            contextMenuStrip1.Items.Add("恢復程式位置");
            contextMenuStrip1.ItemClicked += recoveryToolStripMenuItem_Click;
            contextMenuStrip1.Visible = true;

            notifyIcon1 = new NotifyIcon();
            notifyIcon1.ContextMenuStrip = contextMenuStrip1;
            notifyIcon1.Text = "程序最小化到系統托盤";    //設置系統托盤顯示文字
            //notifyIcon1.Visible = true;
            notifyIcon1.Icon = icon;
        }

        private void recoveryToolStripMenuItem_Click(object sender, EventArgs e)
        {
            MinimizedToNormal();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            NormalToMinimized();
        }

        //NormalToMinimized()是把當前窗體隱藏，並顯示托盤通知按鈕（這個按鈕初始是隱藏的）。
        void NormalToMinimized()
        {
            this.WindowState = FormWindowState.Minimized;
            this.Visible = false;
            this.notifyIcon1.Visible = true;
        }

        //MinimizedToNormal()是重新顯示窗體，並把托盤通知按鈕隱藏。
        void MinimizedToNormal()
        {
            this.Visible = true;
            this.WindowState = FormWindowState.Normal;
            notifyIcon1.Visible = false;
        }
    }
}
