using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_PhysicalMemory
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
            richTextBox1.Text += "\nWin32_PhysicalMemory\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMemory");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "BankLabel: " + mo["BankLabel"] + "\n";
                richTextBox1.Text += "Capacity: " + mo["Capacity"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "DataWidth: " + mo["DataWidth"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "DeviceLocator: " + mo["DeviceLocator"] + "\n";
                richTextBox1.Text += "FormFactor: " + mo["FormFactor"] + "\n";
                richTextBox1.Text += "HotSwappable: " + mo["HotSwappable"] + "\n";
                richTextBox1.Text += "InstallDate: " + mo["InstallDate"] + "\n";
                richTextBox1.Text += "InterleaveDataDepth: " + mo["InterleaveDataDepth"] + "\n";
                richTextBox1.Text += "InterleavePosition: " + mo["InterleavePosition"] + "\n";
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"] + "\n";
                richTextBox1.Text += "MemoryType: " + mo["MemoryType"] + "\n";
                richTextBox1.Text += "Model: " + mo["Model"] + "\n";
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                richTextBox1.Text += "OtherIdentifyingInfo: " + mo["OtherIdentifyingInfo"] + "\n";
                richTextBox1.Text += "PartNumber: " + mo["PartNumber"] + "\n";
                richTextBox1.Text += "PositionInRow: " + mo["PositionInRow"] + "\n";
                richTextBox1.Text += "PoweredOn: " + mo["PoweredOn"] + "\n";
                richTextBox1.Text += "Removable: " + mo["Removable"] + "\n";
                richTextBox1.Text += "Replaceable: " + mo["Replaceable"] + "\n";
                richTextBox1.Text += "SerialNumber: " + mo["SerialNumber"] + "\n";
                richTextBox1.Text += "SKU: " + mo["SKU"] + "\n";
                richTextBox1.Text += "Speed: " + mo["Speed"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "Tag: " + mo["Tag"] + "\n";
                richTextBox1.Text += "TotalWidth: " + mo["TotalWidth"] + "\n";
                richTextBox1.Text += "TypeDetail: " + mo["TypeDetail"] + "\n";
                richTextBox1.Text += "Version: " + mo["Version"] + "\n";

            }



        }

        private void button2_Click(object sender, EventArgs e)
        {

        }
    }
}
