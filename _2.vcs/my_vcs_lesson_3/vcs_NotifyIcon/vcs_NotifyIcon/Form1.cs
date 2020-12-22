using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NotifyIcon
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            // Set the NotifyIcon's context menu.
            notifyIcon1.ContextMenuStrip = contextMenuStrip1;

            // Don't show in the task bar, only in the tray.
            this.ShowInTaskbar = false;

            // Display the happy status.
            radioButton1.Checked = true;
            Happy_Click(null, null);
        }

        // Set the happy status.
        // The RadioButton and ContextMenu use the same event handler.
        private void Happy_Click(object sender, EventArgs e)
        {
            this.Icon = Properties.Resources.Happy;
            notifyIcon1.Icon = Properties.Resources.Happy16x16;
            notifyIcon1.Text = "Status: Happy";
        }

        // Set the sad status.
        // The RadioButton and ContextMenu use the same event handler.
        private void Sad_Click(object sender, EventArgs e)
        {
            this.Icon = Properties.Resources.Sad;
            notifyIcon1.Icon = Properties.Resources.Sad16x16;
            notifyIcon1.Text = "Status: Sad";
        }

        // Restore the form.
        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
        }

        // Exit.
        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            this.Close();
        }

    }
}
