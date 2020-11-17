using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考 / 加入參考 / .NET  System.Management

using System.Management;

namespace vcs_test_all_05_TreeView
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject info in searcher.Get())
            {
                TreeNode node = treeView1.Nodes.Add(info["DeviceID"].ToString());
                node.Nodes.Add("Model: " + info["Model"].ToString());
                node.Nodes.Add("Interface: " + info["InterfaceType"].ToString());
                node.Nodes.Add("Serial#: " + info["SerialNumber"].ToString());
            }
            treeView1.ExpandAll();

            
        }
    }
}
