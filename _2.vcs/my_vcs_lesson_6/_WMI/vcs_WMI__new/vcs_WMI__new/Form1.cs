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
            //獲得CPU的編號
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += "獲得CPU的編號 :\n";
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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "\ncall Processor() ST\n";
            Processor();
            richTextBox1.Text += "call Processor() SP\n";

            richTextBox1.Text += "\n獲取CPU的序號\n";

            string result = GetCpuID1();
            richTextBox1.Text += result + "\n";


            //獲得cpu序號
            string cpu_serial = getCpu();
            richTextBox1.Text += "cpu序號 : " + cpu_serial + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //CPU序號

            ManagementClass mcCpu = new ManagementClass("win32_Processor");
            ManagementObjectCollection mocCpu = mcCpu.GetInstances();
            foreach (ManagementObject m in mocCpu)
            {
                string result1 = m["ProcessorId"].ToString();
                richTextBox1.Text += "取得 : " + result1 + "\n";
            }


            richTextBox1.Text += "CPU信息: \t" + GetCpuID5() + "\n";

            //取得CPU的型號
            GetCPUCode();

            //取得CPU的溫度
            //GetCPUTemperature();  溫度fail

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得處理器參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            int len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "序號 :\t" + mo.GetPropertyValue("ProcessorId").ToString() + "\n";
                }
                catch (System.Exception er)
                {
                }
            }

        }

        //C# 獲得處理器參數程序代碼
        //public void Processor(out string[] Manufacturer, out string[] ID, out string[] ProcessorId)
        private void Processor()
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            int len = mos.Get().Count;
            string[] Manufacturer = new string[len];
            string[] ID = new string[len];
            string[] ProcessorId = new string[len];
            richTextBox1.Text += "count = " + len.ToString() + "\n";
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    Manufacturer[i] = mo.GetPropertyValue("Manufacturer").ToString();//製造商
                    //ID[i] = mo.GetPropertyValue("Id").ToString(); not known
                    ProcessorId[i] = mo.GetPropertyValue("ProcessorId").ToString();//序號

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

        //讀取CPU的序號
        private string GetCpuID1()
        {
            string cpuInfo = "";//cpu序號
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

        //讀取CPU的序號
        private string GetCpuID3()
        {
            string cpuInfo = "";//cpu序號
            using (ManagementClass mc = new ManagementClass("Win32_Processor"))
            {
                ManagementObjectCollection moc = mc.GetInstances();
                foreach (ManagementObject item in moc)
                {
                    cpuInfo += item["ProcessorId"].ToString().Trim();
                }
            }
            return cpuInfo + "\r\n";
        }

        //讀取CPU的序號
        private string GetCpuID4()
        {
            string cpuInfo = "";//cpu序號
            ManagementClass mc = new ManagementClass("Win32_Processor");
            ManagementObjectCollection moc = mc.GetInstances();
            foreach (ManagementObject mo in moc)
            {
                cpuInfo = mo.Properties["ProcessorId"].Value.ToString();
                break;
            }
            return cpuInfo;
        }

        //讀取CPU的序號
        private string GetCpuID5()
        {
            string cpuInfo = "";//cpu序號
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                cpuInfo = mo.Properties["ProcessorId"].Value.ToString();   //取得CPU編號
                //cpuInfo = mo["ProcessorId"].ToString();   //取得CPU編號  same
                return cpuInfo;
            }
            return "";
        }

        //讀取CPU的序號
        private string GetCpuID6()
        {
            string cpuInfo = "";//cpu序號
            using (ManagementClass cimobject = new ManagementClass("Win32_Processor"))
            {
                ManagementObjectCollection moc = cimobject.GetInstances();
                foreach (ManagementObject mo in moc)
                {
                    cpuInfo = mo.Properties["ProcessorId"].Value.ToString();
                    mo.Dispose();
                }
            }
            return cpuInfo.ToString();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //獲得處理器參數程序代碼

            string[] 制造商;
            string[] 型號;
            string[] 序號;

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            int len = mos.Get().Count;
            制造商 = new string[len];
            型號 = new string[len];
            序號 = new string[len];
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    制造商[i] = mo.GetPropertyValue("Manufacturer").ToString();
                    序號[i] = mo.GetPropertyValue("ProcessorId").ToString();

                    richTextBox1.Text += "制造商[" + i.ToString() + "] : " + 制造商[i].ToString() + "\n";
                    richTextBox1.Text += "序號[" + i.ToString() + "] : " + 序號[i].ToString() + "\n";
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


            //獲得網卡參數
            //NetworkAdapter

            //取得網路卡參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            int len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                    richTextBox1.Text += "MAC位址 :\t" + mo.GetPropertyValue("MACAddress").ToString() + "\n";
                }
                catch (System.Exception er)
                {
                }
            }

            //C# 獲得網卡參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            len = mos.Get().Count;
            string[] 制造商 = new string[len];
            string[] MAC地址 = new string[len];
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    制造商[i] = mo.GetPropertyValue("Manufacturer").ToString();
                    MAC地址[i] = mo.GetPropertyValue("MACAddress").ToString();
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }

            ManagementClass mcMAC = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection mocMAC = mcMAC.GetInstances();
            foreach (ManagementObject m in mocMAC)
            {
                if ((bool)m["IPEnabled"])
                {
                    string result = m["MacAddress"].ToString();
                    richTextBox1.Text += "取得 : " + result + "\n";
                    break;
                }
            }


            richTextBox1.Text += "IP地址：" + getIPAddress() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
        }

        private void button7_Click(object sender, EventArgs e)
        {
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

            //獲取主板序號
            //獲取主板序號
            string sn = GetBIOSNumber();
            richTextBox1.Text += "主板序號:\t" + sn + "\n";


            //取得主機板序號
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BIOS");
            len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "取得主機板序號 :\t" + mo.GetPropertyValue("SerialNumber").ToString() + "\n";
            }


            //獲得主板參數
            //Mainboard

            //取得主機板參數
            mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            len = mos.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "製造商 :\t" + mo.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "取得Product :\t" + mo.GetPropertyValue("Product").ToString() + "\n";
            }
        }

        //C# 獲得主板參數
        public static void Mainboard(out string[] 制造商, out string[] 型號)
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            int len = mos.Get().Count;
            制造商 = new string[len];
            型號 = new string[len];
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                制造商[i] = mo.GetPropertyValue("Manufacturer").ToString();
                型號[i] = mo.GetPropertyValue("Product").ToString();
                i++;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //判斷驅動器類型
            richTextBox1.Text += "判斷驅動器類型\n";

            SelectQuery selectQuery = new SelectQuery("SELECT * FROM win32_logicaldisk");
            ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject mo in mos.Get())
            {
                //comboBox1.Items.Add(mo["Name"].ToString());
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

            //------------------------------------------------------------  # 60個

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

            //獲取硬碟相應分區的序號
            string Drive = "C";
            string result = GetSpecialVolumeSerialNumber(Drive);
            richTextBox1.Text += "獲取硬碟相應分區的序號 : " + result + "\n";

            //取得設備硬碟的卷標號
            richTextBox1.Text += "取得設備硬碟的卷標號 : " + GetDiskVolumeSerialNumber() + "\n";

            //獲取硬碟相應序號
            string result2 = GetSpecialVolumeSerialNumber2();
            richTextBox1.Text += "硬碟相應分區的序號 : " + result2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //用C#獲取硬碟序號

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
                richTextBox1.Text += "error\n";
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
        /// 獲取硬碟相應分區的序號
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

        /// 獲取硬碟相應分區的序號
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
                richTextBox1.Text += "EstimatedChargeRemaining: : " + mom.Current.Properties["EstimatedChargeRemaining"].Value + " %\n";
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
        }

        private void button19_Click(object sender, EventArgs e)
        {

        }

        //取機器名 
        public string GetHostName()
        {
            return System.Net.Dns.GetHostName();
        }

        private void button20_Click(object sender, EventArgs e)
        {
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

        private void button23_Click(object sender, EventArgs e)
        {
            //主機名稱
            richTextBox1.Text += "主機名稱：" + Dns.GetHostName() + "\n";

            //獲取本機電腦名稱,IP,MAC地址

            string CpuID = GetCpuID1();
            string MacAddress = GetMacAddress();
            string IpAddress = GetIPAddress();
            string LoginUserName = GetUserName();
            string SystemType = GetSystemType();
            string TotalPhysicalMemory = GetTotalPhysicalMemory(); //單位：M

            //取得電腦名稱
            string ComputerName = System.Environment.GetEnvironmentVariable("ComputerName");

            richTextBox1.Text += "CpuID\t" + CpuID + "\n";
            richTextBox1.Text += "MacAddress\t" + MacAddress + "\n";
            richTextBox1.Text += "IpAddress\t" + IpAddress + "\n";
            richTextBox1.Text += "LoginUserName\t" + LoginUserName + "\n";
            richTextBox1.Text += "SystemType\t" + SystemType + "\n";
            richTextBox1.Text += "TotalPhysicalMemory\t" + TotalPhysicalMemory + "\n";
            richTextBox1.Text += "ComputerName\t" + ComputerName + "\n";
        }

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
            //取得螢幕數量
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

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void GetCPUCode()
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "CPU型號：" + (mo["ProcessorId"].ToString()) + "\n";
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
        }

        private void button28_Click(object sender, EventArgs e)
        {

        }

        private void button29_Click(object sender, EventArgs e)
        {
            //新進待測
            /*
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


