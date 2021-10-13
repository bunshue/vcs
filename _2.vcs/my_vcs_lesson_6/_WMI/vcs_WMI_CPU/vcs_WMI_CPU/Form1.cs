using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Management;

namespace vcs_WMI_CPU
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {

            richTextBox1.Text += "獲取CPU編號\n";
            ManagementClass MyClass = new ManagementClass("Win32_Processor");
            ManagementObjectCollection MyCollection = MyClass.GetInstances();
            String MyInfo = "當前系統CPU編號是：";
            string MyCPUID = "";
            foreach (ManagementObject MyObject in MyCollection)
            {
                MyCPUID = MyObject.Properties["ProcessorId"].Value.ToString();
                break;
            }
            MyInfo += MyCPUID;
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "獲取計算機CPU的當前電壓\n";
            MyInfo = "計算機CPU的當前電壓是：";
            ManagementObjectSearcher MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                try
                {
                    MyInfo += "/n" + String.Format("CurrentVoltage : " + MyObject["CurrentVoltage"].ToString());
                    MyInfo += "/n=========================================================";
                }
                catch { }
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "獲取計算機CPU的外部頻率\n";
            MyInfo = "計算機CPU的外部頻率是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                try
                {
                    MyInfo += "/n" + String.Format("ExtClock : " + MyObject["ExtClock"].ToString());
                    MyInfo += "/n=========================================================";
                }
                catch { }
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "獲取計算機CPU的二級緩存\n";
            MyInfo = "計算機CPU的二級緩存尺寸是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("L2CacheSize: " + MyObject["L2CacheSize"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "獲取計算機CPU的制造商名稱\n";
            MyInfo = "計算機CPU的制造商名稱是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("Manufacturer : " + MyObject["Manufacturer"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "獲取計算機CPU的產品名稱\n";
            MyInfo = "計算機CPU的產品名稱是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("Name : " + MyObject["Name"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "獲取計算機CPU的版本信息\n";
            MyInfo = "計算機CPU的版本信息如下：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("Version: " + MyObject["Version"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "獲取計算機CPU的當前使用百分比 注意要把SQLserver或者其他耗CPU的軟件開著否則看不到效果就一直為0\n";
            MyInfo = "計算機CPU的當前使用百分比是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("LoadPercentage : " + MyObject["LoadPercentage"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "獲取計算機CPU的最大時鐘頻率\n";
            MyInfo = "計算機CPU的最大時鐘頻率是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("MaxClockSpeed : " + MyObject["MaxClockSpeed"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "獲取計算機CPU的當前時鐘頻率\n";
            MyInfo = "計算機CPU的當前時鐘頻率是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("CurrentClockSpeed : " + MyObject["CurrentClockSpeed"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "獲取計算機的CPU地址寬度\n";
            MyInfo = "當前計算機的CPU地址寬度是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("AddressWidth: " + MyObject["AddressWidth"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "獲取計算機的CPU數據寬度\n";
            MyInfo = "當前計算機的CPU數據寬度是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("DataWidth : " + MyObject["DataWidth"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";




        }
    }
}
