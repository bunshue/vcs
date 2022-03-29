using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace Main
{
    public partial class aboutForm : Form
    {
        public aboutForm()
        {
            InitializeComponent();
        }

        private void aboutForm_Load(object sender, EventArgs e)
        {
            lbAbout.Text = "本小软件是基于以前开发的桌面飘着Love的重构，让它更符合开闭原则\r\n     　　该源代码提供免费下载";
        }

        private void lbContact_LinkClicked(object sender, LinkLabelLinkClickedEventArgs e)
        {
            System.Diagnostics.Process.Start("IExplore.exe", "http://wpa.qq.com/msgrd?V=1&Uin=313769823");
        }
    }
}