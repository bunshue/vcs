using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_BaseBoard
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
            richTextBox1.Text += "\n獲取主機板資訊\n";
            richTextBox1.Text += "\nWin32_BaseBoard\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "主機板製造商：" + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "產品：" + mo["Product"].ToString() + "\n";
                richTextBox1.Text += "主機板序號：" + mo["SerialNumber"].ToString() + "\n";
            }


        }
    }
}
