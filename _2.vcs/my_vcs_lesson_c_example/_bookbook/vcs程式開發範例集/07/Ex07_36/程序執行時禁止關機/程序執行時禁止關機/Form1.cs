using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace 程序執行時禁止關機
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private int isClose = 0;
        private const int WM_QUERYENDSESSION = 0x0011;
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case WM_QUERYENDSESSION:
                    m.Result = (IntPtr)isClose;
                    break;
                default:
                base.WndProc(ref m);
                break;
            }
            
        }
        private void button1_Click(object sender, EventArgs e)
        {
            isClose = 0;
            MessageBox.Show("禁止關閉操作系統");
        }
        private void button2_Click(object sender, EventArgs e)
        {
            isClose = 1;
            MessageBox.Show("允許關閉操作系統");
        }
    }
}
