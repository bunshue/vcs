using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_BIOS
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
            richTextBox1.Text += "\n獲取主機板BIOS序號\n";
            richTextBox1.Text += "\nWin32_BIOS\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "主機板BIOS序號：" + mo["SerialNumber"].ToString().Trim() + "\n";

                richTextBox1.Text += "主機板BIOS名稱：" + mo["Name"].ToString().Trim() + "\n";

                richTextBox1.Text += "主機板BIOS時間：" + mo["ReleaseDate"].ToString().Trim() + "\n";
                richTextBox1.Text += "主機板BIOS製造商：" + mo["Manufacturer"].ToString().Trim() + "\n";
                richTextBox1.Text += "主機板BIOS版本：" + mo["SMBIOSBIOSVersion"].ToString().Trim() + "\n";
            }
        }
    }
}
