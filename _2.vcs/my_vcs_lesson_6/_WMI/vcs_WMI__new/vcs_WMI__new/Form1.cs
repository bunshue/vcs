using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Net;       //for Dns
using System.Diagnostics;       //for Process
using System.Collections;   //for DictionaryEntry
using Microsoft.Win32;  //for Registry

using System.Runtime.InteropServices;

// WMI(Windows Management Instrumentation)
// 1. 專案->參考->右鍵->加入參考->.NET->選System.Management->確定
// 2. using System.Management;

//參考 / 加入參考 / .NET  System.Management
using System.Management;    //for WMI

//WMI是Windows Management Instrumentation的簡稱，即：視窗管理規范。

namespace vcs_WMI__new
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            string[] win32_cmd = new string[] { "Win32_BaseBoard", "Win32_Battery", "Win32_BIOS", "Win32_DiskDrive", "Win32_IDEController", "Win32_NetworkAdapter", "Win32_NetworkAdapterConfiguration", "Win32_Processor", "Win32_SerialPort", "Win32_USBController", "Win32_USBHub", "Win32_VideoController", "Win32_VideoSettings" };
            comboBox1.Items.AddRange(win32_cmd);
            comboBox1.Text = win32_cmd[0];
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 12;
            y_st = 12;
            dx = 205;
            dy = 75;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            richTextBox1.Size = new Size(500, 700 + 40);
            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            comboBox1.Location = new Point(x_st + dx * 3 + 500 + 10, y_st + dy * 0);
            bt_get.Location = new Point(x_st + dx * 3 + 500 + 10 + comboBox1.Width + 10, y_st + dy * 0);
            listView1.Size = new Size(400, 700);
            listView1.Location = new Point(x_st + dx * 3 + 500 + 10, y_st + dy * 0 + 40);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //設定表單Client的大小
            this.SetClientSizeCore(1050 + 500, 770);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            listView1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Win32_PageFile 獲取頁面文檔\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PageFile");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "FileName: " + mo["Name"].ToString() + "\n";　　//頁面文檔
                //richTextBox1.Text += "FileName: " + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Status"].ToString() + "\n";
                //richTextBox1.Text += "FileName: " + mo["Version"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Caption"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Description"].ToString() + "\n";
                //richTextBox1.Text += "FileName: " + mo["CompressionMethod"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["CSCreationClassName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["CSName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Drive"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["CreationClassName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["EightDotThreeFileName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FileType"].ToString() + "\n";
                //richTextBox1.Text += "FileName: " + mo["EncryptionMethod"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Extension"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FileName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FSCreationClassName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FSName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Path"].ToString() + "\n";


                long FileSize = mo["FileSize"] == null ? 0 : long.Parse(mo["FileSize"].ToString());//頁面文檔大小
                //計算
                richTextBox1.Text += "FileSize: " + (FileSize / 1024 / 1024).ToString("#0.00") + "G" + "\n";

                richTextBox1.Text += "FileSize: " + mo["FileSize"].ToString() + "\n";
                //richTextBox1.Text += "InUseCount: " + mo["InUseCount"].ToString() + "\n";
                //richTextBox1.Text += "AccessMask: " + mo["AccessMask"].ToString() + "\n";
                //richTextBox1.Text += "FreeSpace: " + mo["FreeSpace"].ToString() + "\n";
                richTextBox1.Text += "InitialSize: " + mo["InitialSize"].ToString() + "\n";
                richTextBox1.Text += "MaximumSize: " + mo["MaximumSize"].ToString() + "\n";

                richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";
                richTextBox1.Text += "CreationDate: " + mo["CreationDate"].ToString() + "\n";
                richTextBox1.Text += "LastAccessed: " + mo["LastAccessed"].ToString() + "\n";
                richTextBox1.Text += "LastModified: " + mo["LastModified"].ToString() + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取CPU的溫度, NG\n";

            //GetCPUTemperature();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            Double CPUtprt = 0;
            mos = new ManagementObjectSearcher(@"root\WMI", "SELECT * FROM MSAcpi_ThermalZoneTemperature");

            foreach (ManagementObject mo in mos.Get())
            {
                CPUtprt = Convert.ToDouble(Convert.ToDouble(mo.GetPropertyValue("CurrentTemperature").ToString()) - 2732) / 10;
                richTextBox1.Text += "CPU 溫度 : " + CPUtprt.ToString() + " °C\n";
            }
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //Win32_Processor

            richTextBox1.Text += "取得處理器參數 :\n";
            //查詢CPU訊息
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    // 取得CPU資訊
                    richTextBox1.Text += "CPU名稱 : " + mo["Name"].ToString() + "\n";

                    richTextBox1.Text += "CPU序號 : " + mo["ProcessorId"].ToString() + "\n";
                    richTextBox1.Text += "CPU序號 : " + mo.GetPropertyValue("ProcessorId").ToString() + "\n";
                    richTextBox1.Text += "CPU序號 : " + mo.Properties["ProcessorId"].Value.ToString() + "\n";

                    // NG richTextBox1.Text += "CPU使用率 : " + mo["LoadPercentage"].ToString() + " %\n"; LoadPercentage 像是被廢棄
                    richTextBox1.Text += "CPU使用率 : " + ((mo["LoadPercentage"] == null) ? 0 : float.Parse(mo["LoadPercentage"].ToString())) + "\n";

                    richTextBox1.Text += "CPU製造商 : " + mo["Manufacturer"].ToString() + "\n";
                    richTextBox1.Text += "CPU製造商 : " + mo.GetPropertyValue("Manufacturer").ToString() + "\n";

                    richTextBox1.Text += "CPU當前時鐘頻率 : " + mo["CurrentClockSpeed"].ToString() + "\n";

                    richTextBox1.Text += "MaxClockSpeed : " + ((mo["MaxClockSpeed"] == null) ? string.Empty : mo["MaxClockSpeed"].ToString()) + "\n";　//獲取最大時鐘頻率
                    richTextBox1.Text += "ExtClock : " + ((mo["ExtClock"] == null) ? string.Empty : mo["ExtClock"].ToString()) + "\n";　//獲取外部頻率
                    richTextBox1.Text += "CurrentVoltage : " + ((mo["CurrentVoltage"] == null) ? string.Empty : mo["CurrentVoltage"].ToString()) + "\n";　//獲取當前電壓
                    richTextBox1.Text += "L2CacheSize : " + ((mo["L2CacheSize"] == null) ? string.Empty : mo["L2CacheSize"].ToString()) + "\n";　//獲取二級緩存
                    richTextBox1.Text += "DataWidth : " + ((mo["DataWidth"] == null) ? string.Empty : mo["DataWidth"].ToString()) + "\n";　//獲取數據帶寬
                    richTextBox1.Text += "位元數\n";
                    richTextBox1.Text += "AddressWidth : " + ((mo["AddressWidth"] == null) ? string.Empty : mo["AddressWidth"].ToString()) + "\n";　//獲取地址帶寬
                    richTextBox1.Text += "NumberOfCores : " + ((mo["NumberOfCores"] == null) ? string.Empty : mo["NumberOfCores"].ToString()) + "\n"; //內核
                    richTextBox1.Text += "NumberOfLogicalProcessors : " + ((mo["NumberOfLogicalProcessors"] == null) ? string.Empty : mo["NumberOfLogicalProcessors"].ToString()) + "\n";    //邏輯處理器

                    richTextBox1.Text += "CPU版本號 : " + mo["Version"].ToString() + "\n";

                    //ID[i] = mo.GetPropertyValue("Id").ToString(); not known
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                //取得核心數
                int num_cores = int.Parse(mo["NumberOfCores"].ToString());
                richTextBox1.Text += "取得核心數 : " + num_cores.ToString() + "\n";
                richTextBox1.Text += "Cores\t" + num_cores.ToString() + "\n";

                //取出作業系統的位元數 32位元/64位元
                richTextBox1.Text += "讀取CPU的地址寬度\n";
                richTextBox1.Text += mo.Properties["AddressWidth"].Value.ToString() + "-bit" + "\n";
                string result = String.Format("AddressWidth: " + mo["AddressWidth"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "讀取CPU編號\n";
                result = mo.Properties["ProcessorId"].Value.ToString();
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "讀取計算機CPU的當前電壓\n";
                try
                {
                    result = String.Format("CurrentVoltage : " + mo["CurrentVoltage"].ToString());
                    richTextBox1.Text += result + "\n";
                }
                catch { }

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的外部頻率\n";
                try
                {
                    result = String.Format("ExtClock : " + mo["ExtClock"].ToString());
                    richTextBox1.Text += result + "\n";
                }
                catch { }

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的二級緩存尺寸\n";
                result = String.Format("L2CacheSize: " + mo["L2CacheSize"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的制造商名稱\n";
                result = String.Format("Manufacturer : " + mo["Manufacturer"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的產品名稱\n";
                result = String.Format("Name : " + mo["Name"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的版本信息\n";
                result = String.Format("Version: " + mo["Version"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的當前使用百分比 注意要把SQLserver或者其他耗CPU的軟件開著否則看不到效果就一直為0\n";
                richTextBox1.Text += "計算機CPU的當前使用百分比是：";
                //NG
                result = "aaaaaa";
                //result = String.Format("LoadPercentage : " + mo["LoadPercentage"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的最大時鐘頻率\n";
                result = String.Format("MaxClockSpeed : " + mo["MaxClockSpeed"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機CPU的當前時鐘頻率\n";
                result = String.Format("CurrentClockSpeed : " + mo["CurrentClockSpeed"].ToString());
                richTextBox1.Text += result + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                richTextBox1.Text += "讀取計算機的CPU數據寬度\n";
                result = String.Format("DataWidth : " + mo["DataWidth"].ToString());
                richTextBox1.Text += result + "\n";

            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 或透過 ManagementObject 類別直接存取特定 CPU 序號
            ManagementObject wmiObj = new ManagementObject("Win32_Processor.DeviceID='CPU0'");
            richTextBox1.Text += "CPU ID:\t" + wmiObj.GetPropertyValue("ProcessorId").ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void GetCPUTemperature()
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher(@"root\WMI", "SELECT * FROM MSAcpi_ThermalZoneTemperature");

            foreach (ManagementObject mo in mos.Get())
            {
                //NG
                //double CPUtprt = Convert.ToDouble(Convert.ToDouble(mo.GetPropertyValue("CrrentTemperature").ToString()) - 2732) / 10;
                //richTextBox1.Text += "CPU温度：" + CPUtprt.ToString() + "°C\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得CPU編號、硬盤編號等系統有關環境、屬性

            richTextBox1.Text += "CPU編號：" + GetCpuId() + "\n";
            richTextBox1.Text += "硬盤編號：" + GetMainHardDiskId() + "\n";
        }

        // 查詢CPU編號 
        private string GetCpuId()
        {
            ManagementClass mClass = new ManagementClass("Win32_Processor");
            ManagementObjectCollection moc = mClass.GetInstances();
            string cpuId = null;
            foreach (ManagementObject mo in moc)
            {
                cpuId = mo.Properties["ProcessorId"].Value.ToString();
                break;
            }
            return cpuId;
        }

        // 查詢硬盤編號 
        private string GetMainHardDiskId()
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            String hardDiskID = null;
            foreach (ManagementObject mo in searcher.Get())
            {
                hardDiskID = mo["SerialNumber"].ToString().Trim();
                break;
            }
            return hardDiskID;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得網卡參數

            //取得本機MAC地址
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "取得本機MAC地址 : " + Convert.ToString(mo["MACAddress"]) + "\n";
                    string mac = mo["MacAddress"].ToString();
                    richTextBox1.Text += "本機MAC：" + mac + "\n";

                    string[] tmpMac = mo["MacAddress"].ToString().Split(':');
                    for (int i = 0; i < tmpMac.Length; i++)
                    {
                        string mac_address = tmpMac[i];
                        richTextBox1.Text += "取得MAC : " + mac_address + "\n";
                    }

                    string str = mo["MacAddress"].ToString();
                    richTextBox1.Text += "取得設備網卡的MAC地址 : " + str + "\n";

                    string result = mo["MacAddress"].ToString();
                    richTextBox1.Text += "取得 : " + result + "\n";

                    richTextBox1.Text += "取得本機的MAC地址：" + mo["MacAddress"].ToString() + "\n";
                    richTextBox1.Text += "IP " + mo["IpAddress"] + "\n";

                    mac = mo["MacAddress"].ToString();
                    richTextBox1.Text += "取得讀取網卡硬件地址 : " + mac + "\n";

                    //讀取IP地址
                    //st=mo["IpAddress"].ToString();
                    System.Array ar;
                    ar = (System.Array)(mo.Properties["IpAddress"].Value);
                    string st = ar.GetValue(0).ToString();
                    richTextBox1.Text += "讀取IP地址 : " + st + "\n";

                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Win32_NetworkAdapterConfiguration 獲取網卡MAC位址\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "網卡MAC位址: " + mo["MacAddress"].ToString() + "\n";
                }
            }


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得網路卡參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            int cnt = 0;
            int len = mos.Get().Count;
            richTextBox1.Text += "共有網卡數目 : " + len.ToString() + " 個\n";

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "全部 :\n" + mo.GetText(TextFormat.Mof) + "\n";
                richTextBox1.Text += "------------------------------\n";  // 30個

                try
                {
                    richTextBox1.Text += "------------------------------\n";  // 30個
                    richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "MAC位址 :\t" + mo.GetPropertyValue("MACAddress").ToString() + "\n";

                    string name = mo.GetPropertyValue("Name").ToString();
                    richTextBox1.Text += "name :\t" + name + "\n";

                    if (mo.GetPropertyValue("GUID") != null)
                    {
                        string guid = mo.GetPropertyValue("GUID").ToString();
                        richTextBox1.Text += "guid :\t" + guid + "\n";
                    }
                    if (mo.GetPropertyValue("MACAddress") != null)
                    {
                        string mac = mo.GetPropertyValue("MACAddress").ToString();
                        richTextBox1.Text += "mac :\t" + mac + "\n";
                    }
                    cnt++;
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                richTextBox1.Text += "cnt = " + cnt.ToString() + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("root\\CIMV2", "SELECT * FROM Win32_NetworkAdapter");

            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += "-----------------------------------\n";
                richTextBox1.Text += "Win32_NetworkAdapter instance\n";
                richTextBox1.Text += "Caption: {0}" + mo["Caption"] + "\n";

                richTextBox1.Text += mo["Caption"] + "\n";
                richTextBox1.Text += mo["AdapterType"] + "\n";
                richTextBox1.Text += mo["CreationClassName"] + "\n";
                richTextBox1.Text += mo["Description"] + "\n";
                richTextBox1.Text += mo["DeviceID"] + "\n";
                richTextBox1.Text += mo["ErrorDescription"] + "\n";
                //richTextBox1.Text += mo["GUID"] + "\n";
                richTextBox1.Text += mo["MACAddress"] + "\n";
                richTextBox1.Text += mo["Manufacturer"] + "\n";
                richTextBox1.Text += mo["Name"] + "\n";
                richTextBox1.Text += mo["NetConnectionID"] + "\n";
                richTextBox1.Text += mo["PermanentAddress"] + "\n";
                richTextBox1.Text += mo["PNPDeviceID"] + "\n";
                richTextBox1.Text += mo["ProductName"] + "\n";
                richTextBox1.Text += mo["ServiceName"] + "\n";
                richTextBox1.Text += mo["Status"] + "\n";
                richTextBox1.Text += mo["SystemCreationClassName"] + "\n";
                richTextBox1.Text += mo["SystemName"] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取網路卡位址\n";

            try
            {
                mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter WHERE ((MACAddress Is Not NULL) AND (Manufacturer <> 'Microsoft'))");
                foreach (ManagementObject mo in mos.Get())
                {
                    string NetCardMACAddress = mo["MACAddress"].ToString().Trim();
                    richTextBox1.Text += "讀取網路卡位址 :\t" + NetCardMACAddress + "\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nWin32_PhysicalMemory\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMemory");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "BankLabel: " + mo["BankLabel"] + "\n";
                richTextBox1.Text += "Capacity: " + mo["Capacity"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "DataWidth: " + mo["DataWidth"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "DeviceLocator: " + mo["DeviceLocator"] + "\n";
                richTextBox1.Text += "FormFactor: " + mo["FormFactor"] + "\n";
                richTextBox1.Text += "HotSwappable: " + mo["HotSwappable"] + "\n";
                richTextBox1.Text += "InstallDate: " + mo["InstallDate"] + "\n";
                richTextBox1.Text += "InterleaveDataDepth: " + mo["InterleaveDataDepth"] + "\n";
                richTextBox1.Text += "InterleavePosition: " + mo["InterleavePosition"] + "\n";
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"] + "\n";
                richTextBox1.Text += "MemoryType: " + mo["MemoryType"] + "\n";
                richTextBox1.Text += "Model: " + mo["Model"] + "\n";
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                richTextBox1.Text += "OtherIdentifyingInfo: " + mo["OtherIdentifyingInfo"] + "\n";
                richTextBox1.Text += "PartNumber: " + mo["PartNumber"] + "\n";
                richTextBox1.Text += "PositionInRow: " + mo["PositionInRow"] + "\n";
                richTextBox1.Text += "PoweredOn: " + mo["PoweredOn"] + "\n";
                richTextBox1.Text += "Removable: " + mo["Removable"] + "\n";
                richTextBox1.Text += "Replaceable: " + mo["Replaceable"] + "\n";
                richTextBox1.Text += "SerialNumber: " + mo["SerialNumber"] + "\n";
                richTextBox1.Text += "SKU: " + mo["SKU"] + "\n";
                richTextBox1.Text += "Speed: " + mo["Speed"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "Tag: " + mo["Tag"] + "\n";
                richTextBox1.Text += "TotalWidth: " + mo["TotalWidth"] + "\n";
                richTextBox1.Text += "TypeDetail: " + mo["TypeDetail"] + "\n";
                richTextBox1.Text += "Version: " + mo["Version"] + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //使用WMI取得USB資訊

            string location = System.Reflection.Assembly.GetExecutingAssembly().Location;
            //string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";

            //Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 

            //使用WMI取得USB資訊

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "------------------------------\n";  // 30個

                string deviceID = mo.GetPropertyValue("DeviceID").ToString();
                richTextBox1.Text += "Device ID : " + deviceID + "\n";

                string pnpDeviceID = mo.GetPropertyValue("PNPDeviceID").ToString();
                richTextBox1.Text += "PNPDeviceID : " + pnpDeviceID + "\n";

                string description = mo.GetPropertyValue("Description").ToString();
                richTextBox1.Text += "Description : " + description + "\n";

                string name = mo.GetPropertyValue("Name").ToString();
                richTextBox1.Text += "Name : " + name + "\n";

                string status = mo.GetPropertyValue("Status").ToString();
                richTextBox1.Text += "Status : " + status + "\n";

                string systemname = mo.GetPropertyValue("SystemName").ToString();
                richTextBox1.Text += "SystemName : " + systemname + "\n";

                string caption = mo.GetPropertyValue("Caption").ToString();
                richTextBox1.Text += "Caption : " + caption + "\n";
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nWin32_PnPEntity\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PnPEntity");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"] + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"] + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "StatusInfo: " + mo["StatusInfo".ToString()] + "\n";
                richTextBox1.Text += "Status: " + mo["Status".ToString()] + "\n";
                richTextBox1.Text += "Service: " + mo["Service".ToString()] + "\n";
                richTextBox1.Text += "ClassGuid: " + mo["ClassGuid".ToString()] + "\n";
                richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription".ToString()] + "\n";
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer".ToString()] + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //取得主機板序號
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    string mb_serial = mo.GetPropertyValue("SerialNumber").ToString();
                    richTextBox1.Text += "取得 : " + mb_serial + "\n";

                    string biosNumber = mo["SerialNumber"].ToString();
                    richTextBox1.Text += "取得 : " + biosNumber + "\n";

                    richTextBox1.Text += "取得主機板序號 :\t" + mo.GetPropertyValue("SerialNumber").ToString() + "\n";

                    string sBIOSSerialNumber = mo.GetPropertyValue("SerialNumber").ToString().Trim();
                    richTextBox1.Text += "取得 : " + sBIOSSerialNumber + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得主機板參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            //foreach (ManagementBaseObject mo in mos.Get()) same
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "製造商 : " + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "型號 : " + mo.GetPropertyValue("Product").ToString() + "\n";
                richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "取得Product :\t" + mo.GetPropertyValue("Product").ToString() + "\n";
                richTextBox1.Text += "主機板製造商：" + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "產品：" + mo["Product"].ToString() + "\n";
                richTextBox1.Text += "主機板序號：" + mo["SerialNumber"].ToString() + "\n";
                richTextBox1.Text += "Board SerialNumber:\t" + mo.GetPropertyValue("SerialNumber").ToString() + "\n";
                richTextBox1.Text += "主板編號\t\t" + mo.GetPropertyValue("SerialNumber").ToString() + "\n";  //取得主板編號
                richTextBox1.Text += "主板製造商\t\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";  //取得主板製造商
                richTextBox1.Text += "主板型號\t\t" + mo.GetPropertyValue("Name").ToString() + "\n";          //取得主板型號
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Win32_BIOS 獲取主機板BIOS序號\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "主機板BIOS序號：" + mo["SerialNumber"].ToString().Trim() + "\n";

                richTextBox1.Text += "主機板BIOS名稱：" + mo["Name"].ToString().Trim() + "\n";

                richTextBox1.Text += "主機板BIOS時間：" + mo["ReleaseDate"].ToString().Trim() + "\n";
                richTextBox1.Text += "主機板BIOS製造商：" + mo["Manufacturer"].ToString().Trim() + "\n";
                richTextBox1.Text += "主機板BIOS版本：" + mo["SMBIOSBIOSVersion"].ToString().Trim() + "\n";
            }



        }

        private void button10_Click(object sender, EventArgs e)
        {
        }

        string get_drive_type(string drive)
        {
            string DriveType;
            string type = string.Empty;
            DriveInfo dinfo = new DriveInfo(drive);
            try
            {
                DriveType = dinfo.DriveType.ToString();
                switch (DriveType)
                {
                    case "Unknown":
                        type = "這是未知設備";
                        break;
                    case "NoRootDirectory":
                        type = "這是未分區";
                        break;
                    case "Removable":
                        type = "這是可移動磁盤";
                        break;
                    case "Fixed":
                        type = "這是硬碟";
                        break;
                    case "Network":
                        type = "這是網絡驅動器";
                        break;
                    case "CDRom":
                        type = "這是光驅";
                        break;
                }
            }
            catch
            {
                type = "這是未知類型";
            }
            return type;
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Win32_DiskDrive 本機硬碟資訊/參數\n";

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            int len = mos.Get().Count;
            richTextBox1.Text += "共有硬碟數目 : " + len.ToString() + " 個\n";

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "------------------------------\n";  // 30個

                //用GetPropertyValue()方法
                richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "型號 :\t" + mo.GetPropertyValue("Model").ToString() + "\n";
                richTextBox1.Text += "介面 :\t" + mo.GetPropertyValue("InterfaceType").ToString() + "\n";
                richTextBox1.Text += "序號 :\t" + mo.GetPropertyValue("Signature").ToString() + "\n";

                richTextBox1.Text += "取得硬碟序號 : " + (string)mo.Properties["Model"].Value + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                //用字典取值
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "Model : " + mo["Model"].ToString() + "\n";
                richTextBox1.Text += "Interface: " + mo["InterfaceType"].ToString() + "\n";
                richTextBox1.Text += "Serial#: " + mo["SerialNumber"].ToString() + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個

                string diskname = mo["Model"].ToString();
                richTextBox1.Text += "取得 : " + diskname + "\n";
                get_detail_data(diskname);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取硬碟序號
            List<string> _serialNumber = new List<string>();

            //讀取U盤序號
            _serialNumber.Clear();

            // 調用這個函數將本機所有U盤序號存儲到_serialNumber中
            string[] diskArray;
            string driveNumber;
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDiskToPartition");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "A\n";
                getValueInQuotes(mo["Dependent"].ToString());
                diskArray = getValueInQuotes(mo["Antecedent"].ToString()).Split(',');
                driveNumber = diskArray[0].Remove(0, 6).Trim();
                var disks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
                foreach (ManagementObject disk in disks.Get())
                {
                    richTextBox1.Text += "B\t" + disk["Name"].ToString() + "\n";
                    if (disk["Name"].ToString() == ("\\\\.\\PHYSICALDRIVE" + driveNumber) & disk["InterfaceType"].ToString() == "USB")
                    {
                        richTextBox1.Text += "C\t" + parseSerialFromDeviceID(disk["PNPDeviceID"].ToString()) + "\n";
                        _serialNumber.Add(parseSerialFromDeviceID(disk["PNPDeviceID"].ToString()));
                    }
                }
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            len = _serialNumber.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "取得序號 : " + _serialNumber[i] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    string sHardDiskSerialNumber = mo["SerialNumber"].ToString().Trim();
                    richTextBox1.Text += "讀取硬碟序號 : " + sHardDiskSerialNumber + "\n";

                    string cc = mo.Properties["SerialNumber"].Value.ToString();
                    richTextBox1.Text += cc + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Win32_PhysicalMedia 獲取媒體資訊\n";

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            foreach (ManagementObject mo in mos.Get())
            {
                // get the hard drive from collection
                // using index
                //HardDrive hd = (HardDrive)hdCollection[i];

                // get the hardware serial no.
                if (mo["SerialNumber"] == null)
                {
                    //hd.SerialNo = "None";
                    richTextBox1.Text += "None" + "\n";
                }
                else
                {
                    richTextBox1.Text += mo["SerialNumber"].ToString() + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            // 抓取硬碟&USB儲存裝置磁碟代號

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "------------------------------\n";  // 30個
                richTextBox1.Text += "Description: ";
                richTextBox1.Text += mo["Description"] + "\n";
                richTextBox1.Text += "Name: ";
                richTextBox1.Text += mo["Name"] + "\n";
            }

            richTextBox1.Text += "------------------------------\n";  // 30個

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "------------------------------\n";  // 30個
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                richTextBox1.Text += "Model: " + mo["Model"] + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceId"] + "\n";
                richTextBox1.Text += "BytesPerSector: " + mo["BytesPerSector".ToString()] + "\n";
                richTextBox1.Text += "Size: " + mo["Size".ToString()] + "\n";
                richTextBox1.Text += "InterfaceType: " + mo["InterfaceType"] + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"] + "\n";
                //richTextBox1.Text += "bbbbbb ";
                // + mo["SerialNumber"] + "\n";
                //richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"] + "\n";

                richTextBox1.Text += "CapabilityDescriptions: " + mo["CapabilityDescriptions"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "CompressionMethod: " + mo["CompressionMethod"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"] + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"] + "\n";
                richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription"] + "\n";
                richTextBox1.Text += "ErrorMethodology: " + mo["ErrorMethodology"] + "\n";
                //richTextBox1.Text += "FirmwareRevision: " + mo["FirmwareRevision"] + "\n";
                richTextBox1.Text += "MediaType: " + mo["MediaType"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";

                richTextBox1.Text += "Index: " + mo["Index".ToString()] + "\n";
                richTextBox1.Text += "LastErrorCode: " + mo["LastErrorCode".ToString()] + "\n";
                richTextBox1.Text += "MediaLoaded: " + mo["MediaLoaded".ToString()] + "\n";
                richTextBox1.Text += "Partitions: " + mo["Partitions".ToString()] + "\n";
                richTextBox1.Text += "SectorsPerTrack: " + mo["SectorsPerTrack".ToString()] + "\n";
                richTextBox1.Text += "Signature: " + mo["Signature".ToString()] + "\n";
                richTextBox1.Text += "CYLINDER: " + mo["TotalCylinders".ToString()] + "\n";
                richTextBox1.Text += "HEAD: : " + mo["TotalHeads".ToString()] + "\n";
                richTextBox1.Text += "SECTOR: " + mo["TotalSectors".ToString()] + "\n";
                richTextBox1.Text += "TRACK: " + mo["TotalTracks".ToString()] + "\n";
                richTextBox1.Text += "TracksPerCylinder: " + mo["TracksPerCylinder".ToString()] + "\n";

                richTextBox1.Text += "DiskPartition: ";
                foreach (ManagementObject b in mo.GetRelated("Win32_DiskPartition"))
                {
                    richTextBox1.Text += "Name: " + b["Name"] + "\n";
                    richTextBox1.Text += "Caption: " + b["Caption"] + "\n";
                    richTextBox1.Text += "CreationClassName: " + b["CreationClassName"] + "\n";
                    richTextBox1.Text += "Description: " + b["Description"] + "\n";
                    richTextBox1.Text += "DeviceID: " + b["DeviceID"] + "\n";
                    richTextBox1.Text += "SystemCreationClassName: " + b["SystemCreationClassName"] + "\n";
                    richTextBox1.Text += "SystemName: " + b["SystemName"] + "\n";
                    richTextBox1.Text += "Type: " + b["Type"] + "\n";

                    richTextBox1.Text += "Index: " + b["Index".ToString()] + "\n";
                    richTextBox1.Text += "DiskIndex: " + b["DiskIndex".ToString()] + "\n";
                    richTextBox1.Text += "BlockSize: " + b["BlockSize".ToString()] + "\n";
                    richTextBox1.Text += "NumberOfBlocks: " + b["NumberOfBlocks".ToString()] + "\n";
                    richTextBox1.Text += "Size: " + b["Size".ToString()] + "\n";
                    richTextBox1.Text += "Bootable: " + b["Bootable".ToString()] + "\n";
                    richTextBox1.Text += "BootPartition: " + b["BootPartition".ToString()] + "\n";
                    richTextBox1.Text += "PrimaryPartition: " + b["PrimaryPartition".ToString()] + "\n";
                    richTextBox1.Text += "StartingOffset: " + b["StartingOffset".ToString()] + "\n";

                    foreach (ManagementBaseObject c in b.GetRelated("Win32_LogicalDisk"))
                    {
                        richTextBox1.Text += "LogicalDisk: " + c["Name"] + "\n";
                        richTextBox1.Text += "SystemCreationClassName: " + c["SystemCreationClassName"] + "\n";
                        richTextBox1.Text += "SystemName: " + c["SystemName"] + "\n";
                        richTextBox1.Text += "VolumeName: " + c["VolumeName"] + "\n";
                        richTextBox1.Text += "VolumeSerialNumber: " + c["VolumeSerialNumber"] + "\n";
                        richTextBox1.Text += "CreationClassName: " + c["CreationClassName"] + "\n";
                        richTextBox1.Text += "Description: " + c["Description"] + "\n";
                        richTextBox1.Text += "DeviceID: " + c["DeviceID"] + "\n";
                        richTextBox1.Text += "FileSystem: " + c["FileSystem"] + "\n";
                        richTextBox1.Text += "Caption: " + c["Caption"] + "\n";
                        richTextBox1.Text += "DriveType: " + c["DriveType".ToString()] + "\n";
                        richTextBox1.Text += "FreeSpace: " + c["FreeSpace".ToString()] + "\n";
                        richTextBox1.Text += "MaximumComponentLength: " + c["MaximumComponentLength".ToString()] + "\n";
                        richTextBox1.Text += "MediaType: " + c["MediaType".ToString()] + "\n";
                        richTextBox1.Text += "Size: " + c["Size".ToString()] + "\n";
                    }
                }
            }
            richTextBox1.Text += "------------------------------\n";  // 30個
        }

        private static string parseSerialFromDeviceID(string deviceId)
        {
            var splitDeviceId = deviceId.Split('\\');
            var arrayLen = splitDeviceId.Length - 1;
            var serialArray = splitDeviceId[arrayLen].Split('&');
            var serial = serialArray[0];
            return serial;
        }

        private static string getValueInQuotes(string inValue)
        {
            var posFoundStart = inValue.IndexOf("\"");
            var posFoundEnd = inValue.IndexOf("\"", posFoundStart + 1);
            var parsedValue = inValue.Substring(posFoundStart + 1, (posFoundEnd - posFoundStart) - 1);
            return parsedValue;
        }

        void get_detail_data(string diskname)
        {
            richTextBox1.Text += "你選擇了 : " + diskname + "\n";

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive WHERE Model = '" + diskname + "'");

            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "Type: " + mo["MediaType"].ToString() + "\n";
                    richTextBox1.Text += "Model: " + mo["Model"].ToString() + "\n";
                    richTextBox1.Text += "Serial: " + mo["SerialNumber"].ToString() + "\n";
                    richTextBox1.Text += "Interface: " + mo["InterfaceType"].ToString() + "\n";

                    richTextBox1.Text += "Capacity: " + mo["Size"].ToString() + " bytes (" + Math.Round(((((double)Convert.ToDouble(mo["Size"]) / 1024) / 1024) / 1024), 2) + " GB)" + "\n";
                    richTextBox1.Text += "Partitions: " + mo["Partitions"].ToString() + "\n";
                    richTextBox1.Text += "Signature: " + mo["Signature"].ToString() + "\n";
                    richTextBox1.Text += "Firmware: " + mo["FirmwareRevision"].ToString() + "\n";
                    richTextBox1.Text += "Cylinders: " + mo["TotalCylinders"].ToString() + "\n";
                    richTextBox1.Text += "Sectors: " + mo["TotalSectors"].ToString() + "\n";
                    richTextBox1.Text += "Heads: " + mo["TotalHeads"].ToString() + "\n";
                    richTextBox1.Text += "Tracks: " + mo["TotalTracks"].ToString() + "\n";
                    richTextBox1.Text += "Bytes per Sector: " + mo["BytesPerSector"].ToString() + "\n";
                    richTextBox1.Text += "Sectors per Track: " + mo["SectorsPerTrack"].ToString() + "\n";
                    richTextBox1.Text += "Tracks per Cylinder: " + mo["TracksPerCylinder"].ToString() + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //"Win32_DiskQuota"

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskQuota");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "------------------------------\n";  // 30個
                //richTextBox1.Text += "全部 :\n" + mo.GetText(TextFormat.Mof) + "\n";
                //印出所有參數名稱及內容
                foreach (var prop in mo.Properties)
                {
                    //richTextBox1.Text += prop.Name + ": " + prop.Value + "\n";
                }
                richTextBox1.Text += "DiskSpaceUsed: " + mo["DiskSpaceUsed"].ToString() + "\n";
                richTextBox1.Text += "Limit: " + mo["Limit"].ToString() + "\n";
                richTextBox1.Text += "QuotaVolume: " + mo["QuotaVolume"].ToString() + "\n";
                richTextBox1.Text += "Status: " + mo["Status"].ToString() + "\n";
                richTextBox1.Text += "User: " + mo["User"].ToString() + "\n";
                richTextBox1.Text += "WarningLimit: " + mo["WarningLimit"].ToString() + "\n";
                richTextBox1.Text += "Next : " + mo.Path + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            ManagementObject mo3 = new ManagementObject("Win32_LogicalDisk.DeviceId='D:'");
            mo3.Get();
            richTextBox1.Text += "取得磁盤配額 Logical Disk Size = " + mo3["Size"] + " bytes\n";

            ManagementObject account = new ManagementObject("Win32_Account.Domain=\"KILO\",Name=\"Administrators\"");
            account.Get();
            richTextBox1.Text += "取得帳號名 : " + account + "\n";

        }

        private void button14_Click(object sender, EventArgs e)
        {
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //Win32_LogicalDisk

            richTextBox1.Text += "讀取邏輯驅動器詳細信息, 判斷驅動器類型\n";

            //找部分
            //ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT Name, DriveType FROM Win32_LogicalDisk");

            //找全部
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
            foreach (ManagementObject mo1 in mos.Get())
            {
                //讀取驅動器盤符
                string name = mo1["Name"].ToString();
                string type = get_drive_type(mo1["Name"].ToString());
                richTextBox1.Text += "取得驅動器 : " + mo1["Name"].ToString() + "\t" + get_drive_type(mo1["Name"].ToString()) + "\n";

                richTextBox1.Text += "磁碟 : " + mo1["Name"] + ", 名稱 : " + mo1["VolumeName"] + ", 型態 : " + mo1["DriveType"] + "\t";
                uint dt = (uint)mo1["DriveType"];
                print_drive_type(dt);

                if (mo1["DeviceID"].ToString() == "C:")
                {
                    string result3 = mo1["VolumeSerialNumber"].ToString();
                    richTextBox1.Text += "磁碟序號 : " + result3 + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //獲得指定磁盤的容量
            string drive = "C";

            ManagementObject mo = new ManagementObject("Win32_LogicalDisk.DeviceID=\"" + drive + ":\"");
            mo.Get();

            richTextBox1.Text += "Logical Disk Size = " + mo["Size"] + " bytes\n";

            //獲得硬碟序號
            richTextBox1.Text += "VolumeSerialNumber = " + mo["VolumeSerialNumber"] + "\n";
            string hdd_serial = mo.GetPropertyValue("VolumeSerialNumber").ToString();
            richTextBox1.Text += "取得硬碟序號 : " + hdd_serial + "\n";

            richTextBox1.Text += "\n字串類\n";

            richTextBox1.Text += "Name: " + mo["Name"] + "\n";
            richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
            richTextBox1.Text += "FileSystem: " + mo["FileSystem"] + "\n";
            richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
            richTextBox1.Text += "Description: " + mo["Description"] + "\n";
            richTextBox1.Text += "DeviceID: " + mo["DeviceID"] + "\n";
            richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"] + "\n";
            richTextBox1.Text += "SystemName: " + mo["SystemName"] + "\n";
            richTextBox1.Text += "VolumeName: " + mo["VolumeName"] + "\n";
            richTextBox1.Text += "序號VolumeSerialNumber: " + mo["VolumeSerialNumber"] + "\n";
            /*  無資料
            richTextBox1.Text += "LogicalDisk: " + mo["ProviderName"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + mo["PNPDeviceID"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + mo["Purpose"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + mo["Status"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + mo["ErrorDescription"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + mo["ErrorMethodology"] + "\n";
            */

            richTextBox1.Text += "\n數字類\n";

            richTextBox1.Text += "Size: " + mo["Size"].ToString() + "\n";
            richTextBox1.Text += "FreeSpace: " + mo["FreeSpace"].ToString() + "\n";
            richTextBox1.Text += "MaximumComponentLength: " + mo["MaximumComponentLength"].ToString() + "\n";
            uint media_type = 0;
            try
            {
                richTextBox1.Text += "MediaType: " + mo["MediaType"].ToString() + "\n";
                media_type = (uint)mo["MediaType"];
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息 : " + ex.Message + "\n";
            }

            //richTextBox1.Text += "Access: " + mo["Access"].ToString() + "\n";
            richTextBox1.Text += "DriveType: " + mo["DriveType"].ToString() + "\t";

            uint drive_type = (uint)mo["DriveType"];
            print_drive_type(drive_type);

            double dblSize = Math.Round(Convert.ToDouble(mo["Size"]) / 1024 / 1024 / 1024);
            //1 KB = 1024 - KiloByte
            //1 MB = 1024 ^ 2 - MegaByte
            //1 GB = 1024 ^ 3 - GigaByte
            //1 TB = 1024 ^ 4 - TeraByte
            //1 PB = 1024 ^ 5 - PetaByte
            //1 EB = 1024 ^ 6 - ExaByte
            //1 ZB = 1024 ^ 7 - ZettaByte
            //1 YB = 1024 ^ 8 - YottaByte
            //1 BB = 1024 ^ 9 - BrontoByte
            richTextBox1.Text += "Hard Disk Size = " + dblSize.ToString() + " GB" + "\n";

            double dblFree = Math.Round(Convert.ToDouble(mo["FreeSpace"]) / 1024 / 1024 / 1024);
            //1 KB = 1024 - KiloByte
            //1 MB = 1024 ^ 2 - MegaByte
            //1 GB = 1024 ^ 3 - GigaByte
            //1 TB = 1024 ^ 4 - TeraByte
            //1 PB = 1024 ^ 5 - PetaByte
            //1 EB = 1024 ^ 6 - ExaByte
            //1 ZB = 1024 ^ 7 - ZettaByte
            //1 YB = 1024 ^ 8 - YottaByte
            //1 BB = 1024 ^ 9 - BrontoByte

            richTextBox1.Text += "Hard Disk Free Space = " + dblFree.ToString() + " GB\n";

            print_media_type(media_type);

            /*  無資料
            //richTextBox1.Text += "Size: " + mo["Availability"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + mo["BlockSize"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + mo["ConfigManagerErrorCode"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + mo["LastErrorCode"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + mo["NumberOfBlocks"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + mo["PowerManagementCapabilities[]"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + mo["StatusInfo"].ToString() + "\n";
            */
            /*  無資料
            richTextBox1.Text += "InstallDate: " + mo["InstallDate"] + "\n";
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");

            System.UInt64 space = UInt64.MinValue;
            foreach (ManagementObject mo2 in mos.Get())
            {
                richTextBox1.Text += "磁碟 : " + mo2["deviceid"] + "\n";
                richTextBox1.Text += "磁碟 : " + (mo2["Name"]).ToString() + "\n";
                if ((mo2["Name"]).ToString() == "C:")
                {
                    space = (System.UInt64)(mo2["FreeSpace"]);
                    richTextBox1.Text += "獲得硬碟空間 : " + space.ToString() + "\n";
                }

                if (Convert.ToString(mo2.Properties["DriveType"].Value) == "3")
                {
                    richTextBox1.Text += "讀取硬碟相應分區的序號 :\n";
                    richTextBox1.Text += "磁碟 : " + mo2.Properties["Name"].Value.ToString().ToUpper().Trim() + "\n";
                    string Dri = mo2.Properties["VolumeSerialNumber"].Value.ToString();
                    richTextBox1.Text += "硬碟相應分區的序號 : " + Dri + "\n";
                }

                // 取得磁碟Volumne 名稱跟序號
                richTextBox1.Text += "Name: " + mo2["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo2["VolumeSerialNumber"] + "\n";

                richTextBox1.Text += mo2["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo2["VolumeSerialNumber"] + "\n";

                richTextBox1.Text += mo2["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo2["VolumeSerialNumber"] + "\n";

                // 取得磁碟Volumne 名稱跟序號
                richTextBox1.Text += mo2["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo2["VolumeSerialNumber"] + "\n";

                richTextBox1.Text += "------------------------------\n";  // 30個
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "獲取硬碟分區資訊, 指定邏輯磁碟機\n";

            //寫法一，直接寫D槽
            //ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk WHERE DeviceID = 'D:'");

            //寫法二，用變數
            string strDrive = "C:"; // 指定C: 邏輯磁碟機
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk WHERE DeviceID = " + "\"" + strDrive + "\"");

            foreach (ManagementObject mo1 in mos.Get())
            {
                richTextBox1.Text += "磁片類型: " + mo1["Description"].ToString() + "\n";
                richTextBox1.Text += "分區類型: " + mo1["FileSystem"].ToString() + "\n";
                richTextBox1.Text += "可用空間: " + mo1["FreeSpace"].ToString() + "\n";
                richTextBox1.Text += "實際大小: " + mo1["Size"].ToString() + "\n";
                richTextBox1.Text += "Name: " + mo1["Name"].ToString() + "\n";
                richTextBox1.Text += "VolumeSerialNumber: " + mo1["VolumeSerialNumber"] + "\n";
                richTextBox1.Text += "DeviceID: " + mo1["DeviceID"] + "\n";
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        void print_drive_type(uint drive_type)
        {
            // DriveType 意義
            /*
            1 No type
            2 Floppy disk
            3 Hard disk
            4 Removable drive or network drive
            5 CD-ROM
            6 RAM disk
            */
            switch (drive_type)
            {
                case 0:
                    richTextBox1.Text += "Unknown." + "\n";
                    break;
                case 1:
                    richTextBox1.Text += "No Root Directory." + "\n";
                    break;
                case 2:
                    richTextBox1.Text += "Removable Disk." + "\n";
                    break;
                case 3:
                    richTextBox1.Text += "Local Disk." + "\n";
                    break;
                case 4:
                    richTextBox1.Text += "Network Drive." + "\n";
                    break;
                case 5:
                    richTextBox1.Text += "Compact Disc." + "\n";
                    break;
                case 6:
                    richTextBox1.Text += "RAM Disk." + "\n";
                    break;
                default:
                    richTextBox1.Text += "Drive type could not be determined." + "\n";
                    break;
            }
            return;
        }

        void print_media_type(uint media_type)
        {
            switch (media_type)
            {
                case 0:
                    richTextBox1.Text += "MediaType 無資料\n"; break;
                case 1:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (1), 5 1/4-Inch Floppy Disk - 1.2 MB - 512 bytes/sector." + "\n"; break;
                case 2:
                    richTextBox1.Text += "3½-Inch Floppy Disk (2), 3 1/2-Inch Floppy Disk - 1.44 MB -512 bytes/sector." + "\n"; break;
                case 3:
                    richTextBox1.Text += "3½-Inch Floppy Disk (3), 3 1/2-Inch Floppy Disk - 2.88 MB - 512 bytes/sector." + "\n"; break;
                case 4:
                    richTextBox1.Text += "3½-Inch Floppy Disk (4), 3 1/2-Inch Floppy Disk - 20.8 MB - 512 bytes/sector." + "\n"; break;
                case 5:
                    richTextBox1.Text += "3½-Inch Floppy Disk (5), 3 1/2-Inch Floppy Disk - 720 KB - 512 bytes/sector." + "\n"; break;
                case 6:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (6), 5 1/4-Inch Floppy Disk - 360 KB - 512 bytes/sector." + "\n"; break;
                case 7:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (7), 5 1/4-Inch Floppy Disk - 320 KB - 512 bytes/sector." + "\n"; break;
                case 8:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (8), 5 1/4-Inch Floppy Disk - 320 KB - 1024 bytes/sector." + "\n"; break;
                case 9:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (9), 5 1/4-Inch Floppy Disk - 180 KB - 512 bytes/sector." + "\n"; break;
                case 10:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (10), 5 1/4-Inch Floppy Disk - 160 KB - 512 bytes/sector." + "\n"; break;
                case 11:
                    richTextBox1.Text += "Removable media other than floppy (11)." + "\n"; break;
                case 12:
                    richTextBox1.Text += "Fixed hard disk media (12)." + "\n"; break;
                case 13:
                    richTextBox1.Text += "3½-Inch Floppy Disk (13), 3 1/2-Inch Floppy Disk - 120 MB - 512 bytes/sector." + "\n"; break;
                case 14:
                    richTextBox1.Text += "3½-Inch Floppy Disk (14), 3 1/2-Inch Floppy Disk - 640 KB - 512 bytes/sector." + "\n"; break;
                case 15:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (15), 5 1/4-Inch Floppy Disk - 640 KB - 512 bytes/sector." + "\n"; break;
                case 16:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (16), 5 1/4-Inch Floppy Disk - 720 KB - 512 bytes/sector." + "\n"; break;
                case 17:
                    richTextBox1.Text += "3½-Inch Floppy Disk (17), 3 1/2-Inch Floppy Disk - 1.2 MB - 512 bytes/sector." + "\n"; break;
                case 18:
                    richTextBox1.Text += "3½-Inch Floppy Disk (18), 3 1/2-Inch Floppy Disk - 1.23 MB - 1024 bytes/sector." + "\n"; break;
                case 19:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (19), 5 1/4-Inch Floppy Disk - 1.23 MB - 1024 bytes/sector." + "\n"; break;
                case 20:
                    richTextBox1.Text += "3½-Inch Floppy Disk (20), 3 1/2-Inch Floppy Disk - 128 MB - 512 bytes/sector." + "\n"; break;
                case 21:
                    richTextBox1.Text += "3½-Inch Floppy Disk (21), 3 1/2-Inch Floppy Disk - 230 MB - 512 bytes/sector." + "\n"; break;
                case 22:
                    richTextBox1.Text += "8-Inch Floppy Disk (22), 8-Inch Floppy Disk - 256 KB - 128 bytes/sector." + "\n"; break;
                default:
                    richTextBox1.Text += "Media type could not be determined." + "\n"; break;
            }
            return;
        }

        private void button16_Click(object sender, EventArgs e)
        {
            HardwareInfo hw_info = new HardwareInfo();

            richTextBox1.Text += "HostName : " + hw_info.GetHostName() + "\n";
            richTextBox1.Text += "CPU ID : " + hw_info.GetCpuID() + "\n";
            richTextBox1.Text += "HDD ID : " + hw_info.GetHardDiskID() + "\n";
            richTextBox1.Text += "MAC Addr : " + hw_info.GetMacAddress() + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {

            richTextBox1.Text += "Win32_DesktopMonitor 獲取顯示器資訊\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DesktopMonitor");
            foreach (ManagementObject mo in mos.Get())
            {

                richTextBox1.Text += "Name: " + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "Status: " + mo["Status"].ToString() + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"].ToString() + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"].ToString() + "\n";
                //richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription"].ToString() + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"].ToString() + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"].ToString() + "\n";
                richTextBox1.Text += "Description: " + mo["Description"].ToString() + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"].ToString() + "\n";
                richTextBox1.Text += "MonitorManufacturer: " + mo["MonitorManufacturer"].ToString() + "\n";
                richTextBox1.Text += "MonitorType: " + mo["MonitorType"].ToString() + "\n";

                richTextBox1.Text += "Availability: " + mo["Availability"].ToString() + "\n";
                //richTextBox1.Text += "Bandwidth: " + mo["Bandwidth"].ToString() + "\n";
                richTextBox1.Text += "ConfigManagerErrorCode: " + mo["ConfigManagerErrorCode"].ToString() + "\n";
                richTextBox1.Text += "ScreenHeight: " + mo["ScreenHeight"].ToString() + "\n";
                richTextBox1.Text += "ScreenWidth: " + mo["ScreenWidth"].ToString() + "\n";
                //richTextBox1.Text += "StatusInfo: " + mo["StatusInfo"].ToString() + "\n";
                //richTextBox1.Text += "DisplayType: " + mo["DisplayType"].ToString() + "\n";
                //richTextBox1.Text += "LastErrorCode: " + mo["LastErrorCode"].ToString() + "\n";
                richTextBox1.Text += "PixelsPerXLogicalInch: " + mo["PixelsPerXLogicalInch"].ToString() + "\n";
                richTextBox1.Text += "PixelsPerYLogicalInch: " + mo["PixelsPerYLogicalInch"].ToString() + "\n";
                //richTextBox1.Text += "PowerManagementCapabilities: " + mo["PowerManagementCapabilities[]"].ToString() + "\n";

                //richTextBox1.Text += "IsLocked: " + mo["IsLocked"].ToString() + "\n";
                //richTextBox1.Text += "PowerManagementSupported: " + mo["PowerManagementSupported"].ToString() + "\n";
                richTextBox1.Text += "ConfigManagerUserConfig: " + mo["ConfigManagerUserConfig"].ToString() + "\n";
                //richTextBox1.Text += "ErrorCleared: " + mo["ErrorCleared"].ToString() + "\n";

                //richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string PNPDeviceID = string.Empty;
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_DesktopMonitor");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "------------------------------\n";  // 30個
                    //richTextBox1.Text += "全部 :\n" + mo.GetText(TextFormat.Mof) + "\n";
                    //richTextBox1.Text += "------------------------------\n";  // 30個
                    richTextBox1.Text += "PNPDeviceID : " + mo["PNPDeviceID"].ToString() + "\n";
                    PNPDeviceID = mo["PNPDeviceID"].ToString();
                }
                catch
                {
                }
            }

            if (PNPDeviceID == string.Empty)
            {
                richTextBox1.Text += "找不到螢幕, 離開\n";
                return;
            }

            //取得螢幕尺寸

            string id = PNPDeviceID;
            SizeF size = GetMonitorPhysicalSize(id);
            richTextBox1.Text += "get size = " + size.ToSize() + "\n";

            richTextBox1.Text += MonitorScaler(size).ToString() + " 吋\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得螢幕數量
            //检测已连接显示器
            richTextBox1.Text += "取得螢幕數量 :\n";

            // 获取屏幕数量
            int count = 0;
            mos = new ManagementObjectSearcher(@"root\wmi", "SELECT * FROM WmiMonitorID");
            foreach (ManagementObject mo in mos.Get())
            {
                //richTextBox1.Text += "全部 :\n" + mo.GetText(TextFormat.Mof) + "\n";
                count++;
            }
            richTextBox1.Text += "共有 : " + count.ToString() + " 個螢幕\n";
        }

        //获取显示器物理尺寸(cm)
        private SizeF GetMonitorPhysicalSize(string monitorPnpDevId)
        {
            byte[] edid = GetMonitorEdid(monitorPnpDevId);
            if (edid.Length < 23)
            {
                return SizeF.Empty;
            }
            richTextBox1.Text += "EDID :\n";
            richTextBox1.Text += "len = " + edid.Length + "\n";
            richTextBox1.Text += "edid[0x15] = " + edid[0x15] + "\n";
            richTextBox1.Text += "edid[0x16] = " + edid[0x16] + "\n";
            richTextBox1.Text += "edid[0x42] = " + edid[0x42] + "\n";
            richTextBox1.Text += "edid[0x43] = " + edid[0x43] + "\n";

            for (int i = 0; i < 30; i++)
            {
                //richTextBox1.Text += "edid[" + i.ToString() + "] = " + edid[i].ToString("X2") + "\n";
            }

            return new SizeF(edid[21], edid[22]);
        }

        private byte[] GetMonitorEdid(string monitorPnpDevId)
        {
            return (byte[])Registry.GetValue(@"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\" + monitorPnpDevId + @"\Device Parameters", "EDID", new byte[] { });
        }

        //通过屏显示器理尺寸转换为显示器大小(inch)
        private float MonitorScaler(SizeF moniPhySize)
        {
            double mDSize = Math.Sqrt(Math.Pow(moniPhySize.Width, 2) + Math.Pow(moniPhySize.Height, 2)) / 2.54d;
            return (float)Math.Round(mDSize, 1);
        }

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Win32_VideoController 獲取顯示卡資訊\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_VideoController");
            //ManagementObjectSearcher mos = new ManagementObjectSearcher(@"root\CIMV2", "SELECT * FROM Win32_VideoController");
            foreach (ManagementObject mo in mos.Get())
            {

                richTextBox1.Text += "顯示設備訊息\n";
                richTextBox1.Text += "名稱： " + mo["Name"].ToString() + "\n";//顯示設備名稱
                richTextBox1.Text += "設備ID" + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "PNPDeviceID： " + mo["PNPDeviceID"].ToString() + "\n";//顯示設備的PNPDeviceID
                richTextBox1.Text += "驅動程序文件： " + mo["InstalledDisplayDrivers"].ToString() + "\n";//顯示設備的驅動程序文件
                richTextBox1.Text += "驅動版本號： " + mo["DriverVersion"].ToString() + "\n";//顯示設備的驅動版本號
                richTextBox1.Text += "顯示處理器： " + mo["VideoProcessor"].ToString() + "\n";//顯示設備的顯示處理器
                richTextBox1.Text += "最大更新率： " + mo["MaxRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "最小更新率： " + mo["MinRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "顯示設備目前顯示模式： " + mo["VideoModeDescription"].ToString() + "\n";//顯示設備目前顯示模式
                richTextBox1.Text += "配接器相容性 " + mo["AdapterCompatibility"].ToString() + "\n";
                richTextBox1.Text += "配接器類型 " + mo["AdapterDACType"].ToString() + "\n";
                richTextBox1.Text += "字幕" + mo["Caption"].ToString() + "\n";
                richTextBox1.Text += "目前比特每圖元" + mo["CurrentBitsPerPixel"].ToString() + "\n";
                richTextBox1.Text += "目前的水準解析度" + mo["CurrentHorizontalResolution"].ToString() + "\n";
                richTextBox1.Text += "描述" + mo["Description"].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Win32_VideoSettings 顯卡支持的顯示模式\n";

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_VideoSettings");

            foreach (ManagementObject mo in mos.Get())
            {
                //印出所有參數名稱及內容
                foreach (var prop in mo.Properties)
                {
                    richTextBox1.Text += prop.Name + ": " + prop.Value + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Win32_SoundDevice\n";
            richTextBox1.Text += "獲取音效卡資訊 PNPDeviceID\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "音效設備名稱：" + mo["ProductName"].ToString() + "\n"; //在当前文本框中显示声音设备的名称
                richTextBox1.Text += "PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";//在当前文本框中显示声音设备的PNPDeviceID
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //查看了一下自己筆記本電池的剩餘時間
            //用WMI方式查看了一下自己筆記本電池的剩餘時間，結果得到了71582788分鐘這個結果，頓感意外，第一感覺是相關的代碼寫錯了。

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Battery");
            ManagementObjectCollection moc = mos.Get();
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += "EstimatedRunTime : " + mo["EstimatedRunTime"].ToString() + "minutes" + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            c#，使用WMI對象讀取筆記本電池剩余電量的百分比

            有時候需要監控到筆記本電池的剩余電量，調查後發現WMI對象可以搞定。
            在使用WMI對象前，先要添加對System.Management的引用，然後就可以調用WMI對象。
            我們使用的WMI對象是：Win32_Battery
            對象參考：http://msdn.microsoft.com/zh-cn/library/aa394074(v=VS.85).aspx
            */

            ManagementClass mc = new ManagementClass("Win32_Battery");
            moc = mc.GetInstances();

            ManagementObjectCollection.ManagementObjectEnumerator mom = moc.GetEnumerator();
            if (mom.MoveNext())
            {
                Console.WriteLine("EstimatedChargeRemaining: \t{0}%", mom.Current.Properties["EstimatedChargeRemaining"].Value);
                richTextBox1.Text += "EstimatedChargeRemaining: : " + mom.Current.Properties["EstimatedChargeRemaining"].Value + " %\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button20_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得 作業系統資訊 Win32_OperatingSystem\n";

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "Caption : " + mo.Properties["Caption"].Value.ToString().Trim() + "\n";
                richTextBox1.Text += "Version : " + mo.Properties["Version"].Value.ToString() + " SP " + mo.Properties["ServicePackMajorVersion"].Value.ToString() + "." + mo.Properties["ServicePackMinorVersion"].Value.ToString() + "\n";

                GetValue(mo, "BootDevice");
                GetValue(mo, "BuildNumber");
                GetValue(mo, "BuildType");
                GetValue(mo, "Caption");
                GetValue(mo, "CodeSet");
                GetValue(mo, "CountryCode");
                GetValue(mo, "CreationClassName");
                GetValue(mo, "CSCreationClassName");
                GetValue(mo, "CSDVersion");
                GetValue(mo, "CSName");
                GetValue(mo, "CurrentTimeZone");
                GetValue(mo, "DataExecutionPrevention_Available");
                GetValue(mo, "DataExecutionPrevention_32BitApplications");
                GetValue(mo, "DataExecutionPrevention_Drivers");
                GetValue(mo, "DataExecutionPrevention_SupportPolicy");
                GetValue(mo, "Debug");
                GetValue(mo, "Description");
                GetValue(mo, "Distributed");
                GetValue(mo, "EncryptionLevel");
                GetValue(mo, "ForegroundApplicationBoost");
                GetValue(mo, "FreePhysicalMemory");
                GetValue(mo, "FreeSpaceInPagingFiles");
                GetValue(mo, "FreeVirtualMemory");
                GetValue(mo, "InstallDate");
                GetValue(mo, "LargeSystemCache");
                GetValue(mo, "LastBootUpTime");
                GetValue(mo, "LocalDateTime");
                GetValue(mo, "Locale");
                GetValue(mo, "Manufacturer");
                GetValue(mo, "MaxNumberOfProcesses");
                GetValue(mo, "MaxProcessMemorySize");
                GetValue(mo, "MUILanguages[]");
                GetValue(mo, "Name");
                GetValue(mo, "NumberOfLicensedUsers");
                GetValue(mo, "NumberOfProcesses");
                GetValue(mo, "NumberOfUsers");
                GetValue(mo, "OperatingSystemSKU");
                GetValue(mo, "Organization");
                GetValue(mo, "OSArchitecture");
                GetValue(mo, "OSLanguage");
                GetValue(mo, "OSProductSuite");
                GetValue(mo, "OSType");
                GetValue(mo, "OtherTypeDescription");
                GetValue(mo, "PAEEnabled");
                GetValue(mo, "PlusProductID");
                GetValue(mo, "PlusVersionNumber");
                GetValue(mo, "Primary");
                GetValue(mo, "ProductType");
                GetValue(mo, "QuantumLength");
                GetValue(mo, "QuantumType");
                GetValue(mo, "RegisteredUser");
                GetValue(mo, "SerialNumber");
                GetValue(mo, "ServicePackMajorVersion");
                GetValue(mo, "ServicePackMinorVersion");
                GetValue(mo, "SizeStoredInPagingFiles");
                GetValue(mo, "Status");
                GetValue(mo, "SuiteMask");
                GetValue(mo, "SystemDevice");
                GetValue(mo, "SystemDirectory");
                GetValue(mo, "SystemDrive");
                GetValue(mo, "TotalSwapSpaceSize");
                GetValue(mo, "TotalVirtualMemorySize");
                GetValue(mo, "TotalVisibleMemorySize");
                GetValue(mo, "Version");
                GetValue(mo, "WindowsDirectory");

                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

                //取得記憶體狀態
                GetInfo(mo, "FreePhysicalMemory");
                GetInfo(mo, "FreeSpaceInPagingFiles");
                GetInfo(mo, "FreeVirtualMemory");
                GetInfo(mo, "SizeStoredInPagingFiles");
                GetInfo(mo, "TotalSwapSpaceSize");
                GetInfo(mo, "TotalVirtualMemorySize");
                GetInfo(mo, "TotalVisibleMemorySize");

                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

                string StrInfo = mo.GetText(TextFormat.Mof);
                string InstallDate = StrInfo.Substring(StrInfo.LastIndexOf("InstallDate") + 15, 14);
                richTextBox1.Text += "取得作業系統安裝時間 :\t" + InstallDate + "\n";
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Win32_OperatingSystem 獲取系統的啟動日期和安裝日期\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "Description: " + mo["Description"].ToString() + "\n";
                richTextBox1.Text += "FreePhysicalMemory: " + mo["FreePhysicalMemory"].ToString() + "\n";
                richTextBox1.Text += "FreeVirtualMemory: " + mo["FreeVirtualMemory"].ToString() + "\n";
                richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";
                richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString().Substring(0, 14) + "\n";
                richTextBox1.Text += "LastBootUpTime: " + mo["LastBootUpTime"].ToString() + "\n";
                richTextBox1.Text += "LastBootUpTime: " + mo["LastBootUpTime"].ToString().Substring(0, 14) + "\n";
                richTextBox1.Text += "LocalDateTime: " + mo["LocalDateTime"].ToString() + "\n";
                richTextBox1.Text += "Name: " + mo["Name"].ToString() + "\n";
                //richTextBox1.Text += "Organization: " + mo["Organization"].ToString() + "\n";
                richTextBox1.Text += "OSLanguage: " + mo["OSLanguage"].ToString() + "\n";
                richTextBox1.Text += "OSType: " + mo["OSType"].ToString() + "\n";
                richTextBox1.Text += "RegisteredUser: " + mo["RegisteredUser"].ToString() + "\n";
                richTextBox1.Text += "SerialNumber: " + mo["SerialNumber"].ToString() + "\n";
                richTextBox1.Text += "ServicePackMajorVersion: " + mo["ServicePackMajorVersion"].ToString() + "\n";
                richTextBox1.Text += "ServicePackMinorVersion: " + mo["ServicePackMinorVersion"].ToString() + "\n";

                richTextBox1.Text += "Caption: " + mo["Caption"].ToString() + "\n";　　//獲取OS　名稱
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"].ToString() + "\n";　　//獲取　OS　製造商
                richTextBox1.Text += "CountryCode: " + mo["CountryCode"].ToString() + "\n";　　//地區
                richTextBox1.Text += "CSName: " + mo["CSName"].ToString() + "\n";　　//獲取系統名稱
                richTextBox1.Text += "WindowsDirectory: " + mo["WindowsDirectory"].ToString() + "\n";　　//獲取Windows　目錄
                richTextBox1.Text += "SystemDirectory: " + mo["SystemDirectory"].ToString() + "\n";　　//獲取系統目錄
                richTextBox1.Text += "BootDevice: " + mo["BootDevice"].ToString() + "\n";　　//獲取啟動設備
                richTextBox1.Text += "Version: " + mo["Version"].ToString() + "\n";//獲取版本
                //richTextBox1.Text += "CSDVersion: " + mo["CSDVersion"].ToString() + "\n";//獲取SP
                richTextBox1.Text += "BuildNumber: " + mo["BuildNumber"].ToString() + "\n";//獲取builderNumber
                richTextBox1.Text += "TotalVisibleMemorySize: " + ((ulong)mo["TotalVisibleMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取總的物理內存
                richTextBox1.Text += "FreePhysicalMemory: " + ((ulong)mo["FreePhysicalMemory"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取可用物理內存
                richTextBox1.Text += "TotalVirtualMemorySize: " + ((ulong)mo["TotalVirtualMemorySize"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　　//獲取總的虛擬內存
                richTextBox1.Text += "FreeVirtualMemory: " + ((ulong)mo["FreeVirtualMemory"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取可用虛擬內存
                richTextBox1.Text += "SizeStoredInPagingFiles: " + ((ulong)mo["SizeStoredInPagingFiles"] / 1024.0 / 1024).ToString("#0.00") + "G" + "\n";　　//獲取頁面文檔大小
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        // Add information about the property to the ListView.
        private void GetInfo(ManagementObject mobj, string property_name)
        {
            object property_obj = mobj[property_name];
            if (property_obj == null)
            {
                //lvwInfo.AddRow(property_name, "???");
                richTextBox1.Text += property_name + "\t\t???\n";
            }
            else
            {
                ulong property_value = (ulong)property_obj * 1024;
                //lvwInfo.AddRow(property_name, property_value.ToFileSizeApi());
                richTextBox1.Text += property_name + "\t\t" + property_value.ToFileSizeApi() + "\n";
            }
        }

        private void GetValue(ManagementObject mo, string property_name)
        {
            string value;
            try
            {
                value = mo[property_name].ToString();
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                value = "錯誤訊息 : " + ex.Message;
            }
            richTextBox1.Text += property_name + "\t" + value + "\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Win32_USBController\n";

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBController");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "\n";
                richTextBox1.Text += "Name: " + mo["Name"].ToString() + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"].ToString() + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"].ToString() + "\n";
                richTextBox1.Text += "Description: " + mo["Description"].ToString() + "\n";
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "PNPDeviceID: " + mo["PNPDeviceID"].ToString() + "\n";
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"].ToString() + "\n";
                //richTextBox1.Text += "ErrorDescription: " + mo["ErrorDescription"].ToString() + "\n";
                richTextBox1.Text += "Status: " + mo["Status"].ToString() + "\n";
                richTextBox1.Text += "SystemCreationClassName: " + mo["SystemCreationClassName"].ToString() + "\n";
                richTextBox1.Text += "SystemName: " + mo["SystemName"].ToString() + "\n";

                //richTextBox1.Text += "Availability: " + mo["Availability"].ToString() + "\n";
                richTextBox1.Text += "ConfigManagerErrorCode: " + mo["ConfigManagerErrorCode"].ToString() + "\n";
                //richTextBox1.Text += "LastErrorCode: " + mo["LastErrorCode"].ToString() + "\n";
                //richTextBox1.Text += "MaxNumberControlled: " + mo["MaxNumberControlled"].ToString() + "\n";
                //richTextBox1.Text += "PowerManagementCapabilities: " + mo["PowerManagementCapabilities[]"].ToString() + "\n";
                richTextBox1.Text += "ProtocolSupported: " + mo["ProtocolSupported"].ToString() + "\n";
                //richTextBox1.Text += "StatusInfo: " + mo["StatusInfo"].ToString() + "\n";

                //richTextBox1.Text += "PowerManagementSupported: " + mo["PowerManagementSupported"].ToString() + "\n";
                richTextBox1.Text += "ConfigManagerUserConfig: " + mo["ConfigManagerUserConfig"].ToString() + "\n";
                //richTextBox1.Text += "ErrorCleared: " + mo["ErrorCleared"].ToString() + "\n";

                //richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";
                //richTextBox1.Text += "TimeOfLastReset: " + mo["TimeOfLastReset"].ToString() + "\n";
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Win32_USBControllerDevice\n";

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBControllerDevice");
            foreach (ManagementObject mo in mos.Get())
            {
                //richTextBox1.Text += "NegotiatedDataWidth: " + mo["NegotiatedDataWidth"].ToString() + "\n";
                //richTextBox1.Text += "NegotiatedSpeed: " + mo["NegotiatedSpeed"].ToString() + "\n";
                //richTextBox1.Text += "AccessState: " + mo["AccessState"].ToString() + "\n";
                //richTextBox1.Text += "NumberOfHardResets: " + mo["NumberOfHardResets"].ToString() + "\n";
                //richTextBox1.Text += "NumberOfSoftResets: " + mo["NumberOfSoftResets"].ToString() + "\n";
            }
        }

        private void button23_Click(object sender, EventArgs e)
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

        private void button24_Click(object sender, EventArgs e)
        {
            //Win32_ComputerSystem

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_ComputerSystem");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "------------------------------\n";  // 30個
                    //richTextBox1.Text += "全部 :\n" + mo.GetText(TextFormat.Mof) + "\n";
                    //richTextBox1.Text += "------------------------------\n";  // 30個

                    int num_physical_processors = int.Parse(mo["NumberOfProcessors"].ToString());
                    richTextBox1.Text += "取得實體核心數 : " + num_physical_processors.ToString() + "\n";

                    richTextBox1.Text += "核心數 : " + mo.Properties["NumberOfLogicalProcessors"].Value.ToString() + " processors" + "\n";

                    string UserName = mo["UserName"].ToString();
                    richTextBox1.Text += "操作系統的登錄用戶名 :\t" + UserName + "\n";

                    string SystemType = mo["SystemType"].ToString();
                    richTextBox1.Text += "PC類型 :\t" + SystemType + "\n";

                    System.UInt64 TotalPhysicalMemory = UInt64.MinValue;
                    TotalPhysicalMemory = (System.UInt64)(mo["TotalPhysicalMemory"]);//單位：拜

                    richTextBox1.Text += "物理內存 :\t" + TotalPhysicalMemory.ToString() + " 拜\n";
                    richTextBox1.Text += "物理內存 :\t" + (TotalPhysicalMemory / 1024).ToString() + " K\n";
                    richTextBox1.Text += "物理內存 :\t" + (TotalPhysicalMemory / 1024 / 1024).ToString() + " M\n";
                    richTextBox1.Text += "物理內存 :\t" + (TotalPhysicalMemory / 1024 / 1024 / 1024).ToString() + " G\n";
                }
                catch
                {
                }
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Win32_ComputerSystem 獲取電腦資訊\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_ComputerSystem");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "操作系統類型：" + mo["SystemType"] + "\n";
                richTextBox1.Text += "實體記憶體：" + mo["TotalPhysicalMemory"].ToString() + "\n";

                richTextBox1.Text += "PrimaryOwnerName: " + mo["PrimaryOwnerName"] + "\n";
                richTextBox1.Text += "Status: " + mo["Status"] + "\n";
                richTextBox1.Text += "UserName: " + mo["UserName"] + "\n";
                richTextBox1.Text += "Caption: " + mo["Caption"] + "\n";
                richTextBox1.Text += "BootupState: " + mo["BootupState"] + "\n";
                richTextBox1.Text += "CreationClassName: " + mo["CreationClassName"] + "\n";
                richTextBox1.Text += "Description: " + mo["Description"] + "\n";
                richTextBox1.Text += "Domain: " + mo["Domain"] + "\n";
                richTextBox1.Text += "Manufacturer: " + mo["Manufacturer"] + "\n";
                richTextBox1.Text += "Model: " + mo["Model"] + "\n";
                richTextBox1.Text += "Name: " + mo["Name"] + "\n";
                /* 無資料
                richTextBox1.Text += "aaaaa: " + mo["NameFormat"] + "\n";
                richTextBox1.Text += "aaaaa: " + mo["Workgroup"] + "\n";
                richTextBox1.Text += "aaaaa: " + mo["PrimaryOwnerContact"] + "\n";
                richTextBox1.Text += "aaaaa: " + mo["LastLoadInfo"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["DNSHostName"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["InitialLoadInfo[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["Roles[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SystemStartupOptions[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["OEMStringArray[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SupportContactDescription[]"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SystemFamily"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["SystemSKUNumber"] + "\n";
                //richTextBox1.Text += "aaaaa: " + mo["ChassisSKUNumber"] + "\n";
                */
                richTextBox1.Text += "nnnn: " + mo["AdminPasswordStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ChassisBootupState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["CurrentTimeZone"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["DomainRole"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["FrontPanelResetStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["KeyboardPasswordStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["NumberOfLogicalProcessors"].ToString() + "\n";
                richTextBox1.Text += "NumberOfProcessors: " + mo["NumberOfProcessors"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PauseAfterReset"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PowerOnPasswordStatus"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PowerState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["PowerSupplyState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ResetCapability"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ResetCount"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ResetLimit"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["SystemStartupDelay"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["SystemStartupSetting"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["ThermalState"].ToString() + "\n";
                richTextBox1.Text += "nnnn: " + mo["WakeUpType"].ToString() + "\n";
                /* 無資料
                //richTextBox1.Text += "nnnn: " + mo["OEMLogoBitmap[]"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["PCSystemType"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["BootOptionOnLimit"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["BootOptionOnWatchDog"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["BootStatus[]"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["PCSystemTypeEx"].ToString() + "\n";
                //richTextBox1.Text += "nnnn: " + mo["PowerManagementCapabilities[]"].ToString() + "\n";
                */

                //richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            int num_logical_processors = Environment.ProcessorCount;
            richTextBox1.Text += "取得邏輯核心數 : " + num_logical_processors.ToString() + "\n";
            richTextBox1.Text += "LogicalProcessors\t" + num_logical_processors.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button25_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得系統其他進程的啟動參數\n";

            int cnt = 0;
            //使用WMI來查詢得到數據
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Process");
            foreach (ManagementObject mo in mos.Get())
            {
                if (mo.Properties["commandLine"].Value != null)
                {
                    richTextBox1.Text += mo.Properties["commandLine"].Value + "\n";
                    cnt++;
                    if (cnt > 20)
                    {
                        break;
                    }
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            cnt = 0;
            richTextBox1.Text += "獲取系統進程的用戶名\n";
            foreach (Process p in Process.GetProcesses())
            {
                //Console.Write(p.ProcessName);
                //Console.Write("----");
                //Console.WriteLine(GetProcessUserName(p.Id));

                if (p.ProcessName != null)
                {
                    richTextBox1.Text += p.ProcessName + "\t" + GetProcessUserName(p.Id) + "\n";
                    cnt++;
                    if (cnt > 20)
                    {
                        break;
                    }
                }
            }
        }

        private static string GetProcessUserName(int pID)
        {
            string text1 = null;
            SelectQuery query1 = new SelectQuery();
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Process WHERE processID=" + pID);
            try
            {
                foreach (ManagementObject mo in mos.Get())
                {
                    ManagementBaseObject inPar = null;
                    ManagementBaseObject outPar = null;
                    inPar = mo.GetMethodParameters("GetOwner");
                    outPar = mo.InvokeMethod("GetOwner", inPar, null);
                    text1 = outPar["User"].ToString();
                    break;
                }
            }
            catch
            {
                text1 = "SYSTEM";
            }
            return text1;
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "列出機器中所有的共享資源\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Share");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "------------------------------\n";  // 30個
                //richTextBox1.Text += "全部 :\n" + mo.GetText(TextFormat.Mof) + "\n";
                //richTextBox1.Text += "---------------\n";  // 15個
                richTextBox1.Text += "Caption : " + mo["Caption"] + "\n";
                richTextBox1.Text += "Description : " + mo["Description"] + "\n";
                richTextBox1.Text += "InstallDate : " + mo["InstallDate"] + "\n";
                richTextBox1.Text += "Status : " + mo["Status"] + "\n";
                richTextBox1.Text += "AccessMask : " + mo["AccessMask"] + "\n";
                richTextBox1.Text += "AllowMaximum : " + mo["AllowMaximum"] + "\n";
                richTextBox1.Text += "MaximumAllowed : " + mo["MaximumAllowed"] + "\n";
                richTextBox1.Text += "Name : " + mo["Name"] + "\n";
                richTextBox1.Text += "Path : " + mo["Path"] + "\n";
                richTextBox1.Text += "Type : " + mo["Path"] + "\n";
                richTextBox1.Text += "------------------------------\n";  // 30個
            }
            richTextBox1.Text += "------------------------------\n";  // 30個
        }

        private void button27_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Win32_USBHub 1\n";
            //取得USB資訊
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "==========================================================";
                richTextBox1.Text += Environment.NewLine;
                richTextBox1.Text += "Name : " + mo["Name"].ToString();
                richTextBox1.Text += Environment.NewLine;
                richTextBox1.Text += "DeviceID : " + mo["DeviceID"].ToString();
                richTextBox1.Text += Environment.NewLine;
            }
            richTextBox1.Text += "==========================================================";
            richTextBox1.Text += Environment.NewLine;

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //Win32_USBHub 2
            richTextBox1.Text += "\nDevice\t\t\t\tPnP Device ID\t\t\t\tDescription\n";
            ManagementObjectSearcher device_searcher = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            foreach (ManagementObject usb_device in device_searcher.Get())
            {
                richTextBox1.Text += usb_device.Properties["DeviceID"].Value.ToString() + "\t\t";
                richTextBox1.Text += usb_device.Properties["PNPDeviceID"].Value.ToString() + "\t\t";
                richTextBox1.Text += usb_device.Properties["Description"].Value.ToString() + "\n";
            }

        }

        private void button29_Click(object sender, EventArgs e)
        {
            string osVersionString = Environment.OSVersion.ToString();
            richTextBox1.Text += "取得Windows版本 : " + osVersionString + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //主機名稱
            richTextBox1.Text += "主機名稱 : " + Dns.GetHostName() + "\n";

            //取得電腦名稱
            string ComputerName = Environment.GetEnvironmentVariable("ComputerName");
            richTextBox1.Text += "ComputerName\t" + ComputerName + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            IPAddress addr;
            // 獲得本機局域網IP地址
            addr = new IPAddress(Dns.GetHostByName(Dns.GetHostName()).AddressList[0].Address);
            string cc = addr.ToString();

            richTextBox1.Text += "IP地址：" + cc + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得系統相關資訊

            listView1.Clear();

            listView1.BackColor = Color.Pink;
            listView1.View = View.Details;//設定控制元件顯示方式
            listView1.GridLines = true;//是否顯示網格
            listView1.Columns.Add("環境變數", 150, HorizontalAlignment.Left);//新增列標頭
            listView1.Columns.Add("變數值", 150, HorizontalAlignment.Left);//新增列標頭
            ListViewItem myItem;//建立ListViewItem對像
            //取得系統環境變數及對應的變數值，並顯示在ListView控制元件中
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                myItem = new ListViewItem(DEntry.Key.ToString(), 0);//建立ListViewItem對像
                myItem.SubItems.Add(DEntry.Value.ToString());//新增子項集合
                listView1.Items.Add(myItem);//將子項集合新增到控制元件中
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        void setup_listView1()
        {
            listView1.Clear();
            listView1.Columns.Add("項目", 150, HorizontalAlignment.Center);
            listView1.Columns.Add("內容", 250, HorizontalAlignment.Center);
        }

        private void bt_get_Click(object sender, EventArgs e)
        {
            string win32 = comboBox1.SelectedItem.ToString();
            get_win32_all_info(win32);
        }

        void get_win32_all_info(string win32)
        {
            setup_listView1();

            string win32_command = "SELECT * FROM " + win32;

            ManagementObjectSearcher mos = new ManagementObjectSearcher(win32_command);
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "------------------------------\n";  // 30個
                //印出所有參數名稱及內容
                foreach (var prop in mo.Properties)
                {
                    richTextBox1.Text += prop.Name + ": " + prop.Value + "\n";

                    ListViewItem i1 = new ListViewItem(prop.Name);
                    ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                    sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
                    i1.SubItems.Add(sub_i1a);
                    listView1.Items.Add(i1);
                }
            }
            richTextBox1.Text += "------------------------------\n";  // 30個
            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }
    }

    /// <summary>
    /// Hardware_Mac 的摘要說明。
    /// </summary>
    public class HardwareInfo
    {
        //取機器名
        public string GetHostName()
        {
            return System.Net.Dns.GetHostName();
        }

        //取CPU編號
        public String GetCpuID()
        {
            try
            {
                ManagementClass mc = new ManagementClass("Win32_Processor");
                ManagementObjectCollection moc = mc.GetInstances();

                String strCpuID = null;
                foreach (ManagementObject mo in moc)
                {
                    strCpuID = mo.Properties["ProcessorId"].Value.ToString();
                    break;
                }
                return strCpuID;
            }
            catch
            {
                return "";
            }

        }//end method

        //取第一塊硬盤編號
        public String GetHardDiskID()
        {
            try
            {
                ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
                String strHardDiskID = null;
                foreach (ManagementObject mo in searcher.Get())
                {
                    strHardDiskID = mo["SerialNumber"].ToString().Trim();
                    break;
                }
                return strHardDiskID;
            }
            catch
            {
                return "";
            }
        }//end

        public enum NCBCONST
        {
            NCBNAMSZ = 16, /* absolute length of a net name */
            MAX_LANA = 254, /* lana's in range 0 to MAX_LANA inclusive */
            NCBENUM = 0x37, /* NCB ENUMERATE LANA NUMBERS */
            NRC_GOODRET = 0x00, /* good return */
            NCBRESET = 0x32, /* NCB RESET */
            NCBASTAT = 0x33, /* NCB ADAPTER STATUS */
            NUM_NAMEBUF = 30, /* Number of NAME's BUFFER */
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct ADAPTER_STATUS
        {
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 6)]
            public byte[] adapter_address;
            public byte rev_major;
            public byte reserved0;
            public byte adapter_type;
            public byte rev_minor;
            public ushort duration;
            public ushort frmr_recv;
            public ushort frmr_xmit;
            public ushort iframe_recv_err;
            public ushort xmit_aborts;
            public uint xmit_success;
            public uint recv_success;
            public ushort iframe_xmit_err;
            public ushort recv_buff_unavail;
            public ushort t1_timeouts;
            public ushort ti_timeouts;
            public uint reserved1;
            public ushort free_ncbs;
            public ushort max_cfg_ncbs;
            public ushort max_ncbs;
            public ushort xmit_buf_unavail;
            public ushort max_dgram_size;
            public ushort pending_sess;
            public ushort max_cfg_sess;
            public ushort max_sess;
            public ushort max_sess_pkt_size;
            public ushort name_count;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct NAME_BUFFER
        {
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = (int)NCBCONST.NCBNAMSZ)]
            public byte[] name;
            public byte name_num;
            public byte name_flags;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct NCB
        {
            public byte ncb_command;
            public byte ncb_retcode;
            public byte ncb_lsn;
            public byte ncb_num;
            public IntPtr ncb_buffer;
            public ushort ncb_length;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = (int)NCBCONST.NCBNAMSZ)]
            public byte[] ncb_callname;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = (int)NCBCONST.NCBNAMSZ)]
            public byte[] ncb_name;
            public byte ncb_rto;
            public byte ncb_sto;
            public IntPtr ncb_post;
            public byte ncb_lana_num;
            public byte ncb_cmd_cplt;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = 10)]
            public byte[] ncb_reserve;
            public IntPtr ncb_event;
        }

        [StructLayout(LayoutKind.Sequential)]
        public struct LANA_ENUM
        {
            public byte length;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = (int)NCBCONST.MAX_LANA)]
            public byte[] lana;
        }

        [StructLayout(LayoutKind.Auto)]
        public struct ASTAT
        {
            public ADAPTER_STATUS adapt;
            [MarshalAs(UnmanagedType.ByValArray, SizeConst = (int)NCBCONST.NUM_NAMEBUF)]
            public NAME_BUFFER[] NameBuff;
        }

        public class Win32API
        {
            [DllImport("NETAPI32.DLL")]
            public static extern char Netbios(ref NCB ncb);
        }

        public string GetMacAddress()
        {
            string addr = "";
            try
            {
                int cb;
                ASTAT adapter;
                NCB Ncb = new NCB();
                char uRetCode;
                LANA_ENUM lenum;

                Ncb.ncb_command = (byte)NCBCONST.NCBENUM;
                cb = Marshal.SizeOf(typeof(LANA_ENUM));
                Ncb.ncb_buffer = Marshal.AllocHGlobal(cb);
                Ncb.ncb_length = (ushort)cb;
                uRetCode = Win32API.Netbios(ref Ncb);
                lenum = (LANA_ENUM)Marshal.PtrToStructure(Ncb.ncb_buffer, typeof(LANA_ENUM));
                Marshal.FreeHGlobal(Ncb.ncb_buffer);
                if (uRetCode != (short)NCBCONST.NRC_GOODRET)
                    return "";

                for (int i = 0; i < lenum.length; i++)
                {
                    Ncb.ncb_command = (byte)NCBCONST.NCBRESET;
                    Ncb.ncb_lana_num = lenum.lana[i];
                    uRetCode = Win32API.Netbios(ref Ncb);
                    if (uRetCode != (short)NCBCONST.NRC_GOODRET)
                        return "";

                    Ncb.ncb_command = (byte)NCBCONST.NCBASTAT;
                    Ncb.ncb_lana_num = lenum.lana[i];
                    Ncb.ncb_callname[0] = (byte)'*';
                    cb = Marshal.SizeOf(typeof(ADAPTER_STATUS)) + Marshal.SizeOf(typeof(NAME_BUFFER)) * (int)NCBCONST.NUM_NAMEBUF;
                    Ncb.ncb_buffer = Marshal.AllocHGlobal(cb);
                    Ncb.ncb_length = (ushort)cb;
                    uRetCode = Win32API.Netbios(ref Ncb);
                    adapter.adapt = (ADAPTER_STATUS)Marshal.PtrToStructure(Ncb.ncb_buffer, typeof(ADAPTER_STATUS));
                    Marshal.FreeHGlobal(Ncb.ncb_buffer);

                    if (uRetCode == (short)NCBCONST.NRC_GOODRET)
                    {
                        if (i > 0)
                            addr += ":";
                        addr = string.Format("{0,2:X}{1,2:X}{2,2:X}{3,2:X}{4,2:X}{5,2:X}",
                        adapter.adapt.adapter_address[0],
                        adapter.adapt.adapter_address[1],
                        adapter.adapt.adapter_address[2],
                        adapter.adapt.adapter_address[3],
                        adapter.adapt.adapter_address[4],
                        adapter.adapt.adapter_address[5]);
                    }
                }
            }
            catch
            { }
            return addr.Replace(' ', '0');
        }
    }
}

//------------------------------------------------------------  # 60個

//------------------------------  # 30個

//---------------  # 15個

// 6060
// richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
// 3030
// richTextBox1.Text += "------------------------------\n";  // 30個
// 1515
// richTextBox1.Text += "---------------\n";  // 15個
