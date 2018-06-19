using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_VideoController
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
            richTextBox1.Text += "\n獲取顯示卡資訊\n";
            richTextBox1.Text += "\nWin32_VideoController\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_VideoController");
            //ManagementObjectSearcher mos = new ManagementObjectSearcher(@"root\CIMV2", "SELECT * FROM Win32_VideoController");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "顯示設備訊息\n";
                richTextBox1.Text += "名稱： " + mo["Name"].ToString() + "\n";//顯示設備名稱
                richTextBox1.Text += "設備ID" + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "PNPDeviceID： " + mo["PNPDeviceID"].ToString() + "\n";//顯示設備的PNPDeviceID
                richTextBox1.Text += "驅動程序文件： " + mo["InstalledDisplayDrivers"].ToString() + "\n";//顯示設備的驅動程序文件
                richTextBox1.Text += "驅動版本號： " + mo["DriverVersion"].ToString() + "\n";//顯示設備的驅動版本號
                richTextBox1.Text += "顯示處理器： " + mo["VideoProcessor"].ToString() + "\n";//顯示設備的顯示處理器
                richTextBox1.Text += "最大更新率： " + mo["MaxRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "最小更新率： " + mo["MinRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "顯示設備目前顯示模式： " + mo["VideoModeDescription"].ToString() + "\n";//顯示設備目前顯示模式
                richTextBox1.Text += "配接器相容性 " + mo["AdapterCompatibility"].ToString() + "\n";
                richTextBox1.Text += "配接器類型 " + mo["AdapterDACType"].ToString() + "\n";
                richTextBox1.Text += "字幕" + mo["Caption"].ToString() + "\n";
                richTextBox1.Text += "目前比特每圖元" + mo["CurrentBitsPerPixel"].ToString() + "\n";
                richTextBox1.Text += "目前的水準解析度" + mo["CurrentHorizontalResolution"].ToString() + "\n";
                richTextBox1.Text += "描述" + mo["Description"].ToString() + "\n";

            }
        }
    }
}
