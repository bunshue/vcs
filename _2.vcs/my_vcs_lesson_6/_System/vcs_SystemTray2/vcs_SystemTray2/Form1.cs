using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

/*
加入 NotifyIcon 和 ContextMenuStrip

NotifyIcon屬性
1. 改 Icon
2. BaloonTipIcon 改 Info
3. ContextMenuStrip 改 contextMenuStrip1
4. 事件 + MouseDoubleClick

ContextMenuStrip屬性
1. 加 退出 項
*/

namespace vcs_SystemTray2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            //Form1 的設定放在這裡, 畫面才不會閃一下
            this.ShowInTaskbar = false;
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.WindowState = FormWindowState.Minimized;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                this.WindowState = FormWindowState.Normal;
            }
            this.Activate();

        }

        private void 退出ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            this.Close();
        }
    }
}
