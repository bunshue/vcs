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

namespace 檢查驅動器容量
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
            DriveInfo dinfo = new DriveInfo(comboBox1.Text);
            label2.Text = "驅動器總容量：" + dinfo.TotalSize + "B";
            label3.Text = "驅動器剩餘容量：" + dinfo.TotalFreeSpace + "B";
        }
    }
}