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
        class USBDeviceInfo
        {
            public USBDeviceInfo(string deviceID, string pnpDeviceID, string description)
            {
                this.DeviceID = deviceID;
                this.PnpDeviceID = pnpDeviceID;
                this.Description = description;
            }
            public string DeviceID { get; private set; }
            public string PnpDeviceID { get; private set; }
            public string Description { get; private set; }
        }

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
            //3、如何用WMI獲得指定磁盤的容量？	  TBD

            //"Win32_LogicalDisk.deviceid=/"c:/"");
            /*
            ManagementObject disk2 = new ManagementObject("Win32_LogicalDisk.deviceid=C://");
            disk2.Get();
            Console.WriteLine("Logical Disk Size = " + disk2["Size"] + " bytes");
            richTextBox1.Text += "Logical Disk Size = " + disk2["Size"] + " bytes\n";
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            ManagementClass mc = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection moc = mc.GetInstances();
            ManagementObjectCollection.ManagementObjectEnumerator disksEnumerator = moc.GetEnumerator();
            while (disksEnumerator.MoveNext())
            {
                ManagementObject mo = (ManagementObject)disksEnumerator.Current;
                richTextBox1.Text += "Disk found: " + mo["deviceid"] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //獲得硬碟空間
            mc = new ManagementClass("Win32_LogicalDisk");
            moc = mc.GetInstances();
            System.UInt64 space = UInt64.MinValue;
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += "磁碟 : " + (mo["Name"]).ToString() + "\n";
                if ((mo["Name"]).ToString() == "C:")
                {
                    space = (System.UInt64)(mo["FreeSpace"]);
                    richTextBox1.Text += "獲得硬碟空間 : " + space.ToString() + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取CPU的溫度, NG\n";

            //GetCPUTemperature();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            Double CPUtprt = 0;
            mos = new System.Management.ManagementObjectSearcher(@"root\WMI", "SELECT * FROM MSAcpi_ThermalZoneTemperature");

            foreach (System.Management.ManagementObject mo in mos.Get())
            {
                CPUtprt = Convert.ToDouble(Convert.ToDouble(mo.GetPropertyValue("CurrentTemperature").ToString()) - 2732) / 10;
                richTextBox1.Text += "CPU 溫度 : " + CPUtprt.ToString() + " °C\n";
            }
            */
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

            //用WMI取出作業系統資訊2

            // Get 32- versus 64-bit.
            // For more information from this query, see:
            //      http://msdn.microsoft.com/library/aa394373.aspx
            string proc_query = "SELECT * FROM Win32_Processor";
            ManagementObjectSearcher proc_searcher = new ManagementObjectSearcher(proc_query);
            foreach (ManagementObject mo in proc_searcher.Get())
            {
                richTextBox1.Text += mo.Properties["AddressWidth"].Value.ToString() + "-bit" + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 或透過 ManagementObject 類別直接存取特定 CPU 序號
            ManagementObject wmiObj = new ManagementObject("Win32_Processor.DeviceID='CPU0'");
            richTextBox1.Text += "CPU ID:\t" + wmiObj.GetPropertyValue("ProcessorId").ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取CPU編號\n";
            ManagementClass mc = new ManagementClass("Win32_Processor");
            ManagementObjectCollection moc = mc.GetInstances();
            String MyInfo = "當前系統CPU編號是：";
            string MyCPUID = "";
            foreach (ManagementObject mo in moc)
            {
                MyCPUID = mo.Properties["ProcessorId"].Value.ToString();
                break;
            }
            MyInfo += MyCPUID;
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的當前電壓\n";
            MyInfo = "計算機CPU的當前電壓是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    MyInfo += "/n" + String.Format("CurrentVoltage : " + mo["CurrentVoltage"].ToString());
                    MyInfo += "/n=========================================================";
                }
                catch { }
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的外部頻率\n";
            MyInfo = "計算機CPU的外部頻率是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    MyInfo += "/n" + String.Format("ExtClock : " + mo["ExtClock"].ToString());
                    MyInfo += "/n=========================================================";
                }
                catch { }
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的二級緩存\n";
            MyInfo = "計算機CPU的二級緩存尺寸是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("L2CacheSize: " + mo["L2CacheSize"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的制造商名稱\n";
            MyInfo = "計算機CPU的制造商名稱是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("Manufacturer : " + mo["Manufacturer"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的產品名稱\n";
            MyInfo = "計算機CPU的產品名稱是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("Name : " + mo["Name"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的版本信息\n";
            MyInfo = "計算機CPU的版本信息如下：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("Version: " + mo["Version"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的當前使用百分比 注意要把SQLserver或者其他耗CPU的軟件開著否則看不到效果就一直為0\n";
            MyInfo = "計算機CPU的當前使用百分比是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                //NG
                //MyInfo += "/n" + String.Format("LoadPercentage : " + mo["LoadPercentage"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的最大時鐘頻率\n";
            MyInfo = "計算機CPU的最大時鐘頻率是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("MaxClockSpeed : " + mo["MaxClockSpeed"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機CPU的當前時鐘頻率\n";
            MyInfo = "計算機CPU的當前時鐘頻率是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("CurrentClockSpeed : " + mo["CurrentClockSpeed"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機的CPU地址寬度\n";
            MyInfo = "當前計算機的CPU地址寬度是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("AddressWidth: " + mo["AddressWidth"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取計算機的CPU數據寬度\n";
            MyInfo = "當前計算機的CPU數據寬度是：";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                MyInfo += "/n" + String.Format("DataWidth : " + mo["DataWidth"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得CPU編號、硬盤編號等系統有關環境、屬性
            //TBD
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

            //取得網路卡參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "MAC位址 :\t" + mo.GetPropertyValue("MACAddress").ToString() + "\n";
                    string guid = mo.GetPropertyValue("GUID").ToString();
                    string name = mo.GetPropertyValue("Name").ToString();
                    string mac = mo.GetPropertyValue("MACAddress").ToString();
                    richTextBox1.Text += "guid :\t" + guid + "\n";
                    richTextBox1.Text += "name :\t" + name + "\n";
                    richTextBox1.Text += "mac :\t" + mac + "\n";
                }
                catch
                {
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            ManagementObjectCollection collection = mos.Get();
            var networkList = from n in collection.Cast<ManagementBaseObject>()
                              select new
                              {
                                  guid = n.GetPropertyValue("GUID"),
                                  name = n.GetPropertyValue("Name"),
                                  mac = n.GetPropertyValue("MACAddress")
                              };
            foreach (var n in networkList)
            {
                richTextBox1.Text += String.Format("{0}{2}{1}{2}{2}", n.name, n.mac, Environment.NewLine);
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
            catch
            {
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //使用WMI取得USB資訊

            string strServiceName = string.Empty;

            string location = System.Reflection.Assembly.GetExecutingAssembly().Location;
            //string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";

            //Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 

            //使用WMI取得USB資訊

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            ManagementObjectCollection collection = mos.Get();
            var usbList = from u in collection.Cast<ManagementBaseObject>()
                          select new
                          {
                              id = u.GetPropertyValue("DeviceID"),
                              name = u.GetPropertyValue("Name"),
                              status = u.GetPropertyValue("Status"),
                              system = u.GetPropertyValue("SystemName"),
                              caption = u.GetPropertyValue("Caption"),
                              pnp = u.GetPropertyValue("PNPDeviceID"),
                              description = u.GetPropertyValue("Description")
                          };
            foreach (var u in usbList)
            {
                richTextBox1.Text += String.Format("{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}{7}{7}{7}", u.id, u.name, u.status, u.system, u.caption, u.pnp, u.description, Environment.NewLine);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //C#.Net 使用WMI取得USB資訊 
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            collection = mos.Get();
            usbList = from u in collection.Cast<ManagementBaseObject>()
                      select new
                      {
                          id = u.GetPropertyValue("DeviceID"),
                          name = u.GetPropertyValue("Name"),
                          status = u.GetPropertyValue("Status"),
                          system = u.GetPropertyValue("SystemName"),
                          caption = u.GetPropertyValue("Caption"),
                          pnp = u.GetPropertyValue("PNPDeviceID"),
                          description = u.GetPropertyValue("Description")
                      };
            foreach (var u in usbList)
            {
                richTextBox1.Text += String.Format("{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}{7}{7}{7}", u.id, u.name, u.status, u.system, u.caption, u.pnp, u.description, Environment.NewLine);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            var usbDevices = GetUSBDevices();

            foreach (var usbDevice in usbDevices)
            {
                //richTextBox1.Text += "Device ID: {0}, PNP Device ID: {1}, Description: {2}",
                //    usbDevice.DeviceID, usbDevice.PnpDeviceID, usbDevice.Description);

                richTextBox1.Text += "Device ID: " + usbDevice.DeviceID + "\n" + "PNP Device ID" + usbDevice.PnpDeviceID + "\n"
                + "Description: " + usbDevice.Description + "\n\n";
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        static List<USBDeviceInfo> GetUSBDevices()
        {
            List<USBDeviceInfo> devices = new List<USBDeviceInfo>();

            ManagementObjectCollection collection;
            using (var mos = new ManagementObjectSearcher(@"SELECT * FROM Win32_USBHub"))
                collection = mos.Get();

            foreach (var device in collection)
            {
                devices.Add(new USBDeviceInfo(
                (string)device.GetPropertyValue("DeviceID"),
                (string)device.GetPropertyValue("PNPDeviceID"),
                (string)device.GetPropertyValue("Description")
                ));
            }
            collection.Dispose();
            return devices;
        }

        private void button8_Click(object sender, EventArgs e)
        {
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
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            SelectQuery query = new SelectQuery("SELECT * FROM Win32_BaseBoard"); // 查詢主板
            ManagementObjectSearcher dev = new ManagementObjectSearcher(query);   // 執行query
            ManagementObjectCollection.ManagementObjectEnumerator enumerator = dev.Get().GetEnumerator();
            enumerator.MoveNext();
            ManagementBaseObject mbo = enumerator.Current;                    // 取得目前主板
            richTextBox1.Text += "主板編號\t\t" + mbo.GetPropertyValue("SerialNumber").ToString() + "\n";  //取得主板編號
            richTextBox1.Text += "主板製造商\t\t" + mbo.GetPropertyValue("Manufacturer").ToString() + "\n";  //取得主板製造商
            richTextBox1.Text += "主板型號\t\t" + mbo.GetPropertyValue("Name").ToString() + "\n";          //取得主板型號

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取邏輯驅動器詳細信息, 判斷驅動器類型\n";

            //找部分
            //SelectQuery selectQuery = new SelectQuery("SELECT Name,DriveType FROM Win32_LogicalDisk");

            //找全部
            SelectQuery selectQuery = new SelectQuery("SELECT * FROM Win32_LogicalDisk");

            ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject mo in mos.Get())
            {
                //讀取驅動器盤符
                string name = mo["Name"].ToString();
                string type = get_drive_type(mo["Name"].ToString());
                richTextBox1.Text += "取得驅動器 : " + mo["Name"].ToString() + "\t" + get_drive_type(mo["Name"].ToString()) + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            SelectQuery query = new SelectQuery("SELECT * FROM Win32_LogicalDisk");
            mos = new ManagementObjectSearcher(query);

            foreach (ManagementBaseObject mo in mos.Get())
            {
                richTextBox1.Text += mo["Name"] + " " + mo["DriveType"] + " " + mo["VolumeName"] + "\n";
            }
            /*
            mo["DriveType"] 的返回值意義如下:
            1 No type
            2 Floppy disk
            3 Hard disk
            4 Removable drive or network drive
            5 CD-ROM
            6 RAM disk
            */
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
            //Win32_DiskDrive

            richTextBox1.Text += "本機硬碟資訊/參數\n";

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            int len = mos.Get().Count;
            richTextBox1.Text += "共有硬碟數目 : " + len.ToString() + " 個\n";

            foreach (ManagementObject mo in mos.Get())
            {
                //用GetPropertyValue()方法
                richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "型號 :\t" + mo.GetPropertyValue("Model").ToString() + "\n";
                richTextBox1.Text += "介面 :\t" + mo.GetPropertyValue("InterfaceType").ToString() + "\n";
                richTextBox1.Text += "序號 :\t" + mo.GetPropertyValue("Signature").ToString() + "\n";
                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


                //用字典取值
                richTextBox1.Text += "DeviceID: " + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "Model: " + mo["Model"].ToString() + "\n";
                richTextBox1.Text += "Interface: " + mo["InterfaceType"].ToString() + "\n";
                richTextBox1.Text += "Serial#: " + mo["SerialNumber"].ToString() + "\n";
                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "本機的硬碟序號 :\n";

            string HardID = "";
            using (ManagementClass mc = new ManagementClass("Win32_DiskDrive"))
            {
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    HardID = mo["Model"].ToString().Trim();
                    //HardID = (string)mo.Properties["Model"].Value; same
                    richTextBox1.Text += "取得硬碟序號 : " + HardID + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取U盤序號
            _serialNumber.Clear();
            matchDriveLetterWithSerial();

            len = _serialNumber.Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "取得序號 : " + _serialNumber[i] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //獲得硬碟序號
            //string hdd_serial = GetDiskVolumeSerialNumber();

            ManagementObject mo1 = new ManagementObject("Win32_LogicalDisk.deviceid=\"c:\"");
            mo1.Get();
            string result = mo1.GetPropertyValue("VolumeSerialNumber").ToString();

            richTextBox1.Text += "取得硬碟序號 : " + result + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            ManagementClass mcHD = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection mocHD = mcHD.GetInstances();
            foreach (ManagementObject mo in mocHD)
            {
                if (mo["DeviceID"].ToString() == "C:")
                {
                    string result3 = mo["VolumeSerialNumber"].ToString();
                    richTextBox1.Text += "取得 : " + result3 + "\n";
                    break;
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "\n讀取硬碟序號\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            richTextBox1.Text += "硬碟個數：" + mos.Get().Count.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "硬碟 Model：" + mo["Model"].ToString() + "\n";
                richTextBox1.Text += "硬碟 DeviceID：" + mo["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Get HDD serial\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += mo["DeviceID"].ToString() + "\t";
                richTextBox1.Text += "Model: " + mo["Model"].ToString() + "\t";
                richTextBox1.Text += "Interface: " + mo["InterfaceType"].ToString() + "\t";
                richTextBox1.Text += "Serial#: " + mo["SerialNumber"].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //WMI 從C＃中的USB閃存驅動器讀取VID/PID

            // Get all the disk drives 

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            // Loop through each object (disk) retrieved by WMI 

            foreach (ManagementObject moDisk in mos.Get())
            {
                // Add the HDD to the list (use the Model field as the item's caption) 

                string diskname = moDisk["Model"].ToString();
                richTextBox1.Text += "取得 : " + diskname + "\n";
                get_detail_data(diskname);
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





            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        //讀取硬碟序號
        private List<string> _serialNumber = new List<string>();

        /// <summary>
        /// 調用這個函數將本機所有U盤序號存儲到_serialNumber中
        /// </summary>
        private void matchDriveLetterWithSerial()
        {
            string[] diskArray;
            string driveNumber;
            var mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDiskToPartition");
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
            // Get all the disk drives from WMI that match the Model name selected in the ComboBox 

            richTextBox1.Text += "你選擇了 : " + diskname + "\n";

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive WHERE Model = '" + diskname + "'");

            // Loop through the drives retrieved, although it should normally be only one loop going on here 

            foreach (ManagementObject moDisk in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "Type: " + moDisk["MediaType"].ToString() + "\n";
                    richTextBox1.Text += "Model: " + moDisk["Model"].ToString() + "\n";
                    richTextBox1.Text += "Serial: " + moDisk["SerialNumber"].ToString() + "\n";
                    richTextBox1.Text += "Interface: " + moDisk["InterfaceType"].ToString() + "\n";

                    // The capacity in gigabytes is easily calculated 
                    richTextBox1.Text += "Capacity: " + moDisk["Size"].ToString() + " bytes (" + Math.Round(((((double)Convert.ToDouble(moDisk["Size"]) / 1024) / 1024) / 1024), 2) + " GB)" + "\n";
                    richTextBox1.Text += "Partitions: " + moDisk["Partitions"].ToString() + "\n";
                    richTextBox1.Text += "Signature: " + moDisk["Signature"].ToString() + "\n";
                    richTextBox1.Text += "Firmware: " + moDisk["FirmwareRevision"].ToString() + "\n";
                    richTextBox1.Text += "Cylinders: " + moDisk["TotalCylinders"].ToString() + "\n";
                    richTextBox1.Text += "Sectors: " + moDisk["TotalSectors"].ToString() + "\n";
                    richTextBox1.Text += "Heads: " + moDisk["TotalHeads"].ToString() + "\n";
                    richTextBox1.Text += "Tracks: " + moDisk["TotalTracks"].ToString() + "\n";
                    richTextBox1.Text += "Bytes per Sector: " + moDisk["BytesPerSector"].ToString() + "\n";
                    richTextBox1.Text += "Sectors per Track: " + moDisk["SectorsPerTrack"].ToString() + "\n";
                    richTextBox1.Text += "Tracks per Cylinder: " + moDisk["TracksPerCylinder"].ToString() + "\n";
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //取得磁盤配額
            try
            {
                ManagementClass mc1 = new ManagementClass("Win32_DiskQuota");
                richTextBox1.Text += "aaaa : " + mc1.SystemProperties + "\n";
                foreach (ManagementObject o in mc1.GetInstances())
                {
                    richTextBox1.Text += "Next : " + o.Path + "\n";
                }

                mc1 = new ManagementClass("Win32_DiskQuota");
                ManagementObject quota = mc1.CreateInstance();
                quota["Limit"] = 400000000;
                quota["WarningLimit"] = 200000000;
                /* 以下NG
                // Get user account object
                ManagementObject account = new ManagementObject("Win32_Account.Domain=TODAY20040216,Name=ASPNET");
                account.Get();
                // get disk object 
                ManagementObject mo = new ManagementObject("Win32_LogicalDisk.DeviceId='D:'");
                mo.Get();
                quota["QuotaVolume"] = mo;
                quota["User"] = account;
                quota.Put(); // commit
                */
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //獲取硬碟資訊

            richTextBox1.Text += "\n獲取硬碟資訊\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject mo in mos.Get())
            {
                //印出所有參數名稱及內容
                foreach (var prop in mo.Properties)
                {
                    richTextBox1.Text += prop.Name + ": " + prop.Value + "\n";
                }
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            // Win32_LogicalDisk
            // 讀取硬碟相應分區的序號
            richTextBox1.Text += "讀取硬碟相應分區的序號 :\n";

            ManagementClass mc = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection moc = mc.GetInstances();
            foreach (ManagementObject mo in moc)
            {
                if (Convert.ToString(mo.Properties["DriveType"].Value) == "3")
                {
                    richTextBox1.Text += "磁碟 : " + mo.Properties["Name"].Value.ToString().ToUpper().Trim() + "\n";
                    string Dri = mo.Properties["VolumeSerialNumber"].Value.ToString();
                    richTextBox1.Text += "硬碟相應分區的序號 : " + Dri + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "獲取硬碟分區資訊\n";
            richTextBox1.Text += "\n指定邏輯磁碟機\n";

            //寫法一，直接寫D槽
            //ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk WHERE DeviceID = 'D:'");

            //寫法二，用變數
            string strDrive = "C:"; // 指定C: 邏輯磁碟機
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk WHERE DeviceID = " + "\"" + strDrive + "\"");

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

            richTextBox1.Text += "\n所有硬碟\n";
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
            foreach (ManagementObject mo2 in mos2.Get())
            {
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
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //Win32_LogicalDisk
            string drive = "C";
            richTextBox1.Text += "硬碟： " + drive + "\n";
            double dblSize = 0;
            double dblFree = 0;
            uint drive_type = 0;
            uint media_type = 0;

            if (string.IsNullOrEmpty(drive) || drive == null)
            {
                drive = "C";
            }
            //create our ManagementObject, passing it the drive letter to the
            //DevideID using WQL
            ManagementObject disk = new ManagementObject("Win32_LogicalDisk.DeviceID=\"" + drive + ":\"");
            //bind our management object
            disk.Get();

            richTextBox1.Text += "\n字串類\n";

            richTextBox1.Text += "Name: " + disk["Name"] + "\n";
            richTextBox1.Text += "Caption: " + disk["Caption"] + "\n";
            richTextBox1.Text += "FileSystem: " + disk["FileSystem"] + "\n";
            richTextBox1.Text += "CreationClassName: " + disk["CreationClassName"] + "\n";
            richTextBox1.Text += "Description: " + disk["Description"] + "\n";
            richTextBox1.Text += "DeviceID: " + disk["DeviceID"] + "\n";
            richTextBox1.Text += "SystemCreationClassName: " + disk["SystemCreationClassName"] + "\n";
            richTextBox1.Text += "SystemName: " + disk["SystemName"] + "\n";
            richTextBox1.Text += "VolumeName: " + disk["VolumeName"] + "\n";
            richTextBox1.Text += "序號VolumeSerialNumber: " + disk["VolumeSerialNumber"] + "\n";
            /*  無資料
            richTextBox1.Text += "LogicalDisk: " + disk["ProviderName"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["PNPDeviceID"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["Purpose"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["Status"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["ErrorDescription"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["ErrorMethodology"] + "\n";
            */

            richTextBox1.Text += "\n數字類\n";

            richTextBox1.Text += "Size: " + disk["Size"].ToString() + "\n";
            richTextBox1.Text += "FreeSpace: " + disk["FreeSpace"].ToString() + "\n";
            richTextBox1.Text += "MaximumComponentLength: " + disk["MaximumComponentLength"].ToString() + "\n";
            try
            {
                richTextBox1.Text += "MediaType: " + disk["MediaType"].ToString() + "\n";
                media_type = (uint)disk["MediaType"];
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "xxx錯誤訊息 : " + ex.Message + "\n";
            }

            //richTextBox1.Text += "Access: " + disk["Access"].ToString() + "\n";
            richTextBox1.Text += "DriveType: " + disk["DriveType"].ToString() + "\t";

            drive_type = (uint)disk["DriveType"];

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

            dblSize = Math.Round(Convert.ToDouble(disk["Size"]) / 1024 / 1024 / 1024);
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

            dblFree = Math.Round(Convert.ToDouble(disk["FreeSpace"]) / 1024 / 1024 / 1024);
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

            /*  無資料
            //richTextBox1.Text += "Size: " + disk["Availability"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["BlockSize"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["ConfigManagerErrorCode"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["LastErrorCode"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["NumberOfBlocks"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["PowerManagementCapabilities[]"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["StatusInfo"].ToString() + "\n";
            */
            /*  無資料
            richTextBox1.Text += "InstallDate: " + disk["InstallDate"] + "\n";
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private void button16_Click(object sender, EventArgs e)
        {
            // 抓取硬碟&USB儲存裝置磁碟代號
            using (ManagementClass devs = new ManagementClass(@"Win32_DiskDrive"))
            {
                ManagementObjectCollection moc = devs.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    richTextBox1.Text += "==========================================================\n";
                    richTextBox1.Text += "Description: ";
                    richTextBox1.Text += mo["Description"] + "\n";
                    richTextBox1.Text += "Name: ";
                    richTextBox1.Text += mo["Name"] + "\n";
                }
                richTextBox1.Text += "==========================================================\n";

                foreach (ManagementObject mo in moc)
                {
                    richTextBox1.Text += "==========================================================";
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
            }
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

        private void button17_Click(object sender, EventArgs e)
        {
            string PNPDeviceID = string.Empty;
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DesktopMonitor");
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

            if(PNPDeviceID == string.Empty)
            {
                richTextBox1.Text += "找不到螢幕, 離開\n";
                return;
            }

            //取得螢幕尺寸

            string id = PNPDeviceID;
            SizeF size = GetMonitorPhysicalSize(id);
            richTextBox1.Text += "get size = " + size.ToSize() + "\n";

            richTextBox1.Text += MonitorScaler(size).ToString() + " 吋\n";


            return;

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

        private void button18_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n一些資訊\n";

            richTextBox1.Text += "\n顯卡PNPDeviceID\n";
            richTextBox1.Text += "\nWin32_VideoController\n";
            ManagementObjectSearcher mos1 = new ManagementObjectSearcher("SELECT * FROM Win32_VideoController");
            foreach (ManagementObject mo in mos1.Get())
            {
                richTextBox1.Text += "顯卡PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "\n獲取顯示卡資訊\n";
            richTextBox1.Text += "\nWin32_VideoController\n";
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

            richTextBox1.Text += "\n聲卡PNPDeviceID\n";
            richTextBox1.Text += "\nWin32_SoundDevice\n";
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");
            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += "聲卡PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            richTextBox1.Text += "\n獲取音效卡資訊\n";
            richTextBox1.Text += "\nWin32_SoundDevice\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "音效設備名稱：" + mo["ProductName"].ToString() + "\n"; //在当前文本框中显示声音设备的名称
                richTextBox1.Text += "PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";//在当前文本框中显示声音设备的PNPDeviceID
            }
            */
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
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //用WMI取出作業系統資訊1

            richTextBox1.Text += "取得 Win32_OperatingSystem 所有資料\n";

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
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得作業系統安裝時間
            ObjectQuery MyQuery = new ObjectQuery("SELECT * FROM Win32_OperatingSystem");
            ManagementScope MyScope = new ManagementScope();
            ManagementObjectSearcher MySearch = new ManagementObjectSearcher(MyScope, MyQuery);
            ManagementObjectCollection moc = MySearch.Get();
            string StrInfo = "";
            foreach (ManagementObject MyObject in moc)
            {
                StrInfo = MyObject.GetText(TextFormat.Mof);
            }
            string InstallDate = StrInfo.Substring(StrInfo.LastIndexOf("InstallDate") + 15, 14);

            richTextBox1.Text += "取得作業系統安裝時間 :\t" + InstallDate + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得記憶體狀態
            //取得記憶體狀態2
            ManagementObjectSearcher os_searcher = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");

            foreach (ManagementObject mobj in os_searcher.Get())
            {
                GetInfo(mobj, "FreePhysicalMemory");
                GetInfo(mobj, "FreeSpaceInPagingFiles");
                GetInfo(mobj, "FreeVirtualMemory");
                GetInfo(mobj, "SizeStoredInPagingFiles");
                GetInfo(mobj, "TotalSwapSpaceSize");
                GetInfo(mobj, "TotalVirtualMemorySize");
                GetInfo(mobj, "TotalVisibleMemorySize");
            }
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
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
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
                    richTextBox1.Text += "------------------------------\n";  // 30個

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

            // Get the number of cores.
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject proc in mos.Get())
            {
                int num_cores = int.Parse(proc["NumberOfCores"].ToString());
                richTextBox1.Text += "取得核心數 : " + num_cores.ToString() + "\n";
                richTextBox1.Text += "Cores\t" + num_cores.ToString() + "\n";
            }

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
            SelectQuery query1 = new SelectQuery("SELECT * FROM Win32_Process WHERE processID=" + pID);
            ManagementObjectSearcher searcher1 = new ManagementObjectSearcher(query1);
            try
            {
                foreach (ManagementObject disk in searcher1.Get())
                {
                    ManagementBaseObject inPar = null;
                    ManagementBaseObject outPar = null;
                    inPar = disk.GetMethodParameters("GetOwner");
                    outPar = disk.InvokeMethod("GetOwner", inPar, null);
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
                richTextBox1.Text += "全部 :\n" + mo.GetText(TextFormat.Mof) + "\n";
                richTextBox1.Text += "---------------\n";  // 15個
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
        }

        private void button28_Click(object sender, EventArgs e)
        {
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
            setup_listView1();

            string win32_command;

            richTextBox1.Text += "選擇了： " + comboBox1.SelectedItem + "\n";

            win32_command = "SELECT * FROM " + comboBox1.SelectedItem;

            ManagementObjectSearcher mos = new ManagementObjectSearcher(win32_command);
            foreach (ManagementObject mo in mos.Get())
            {
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
            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();
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

