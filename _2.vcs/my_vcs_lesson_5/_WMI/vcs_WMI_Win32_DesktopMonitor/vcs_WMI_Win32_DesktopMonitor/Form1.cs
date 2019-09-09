using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_DesktopMonitor
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
            richTextBox1.Text += "\n獲取顯示器資訊\n";
            richTextBox1.Text += "\nWin32_DesktopMonitor\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DesktopMonitor");
            foreach (ManagementObject mo in mos.Get())
            {

                richTextBox1.Text += "Name: " + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "Status: " + mo["Status"].ToString() + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"].ToString() + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"].ToString() + "\n";
                //richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription"].ToString() + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"].ToString() + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"].ToString() + "\n";
                richTextBox1.Text += "Description: " + mo["Description"].ToString() + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"].ToString() + "\n";
                richTextBox1.Text += "MonitorManufacturer: " + mo["MonitorManufacturer"].ToString() + "\n";
                richTextBox1.Text += "MonitorType: " + mo["MonitorType"].ToString() + "\n";



                richTextBox1.Text += "Availability: " + mo["Availability"].ToString() + "\n";
                //richTextBox1.Text += "Bandwidth: " + mo["Bandwidth"].ToString() + "\n";
                richTextBox1.Text += "ConfigManagerErrorCode: " + mo["ConfigManagerErrorCode"].ToString() + "\n";
                richTextBox1.Text += "ScreenHeight: " + mo["ScreenHeight"].ToString() + "\n";
                richTextBox1.Text += "ScreenWidth: " + mo["ScreenWidth"].ToString() + "\n";
                //richTextBox1.Text += "StatusInfo: " + mo["StatusInfo"].ToString() + "\n";
                //richTextBox1.Text += "DisplayType: " + mo["DisplayType"].ToString() + "\n";
                //richTextBox1.Text += "LastErrorCode: " + mo["LastErrorCode"].ToString() + "\n";
                richTextBox1.Text += "PixelsPerXLogicalInch: " + mo["PixelsPerXLogicalInch"].ToString() + "\n";
                richTextBox1.Text += "PixelsPerYLogicalInch: " + mo["PixelsPerYLogicalInch"].ToString() + "\n";
                //richTextBox1.Text += "PowerManagementCapabilities: " + mo["PowerManagementCapabilities[]"].ToString() + "\n";

                //richTextBox1.Text += "IsLocked: " + mo["IsLocked"].ToString() + "\n";
                //richTextBox1.Text += "PowerManagementSupported: " + mo["PowerManagementSupported"].ToString() + "\n";
                richTextBox1.Text += "ConfigManagerUserConfig: " + mo["ConfigManagerUserConfig"].ToString() + "\n";
                //richTextBox1.Text += "ErrorCleared: " + mo["ErrorCleared"].ToString() + "\n";

                //richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";




            }


        }
    }
}
