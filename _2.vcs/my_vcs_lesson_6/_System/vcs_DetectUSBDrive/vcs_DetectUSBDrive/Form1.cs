using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_DetectUSBDrive
{
    public partial class Form1 : Form
    {
        CUSBMonitor usbMonitor = new CUSBMonitor();

        //windows消息處理函數 捕獲Message的系統硬件改變發出的系統消息
        protected override void WndProc(ref Message m)
        {
            usbMonitor.FillData(this, m, listBox1);

            base.WndProc(ref m);
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
