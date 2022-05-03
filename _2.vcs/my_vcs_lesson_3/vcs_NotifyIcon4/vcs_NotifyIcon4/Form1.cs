using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_NotifyIcon4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Enabled = true;
            this.WindowState = FormWindowState.Minimized;

        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
        }

        private void Form1_Resize(object sender, EventArgs e)
        {
            if (this.WindowState == FormWindowState.Minimized)
            {
                this.ShowInTaskbar = false;
                notifyIcon1.Visible = true;
                notifyIcon1.BalloonTipText = "使用 NotifyIcon 每10分鐘報時一次";
                notifyIcon1.ShowBalloonTip(300);
                this.Hide();
            }

        }

        private void notifyIcon1_MouseDoubleClick(object sender, MouseEventArgs e)
        {
            this.WindowState = FormWindowState.Normal;
            this.ShowInTaskbar = true;
            notifyIcon1.Visible = false;
            this.Show();
            //this.BringToFront();

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            if (dt.Second == 0)
            {
                notifyIcon1.BalloonTipText = DateTime.Now.ToString();
                notifyIcon1.ShowBalloonTip(300);
            }
        }







    }
}
