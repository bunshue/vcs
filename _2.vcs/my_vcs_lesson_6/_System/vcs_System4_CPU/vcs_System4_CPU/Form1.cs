using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Threading;
using System.Runtime.InteropServices;
using System.Management;

namespace vcs_System4_CPU
{
    public partial class Form1 : Form
    {
        Process[] MyProcesses;
        Thread td;

        public Form1()
        {
            InitializeComponent();
        }

        private void myUser()
        {
            Memory();
        }

        private void Memory()
        {
            Microsoft.VisualBasic.Devices.Computer myInfo = new Microsoft.VisualBasic.Devices.Computer();
            //获取物理内存总量
            pbMemorySum.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemorySum.Value = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            lblSum.Text = (myInfo.Info.TotalPhysicalMemory / 1024).ToString();
            //获取可用物理内存总量
            pbMemoryUse.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemoryUse.Value = Convert.ToInt32(myInfo.Info.AvailablePhysicalMemory / 1024 / 1024);
            lblMuse.Text = (myInfo.Info.AvailablePhysicalMemory / 1024).ToString();
            //获取虚拟内存总量
            pbVmemorysum.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemorysum.Value = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            lblVinfo.Text = (myInfo.Info.TotalVirtualMemory / 1024).ToString();
            //获取可用虚拟内存总量
            pbVmemoryuse.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemoryuse.Value = Convert.ToInt32(myInfo.Info.AvailableVirtualMemory / 1024 / 1024);
            lblVuse.Text = (myInfo.Info.AvailableVirtualMemory / 1024).ToString();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            CheckForIllegalCrossThreadCalls = false;
            MyProcesses = Process.GetProcesses();
            tsslNum.Text = MyProcesses.Length.ToString();
            myUser();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            MyProcesses = Process.GetProcesses();
            tsslNum.Text = MyProcesses.Length.ToString();
            td = new Thread(new ThreadStart(myUser));
            td.Start();
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (td != null)
            {
                td.Abort();
            }
        }
    }
}


//6060
//------------------------------------------------------------  # 60個

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個

//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//richTextBox1.Text += "------------------------------\n";  // 30個
//richTextBox1.Text += "---------------\n";  // 15個


