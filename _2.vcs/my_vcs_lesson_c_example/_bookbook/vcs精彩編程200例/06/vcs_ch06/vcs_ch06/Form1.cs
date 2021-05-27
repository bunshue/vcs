using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;
using System.DirectoryServices;

namespace vcs_ch06
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //參考/加入參考/.NET/System.Management
            //得到本机MAC地址
            ManagementObjectSearcher nisc = new ManagementObjectSearcher("select * from Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject nic in nisc.Get())
            {
                if (Convert.ToBoolean(nic["ipEnabled"]) == true)
                {
                    richTextBox1.Text += Convert.ToString(nic["MACAddress"]);

                }
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //參考/加入參考/.NET/System.DirectoryServices
            //获取网络中所有工作组名称
            DirectoryEntry MainGroup = new DirectoryEntry("WinNT:");
            foreach (DirectoryEntry domain in MainGroup.Children)
            {
                richTextBox1.Text += domain.Name + "\n";
                //listBox1.Text = "";
                //listBox1.Items.Add(domain.Name);
            }   



        }
    }
}
