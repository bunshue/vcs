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

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nWMI寫法一：\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += mo["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo["VolumeSerialNumber"] + "\n";
            }

            richTextBox1.Text += "\nWMI寫法二：\n";
            SelectQuery sq = new SelectQuery("SELECT * FROM Win32_LogicalDisk");
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher(sq);
            foreach (ManagementObject mo2 in mos2.Get())
            {
                richTextBox1.Text += mo2["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo2["VolumeSerialNumber"] + "\n";
            }

            richTextBox1.Text += "\nWMI寫法三：\n";
            String strQry = "SELECT * FROM Win32_LogicalDisk"; // 指定查詢Win32_LogicalDisk ( 邏輯磁碟)
            // ManagementObjectSearcher 類別, 根據指定的查詢擷取管理物件的集合。
            mos = new ManagementObjectSearcher(strQry);
            // 使用Foreach 陳述式存取集合類別中物件(元素), Get 方法, 叫用指定的WMI 查詢, 並傳回產生的集合。
            foreach (ManagementObject mo3 in mos.Get())
            {
                // 取得磁碟Volumne 名稱跟序號
                richTextBox1.Text += mo3["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo3["VolumeSerialNumber"] + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //WMI 使用
            SelectQuery query = new SelectQuery("SELECT * FROM Win32_LogicalDisk");
            ManagementObjectSearcher mos = new ManagementObjectSearcher(query);

            foreach (ManagementBaseObject disk in mos.Get())
            {
                richTextBox1.Text += disk["Name"] + " " + disk["DriveType"] + " " + disk["VolumeName"] + "\n";
            }
            /*
            disk["DriveType"] 的返回值意義如下:
            1 No type
            2 Floppy disk
            3 Hard disk
            4 Removable drive or network drive
            5 CD-ROM
            6 RAM disk
            */

            //3、如何用WMI獲得指定磁盤的容量？	  TBD

            //"win32_logicaldisk.deviceid=/"c:/"");
            /*
            ManagementObject disk2 = new ManagementObject("win32_logicaldisk.deviceid=C://");
            disk2.Get();
            Console.WriteLine("Logical Disk Size = " + disk2["Size"] + " bytes");
            richTextBox1.Text += "Logical Disk Size = " + disk2["Size"] + " bytes\n";
            */

            ManagementClass diskClass = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection disks = diskClass.GetInstances();
            ManagementObjectCollection.ManagementObjectEnumerator disksEnumerator = disks.GetEnumerator();
            while (disksEnumerator.MoveNext())
            {
                ManagementObject disk = (ManagementObject)disksEnumerator.Current;
                richTextBox1.Text += "Disk found: " + disk["deviceid"] + "\n";
            }

            richTextBox1.Text += "列出機器中所有的共享資源\n";
            ManagementObjectSearcher searcher2 = new ManagementObjectSearcher("SELECT * FROM Win32_share");
            foreach (ManagementObject mo in searcher2.Get())
            {
                richTextBox1.Text += mo.GetText(TextFormat.Mof) + "\n";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //獲得CPU的編號
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += "獲得CPU的編號 :\n";
                richTextBox1.Text += mo["processorid"].ToString() + "\n";   //取得CPU編號
                richTextBox1.Text += "cpu info:\t" + mo.Properties["ProcessorId"].Value.ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得處理器參數
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "序號 :\t" + mo.GetPropertyValue("ProcessorId").ToString() + "\n";
                    richTextBox1.Text += mo["Manufacturer"].ToString() + "\n";//取得CPU製造商名稱
                    richTextBox1.Text += mo["Version"].ToString() + "\n";     //取得CPU版本號 
                    richTextBox1.Text += mo["Name"].ToString() + "\n";        //取得CPU產品名稱

                    richTextBox1.Text += "製造商 : " + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "序號 : " + mo.GetPropertyValue("ProcessorId").ToString() + "\n";
                    //ID[i] = mo.GetPropertyValue("Id").ToString(); not known

                    richTextBox1.Text += "CPU型號：" + (mo["ProcessorId"].ToString()) + "\n";
                    richTextBox1.Text += "CPU名稱：" + mo["Name"].ToString() + "\n";
                    richTextBox1.Text += "CPU版本信息：" + mo["Version"].ToString() + "\n";
                    richTextBox1.Text += "CPU製造廠商：" + mo["Manufacturer"].ToString() + "\n";

                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取CPU的序號\n";

            string result = GetCpuID1();
            richTextBox1.Text += result + "\n";


            richTextBox1.Text += "讀取CPU的序號\n";

            string CpuID = GetCpuID1();
            richTextBox1.Text += "CpuID\t" + CpuID + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取CPU的序號\n";

            //獲得cpu序號
            string cpu_serial = getCpu();
            richTextBox1.Text += "cpu序號 : " + cpu_serial + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取CPU的序號\n";

            ManagementClass mcCpu = new ManagementClass("win32_Processor");
            ManagementObjectCollection mocCpu = mcCpu.GetInstances();
            foreach (ManagementObject m in mocCpu)
            {
                string result1 = m["ProcessorId"].ToString();
                richTextBox1.Text += "取得 : " + result1 + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取CPU的序號\n";

            //取得CPU的型號
            GetCPUCode();

            //取得CPU的溫度
            //GetCPUTemperature();  溫度fail

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            int num_physical_processors, num_cores, num_logical_processors;
            GetProcessorCounts(out num_physical_processors, out num_cores, out num_logical_processors);

            richTextBox1.Text += "PhysicalProcessors\t" + num_physical_processors.ToString() + "\n";
            richTextBox1.Text += "Cores\t" + num_cores.ToString() + "\n";
            richTextBox1.Text += "LogicalProcessors\t" + num_logical_processors.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取CPU的序號\n";

            List<string> results = GetCpuIds();
            richTextBox1.Text += results.Count.ToString() + "\n";
            for (int i = 0; i < results.Count; i++)
            {
                richTextBox1.Text += results[i] + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取CPU序號\t" + GetCPUSerialNumber() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private List<string> GetCpuIds()
        {
            List<string> results = new List<string>();

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject mo in mos.Get())
            {
                results.Add(mo.GetPropertyValue("ProcessorId").ToString());
                richTextBox1.Text += "CPU ID:\t" + mo.GetPropertyValue("ProcessorId").ToString() + "\n";
            }
            return results;
        }

        //讀取CPU的序號
        private string GetCpuID1()
        {
            string cpuInfo = "";//cpu序號
            using (ManagementClass mc = new ManagementClass("Win32_Processor"))
            {
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    //cpuInfo = mo.Properties["ProcessorId"].Value.ToString();
                    cpuInfo += mo["ProcessorId"].ToString().Trim();
                    cpuInfo = mo.Properties["ProcessorId"].Value.ToString();   //取得CPU編號
                    //cpuInfo = mo["ProcessorId"].ToString();   //取得CPU編號  same
                }
            }
            return cpuInfo;
        }

        // Return the numbers of physical processors, cores,
        // and logical processors.
        private void GetProcessorCounts(out int num_physical_processors,
            out int num_cores, out int num_logical_processors)
        {
            ManagementObjectSearcher mos;

            // Get the number of physical processors.
            num_physical_processors = 0;
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_ComputerSystem");
            foreach (ManagementObject sys in mos.Get())
                num_physical_processors =
                    int.Parse(sys["NumberOfProcessors"].ToString());

            // Get the number of cores.
            num_cores = 0;
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject proc in mos.Get())
                num_cores += int.Parse(proc["NumberOfCores"].ToString());

            num_logical_processors = Environment.ProcessorCount;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取CPU編號\n";
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

            richTextBox1.Text += "讀取計算機CPU的當前電壓\n";
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

            richTextBox1.Text += "讀取計算機CPU的外部頻率\n";
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

            richTextBox1.Text += "讀取計算機CPU的二級緩存\n";
            MyInfo = "計算機CPU的二級緩存尺寸是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("L2CacheSize: " + MyObject["L2CacheSize"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "讀取計算機CPU的制造商名稱\n";
            MyInfo = "計算機CPU的制造商名稱是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("Manufacturer : " + MyObject["Manufacturer"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "讀取計算機CPU的產品名稱\n";
            MyInfo = "計算機CPU的產品名稱是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("Name : " + MyObject["Name"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "讀取計算機CPU的版本信息\n";
            MyInfo = "計算機CPU的版本信息如下：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("Version: " + MyObject["Version"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";

            richTextBox1.Text += "讀取計算機CPU的當前使用百分比 注意要把SQLserver或者其他耗CPU的軟件開著否則看不到效果就一直為0\n";
            MyInfo = "計算機CPU的當前使用百分比是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                //NG
                //MyInfo += "/n" + String.Format("LoadPercentage : " + MyObject["LoadPercentage"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "讀取計算機CPU的最大時鐘頻率\n";
            MyInfo = "計算機CPU的最大時鐘頻率是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("MaxClockSpeed : " + MyObject["MaxClockSpeed"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "讀取計算機CPU的當前時鐘頻率\n";
            MyInfo = "計算機CPU的當前時鐘頻率是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("CurrentClockSpeed : " + MyObject["CurrentClockSpeed"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "讀取計算機的CPU地址寬度\n";
            MyInfo = "當前計算機的CPU地址寬度是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("AddressWidth: " + MyObject["AddressWidth"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";


            richTextBox1.Text += "讀取計算機的CPU數據寬度\n";
            MyInfo = "當前計算機的CPU數據寬度是：";
            MySearcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            foreach (ManagementObject MyObject in MySearcher.Get())
            {
                MyInfo += "/n" + String.Format("DataWidth : " + MyObject["DataWidth"].ToString());
                MyInfo += "/n=========================================================";
            }
            richTextBox1.Text += MyInfo + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得網卡參數

            //取得本機MAC地址
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if (Convert.ToBoolean(mo["ipEnabled"]) == true)
                {
                    richTextBox1.Text += "取得本機MAC地址 : " + Convert.ToString(mo["MACAddress"]) + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "取得本機mac地址1\n";

            string mac = "";
            ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection moc = mc.GetInstances();

            foreach (ManagementObject mo in moc)
            {
                if ((bool)mo["IPEnabled"])
                {
                    mac = mo["MacAddress"].ToString();

                    richTextBox1.Text += "本機MAC：" + mac + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "取得本機mac地址2\n";

            string mac_address = "本機的MAC地址:";

            using (mc = new ManagementClass("Win32_NetworkAdapterConfiguration"))
            {
                moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    if ((bool)mo["IPEnabled"])
                    {
                        string[] tmpMac = mo["MacAddress"].ToString().Split(':');
                        for (int i = 0; i < tmpMac.Length; i++)
                        {
                            mac_address = tmpMac[i];
                            richTextBox1.Text += "取得MAC : " + mac_address + "\n";
                        }
                    }
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得設備網卡的MAC地址

            //ManagementClass mc;
            //ManagementObjectCollection moc;

            mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            moc = mc.GetInstances();
            string str = "";
            foreach (ManagementObject mo in moc)
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    str = mo["MacAddress"].ToString();
                }
            }
            richTextBox1.Text += "取得設備網卡的MAC地址 : " + str + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得網路卡參數
            ManagementClass mcMAC = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection mocMAC = mcMAC.GetInstances();
            foreach (ManagementObject mo in mocMAC)
            {
                if ((bool)mo["IPEnabled"])
                {
                    string result = mo["MacAddress"].ToString();
                    richTextBox1.Text += "取得 : " + result + "\n";
                    break;
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
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if ((bool)mo["IPEnabled"] == true)
                {
                    richTextBox1.Text += "取得本機的MAC地址：" + mo["MacAddress"].ToString() + "\n";
                    richTextBox1.Text += "IP " + mo["IpAddress"] + "\n";
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //C#.Net 使用WMI取得網路卡資訊
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
                richTextBox1.Text += String.Format("{0}{2}{1}{2}{2}", n.name, n.mac, Environment.NewLine);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "IP地址：" + getIPAddress() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string MacAddress = GetMacAddress();
            string IpAddress = GetIPAddress();
            richTextBox1.Text += "MacAddress\t" + MacAddress + "\n";
            richTextBox1.Text += "IpAddress\t" + IpAddress + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取網路卡位址\t" + GetNetCardMACAddress() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

        }

        private static string getIPAddress()
        {
            IPAddress addr;
            // 獲得本機局域網IP地址
            addr = new IPAddress(Dns.GetHostByName(Dns.GetHostName()).AddressList[0].Address);
            return addr.ToString();
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
            using (var mos = new ManagementObjectSearcher(@"SELECT * From Win32_USBHub"))
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

        private static string GetBIOSNumber()
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT SerialNumber FROM Win32_BIOS");
            string biosNumber = string.Empty;
            foreach (ManagementObject mo in mos.Get())
            {
                biosNumber += mo["SerialNumber"].ToString();
            }
            return biosNumber;
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //獲得主板序號
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
            int len = mos.Get().Count;
            string[] 序號 = new string[len];
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                序號[i] = mo.GetPropertyValue("SerialNumber").ToString();
                i++;
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //讀取主板序號
            string sn = GetBIOSNumber();
            richTextBox1.Text += "主板序號:\t" + sn + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得主機板序號
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
            len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "取得主機板序號 :\t" + mo.GetPropertyValue("SerialNumber").ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //獲得主板參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "製造商 : " + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "型號 : " + mo.GetPropertyValue("Product").ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得主機板參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "取得Product :\t" + mo.GetPropertyValue("Product").ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "\n讀取主機板資訊\n";
            richTextBox1.Text += "\nWin32_BaseBoard\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "主機板製造商：" + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "產品：" + mo["Product"].ToString() + "\n";
                richTextBox1.Text += "主機板序號：" + mo["SerialNumber"].ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // Board SerialNumber
            GetBoardSerialNumbers();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取主機板序號\t" + GetBIOSSerialNumber() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


        }

        // Use WMI to return the system's base board serial numbers.
        private List<string> GetBoardSerialNumbers()
        {
            List<string> results = new List<string>();

            ManagementObjectSearcher mos =
                new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            foreach (ManagementObject mo in mos.Get())
            {
                results.Add(mo.GetPropertyValue("SerialNumber").ToString());
                richTextBox1.Text += "Board SerialNumber:\t" + mo.GetPropertyValue("SerialNumber").ToString() + "\n";
            }
            return results;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //判斷驅動器類型
            richTextBox1.Text += "判斷驅動器類型\n";

            SelectQuery selectQuery = new SelectQuery("SELECT * FROM win32_logicaldisk");
            ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "取得驅動器 : " + mo["Name"].ToString() + "\t" + get_drive_type(mo["Name"].ToString()) + "\n";
            }
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
            //取得系統其他進程的啟動參數
            //使用WMI來查詢得到數據
            foreach (ManagementObject p in new ManagementObjectSearcher(new SelectQuery("SELECT * FROM Win32_Process")).Get())
            {
                richTextBox1.Text += p.Properties["commandLine"].Value + "\n";
            }
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
            string hdd_serial = GetDiskVolumeSerialNumber();
            richTextBox1.Text += "硬碟序號 : " + hdd_serial + "\n";

            //讀取硬碟相應分區的序號
            string Drive = "C";
            string result = GetSpecialVolumeSerialNumber(Drive);
            richTextBox1.Text += "讀取硬碟相應分區的序號 : " + result + "\n";

            //取得設備硬碟的卷標號
            richTextBox1.Text += "取得設備硬碟的卷標號 : " + GetDiskVolumeSerialNumber() + "\n";

            //讀取硬碟相應序號
            string result2 = GetSpecialVolumeSerialNumber2();
            richTextBox1.Text += "硬碟相應分區的序號 : " + result2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //用C#讀取硬碟序號

            ManagementClass mcHD = new ManagementClass("win32_logicaldisk");
            ManagementObjectCollection mocHD = mcHD.GetInstances();
            foreach (ManagementObject m in mocHD)
            {
                if (m["DeviceID"].ToString() == "C:")
                {
                    string result3 = m["VolumeSerialNumber"].ToString();
                    richTextBox1.Text += "取得 : " + result3 + "\n";
                    break;
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            /*
            richTextBox1.Text += "HDD信息:\n";

            //C#讀取硬碟信息
            ManagementClass mc = new ManagementClass("Win32_PhysicalMedia");
            ManagementObjectCollection moc = mc.GetInstances();
            foreach (ManagementObject mo in moc)
            {
                string cc = mo.Properties["SerialNumber"].Value.ToString();
                richTextBox1.Text += cc + "\n";
            }
            */
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得硬碟編號
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            String strHardDiskID = null;
            foreach (ManagementObject mo in mos.Get())
            {
                strHardDiskID = mo["SerialNumber"].ToString().Trim();
                break;
            }
            richTextBox1.Text += "硬碟編號 : " + strHardDiskID + "\n";

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

            ManagementObjectSearcher mosDisks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            // Loop through each object (disk) retrieved by WMI 

            foreach (ManagementObject moDisk in mosDisks.Get())
            {
                // Add the HDD to the list (use the Model field as the item's caption) 

                string diskname = moDisk["Model"].ToString();
                richTextBox1.Text += "取得 : " + diskname + "\n";
                get_detail_data(diskname);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "讀取硬碟序號\t" + GetHardDiskSerialNumber() + "\n";

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

            ManagementObjectSearcher mosDisks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive WHERE Model = '" + diskname + "'");

            // Loop through the drives retrieved, although it should normally be only one loop going on here 

            foreach (ManagementObject moDisk in mosDisks.Get())
            {
                // Set all the fields to the appropriate values 

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
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //取得磁盤配額
            try
            {
                ManagementClass mc1 = new ManagementClass("Win32_DiskQuota");
                ManagementObject quota = mc1.CreateInstance();
                quota["Limit"] = 400000000;
                quota["WarningLimit"] = 200000000;
                // Get user account object 
                ManagementObject account = new ManagementObject("Win32_Account.Domain=TODAY20040216,Name=ASPNET");
                account.Get();
                // get disk object 
                ManagementObject disk = new ManagementObject("Win32_LogicalDisk.DeviceId='D:'");
                disk.Get();
                quota["QuotaVolume"] = disk;
                quota["User"] = account;
                quota.Put(); // commit 

                ManagementClass mc2 = new ManagementClass("Win32_DiskQuota");
                Console.WriteLine(mc2.SystemProperties);
                richTextBox1.Text += "aaaa : " + mc2.SystemProperties + "\n";
                foreach (ManagementObject o in mc2.GetInstances())
                {
                    Console.WriteLine("Next : {0}", o.Path);
                    richTextBox1.Text += "Next : " + o.Path + "\n";
                }
            }
            catch (Exception ex)
            {
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //獲得硬碟空間
            ManagementClass diskClass = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection disks = diskClass.GetInstances();
            System.UInt64 space = UInt64.MinValue;
            foreach (ManagementObject disk in disks)
            {
                richTextBox1.Text += "磁碟 : " + (disk["Name"]).ToString() + "\n";
                if ((disk["Name"]).ToString() == "C:")
                {
                    space = (System.UInt64)(disk["FreeSpace"]);
                    richTextBox1.Text += "獲得硬碟空間 : " + space.ToString() + "\n";
                }
            }
        }

        /// <summary>
        /// 讀取硬碟相應分區的序號
        /// </summary>
        /// <param name="Drive">盤符（如 C）</param>
        /// <returns></returns>
        private string GetSpecialVolumeSerialNumber(string Drive)
        {
            string Dri = "";

            ManagementClass mo = new ManagementClass("Win32_LogicalDisk");

            ManagementObjectCollection mc = mo.GetInstances();

            foreach (ManagementObject m in mc)
            {
                if (Convert.ToString(m.Properties["DriveType"].Value) == "3")
                {
                    if (m.Properties["Name"].Value.ToString().ToUpper().Trim().Substring(0, 1) == Drive.ToUpper().Trim())
                    {
                        Dri = Dri + m.Properties["VolumeSerialNumber"].Value.ToString();

                        break;
                    }
                }
            }
            return Dri;
        }

        /// 讀取硬碟相應分區的序號
        private string GetSpecialVolumeSerialNumber2()
        {
            string Dri = "";

            ManagementClass mo = new ManagementClass("Win32_LogicalDisk");

            ManagementObjectCollection mc = mo.GetInstances();

            foreach (ManagementObject m in mc)
            {
                if (Convert.ToString(m.Properties["DriveType"].Value) == "3")
                {
                    Dri = Dri + m.Properties["VolumeSerialNumber"].Value.ToString() + "/n";
                }
            }
            Dri = Dri.Substring(0, Dri.Length - 1);
            return Dri;
        }

        //獲得CPU的序號
        public string getCpu()
        {
            string cpuInfo = "";//cpu序號
            ManagementClass myCpu = new ManagementClass("win32_Processor");
            ManagementObjectCollection myCpuConnection = myCpu.GetInstances();
            foreach (ManagementObject myObject in myCpuConnection)
            {
                cpuInfo = myObject.Properties["Processorid"].Value.ToString();
                break;
            }
            return cpuInfo;
        }

        //獲得硬碟的序號
        public string GetDiskVolumeSerialNumber()
        {
            ManagementObject disk = new ManagementObject("win32_logicaldisk.deviceid=\"c:\"");
            disk.Get();
            return disk.GetPropertyValue("VolumeSerialNumber").ToString();
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //查看了一下自己筆記本電池的剩餘時間
            //用WMI方式查看了一下自己筆記本電池的剩餘時間，結果得到了71582788分鐘這個結果，頓感意外，第一感覺是相關的代碼寫錯了。

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Battery");
            ManagementObjectCollection m = mos.Get();
            foreach (ManagementObject mo in m)
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
            ManagementObjectCollection moc = mc.GetInstances();

            ManagementObjectCollection.ManagementObjectEnumerator mom = moc.GetEnumerator();
            if (mom.MoveNext())
            {
                Console.WriteLine("EstimatedChargeRemaining: \t{0}%", mom.Current.Properties["EstimatedChargeRemaining"].Value);
                richTextBox1.Text += "EstimatedChargeRemaining: : " + mom.Current.Properties["EstimatedChargeRemaining"].Value + " %\n";
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //取得螢幕尺寸
            SystemInfo sysInfo = new SystemInfo();
            string id = sysInfo.GetMonitorPnpDeviceId()[0];
            SizeF size = sysInfo.GetMonitorPhysicalSize(id);
            richTextBox1.Text += SystemInfo.MonitorScaler(size).ToString() + " 吋\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得螢幕數量
            //检测已连接显示器
            richTextBox1.Text += "取得螢幕數量 :\n";

            // 获取屏幕数量
            string text = string.Empty;
            int count = 0;
            ManagementObjectSearcher mos = new ManagementObjectSearcher(@"root\wmi", "SELECT * FROM WmiMonitorID");
            foreach (ManagementObject mo in mos.Get())
            {
                text += mo.GetText(TextFormat.Mof);
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

            richTextBox1.Text += "\n聲卡PNPDeviceID\n";
            richTextBox1.Text += "\nWin32_SoundDevice\n";
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher("SELECT * FROM Win32_SoundDevice");
            foreach (ManagementObject mo in mos2.Get())
            {
                richTextBox1.Text += "聲卡PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
            // 抓取硬碟&USB儲存裝置磁碟代號
            using (ManagementClass devs = new ManagementClass(@"Win32_Diskdrive"))
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

        private void button20_Click(object sender, EventArgs e)
        {
            //用WMI取出作業系統資訊1
            //用WMI取出作業系統資訊
            get_wmi_os_info();
        }

        void get_wmi_os_info()
        {
            // Get and display OS properties.
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");

            foreach (ManagementObject mobj in mos.Get())
            {
                GetValue(mobj, "BootDevice");
                GetValue(mobj, "BuildNumber");
                GetValue(mobj, "BuildType");
                GetValue(mobj, "Caption");
                GetValue(mobj, "CodeSet");
                GetValue(mobj, "CountryCode");
                GetValue(mobj, "CreationClassName");
                GetValue(mobj, "CSCreationClassName");
                GetValue(mobj, "CSDVersion");
                GetValue(mobj, "CSName");
                GetValue(mobj, "CurrentTimeZone");
                GetValue(mobj, "DataExecutionPrevention_Available");
                GetValue(mobj, "DataExecutionPrevention_32BitApplications");
                GetValue(mobj, "DataExecutionPrevention_Drivers");
                GetValue(mobj, "DataExecutionPrevention_SupportPolicy");
                GetValue(mobj, "Debug");
                GetValue(mobj, "Description");
                GetValue(mobj, "Distributed");
                GetValue(mobj, "EncryptionLevel");
                GetValue(mobj, "ForegroundApplicationBoost");
                GetValue(mobj, "FreePhysicalMemory");
                GetValue(mobj, "FreeSpaceInPagingFiles");
                GetValue(mobj, "FreeVirtualMemory");
                GetValue(mobj, "InstallDate");
                GetValue(mobj, "LargeSystemCache");
                GetValue(mobj, "LastBootUpTime");
                GetValue(mobj, "LocalDateTime");
                GetValue(mobj, "Locale");
                GetValue(mobj, "Manufacturer");
                GetValue(mobj, "MaxNumberOfProcesses");
                GetValue(mobj, "MaxProcessMemorySize");
                GetValue(mobj, "MUILanguages[]");
                GetValue(mobj, "Name");
                GetValue(mobj, "NumberOfLicensedUsers");
                GetValue(mobj, "NumberOfProcesses");
                GetValue(mobj, "NumberOfUsers");
                GetValue(mobj, "OperatingSystemSKU");
                GetValue(mobj, "Organization");
                GetValue(mobj, "OSArchitecture");
                GetValue(mobj, "OSLanguage");
                GetValue(mobj, "OSProductSuite");
                GetValue(mobj, "OSType");
                GetValue(mobj, "OtherTypeDescription");
                GetValue(mobj, "PAEEnabled");
                GetValue(mobj, "PlusProductID");
                GetValue(mobj, "PlusVersionNumber");
                GetValue(mobj, "Primary");
                GetValue(mobj, "ProductType");
                GetValue(mobj, "QuantumLength");
                GetValue(mobj, "QuantumType");
                GetValue(mobj, "RegisteredUser");
                GetValue(mobj, "SerialNumber");
                GetValue(mobj, "ServicePackMajorVersion");
                GetValue(mobj, "ServicePackMinorVersion");
                GetValue(mobj, "SizeStoredInPagingFiles");
                GetValue(mobj, "Status");
                GetValue(mobj, "SuiteMask");
                GetValue(mobj, "SystemDevice");
                GetValue(mobj, "SystemDirectory");
                GetValue(mobj, "SystemDrive");
                GetValue(mobj, "TotalSwapSpaceSize");
                GetValue(mobj, "TotalVirtualMemorySize");
                GetValue(mobj, "TotalVisibleMemorySize");
                GetValue(mobj, "Version");
                GetValue(mobj, "WindowsDirectory");
            }
        }

        // Get a value from the ManagementObject.
        private void GetValue(ManagementObject mobj, string property_name)
        {
            string value;
            try
            {
                value = mobj[property_name].ToString();
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
            //用WMI取出作業系統資訊2
            // Display the operating system's name.
            // Get the OS information.
            // For more information from this query, see:
            //      http://msdn.microsoft.com/library/aa394239.aspx
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");
            foreach (ManagementObject mo in mos.Get())
            {
                //lblCaption.Text = mo.Properties["Caption"].Value.ToString().Trim();
                //lblVersion.Text = "Version " + mo.Properties["Version"].Value.ToString() + " SP " + mo.Properties["ServicePackMajorVersion"].Value.ToString() + "." + mo.Properties["ServicePackMinorVersion"].Value.ToString();

                richTextBox1.Text += mo.Properties["Caption"].Value.ToString().Trim() + "\n";
                richTextBox1.Text += "Version " + mo.Properties["Version"].Value.ToString() + " SP " + mo.Properties["ServicePackMajorVersion"].Value.ToString() + "." + mo.Properties["ServicePackMinorVersion"].Value.ToString() + "\n";
            }

            // Get number of processors.
            // For more information from this query, see:
            //      http://msdn.microsoft.com/library/aa394373.aspx
            string cpus_query = "SELECT * FROM Win32_ComputerSystem";
            ManagementObjectSearcher cpus_searcher = new ManagementObjectSearcher(cpus_query);
            foreach (ManagementObject mo in cpus_searcher.Get())
            {
                richTextBox1.Text += mo.Properties["NumberOfLogicalProcessors"].Value.ToString() + " processors" + "\n";
            }

            // Get 32- versus 64-bit.
            // For more information from this query, see:
            //      http://msdn.microsoft.com/library/aa394373.aspx
            string proc_query = "SELECT * FROM Win32_Processor";
            ManagementObjectSearcher proc_searcher = new ManagementObjectSearcher(proc_query);
            foreach (ManagementObject mo in proc_searcher.Get())
            {
                richTextBox1.Text += mo.Properties["AddressWidth"].Value.ToString() + "-bit" + "\n";
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //取得Windows版本
            string version = OSInfoMation.GetOsVersion();
            richTextBox1.Text += version + "\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //主機名稱
            richTextBox1.Text += "主機名稱 : " + Dns.GetHostName() + "\n";

            //取得電腦名稱
            string ComputerName = System.Environment.GetEnvironmentVariable("ComputerName");
            richTextBox1.Text += "ComputerName\t" + ComputerName + "\n";

            string LoginUserName = GetUserName();
            string SystemType = GetSystemType();
            string TotalPhysicalMemory = GetTotalPhysicalMemory(); //單位：M

            richTextBox1.Text += "LoginUserName\t" + LoginUserName + "\n";
            richTextBox1.Text += "SystemType\t" + SystemType + "\n";
            richTextBox1.Text += "TotalPhysicalMemory\t" + TotalPhysicalMemory + "\n";
        }

        //讀取網卡硬件地址
        public string GetMacAddress()
        {
            try
            {
                string mac = "";
                ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    if ((bool)mo["IPEnabled"] == true)
                    {
                        mac = mo["MacAddress"].ToString();
                        break;
                    }
                }
                moc = null;
                mc = null;
                return mac;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //讀取IP地址
        public string GetIPAddress()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    if ((bool)mo["IPEnabled"] == true)
                    {
                        //st=mo["IpAddress"].ToString();
                        System.Array ar;
                        ar = (System.Array)(mo.Properties["IpAddress"].Value);
                        st = ar.GetValue(0).ToString();
                        break;
                    }
                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //操作系統的登錄用戶名
        public string GetUserName()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_ComputerSystem");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {

                    st = mo["UserName"].ToString();

                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //PC類型
        public string GetSystemType()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_ComputerSystem");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    st = mo["SystemType"].ToString();
                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //物理內存
        public string GetTotalPhysicalMemory()
        {
            try
            {
                string st = "";
                ManagementClass mc = new ManagementClass("Win32_ComputerSystem");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    st = mo["TotalPhysicalMemory"].ToString();
                }
                moc = null;
                mc = null;
                return st;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        private void button24_Click(object sender, EventArgs e)
        {
        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        //讀取CPU序號
        public string GetCPUSerialNumber()
        {
            try
            {
                ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * From Win32_Processor");
                string sCPUSerialNumber = "";
                foreach (ManagementObject mo in mos.Get())
                {
                    sCPUSerialNumber = mo["ProcessorId"].ToString().Trim();
                    break;
                }
                return sCPUSerialNumber;
            }
            catch
            {
                return "";
            }
        }

        //讀取主機板序號
        public string GetBIOSSerialNumber()
        {
            try
            {
                ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * From Win32_BIOS");
                string sBIOSSerialNumber = "";
                foreach (ManagementObject mo in mos.Get())
                {
                    sBIOSSerialNumber = mo.GetPropertyValue("SerialNumber").ToString().Trim();
                    break;
                }
                return sBIOSSerialNumber;
            }
            catch
            {
                return "";
            }
        }

        //讀取硬碟序號
        public string GetHardDiskSerialNumber()
        {
            try
            {
                ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
                string sHardDiskSerialNumber = "";
                foreach (ManagementObject mo in mos.Get())
                {
                    sHardDiskSerialNumber = mo["SerialNumber"].ToString().Trim();
                    break;
                }
                return sHardDiskSerialNumber;
            }
            catch
            {
                return "";
            }
        }

        //讀取網路卡位址
        public string GetNetCardMACAddress()
        {
            try
            {
                ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter WHERE ((MACAddress Is Not NULL) AND (Manufacturer <> 'Microsoft'))");
                string NetCardMACAddress = "";
                foreach (ManagementObject mo in mos.Get())
                {
                    NetCardMACAddress = mo["MACAddress"].ToString().Trim();
                    break;
                }
                return NetCardMACAddress;
            }
            catch
            {
                return "";
            }
        }

        private void GetCPUCode()
        {
        }

        private void GetCPUTemperature()
        {
            double CPUtprt = 0;
            ManagementObjectSearcher mos = new ManagementObjectSearcher(@"root\WMI", "SELECT * FROM MSAcpi_ThermalZoneTemperature");

            foreach (ManagementObject mo in mos.Get())
            {
                CPUtprt = Convert.ToDouble(Convert.ToDouble(mo.GetPropertyValue("CrrentTemperature").ToString()) - 2732) / 10;
                richTextBox1.Text += "CPU温度：" + CPUtprt.ToString() + "°C\n";
            }
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
            //新進待測
            /*
            用C#和WMI讀取邏輯驅動器詳細信息
	
                SelectQuery selectQuery = new SelectQuery("win32_logicaldisk");
	
                  或者使用wql查詢來創建查詢類的實例，代碼如下：
	              SelectQuery selectQuery = new SelectQuery("SELECT * FROM win32_logicaldisk");
	
                  或者只讀取類的部分屬性，代碼如下：
	              SelectQuery selectQuery = new SelectQuery("SELECT Name,DriveType FROM win32_logicaldisk");
		
                SelectQuery selectQuery = new SelectQuery("SELECT * FROM win32_logicaldisk");
	
                ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
                  int i=0;
                foreach (ManagementObject disk in mos.Get()) {
                 //讀取驅動器盤符
                 listView1.Items.Add(disk["Name"].ToString());
                }
            */
        }
    }

    public class OSInfoMation
    {
        public static string OSBit()
        {
            try
            {
                ConnectionOptions oConn = new ConnectionOptions();
                ManagementScope managementScope = new ManagementScope("\\\\localhost", oConn);
                ObjectQuery objectQuery = new ObjectQuery("SELECT AddressWidth FROM Win32_Processor");
                ManagementObjectSearcher mos = new ManagementObjectSearcher(managementScope, objectQuery);
                ManagementObjectCollection moReturnCollection = null;
                string addressWidth = null;
                moReturnCollection = mos.Get();
                foreach (ManagementObject oReturn in moReturnCollection)
                {
                    addressWidth = oReturn["AddressWidth"].ToString();
                } //www.heatpress123.net
                return addressWidth;
            }
            catch
            {
                return "讀取錯誤";
            }
        }

        public static string GetOsVersion()
        {
            string osBitString = OSBit();
            string osVersionString = Environment.OSVersion.ToString();
            return string.Format(@"系統：{0}。位：{1}", osVersionString, osBitString);
        }
    }

    class SystemInfo
    {
        public virtual List<string> GetMonitorPnpDeviceId()
        {
            List<string> rt = new List<string>();
            using (ManagementClass mc = new ManagementClass("Win32_DesktopMonitor"))
            {
                using (ManagementObjectCollection moc = mc.GetInstances())
                {
                    foreach (var o in moc)
                    {
                        var each = (ManagementObject)o;
                        object obj = each.Properties["PNPDeviceID"].Value;
                        if (obj == null)
                            continue;

                        rt.Add(each.Properties["PNPDeviceID"].Value.ToString());
                    }
                }
            }

            return rt;
        }

        public virtual byte[] GetMonitorEdid(string monitorPnpDevId)
        {
            return (byte[])Registry.GetValue(@"HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Enum\" + monitorPnpDevId + @"\Device Parameters", "EDID", new byte[] { });
        }

        //获取显示器物理尺寸(cm)
        public virtual SizeF GetMonitorPhysicalSize(string monitorPnpDevId)
        {
            byte[] edid = GetMonitorEdid(monitorPnpDevId);
            if (edid.Length < 23)
                return SizeF.Empty;

            return new SizeF(edid[21], edid[22]);
        }

        //通过屏显示器理尺寸转换为显示器大小(inch)
        public static float MonitorScaler(SizeF moniPhySize)
        {
            double mDSize = Math.Sqrt(Math.Pow(moniPhySize.Width, 2) + Math.Pow(moniPhySize.Height, 2)) / 2.54d;
            return (float)Math.Round(mDSize, 1);
        }
    }
}


//6060
//------------------------------------------------------------  # 60個

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個

//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//richTextBox1.Text += "------------------------------\n";  // 30個
//richTextBox1.Text += "---------------\n";  // 15個


