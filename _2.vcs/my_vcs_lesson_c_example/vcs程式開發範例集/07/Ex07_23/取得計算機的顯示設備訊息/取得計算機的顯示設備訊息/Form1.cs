using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;
namespace 取得計算機的顯示設備訊息
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        
        private void Form1_Load(object sender, EventArgs e)
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("select * from Win32_VideoController");
            foreach (ManagementObject mobject in searcher.Get())
            {
                lblname.Text = mobject["Name"].ToString();//顯示設備名稱
                lblpnp.Text = mobject["PNPDeviceID"].ToString();//顯示設備的PNPDeviceID
                lbldrivers.Text=mobject["InstalledDisplayDrivers"].ToString();//顯示設備的驅動程序文件
                lblVersion.Text=mobject["DriverVersion"].ToString();//顯示設備的驅動版本號
                lblProcessor.Text=mobject["VideoProcessor"].ToString();//顯示設備的顯示處理器
                lblMaxRefreshRate.Text=mobject["MaxRefreshRate"].ToString();//顯示設備的最大更新率
                lblMinRefreshRate.Text=mobject["MinRefreshRate"].ToString();//顯示設備的最大更新率
                lblDescription.Text=mobject["VideoModeDescription"].ToString();//顯示設備目前顯示模式

            }
        }
    }
}
