using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_PnPEntity
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
            richTextBox1.Text += "\nWin32_PnPEntity\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PnPEntity");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"] + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"] + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "StatusInfo: " + mo["StatusInfo".ToString()] + "\n";
                richTextBox1.Text += "Status: " + mo["Status".ToString()] + "\n";
                richTextBox1.Text += "Service: " + mo["Service".ToString()] + "\n";
                richTextBox1.Text += "ClassGuid: " + mo["ClassGuid".ToString()] + "\n";
                richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription".ToString()] + "\n";
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer".ToString()] + "\n";
            }
        }
    }
}
