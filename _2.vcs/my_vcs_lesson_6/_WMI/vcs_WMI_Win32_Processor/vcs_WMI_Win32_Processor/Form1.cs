using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_Processor
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
            richTextBox1.Text += "\nWMI寫法一：\n";
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += mo["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo["VolumeSerialNumber"] + "\n";
            }

            richTextBox1.Text += "\nWin32_Processor\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                // 取得CPU資訊
                richTextBox1.Text += "CPU名稱： " + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "CPU序號： " + mo["ProcessorId"].ToString() + "\n";
                richTextBox1.Text += "CPU使用率： " + mo["LoadPercentage"].ToString() + " %\n";
                richTextBox1.Text += "CPU製造商： " + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "CPU當前時鐘頻率： " + mo["CurrentClockSpeed"].ToString() + "\n";

                richTextBox1.Text += "MaxClockSpeed： " + ((mo["MaxClockSpeed"] == null) ? string.Empty : mo["MaxClockSpeed"].ToString()) + "\n";　//獲取最大時鐘頻率
                richTextBox1.Text += "ExtClock： " + ((mo["ExtClock"] == null) ? string.Empty : mo["ExtClock"].ToString()) + "\n";　//獲取外部頻率
                richTextBox1.Text += "CurrentVoltage： " + ((mo["CurrentVoltage"] == null) ? string.Empty : mo["CurrentVoltage"].ToString()) + "\n";　//獲取當前電壓
                richTextBox1.Text += "L2CacheSize： " + ((mo["L2CacheSize"] == null) ? string.Empty : mo["L2CacheSize"].ToString()) + "\n";　//獲取二級緩存
                richTextBox1.Text += "DataWidth： " + ((mo["DataWidth"] == null) ? string.Empty : mo["DataWidth"].ToString()) + "\n";　//獲取數據帶寬
                richTextBox1.Text += "AddressWidth： " + ((mo["AddressWidth"] == null) ? string.Empty : mo["AddressWidth"].ToString()) + "\n";　//獲取地址帶寬
                richTextBox1.Text += "NumberOfCores： " + ((mo["NumberOfCores"] == null) ? string.Empty : mo["NumberOfCores"].ToString()) + "\n"; //內核
                richTextBox1.Text += "NumberOfLogicalProcessors： " + ((mo["NumberOfLogicalProcessors"] == null) ? string.Empty : mo["NumberOfLogicalProcessors"].ToString()) + "\n";    //邏輯處理器
                richTextBox1.Text += "LoadPercentage： " + ((mo["LoadPercentage"] == null) ? 0 : float.Parse(mo["LoadPercentage"].ToString())) + "\n";
            
            }

            // 或透過 ManagementObject 類別直接存取特定 CPU 序號
            ManagementObject wmiObj = new ManagementObject("Win32_Processor.DeviceID='CPU0'");
            richTextBox1.Text += "CPU ID:\t" + wmiObj.GetPropertyValue("ProcessorId").ToString() + Environment.NewLine;



        }

        private void button2_Click(object sender, EventArgs e)
        {
            Double CPUtprt = 0;
            System.Management.ManagementObjectSearcher mos = new System.Management.ManagementObjectSearcher(@"root\WMI", "Select * From MSAcpi_ThermalZoneTemperature");

            foreach (System.Management.ManagementObject mo in mos.Get())
            {
                CPUtprt = Convert.ToDouble(Convert.ToDouble(mo.GetPropertyValue("CurrentTemperature").ToString()) - 2732) / 10;
                richTextBox1.Text += "CPU 溫度 : " + CPUtprt.ToString() + " °C\n";
            }

        }
    }
}
