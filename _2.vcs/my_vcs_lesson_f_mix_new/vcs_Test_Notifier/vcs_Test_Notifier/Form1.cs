using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Test_Notifier
{
    public partial class Form1 : Form
    {
        //移動無邊框窗體 ST
        private const int WM_NCHITTEST = 0x84;
        private const int HTCLIENT = 0x1;
        private const int HTCAPTION = 0x2;

        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_NCHITTEST:
                    base.WndProc(ref m);
                    if ((int)m.Result == HTCLIENT)
                        m.Result = (IntPtr)HTCAPTION;
                    return;
                    break;
            }
            base.WndProc(ref m);
        }
        //移動無邊框窗體 SP

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            this.FormBorderStyle = FormBorderStyle.None;//設定無邊框
            this.WindowState = FormWindowState.Minimized;
            this.ShowInTaskbar = false;
        }

        int cnt = 0;
        private void timer1_Tick(object sender, EventArgs e)
        {
            cnt++;
            if (cnt == 10)
            {
                this.WindowState = FormWindowState.Normal;
                this.ShowInTaskbar = true;
                this.TopMost = true;
                cnt = 0;

                richTextBox1.Text += "Here 1111\n";
            }
            else if (cnt == 15)
            {
                if (this.WindowState == FormWindowState.Minimized)
                {
                    this.WindowState = FormWindowState.Normal;
                    this.ShowInTaskbar = true;
                    this.TopMost = true;
                    cnt = 0;
                    richTextBox1.Text += "Here 2222\n";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            this.TopMost = false;
            this.WindowState = FormWindowState.Minimized;
            this.ShowInTaskbar = false;
            cnt = 0;

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
