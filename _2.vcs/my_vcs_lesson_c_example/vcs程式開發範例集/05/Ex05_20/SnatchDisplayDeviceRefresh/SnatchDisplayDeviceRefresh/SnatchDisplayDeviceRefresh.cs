﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;

namespace SnatchDisplayDeviceRefresh
{
    public partial class SnatchDisplayDeviceRefresh : Form
    {
        public SnatchDisplayDeviceRefresh()
        {
            InitializeComponent();
        }

        private void snatch_Click(object sender,EventArgs e)
        {
            ManagementObjectSearcher RefreshSearcher = new ManagementObjectSearcher("select * from Win32_VideoController");//声明一个用于检索设备管理信息的对象
            foreach(ManagementObject RefreshObject in RefreshSearcher.Get())//循环遍历WMI实例中的每一个对象
            {
                maxRefresh.Text  = RefreshObject["MaxRefreshRate"].ToString(); //在当前文本框中显示最大刷新率
                minRefresh.Text = RefreshObject["MinRefreshRate"].ToString(); //在当前文本框中显示最小刷新率
                nowRefresh.Text = RefreshObject["CurrentRefreshRate"].ToString(); //在当前文本框中显示当前刷新率
            }
            snatch.Enabled = false;//设置“获取”按钮为不可用状态
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }
    }
}
