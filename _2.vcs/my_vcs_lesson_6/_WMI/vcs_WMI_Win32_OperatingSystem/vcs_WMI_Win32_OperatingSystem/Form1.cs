using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_OperatingSystem
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
            richTextBox1.Text += "\n獲取系統的啟動日期和安裝日期\n";
            richTextBox1.Text += "\nWin32_OperatingSystem\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "Description: " + mo["Description"].ToString() + "\n";
                richTextBox1.Text += "FreePhysicalMemory: " + mo["FreePhysicalMemory"].ToString() + "\n";
                richTextBox1.Text += "FreeVirtualMemory: " + mo["FreeVirtualMemory"].ToString() + "\n";
                richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";
                richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString().Substring(0, 14) + "\n";
                richTextBox1.Text += "LastBootUpTime: " + mo["LastBootUpTime"].ToString() + "\n";
                richTextBox1.Text += "LastBootUpTime: " + mo["LastBootUpTime"].ToString().Substring(0, 14) + "\n";
                richTextBox1.Text += "LocalDateTime: " + mo["LocalDateTime"].ToString() + "\n";
                richTextBox1.Text += "Name: " + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "Organization: " + mo["Organization"].ToString() + "\n";
                richTextBox1.Text += "OSLanguage: " + mo["OSLanguage"].ToString() + "\n";
                richTextBox1.Text += "OSType: " + mo["OSType"].ToString() + "\n";
                richTextBox1.Text += "RegisteredUser: " + mo["RegisteredUser"].ToString() + "\n";
                richTextBox1.Text += "SerialNumber: " + mo["SerialNumber"].ToString() + "\n";
                richTextBox1.Text += "ServicePackMajorVersion: " + mo["ServicePackMajorVersion"].ToString() + "\n";
                richTextBox1.Text += "ServicePackMinorVersion: " + mo["ServicePackMinorVersion"].ToString() + "\n";

                richTextBox1.Text += "Caption: " + mo["Caption"].ToString() + "\n";　　//獲取OS　名稱
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"].ToString() + "\n";　　//獲取　OS　製造商
                richTextBox1.Text += "CountryCode: " + mo["CountryCode"].ToString() + "\n";　　//地區
                richTextBox1.Text += "CSName: " + mo["CSName"].ToString() + "\n";　　//獲取系統名稱
                richTextBox1.Text += "WindowsDirectory: " + mo["WindowsDirectory"].ToString() + "\n";　　//獲取Windows　目錄
                richTextBox1.Text += "SystemDirectory: " + mo["SystemDirectory"].ToString() + "\n";　　//獲取系統目錄
                richTextBox1.Text += "BootDevice: " + mo["BootDevice"].ToString() + "\n";　　//獲取啟動設備
                richTextBox1.Text += "Version: " + mo["Version"].ToString() + "\n";//獲取版本
                richTextBox1.Text += "CSDVersion: " + mo["CSDVersion"].ToString() + "\n";//獲取SP
                richTextBox1.Text += "BuildNumber: " + mo["BuildNumber"].ToString() + "\n";//獲取builderNumber
                richTextBox1.Text += "TotalVisibleMemorySize: " + ((ulong)mo["TotalVisibleMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取總的物理內存
                richTextBox1.Text += "FreePhysicalMemory: " + ((ulong)mo["FreePhysicalMemory"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取可用物理內存
                richTextBox1.Text += "TotalVirtualMemorySize: " + ((ulong)mo["TotalVirtualMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　　//獲取總的虛擬內存
                richTextBox1.Text += "FreeVirtualMemory: " + ((ulong)mo["FreeVirtualMemory"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取可用虛擬內存
                richTextBox1.Text += "SizeStoredInPagingFiles: " + ((ulong)mo["SizeStoredInPagingFiles"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取頁面文檔大小
            }
        }
    }
}
