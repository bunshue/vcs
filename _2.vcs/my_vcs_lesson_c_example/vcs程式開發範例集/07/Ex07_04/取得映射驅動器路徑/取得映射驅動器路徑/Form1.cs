using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;

namespace 取得映射驅動器路徑
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            int i = 0;
            foreach (ManagementObject disk in searcher.Get())
            {
                string DriveType;
                DriveType = disk["DriveType"].ToString();
                if (DriveType == "4")
                    listBox1.Items.Add(disk["Name"].ToString());
                i++;
            }
        }
    }
}