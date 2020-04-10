using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_LogicalDisk
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
            richTextBox1.Text += "\n獲取硬碟分區資訊\n";
            richTextBox1.Text += "\nWin32_LogicalDisk\n";

            richTextBox1.Text += "\n指定邏輯磁碟機\n";

            //寫法一，直接寫D槽
            //ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk WHERE DeviceID = 'D:'");

            //寫法二，用變數
            string strDrive = "C:"; // 指定C: 邏輯磁碟機
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk WHERE DeviceID = " + "\"" + strDrive + "\"");

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "磁片類型: " + mo["Description"].ToString() + "\n";
                richTextBox1.Text += "分區類型: " + mo["FileSystem"].ToString() + "\n";
                richTextBox1.Text += "可用空間: " + mo["FreeSpace"].ToString() + "\n";
                richTextBox1.Text += "實際大小: " + mo["Size"].ToString() + "\n";
                richTextBox1.Text += "Name: " + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "VolumeSerialNumber: " + mo["VolumeSerialNumber"] + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"] + "\n";
            }

            richTextBox1.Text += "\n所有硬碟\n";
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
            foreach (ManagementObject mo2 in mos2.Get())
            {
                // 取得磁碟Volumne 名稱跟序號
                richTextBox1.Text += "Name: " + mo2["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo2["VolumeSerialNumber"] + "\n";
            }

        }
    }
}
