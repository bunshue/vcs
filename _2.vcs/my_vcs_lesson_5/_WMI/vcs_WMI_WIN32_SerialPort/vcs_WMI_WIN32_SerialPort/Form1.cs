using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_SerialPort
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
            richTextBox1.Text += "\nWin32_SerialPort\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_SerialPort");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"] + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"] + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "ProviderType: " + mo["ProviderType"] + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "MaxBaudRate: " + mo["MaxBaudRate".ToString()] + "\n";
                richTextBox1.Text += "StatusInfo: " + mo["StatusInfo".ToString()] + "\n";


                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription"] + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"] + "\n";
                //richTextBox1.Text += "CapabilityDescriptions: " + mo["CapabilityDescriptions[]"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "ProviderType: " + mo["ProviderType"] + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"] + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"] + "\n";

                richTextBox1.Text += "Availability: " + mo["Availability".ToString()] + "\n";
                //richTextBox1.Text += "Capabilities: " + mo["Capabilities[]".ToString()] + "\n";
                richTextBox1.Text += "ConfigManagerErrorCode: " + mo["ConfigManagerErrorCode".ToString()] + "\n";
                richTextBox1.Text += "LastErrorCode: " + mo["LastErrorCode".ToString()] + "\n";
                richTextBox1.Text += "MaxBaudRate: " + mo["MaxBaudRate".ToString()] + "\n";
                richTextBox1.Text += "MaximumInputBufferSize: " + mo["MaximumInputBufferSize".ToString()] + "\n";
                richTextBox1.Text += "MaximumOutputBufferSize: " + mo["MaximumOutputBufferSize".ToString()] + "\n";
                richTextBox1.Text += "MaxNumberControlled: " + mo["MaxNumberControlled".ToString()] + "\n";
                //richTextBox1.Text += "PowerManagementCapabilities: " + mo["PowerManagementCapabilities[]".ToString()] + "\n";
                richTextBox1.Text += "ProtocolSupported: " + mo["ProtocolSupported".ToString()] + "\n";
                richTextBox1.Text += "StatusInfo: " + mo["StatusInfo".ToString()] + "\n";

                richTextBox1.Text += "Binary: " + mo["Binary".ToString()] + "\n";
                richTextBox1.Text += "ConfigManagerUserConfig: " + mo["ConfigManagerUserConfig".ToString()] + "\n";
                richTextBox1.Text += "ErrorCleared: " + mo["ErrorCleared".ToString()] + "\n";
                richTextBox1.Text += "OSAutoDiscovered: " + mo["OSAutoDiscovered".ToString()] + "\n";
                richTextBox1.Text += "PowerManagementSupported: " + mo["PowerManagementSupported".ToString()] + "\n";
                richTextBox1.Text += "SettableBaudRate: " + mo["SettableBaudRate".ToString()] + "\n";
                richTextBox1.Text += "SettableDataBits: " + mo["SettableDataBits".ToString()] + "\n";
                richTextBox1.Text += "SettableFlowControl: " + mo["SettableFlowControl".ToString()] + "\n";
                richTextBox1.Text += "SettableParity: " + mo["SettableParity".ToString()] + "\n";
                richTextBox1.Text += "SettableParityCheck: " + mo["SettableParityCheck".ToString()] + "\n";
                richTextBox1.Text += "SettableRLSD: " + mo["SettableRLSD".ToString()] + "\n";
                richTextBox1.Text += "SettableStopBits: " + mo["SettableStopBits".ToString()] + "\n";
                richTextBox1.Text += "Supports16BitMode: " + mo["Supports16BitMode".ToString()] + "\n";
                richTextBox1.Text += "SupportsDTRDSR: " + mo["SupportsDTRDSR".ToString()] + "\n";
                richTextBox1.Text += "SupportsElapsedTimeouts: " + mo["SupportsElapsedTimeouts".ToString()] + "\n";
                richTextBox1.Text += "SupportsIntTimeouts: " + mo["SupportsIntTimeouts".ToString()] + "\n";
                richTextBox1.Text += "SupportsParityCheck: " + mo["SupportsParityCheck".ToString()] + "\n";
                richTextBox1.Text += "SupportsRLSD: " + mo["SupportsRLSD".ToString()] + "\n";
                richTextBox1.Text += "SupportsRTSCTS: " + mo["SupportsRTSCTS".ToString()] + "\n";
                richTextBox1.Text += "SupportsSpecialCharacters: " + mo["SupportsSpecialCharacters".ToString()] + "\n";
                richTextBox1.Text += "SupportsXOnXOff: " + mo["SupportsXOnXOff".ToString()] + "\n";
                richTextBox1.Text += "SupportsXOnXOffSet: " + mo["SupportsXOnXOffSet".ToString()] + "\n";

                richTextBox1.Text += "TimeOfLastReset: " + mo["TimeOfLastReset".ToString()] + "\n";
                richTextBox1.Text += "InstallDate: " + mo["InstallDate".ToString()] + "\n";



            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nMSSerial_PortName\n";
            //找USB插入的佔用的Port name
            ManagementObjectSearcher mos = new ManagementObjectSearcher("root\\WMI", "SELECT * FROM MSSerial_PortName");
            //ManagementObjectSearcher mos = new ManagementObjectSearcher("root\\WMI", "SELECT * FROM MSSerial_PortName Where InstanceName like '%VID_067B&PID_2303%'");   //這裡是利用Prolific做的驅動程式
            //ManagementObjectSearcher mos = new ManagementObjectSearcher("root\\WMI", "SELECT * FROM MSSerial_PortName Where InstanceName like '%USB%'");                 //搜尋名字含有USB的部分

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "\nInstanceName: " + mo["InstanceName"] + "\n";
                richTextBox1.Text += "PortName: " + mo["PortName"] + "\n";
                richTextBox1.Text += "Active: " + mo["Active"].ToString() + "\n";

                //If the serial port's instance name contains USB 
                //it must be a USB to serial device
                if (mo["InstanceName"].ToString().Contains("USB"))
                {
                    richTextBox1.Text += "\t" + mo["PortName"] + " is a USB to SERIAL adapter/converter" + "\n";
                }
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }
    }
}
