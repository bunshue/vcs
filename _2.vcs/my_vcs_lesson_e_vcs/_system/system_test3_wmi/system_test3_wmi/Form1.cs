using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;       //for Dns
using System.Management;
using Microsoft.Win32;  //for Registry

//WMI是Windows Management Instrumentation的簡稱，即：視窗管理規范。

namespace system_test3_wmi
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
            x_st = 15;
            y_st = 15;
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            button16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //獲取主板序列號
            string sn = GetBIOSNumber();
            richTextBox1.Text += "主板序列號:\t" + sn + "\n";
        }

        private static string GetBIOSNumber()
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select SerialNumber From Win32_BIOS");
            string biosNumber = string.Empty;
            foreach (ManagementObject mgt in searcher.Get())
            {
                biosNumber += mgt["SerialNumber"].ToString();
            }
            return biosNumber;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //獲得CPU的編號
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息
            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += mo["processorid"].ToString() + "\n";   //取得CPU編號
                richTextBox1.Text += "cpu info:\t" + mo.Properties["ProcessorId"].Value.ToString() + "\n";
            }

            ManagementObjectSearcher mos = new ManagementObjectSearcher("Select * From Win32_Processor"); //查詢CPU訊息
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
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            string[] Manufacturer = new string[searcher.Get().Count];
            string[] ID = new string[searcher.Get().Count];
            string[] ProcessorId = new string[searcher.Get().Count];
            richTextBox1.Text += "count = " + searcher.Get().Count.ToString() + "\n";
            int i = 0;
            foreach (ManagementObject share in searcher.Get())
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


        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "CPU信息: \t" + getCpuInfo() + "\n";
            richTextBox1.Text += "HDD信息: \t" + getHddInfo() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得CPU的型號和溫度
            GetCPUCode();
            //GetCPUTemperature();  溫度fail
        }

        private void GetCPUCode()
        {
            ManagementObjectSearcher moSearch = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");

            foreach (ManagementObject mObject in moSearch.Get())
            {
                richTextBox1.Text += "CPU型號：" + (mObject["ProcessorId"].ToString()) + "\n";
            }
        }

        private void GetCPUTemperature()
        {
            double CPUtprt = 0;
            System.Management.ManagementObjectSearcher mos = new System.Management.ManagementObjectSearcher(@"root\WMI", "Select * From MSAcpi_ThermalZoneTemperature");

            foreach (System.Management.ManagementObject mo in mos.Get())
            {
                CPUtprt = Convert.ToDouble(Convert.ToDouble(mo.GetPropertyValue("CrrentTemperature").ToString()) - 2732) / 10;
                richTextBox1.Text += "CPU温度：" + CPUtprt.ToString() + "°C\n";
            }
        }

        private void button4_Click(object sender, EventArgs e)
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

        private void button5_Click(object sender, EventArgs e)
        {
            //取得主機板序號
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select * From Win32_BIOS");

            int len = searcher.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in searcher.Get())
            {
                richTextBox1.Text += "取得主機板序號 :\t" + share.GetPropertyValue("SerialNumber").ToString() + "\n";
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得主機板參數
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            int len = searcher.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in searcher.Get())
            {
                richTextBox1.Text += "取得Manufacturer :\t" + share.GetPropertyValue("Manufacturer").ToString() + "\n";
                richTextBox1.Text += "取得Product :\t" + share.GetPropertyValue("Product").ToString() + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //取得網路卡參數
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            int len = searcher.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";
            foreach (ManagementObject share in searcher.Get())
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

        private void button8_Click(object sender, EventArgs e)
        {
            //取得Windows版本
            string version = OSInfoMation.GetOsVersion();
            richTextBox1.Text += version + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //取得螢幕尺寸
            SystemInfo sysInfo = new SystemInfo();
            string id = sysInfo.GetMonitorPnpDeviceId()[0];
            SizeF size = sysInfo.GetMonitorPhysicalSize(id);
            richTextBox1.Text += SystemInfo.MonitorScaler(size).ToString() + " 吋\n";
        }

        /// <summary>
        /// 获取屏幕数量
        /// </summary>
        /// <returns></returns>
        public int GetMonitorCount()
        {
            string text = string.Empty;
            int count = 0;
            ManagementObjectSearcher mos = new ManagementObjectSearcher(@"root\wmi", "Select * from WmiMonitorID");
            foreach (ManagementObject mo in mos.Get())
            {
                text += mo.GetText(TextFormat.Mof);
                count++;
            }
            return count;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //取得螢幕數量
            //检测已连接显示器
            richTextBox1.Text += "取得螢幕數量 : " + GetMonitorCount().ToString() + "\n";


        }

        private void button11_Click(object sender, EventArgs e)
        {
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


        private void button12_Click(object sender, EventArgs e)
        {
            //獲取硬盤相應序列號

            //獲取硬盤相應序列號
            string result = clsIDE.GetAllSerialNumber();
            richTextBox1.Text += "獲取硬盤序列號 : " + result + "\n";

        }

        private void button13_Click(object sender, EventArgs e)
        {
            //WMI 使用
            //WMI 使用
            SelectQuery query = new SelectQuery("Select * From Win32_LogicalDisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(query);

            foreach (ManagementBaseObject disk in searcher.Get())
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

        private void button14_Click(object sender, EventArgs e)
        {
            //取得硬碟參數
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            int len = searcher.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in searcher.Get())
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
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //取得處理器參數
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            int len = searcher.Get().Count;
            richTextBox1.Text += "len = " + len.ToString() + "\n";

            foreach (ManagementObject share in searcher.Get())
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

        private void button16_Click(object sender, EventArgs e)
        {
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
    }

    public class OSInfoMation
    {
        public static string OSBit()
        {
            try
            {
                ConnectionOptions oConn = new ConnectionOptions();
                System.Management.ManagementScope managementScope = new System.Management.ManagementScope("\\\\localhost", oConn);
                System.Management.ObjectQuery objectQuery = new System.Management.ObjectQuery("select AddressWidth from Win32_Processor");
                ManagementObjectSearcher moSearcher = new ManagementObjectSearcher(managementScope, objectQuery);
                ManagementObjectCollection moReturnCollection = null;
                string addressWidth = null;
                moReturnCollection = moSearcher.Get();
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

            System.Management.ManagementClass mo = new System.Management.ManagementClass("Win32_LogicalDisk");

            System.Management.ManagementObjectCollection mc = mo.GetInstances();

            foreach (System.Management.ManagementObject m in mc)
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

            System.Management.ManagementClass mo = new System.Management.ManagementClass("Win32_LogicalDisk");

            System.Management.ManagementObjectCollection mc = mo.GetInstances();

            foreach (System.Management.ManagementObject m in mc)
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
