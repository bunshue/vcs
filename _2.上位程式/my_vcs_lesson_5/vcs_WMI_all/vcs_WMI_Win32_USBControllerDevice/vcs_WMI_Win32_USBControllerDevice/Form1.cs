using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_USBControllerDevice
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
            richTextBox1.Text += "\nWin32_USBControllerDevice\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBControllerDevice");
            foreach (ManagementObject mo in mos.Get())
            {
                //richTextBox1.Text += "NegotiatedDataWidth: " + mo["NegotiatedDataWidth"].ToString() + "\n";
                //richTextBox1.Text += "NegotiatedSpeed: " + mo["NegotiatedSpeed"].ToString() + "\n";
                //richTextBox1.Text += "AccessState: " + mo["AccessState"].ToString() + "\n";
                //richTextBox1.Text += "NumberOfHardResets: " + mo["NumberOfHardResets"].ToString() + "\n";
                //richTextBox1.Text += "NumberOfSoftResets: " + mo["NumberOfSoftResets"].ToString() + "\n";

            }
        }
    }
}
