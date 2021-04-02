using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;

namespace 獲得硬盤序列號
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            string strHardDiskID ="";
            foreach (ManagementObject mo in searcher.Get())
            {
                strHardDiskID = mo["SerialNumber"].ToString().Trim();
                break;
            }
            label2.Text = strHardDiskID;
        }
    }
}