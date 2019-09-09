using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_Network_X
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
            richTextBox1.Text += "\n獲取網卡MAC位址\n";
            richTextBox1.Text += "\nWin32_NetworkAdapterConfiguration\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "網卡MAC位址: " + mo["MacAddress"].ToString() + "\n";
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("root\\CIMV2", "SELECT * FROM Win32_NetworkAdapter");

            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += "-----------------------------------\n";
                richTextBox1.Text += "Win32_NetworkAdapter instance\n";
                richTextBox1.Text += "Caption: {0}" + mo["Caption"] + "\n";

                richTextBox1.Text += mo["Caption"] + "\n";
                richTextBox1.Text += mo["AdapterType"] + "\n";
                richTextBox1.Text += mo["CreationClassName"] + "\n";
                richTextBox1.Text += mo["Description"] + "\n";
                richTextBox1.Text += mo["DeviceID"] + "\n";
                richTextBox1.Text += mo["ErrorDescription"] + "\n";
                //richTextBox1.Text += mo["GUID"] + "\n";
                richTextBox1.Text += mo["MACAddress"] + "\n";
                richTextBox1.Text += mo["Manufacturer"] + "\n";
                richTextBox1.Text += mo["Name"] + "\n";
                richTextBox1.Text += mo["NetConnectionID"] + "\n";
                richTextBox1.Text += mo["PermanentAddress"] + "\n";
                richTextBox1.Text += mo["PNPDeviceID"] + "\n";
                richTextBox1.Text += mo["ProductName"] + "\n";
                richTextBox1.Text += mo["ServiceName"] + "\n";
                richTextBox1.Text += mo["Status"] + "\n";
                richTextBox1.Text += mo["SystemCreationClassName"] + "\n";
                richTextBox1.Text += mo["SystemName"] + "\n";
            }

        }
    }
}
