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
using System.Management;    //for WMI
using Microsoft.Win32;  //for Registry

// WMI(Windows Management Instrumentation)
// 1. 專案->參考->右鍵->加入參考->.NET->選System.Management->確定
// 2. using System.Management;

//參考 / 加入參考 / .NET  System.Management
using System.Management;

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
            ManagementObjectSearcher mos3 = new ManagementObjectSearcher(strQry);
            // 使用Foreach 陳述式存取集合類別中物件(元素), Get 方法, 叫用指定的WMI 查詢, 並傳回產生的集合。
            foreach (ManagementObject mo3 in mos3.Get())
            {
                // 取得磁碟Volumne 名稱跟序號
                richTextBox1.Text += mo3["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo3["VolumeSerialNumber"] + "\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
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
        }

        private void button2_Click(object sender, EventArgs e)
        {
            /*
            //獲得CPU的編號
            ManagementClass mc = new ManagementClass("win32_processor");
            ManagementObjectCollection moc = mc.GetInstances();
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += "獲得CPU的編號 : " + mo["processorid"].ToString() + "\n";
            }
            */
            
            //獲得CPU的編號
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += mo["processorid"].ToString() + "\n";   //取得CPU編號
                richTextBox1.Text += "cpu info:\t" + mo.Properties["ProcessorId"].Value.ToString() + "\n";
            }

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor"); //查詢CPU訊息
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += mo["Manufacturer"].ToString() + "\n";//取得CPU製造商名稱
                richTextBox1.Text += mo["Version"].ToString() + "\n";     //取得CPU版本號 
                richTextBox1.Text += mo["Name"].ToString() + "\n";        //取得CPU產品名稱
            }

            richTextBox1.Text += "\ncall Processor() ST\n";
            Processor();
            richTextBox1.Text += "call Processor() SP\n";

            richTextBox1.Text += "\n獲取CPU的序列號\n";
            string result = GetCpuID();
            richTextBox1.Text += result + "\n";
        }

        //C# 獲得處理器參數程序代碼
        //public void Processor(out string[] Manufacturer, out string[] ID, out string[] ProcessorId)
        public void Processor()
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            string[] Manufacturer = new string[mos.Get().Count];
            string[] ID = new string[mos.Get().Count];
            string[] ProcessorId = new string[mos.Get().Count];
            richTextBox1.Text += "count = " + mos.Get().Count.ToString() + "\n";
            int i = 0;
            foreach (ManagementObject share in mos.Get())
            {
                try
                {
                    Manufacturer[i] = share.GetPropertyValue("Manufacturer").ToString();
                    //ID[i] = share.GetPropertyValue("Id").ToString(); not known
                    ProcessorId[i] = share.GetPropertyValue("ProcessorId").ToString();

                    richTextBox1.Text += "i = " + i.ToString() + "\n";
                    richTextBox1.Text += "Manufacturer : " + Manufacturer[i] + "\n";
                    richTextBox1.Text += "ProcessorId : " + ProcessorId[i] + "\n";

                }
                catch (System.Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }

        //獲取CPU的序列號
        private string GetCpuID()
        {
            try
            {
                //獲取CPU序列號代碼
                string cpuInfo = "";//cpu序列號
                ManagementClass mc = new ManagementClass("Win32_Processor");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    cpuInfo = mo.Properties["ProcessorId"].Value.ToString();
                }
                moc = null;
                mc = null;
                return cpuInfo;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //C#讀取計算機CPU信息
        public string getCpuInfo() //讀取CPU信息
        {
            //獲得CPU訊息
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                return mo.Properties["ProcessorId"].Value.ToString();   //取得CPU編號
                //return mo["ProcessorId"].ToString();   //取得CPU編號  same
            }
            return "";
        }

        //C#讀取計算機HDD信息
        public string getHddInfo() //讀取硬盤信息
        {
            ManagementClass mc = new ManagementClass("Win32_PhysicalMedia");
            ManagementObjectCollection moc = mc.GetInstances();
            foreach (ManagementObject mo in moc)
            {
                return mo.Properties["SerialNumber"].Value.ToString();
            }
            return "";
        }



        private void button3_Click(object sender, EventArgs e)
        {
            //獲得處理器參數程序代碼
            get_ProcessorInfo();
        }

        void get_ProcessorInfo()
        {
            string[] 制造商;
            string[] 型號;
            string[] 序列號;

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            制造商 = new string[mos.Get().Count];
            型號 = new string[mos.Get().Count];
            序列號 = new string[mos.Get().Count];
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    制造商[i] = mo.GetPropertyValue("Manufacturer").ToString();
                    序列號[i] = mo.GetPropertyValue("ProcessorId").ToString();

                    richTextBox1.Text += "制造商[" + i.ToString() + "] : " + 制造商[i].ToString() + "\n";
                    richTextBox1.Text += "序列號[" + i.ToString() + "] : " + 序列號[i].ToString() + "\n";
                }
                catch (System.Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //獲得硬盤空間
            richTextBox1.Text += "獲得硬盤空間 : " + GetDiskSpace() + "\n";
        }

        //獲得硬盤空間
        public System.UInt64 GetDiskSpace()
        {
            ManagementClass diskClass = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection disks = diskClass.GetInstances();
            System.UInt64 space = UInt64.MinValue;
            foreach (ManagementObject disk in disks)
            {
                if ((disk["Name"]).ToString() == "C:")
                    space = (System.UInt64)(disk["FreeSpace"]);
            }
            return space;
        }


        private void button5_Click(object sender, EventArgs e)
        {
            //取得本機MAC地址
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if (Convert.ToBoolean(mo["ipEnabled"]) == true)
                {
                    richTextBox1.Text += "取得本機MAC地址 : " + Convert.ToString(mo["MACAddress"]) + "\n";
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得設備網卡的MAC地址
            //取得設備網卡的MAC地址
            richTextBox1.Text += "取得設備網卡的MAC地址 : " + GetNetCardMacAddress() + "\n";
        }

        ///
        /// 取得設備網卡的MAC地址
        ///
        public string GetNetCardMacAddress()
        {
            ManagementClass mc;
            ManagementObjectCollection moc;

            mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            moc = mc.GetInstances();
            string str = "";
            foreach (ManagementObject mo in moc)
            {
                if ((bool)mo["IPEnabled"] == true)
                    str = mo["MacAddress"].ToString();
            }
            return str;

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //獲得網卡參數
            //NetworkAdapter

            //取得網路卡參數
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            int len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject share in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "取得製造商 :\t" + share.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "取得MAC位址 :\t" + share.GetPropertyValue("MACAddress").ToString() + "\n";
                }
                catch (System.Exception er)
                {
                }
            }
        }

        //C# 獲得網卡參數程序代碼如下：
        public void NetworkAdapter(out string[] 制造商, out string[] MAC地址)
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            制造商 = new string[mos.Get().Count];
            MAC地址 = new string[mos.Get().Count];
            int i = 0;
            foreach (ManagementObject share in mos.Get())
            {
                try
                {
                    制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                    MAC地址[i] = share.GetPropertyValue("MACAddress").ToString();
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }


        private void button8_Click(object sender, EventArgs e)
        {
            //獲得主板序列號
            //MainboardSerialNumber


            //獲取主板序列號
            //獲取主板序列號
            string sn = GetBIOSNumber();
            richTextBox1.Text += "主板序列號:\t" + sn + "\n";


            //取得主機板序號
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");

            int len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in mos.Get())
            {
                richTextBox1.Text += "取得主機板序號 :\t" + share.GetPropertyValue("SerialNumber").ToString() + "\n";
            }

        }

        private static string GetBIOSNumber()
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT SerialNumber FROM Win32_BIOS");
            string biosNumber = string.Empty;
            foreach (ManagementObject mgt in mos.Get())
            {
                biosNumber += mgt["SerialNumber"].ToString();
            }
            return biosNumber;
        }

        //C# 獲得主板序列號程序代碼如下：
        public static void MainboardSerialNumber(out string[] 序列號)
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
            序列號 = new string[mos.Get().Count];
            int i = 0;
            foreach (ManagementObject share in mos.Get())
            {
                序列號[i] = share.GetPropertyValue("SerialNumber").ToString();
                i++;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //獲得主板參數
            //Mainboard


            //取得主機板參數
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            int len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in mos.Get())
            {
                richTextBox1.Text += "取得Manufacturer :\t" + share.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "取得Product :\t" + share.GetPropertyValue("Product").ToString() + "\n";
            }
        }

        //C# 獲得主板參數程序代碼如下：
        public static void Mainboard(out string[] 制造商, out string[] 型號)
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            制造商 = new string[mos.Get().Count];
            型號 = new string[mos.Get().Count];
            int i = 0;
            foreach (ManagementObject share in mos.Get())
            {
                制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                型號[i] = share.GetPropertyValue("Product").ToString();
                i++;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //判斷驅動器類型
            richTextBox1.Text += "判斷驅動器類型\n";

            SelectQuery selectQuery = new SelectQuery("SELECT * FROM win32_logicaldisk");
            ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject disk in mos.Get())
            {
                //comboBox1.Items.Add(disk["Name"].ToString());
                richTextBox1.Text += "取得驅動器 : " + disk["Name"].ToString() + "\t" + get_drive_type(disk["Name"].ToString()) + "\n";
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
                        type = "這是硬盤";
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

            //取得硬碟參數
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            int len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "取得製造商 :\t" + share.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "取得型號 :\t" + share.GetPropertyValue("Model").ToString() + "\n";
                    richTextBox1.Text += "取得序列號 :\t" + share.GetPropertyValue("Signature").ToString() + "\n";
                }
                catch (System.Exception er)
                {
                }
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "本機硬碟資訊\n";
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject info in mos.Get())
            {
                richTextBox1.Text += "---------------------------------------------------\n";
                richTextBox1.Text += "DeviceID: " + info["DeviceID"].ToString() + "\n";
                richTextBox1.Text += "Model: " + info["Model"].ToString() + "\n";
                richTextBox1.Text += "Interface: " + info["InterfaceType"].ToString() + "\n";
                richTextBox1.Text += "Serial#: " + info["SerialNumber"].ToString() + "\n";
            }
            richTextBox1.Text += "---------------------------------------------------\n";


            //HardDisk()


            richTextBox1.Text += "---------------------------------------------------\n";

            //GetHardID()

            richTextBox1.Text += "---------------------------------------------------\n";

            //讀取U盤序列號
            _serialNumber.Clear();
            matchDriveLetterWithSerial();
            richTextBox1.Text += "len = " + _serialNumber.Count.ToString() + "\n";

            len = _serialNumber.Count;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "取得序號 : " + _serialNumber[i] + "\n";
            }
        }

        //讀取硬盤序列號
        private List<string> _serialNumber = new List<string>();

        /// <summary>
        /// 調用這個函數將本機所有U盤序列號存儲到_serialNumber中
        /// </summary>
        private void matchDriveLetterWithSerial()
        {
            string[] diskArray;
            string driveNumber;
            var mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDiskToPartition");
            foreach (ManagementObject dm in mos.Get())
            {
                richTextBox1.Text += "A\n";
                getValueInQuotes(dm["Dependent"].ToString());
                diskArray = getValueInQuotes(dm["Antecedent"].ToString()).Split(',');
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



        //C# 獲得硬盤參數程序代碼如下：
        public void HardDisk(out string[] 制造商, out string[] 型號, out string[] 序列號)
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            制造商 = new string[mos.Get().Count];
            型號 = new string[mos.Get().Count];
            序列號 = new string[mos.Get().Count];
            int i = 0;
            foreach (ManagementObject share in mos.Get())
            {
                try
                {
                    制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                    型號[i] = share.GetPropertyValue("Model").ToString();
                    序列號[i] = share.GetPropertyValue("Signature").ToString();
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }

        /// <summary>
        /// 獲取本機硬盤序列號
        /// </summary>
        /// <returns></returns>
        private string GetHardID()
        {
            string HardID = "本機的CPU序列號:";
            using (ManagementClass mc = new ManagementClass("Win32_DiskDrive"))
            {
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject item in moc)
                {
                    HardID += item["Model"].ToString().Trim();
                }
            }
            return HardID + "\r\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //取得設備硬盤的卷標號

            //取得設備硬盤的卷標號
            richTextBox1.Text += "取得設備硬盤的卷標號 : " + GetDiskVolumeSerialNumber2() + "\n";
        }

        ///
        /// 取得設備硬盤的卷標號
        ///
        ///
        public string GetDiskVolumeSerialNumber2()
        {
            ManagementClass mc;
            ManagementObject disk;
            mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            disk = new ManagementObject("win32_logicaldisk.deviceid=\"c:\"");
            disk.Get();
            return disk.GetPropertyValue("VolumeSerialNumber").ToString();
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //獲得cpu序列號和硬盤序列號
            //獲得cpu序列號和硬盤序列號
            string cpu_serial = string.Empty;
            string hdd_serial = string.Empty;
            cpu_serial = GetDiskVolumeSerialNumber();
            hdd_serial = getCpu();
            richTextBox1.Text += "cpu序列號 : " + cpu_serial + "\n";
            richTextBox1.Text += "硬盤序列號 : " + hdd_serial + "\n";
        }

        //獲得CPU的序列號
        public string getCpu()
        {
            string strCpu = null;
            ManagementClass myCpu = new ManagementClass("win32_Processor");
            ManagementObjectCollection myCpuConnection = myCpu.GetInstances();
            foreach (ManagementObject myObject in myCpuConnection)
            {
                strCpu = myObject.Properties["Processorid"].Value.ToString();
                break;
            }
            return strCpu;
        }

        //獲得硬盤的序列號
        public string GetDiskVolumeSerialNumber()
        {
            ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
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
            c#，使用WMI對象獲取筆記本電池剩余電量的百分比

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
            }

        }

        private void button16_Click(object sender, EventArgs e)
        {
            //取得Windows版本
            string version = OSInfoMation.GetOsVersion();
            richTextBox1.Text += version + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //取得螢幕尺寸
            SystemInfo sysInfo = new SystemInfo();
            string id = sysInfo.GetMonitorPnpDeviceId()[0];
            SizeF size = sysInfo.GetMonitorPhysicalSize(id);
            richTextBox1.Text += SystemInfo.MonitorScaler(size).ToString() + " 吋\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //獲取硬盤相應序列號
            string result = clsIDE.GetAllSerialNumber();
            richTextBox1.Text += "獲取硬盤序列號 : " + result + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //用C#獲取硬盤序列號,CPU序列號,網卡MAC地址
            //用C#獲取硬盤序列號,CPU序列號,網卡MAC地址
            string[] str = new string[3];
            ManagementClass mcCpu = new ManagementClass("win32_Processor");
            ManagementObjectCollection mocCpu = mcCpu.GetInstances();
            foreach (ManagementObject m in mocCpu)
            {
                str[0] = m["ProcessorId"].ToString();
            }

            ManagementClass mcHD = new ManagementClass("win32_logicaldisk");
            ManagementObjectCollection mocHD = mcHD.GetInstances();
            foreach (ManagementObject m in mocHD)
            {
                if (m["DeviceID"].ToString() == "C:")
                {
                    str[1] = m["VolumeSerialNumber"].ToString();
                    break;
                }
            }

            ManagementClass mcMAC = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection mocMAC = mcMAC.GetInstances();
            foreach (ManagementObject m in mocMAC)
            {
                if ((bool)m["IPEnabled"])
                {
                    str[2] = m["MacAddress"].ToString();
                    break;
                }
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //主機名稱/IP/MAC
            //主機名稱/IP/MAC
            richTextBox1.Text += "主機名稱：" + Dns.GetHostName() + "\n";

            richTextBox1.Text += "IP地址：" + getIPAddress() + "\n";


            //本機mac地址

            string mac = "";
            ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection moc = mc.GetInstances();

            foreach (ManagementObject mo in moc)
            {
                if ((bool)mo["IPEnabled"])
                {
                    mac = mo["MacAddress"].ToString();

                    //本機MAC
                    richTextBox1.Text += "本機MAC：" + mac + "\n";
                }
            }
        }

        private static string getIPAddress()
        {
            IPAddress addr;
            // 獲得本機局域網IP地址
            addr = new IPAddress(Dns.GetHostByName(Dns.GetHostName()).AddressList[0].Address);
            return addr.ToString();
        }

        private void button21_Click(object sender, EventArgs e)
        {
            //取得處理器參數
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            int len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "取得製造商 :\t" + share.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "取得序列號 :\t" + share.GetPropertyValue("ProcessorId").ToString() + "\n";
                }
                catch (System.Exception er)
                {
                }
            }
        }

        private void button22_Click(object sender, EventArgs e)
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
            foreach (ManagementObject share in searcher2.Get())
            {
                richTextBox1.Text += share.GetText(TextFormat.Mof) + "\n";
            }
        }

        private void button23_Click(object sender, EventArgs e)
        {
            //獲取本機電腦名稱,IP,MAC地址,硬碟ID
            //獲取本機電腦名稱,IP,MAC地址,硬碟ID
            //獲取本機電腦名稱,IP,MAC地址,硬碟ID

            string CpuID;
            string MacAddress;
            string DiskID;
            string IpAddress;
            string LoginUserName;
            string ComputerName;
            string SystemType;
            string TotalPhysicalMemory; //單位：M

            CpuID = GetCpuID2();
            MacAddress = GetMacAddress();
            DiskID = GetDiskID();
            IpAddress = GetIPAddress();
            LoginUserName = GetUserName();
            SystemType = GetSystemType();
            TotalPhysicalMemory = GetTotalPhysicalMemory();
            ComputerName = GetComputerName();

            richTextBox1.Text += "CpuID\t" + CpuID + "\n";
            richTextBox1.Text += "MacAddress\t" + MacAddress + "\n";
            richTextBox1.Text += "DiskID\t" + DiskID + "\n";
            richTextBox1.Text += "IpAddress\t" + IpAddress + "\n";
            richTextBox1.Text += "LoginUserName\t" + LoginUserName + "\n";
            richTextBox1.Text += "SystemType\t" + SystemType + "\n";
            richTextBox1.Text += "TotalPhysicalMemory\t" + TotalPhysicalMemory + "\n";
            richTextBox1.Text += "ComputerName\t" + ComputerName + "\n";
        }

        //獲取CPU序列號
        public string GetCpuID2()
        {
            try
            {
                string cpuInfo = "";
                ManagementClass mc = new ManagementClass("Win32_Processor");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    cpuInfo = mo.Properties["ProcessorId"].Value.ToString();
                }
                moc = null;
                mc = null;
                return cpuInfo;
            }
            catch
            {
                return "unknow";
            }
            finally
            {
            }
        }

        //獲取網卡硬件地址
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

        //獲取IP地址
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

        //獲取硬盤ID
        public string GetDiskID()
        {
            try
            {
                String HDid = "";
                ManagementClass mc = new ManagementClass("Win32_DiskDrive");
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    HDid = (string)mo.Properties["Model"].Value;
                }
                moc = null;
                mc = null;
                return HDid;
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

        //電腦名稱
        public string GetComputerName()
        {
            try
            {
                return System.Environment.GetEnvironmentVariable("ComputerName");
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
            //取得螢幕數量
            //取得螢幕數量
            //检测已连接显示器
            richTextBox1.Text += "取得螢幕數量 : " + GetMonitorCount().ToString() + "\n";
        }

        /// <summary>
        /// 获取屏幕数量
        /// </summary>
        /// <returns></returns>
        public int GetMonitorCount()
        {
            string text = string.Empty;
            int count = 0;
            ManagementObjectSearcher mos = new ManagementObjectSearcher(@"root\wmi", "SELECT * FROM WmiMonitorID");
            foreach (ManagementObject mo in mos.Get())
            {
                text += mo.GetText(TextFormat.Mof);
                count++;
            }
            return count;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "CPU信息: \t" + getCpuInfo() + "\n";
            richTextBox1.Text += "HDD信息: \t" + getHddInfo() + "\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //取得CPU的型號和溫度
            //取得CPU的型號和溫度
            GetCPUCode();
            //GetCPUTemperature();  溫度fail
        }

        private void GetCPUCode()
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");

            foreach (ManagementObject mObject in mos.Get())
            {
                richTextBox1.Text += "CPU型號：" + (mObject["ProcessorId"].ToString()) + "\n";
            }
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
            //取得磁盤配額
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
                foreach (ManagementObject o in mc2.GetInstances())
                {
                    Console.WriteLine("Next : {0}", o.Path);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("error:" + ex);
            }
        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {
            //新進待測
            /*
                 //C#獲取本機的MAC地址\序列號\硬盤序列號

            /// <summary>
                  /// 顯示MAC地址
                  /// </summary>
                  /// <returns></returns>
                  private string GetMAC()
                  {
                      string mac = "本機的MAC地址:";
                      using (ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration"))
                      {
                          ManagementObjectCollection moc = mc.GetInstances();
                          foreach (ManagementObject mo in moc)
                          {
                              if ((bool)mo["IPEnabled"])
                              {
                                  string[] tmpMac = mo["MacAddress"].ToString().Split(':');
                                  for (int i = 0; i < tmpMac.Length; i++)
                                  {
                                      mac += tmpMac[i];
                                  }
                              }
                          }
                      }
                      return mac + "\r\n";
                  }

                  /// <summary>
                  /// 獲取本機CPU序列號  
                  /// </summary>
                  /// <returns></returns>
                  private string GetCPUID()
                  {
                      string CPUID = "本機的CPU序列號:";
                      using (ManagementClass mc = new ManagementClass("Win32_Processor"))
                      {
                          ManagementObjectCollection moc = mc.GetInstances();
                          foreach (ManagementObject item in moc)
                          {
                              CPUID += item["ProcessorId"].ToString().Trim();
                          }
                      }
                      return CPUID + "\r\n";
                  }


            //C#獲取機器碼

            1 /// <summary>   
             2     /// 機器碼   
             3     /// </summary>   
             4    public class MachineCode   
             5     {   
             6         ///   <summary>    
             7         ///   獲取cpu序列號        
             8         ///   </summary>    
             9         ///   <returns> string </returns>    
            10         public string GetCpuInfo()   
            11         {   
            12             string cpuInfo = " ";   
            13             using (ManagementClass cimobject = new ManagementClass("Win32_Processor"))   
            14             {   
            15                 ManagementObjectCollection moc = cimobject.GetInstances();   
            16   
            17                 foreach (ManagementObject mo in moc)   
            18                 {   
            19                     cpuInfo = mo.Properties["ProcessorId"].Value.ToString();   
            20                     mo.Dispose();   
            21                 }   
            22             }   
            23             return cpuInfo.ToString();   
            24         }   
            25   



            C#如何取硬件標志

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

                String strCpuID = null ;
                foreach( ManagementObject mo in moc ) 
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
                ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
                String strHardDiskID = null ;
                foreach(ManagementObject mo in mos.Get()) 
                {    
                 strHardDiskID = mo["SerialNumber"].ToString().Trim();
                 break;          
                }
                return strHardDiskID ;
               }
               catch
               {
                return "";
               }
              }//end 


            用C#和WMI獲取邏輯驅動器詳細信息
	
                SelectQuery selectQuery = new SelectQuery("win32_logicaldisk");
	
                  或者使用wql查詢來創建查詢類的實例，代碼如下：
	
                SelectQuery selectQuery = new SelectQuery("SELECT * FROM win32_logicaldisk");
	
                  或者只獲取類的部分屬性，代碼如下：
	
                SelectQuery selectQuery = new SelectQuery("SELECT Name,DriveType FROM win32_logicaldisk");
	
	
                SelectQuery selectQuery = new SelectQuery("SELECT * FROM win32_logicaldisk");
	
                ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
                  int i=0;
                foreach (ManagementObject disk in mos.Get()) {
                 //獲取驅動器盤符
                 listView1.Items.Add(disk["Name"].ToString());
                }


            C# 獲得主板參數程序代碼
            public static void Mainboard(out string[] 制造商, out string[] 型號)
            {
                    ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
                    制造商 = new string[mos.Get().Count];
                    型號 = new string[mos.Get().Count];
                    int i = 0;
                    foreach (ManagementObject share in mos.Get())
                    {
                            制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                            型號[i] = share.GetPropertyValue("Product").ToString();
                            i ;
                    }
            } 


            C# 獲得主板序列號程序代碼

            C# 獲得主板序列號程序代碼如下：
            public static void MainboardSerialNumber(out string[] 序列號)
            {
                    ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
                    序列號 = new string[mos.Get().Count];
                    int i = 0;
                    foreach (ManagementObject share in mos.Get())
                    {
                            序列號[i] = share.GetPropertyValue("SerialNumber").ToString();
                            i ;
                    }
            }


            C# 獲得網卡參數程序代碼

            C# 獲得網卡參數程序代碼如下：
            public static void NetworkAdapter(out string[] 制造商, out string[] MAC地址)
            {
                    ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
                    制造商 = new string[mos.Get().Count];
                    MAC地址 = new string[mos.Get().Count];
                    int i = 0;
                    foreach (ManagementObject share in mos.Get())
                    {
                            try
                            {
                                    制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                                    MAC地址[i] = share.GetPropertyValue("MACAddress").ToString();
                            }
                                    catch (System.Exception er)
                            {
                            }
                            i ;
                    }
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
                return "獲取錯誤";
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



    /// <summary>
    /// Summary description for clsIDE.
    /// </summary>
    public class clsIDE
    {
        /// <summary>
        /// 獲取硬盤相應分區的序列號
        /// </summary>
        /// <returns></returns>
        public static string GetAllSerialNumber()
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

        /// <summary>
        /// 獲取硬盤相應分區的序列號
        /// </summary>
        /// <param name="Drive">盤符（如 C）</param>
        /// <returns></returns>
        public static string GetSpecialVolumeSerialNumber(string Drive)
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
    }
}


//6060
//------------------------------------------------------------  # 60個

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個


