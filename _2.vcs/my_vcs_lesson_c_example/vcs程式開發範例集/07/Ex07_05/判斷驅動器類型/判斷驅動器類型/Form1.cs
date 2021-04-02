using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;
using System.IO;

namespace 判斷驅動器類型
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject disk in searcher.Get())
            {
                comboBox1.Items.Add(disk["Name"].ToString());
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string DriveType;
            DriveInfo dinfo = new DriveInfo(comboBox1.Text);
            try
            {
                DriveType = dinfo.DriveType.ToString();
                switch (DriveType)
                {
                    case "Unknown":
                        label2.Text = "這是未知設備";
                        break;
                    case "NoRootDirectory":
                        label2.Text = "這是未分區";
                        break;
                    case "Removable":
                        label2.Text = "這是可移動磁盤";
                        break;
                    case "Fixed":
                        label2.Text = "這是硬盤";
                        break;
                    case "Network":
                        label2.Text = "這是網絡驅動器";
                        break;
                    case "CDRom":
                        label2.Text = "這是光驅";
                        break;
                }
            }
            catch
            {
                label2.Text = "這是未知類型";
            }
        }
    }
}