using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_PhysicalMedia
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
            richTextBox1.Text += "\n獲取媒體資訊\n";
            richTextBox1.Text += "\nWin32_PhysicalMedia\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            foreach (ManagementObject mo in mos.Get())
            {
                // get the hard drive from collection
                // using index
                //HardDrive hd = (HardDrive)hdCollection[i];

                // get the hardware serial no.
                if (mo["SerialNumber"] == null)
                {
                    //hd.SerialNo = "None";
                    richTextBox1.Text += "None" + "\n";
                }
                else
                {
                    richTextBox1.Text += mo["SerialNumber"].ToString() + "\n";
                }
            }
        }
    }
}
