using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Threading;

namespace 取得計算機內存訊息
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Memory()
        {
            Microsoft.VisualBasic.Devices.Computer myInfo = new Microsoft.VisualBasic.Devices.Computer();
            //取得物理內存總量
            pbMemorySum.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemorySum.Value = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            lblSum.Text = (myInfo.Info.TotalPhysicalMemory / 1024).ToString();
            //取得可用物理內存總量
            pbMemoryUse.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemoryUse.Value = Convert.ToInt32(myInfo.Info.AvailablePhysicalMemory / 1024 / 1024);
            lblMuse.Text = (myInfo.Info.AvailablePhysicalMemory / 1024).ToString();
            //取得虛擬內存總量
            pbVmemorysum.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemorysum.Value = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            lblVinfo.Text = (myInfo.Info.TotalVirtualMemory / 1024).ToString();
            //取得可用虛擬內存總量
            pbVmemoryuse.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemoryuse.Value = Convert.ToInt32(myInfo.Info.AvailableVirtualMemory / 1024 / 1024);
            lblVuse.Text = (myInfo.Info.AvailableVirtualMemory / 1024).ToString();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            CheckForIllegalCrossThreadCalls = false;
        }
        Thread td;
        private void timer1_Tick(object sender, EventArgs e)
        {
            td = new Thread(new ThreadStart(Memory));
            td.Start();
        }

        private void pbVmemorysum_Click(object sender, EventArgs e)
        {

        }
    }
}
