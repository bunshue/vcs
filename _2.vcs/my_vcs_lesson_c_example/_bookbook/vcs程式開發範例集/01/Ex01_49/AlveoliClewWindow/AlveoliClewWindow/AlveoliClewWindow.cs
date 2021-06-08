using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace AlveoliClewWindow
{
    public partial class AlveoliClewWindow : Form
    {
        public AlveoliClewWindow()
        {
            InitializeComponent();
        }

        private void clewButton_Click(object sender,EventArgs e)
        {
            this.notifyIcon1.Visible = true;
            this.notifyIcon1.ShowBalloonTip(1000,"当前时间：",DateTime.Now.ToLocalTime().ToString(),ToolTipIcon.Info);
        }

        private void closeButton_Click(object sender,EventArgs e)
        {
            this.notifyIcon1.Visible = false;
        }

        private void notifyIcon1_MouseMove(object sender,MouseEventArgs e)
        {
            this.notifyIcon1.ShowBalloonTip(1000,"当前时间：",DateTime.Now.ToLocalTime().ToString(),ToolTipIcon.Info);


            richTextBox1.Text += "A ";
        }
    }
}
