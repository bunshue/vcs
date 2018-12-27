using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_USBHub
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
            richTextBox1.Text += "\nWin32_USBHub\n";
            //取得USB資訊
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "==========================================================";
                richTextBox1.Text += Environment.NewLine;
                richTextBox1.Text += "Name : " + mo["Name"].ToString();
                richTextBox1.Text += Environment.NewLine;
                richTextBox1.Text += "DeviceID : " + mo["DeviceID"].ToString();
                richTextBox1.Text += Environment.NewLine;
            }
            richTextBox1.Text += "==========================================================";
            richTextBox1.Text += Environment.NewLine;
        }
    }
}
