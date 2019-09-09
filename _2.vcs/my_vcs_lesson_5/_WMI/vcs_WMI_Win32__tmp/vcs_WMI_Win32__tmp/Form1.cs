using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32__tmp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取主機板資訊\n";
            richTextBox1.Text += "\nWin32_BaseBoard\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "主機板製造商：" + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "產品：" + mo["Product"].ToString() + "\n";
                richTextBox1.Text += "主機板序號：" + mo["SerialNumber"].ToString() + "\n";
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n取得本機的MAC\n";
            richTextBox1.Text += "\nWin32_NetworkAdapterConfiguration\n";   //網絡適配器設置
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "取得本機的MAC：" + mo["MacAddress"].ToString() + "\n";
                }

            }


        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n取得網卡地址\n";
            richTextBox1.Text += "\nWin32_NetworkAdapter\n";   //網絡適配器
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "取得網卡地址：" + mo["MacAddress"].ToString() + "\n";
                }

            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取硬碟序號\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "硬碟序號：" + mo["Model"].ToString() + "\n";
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {
            //fail
            richTextBox1.Text += "\n獲取IP位址\n";
            richTextBox1.Text += "\nWin32_NetworkAdapterConfiguration\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                    richTextBox1.Text += "IP " + mo["IpAddress"] + "\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n一些資訊\n";

            richTextBox1.Text += "\n顯卡PNPDeviceID\n";
            richTextBox1.Text += "\nWin32_VideoController\n";
            ManagementObjectSearcher mos1 = new ManagementObjectSearcher("SELECT * FROM Win32_VideoController");
            foreach (ManagementObject mo in mos1.Get())
            {
                richTextBox1.Text += "顯卡PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";
            }


            richTextBox1.Text += "\n聲卡PNPDeviceID\n";
            richTextBox1.Text += "\nWin32_SoundDevice\n";
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");
            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += "聲卡PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";
            }

            richTextBox1.Text += "\nCPU版本信息\n";
            richTextBox1.Text += "\nWin32_Processor\n";
            ManagementObjectSearcher mos3 = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos3.Get())
            {
                richTextBox1.Text += "CPU名稱：" + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "CPU版本信息：" + mo["Version"].ToString() + "\n";
                richTextBox1.Text += "CPU製造廠商：" + mo["Manufacturer"].ToString() + "\n";
            }


        }
    }
}
