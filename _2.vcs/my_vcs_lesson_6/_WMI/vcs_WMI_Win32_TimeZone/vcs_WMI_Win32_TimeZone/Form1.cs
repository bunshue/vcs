using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_TimeZone
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
            richTextBox1.Text += "\n獲取時區資訊\n";
            richTextBox1.Text += "\nWin32_TimeZone\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_TimeZone");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "時區：" + mo["StandardName"].ToString() + "\n";

                //richTextBox1.Text += "Caption: " + mo["Caption"].ToString() + "\n";
                //richTextBox1.Text += "Description: " + mo["Description"].ToString() + "\n";
                //richTextBox1.Text += "SettingID: " + mo["SettingID"].ToString() + "\n";
                richTextBox1.Text += "DaylightName: " + mo["DaylightName"].ToString() + "\n";

            }


        }
    }
}
