using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_SoundDevice
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
            richTextBox1.Text += "\n獲取音效卡資訊\n";
            richTextBox1.Text += "\nWin32_SoundDevice\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "音效設備名稱：" + mo["ProductName"].ToString() + "\n"; //在当前文本框中显示声音设备的名称
                richTextBox1.Text += "PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";//在当前文本框中显示声音设备的PNPDeviceID
            }
        }
    }
}
