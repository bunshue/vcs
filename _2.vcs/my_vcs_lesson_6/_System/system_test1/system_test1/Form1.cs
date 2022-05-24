using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;
using System.Runtime.InteropServices;   //for StructLayout

namespace system_test1
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// 操作系統關閉時，關閉應用程序
        /// </summary>
        /// <param name="m">截獲系統消息</param>
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case 0x0011://WM_QUERYENDSESSION
                    //m.Result = (IntPtr)1;
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    break;
                default:
                    base.WndProc(ref m);
                    break;
            }
        }
        /*
        做了一個定時播放器,程序運行時最小化到任務欄托盤,可這時候關閉或重啟操作系統使如果程序沒有退出,
        則系統不能關閉.那麼如何實現關機時自動退出程序呢?其實很簡單,當windows操作系統執行關閉動作時,
        它會發送給各個正在運行的應用程序一個消息WM_QUERYENDSESSION,告訴應用程序要關機了,如果反饋回來的消息值為1,
        那麼windows操作系統就會自動關閉.因此,通過截獲WM_QUERYENDSESSION消息,就能實現自動退出程序.
        */

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

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 0);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //獲取系統版本信息方法
            richTextBox1.Text += OSInfoMation.GetOsVersion() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //取得CPU編號、硬盤編號等系統有關環境、屬性
            SystemInfo systemInfo = new SystemInfo();
            richTextBox1.Text += "操作系统：" + systemInfo.GetOperationSystemInName() + "\n";
            richTextBox1.Text += "CPU编号：" + systemInfo.GetCpuId() + "\n";
            richTextBox1.Text += "硬盘编号：" + systemInfo.GetMainHardDiskId() + "\n";
            richTextBox1.Text += "Windows目录所在位置：" + systemInfo.GetSysDirectory() + "\n";
            richTextBox1.Text += "系统目录所在位置：" + systemInfo.GetWinDirectory() + "\n";
            MemoryInfo memoryInfo = systemInfo.GetMemoryInfo();
            CpuInfo cpuInfo = systemInfo.GetCpuInfo();
            richTextBox1.Text += "dwActiveProcessorMask" + cpuInfo.dwActiveProcessorMask + "\n";
            richTextBox1.Text += "dwAllocationGranularity" + cpuInfo.dwAllocationGranularity + "\n";
            richTextBox1.Text += "CPU个数：" + cpuInfo.dwNumberOfProcessors + "\n";
            richTextBox1.Text += "OEM ID：" + cpuInfo.dwOemId + "\n";
            richTextBox1.Text += "页面大小" + cpuInfo.dwPageSize + "\n";
            richTextBox1.Text += "CPU等级" + cpuInfo.dwProcessorLevel + "\n";
            richTextBox1.Text += "dwProcessorRevision" + cpuInfo.dwProcessorRevision + "\n";
            richTextBox1.Text += "CPU类型" + cpuInfo.dwProcessorType + "\n";
            richTextBox1.Text += "lpMaximumApplicationAddress" + cpuInfo.lpMaximumApplicationAddress + "\n";
            richTextBox1.Text += "lpMinimumApplicationAddress" + cpuInfo.lpMinimumApplicationAddress + "\n";
            richTextBox1.Text += "CPU类型：" + cpuInfo.dwProcessorType + "\n";
            richTextBox1.Text += "可用交换文件大小：" + memoryInfo.dwAvailPageFile + "\n";
            richTextBox1.Text += "可用物理内存大小：" + memoryInfo.dwAvailPhys + "\n";
            richTextBox1.Text += "可用虚拟内存大小" + memoryInfo.dwAvailVirtual + "\n";
            richTextBox1.Text += "操作系统位数：" + memoryInfo.dwLength + "\n";
            richTextBox1.Text += "已经使用内存大小：" + memoryInfo.dwMemoryLoad + "\n";
            richTextBox1.Text += "交换文件总大小：" + memoryInfo.dwTotalPageFile + "\n";
            richTextBox1.Text += "总物理内存大小：" + memoryInfo.dwTotalPhys + "\n";
            richTextBox1.Text += "总虚拟内存大小：" + memoryInfo.dwTotalVirtual + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

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

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

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
                ObjectQuery objectQuery = new ObjectQuery("select AddressWidth from Win32_Processor");

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


    /**/
    /**
* LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
* 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
* LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
* LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
*/
    /**/
    /// <summary>
    /// 定義CPU的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct CpuInfo
    {
        /**/
        /// <summary>
        /// OEM ID
        /// </summary>
        public uint dwOemId;
        /**/
        /// <summary>
        /// 頁面大小
        /// </summary>
        public uint dwPageSize;
        public uint lpMinimumApplicationAddress;
        public uint lpMaximumApplicationAddress;
        public uint dwActiveProcessorMask;
        /**/
        /// <summary>
        /// CPU個數
        /// </summary>
        public uint dwNumberOfProcessors;
        /**/
        /// <summary>
        /// CPU類型
        /// </summary>
        public uint dwProcessorType;
        public uint dwAllocationGranularity;
        /**/
        /// <summary>
        /// CPU等級
        /// </summary>
        public uint dwProcessorLevel;
        public uint dwProcessorRevision;
    }


    /**/
    /**
* LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
* 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
* LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
* LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
*/
    /**/
    /// <summary>
    /// 定義內存的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct MemoryInfo
    {
        /**/
        /// <summary>
        ///
        /// </summary>
        public uint dwLength;
        /**/
        /// <summary>
        /// 已經使用的內存
        /// </summary>
        public uint dwMemoryLoad;
        /**/
        /// <summary>
        /// 總物理內存大小
        /// </summary>
        public uint dwTotalPhys;
        /**/
        /// <summary>
        /// 可用物理內存大小
        /// </summary>
        public uint dwAvailPhys;
        /**/
        /// <summary>
        /// 交換文件總大小
        /// </summary>
        public uint dwTotalPageFile;
        /**/
        /// <summary>
        /// 可用交換文件大小
        /// </summary>
        public uint dwAvailPageFile;
        /**/
        /// <summary>
        /// 總虛擬內存大小
        /// </summary>
        public uint dwTotalVirtual;
        /**/
        /// <summary>
        /// 可用虛擬內存大小
        /// </summary>
        public uint dwAvailVirtual;
    }


    /**/
    /**
* LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
* 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
* LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
* LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
*/
    /**/
    /// <summary>
    /// 定義系統時間的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct SystemTimeInfo
    {
        /**/
        /// <summary>
        /// 年
        /// </summary>
        public ushort wYear;
        /**/
        /// <summary>
        /// 月
        /// </summary>
        public ushort wMonth;
        /**/
        /// <summary>
        /// 星期
        /// </summary>
        public ushort wDayOfWeek;
        /**/
        /// <summary>
        /// 天
        /// </summary>
        public ushort wDay;
        /**/
        /// <summary>
        /// 小時
        /// </summary>
        public ushort wHour;
        /**/
        /// <summary>
        /// 分鐘
        /// </summary>
        public ushort wMinute;
        /**/
        /// <summary>
        /// 秒
        /// </summary>
        public ushort wSecond;
        /**/
        /// <summary>
        /// 毫秒
        /// </summary>
        public ushort wMilliseconds;
    }





    /**/
    /// <summary> 
    /// SystemInfo 的摘要说明 
    /// </summary> 
    public class SystemInfo
    {
        private const int CHAR_COUNT = 128;
        public SystemInfo()
        {

        }
        [DllImport("kernel32")]
        private static extern void GetWindowsDirectory(StringBuilder WinDir, int count);

        [DllImport("kernel32")]
        private static extern void GetSystemDirectory(StringBuilder SysDir, int count);

        [DllImport("kernel32")]
        private static extern void GetSystemInfo(ref CpuInfo cpuInfo);

        [DllImport("kernel32")]
        private static extern void GlobalMemoryStatus(ref MemoryInfo memInfo);

        [DllImport("kernel32")]
        private static extern void GetSystemTime(ref SystemTimeInfo sysInfo);

        /**/
        /// <summary> 
        /// 查询CPU编号 
        /// </summary> 
        /// <returns></returns> 
        public string GetCpuId()
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

        /**/
        /// <summary> 
        /// 查询硬盘编号 
        /// </summary> 
        /// <returns></returns> 
        public string GetMainHardDiskId()
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

        /**/
        /// <summary> 
        /// 获取Windows目录 
        /// </summary> 
        /// <returns></returns> 
        public string GetWinDirectory()
        {
            StringBuilder sBuilder = new StringBuilder(CHAR_COUNT);
            GetWindowsDirectory(sBuilder, CHAR_COUNT);
            return sBuilder.ToString();
        }

        /**/
        /// <summary> 
        /// 获取系统目录 
        /// </summary> 
        /// <returns></returns> 
        public string GetSysDirectory()
        {
            StringBuilder sBuilder = new StringBuilder(CHAR_COUNT);
            GetSystemDirectory(sBuilder, CHAR_COUNT);
            return sBuilder.ToString();
        }

        /**/
        /// <summary> 
        /// 获取CPU信息 
        /// </summary> 
        /// <returns></returns> 
        public CpuInfo GetCpuInfo()
        {
            CpuInfo cpuInfo = new CpuInfo();
            GetSystemInfo(ref cpuInfo);
            return cpuInfo;
        }

        /**/
        /// <summary> 
        /// 获取系统内存信息 
        /// </summary> 
        /// <returns></returns> 
        public MemoryInfo GetMemoryInfo()
        {
            MemoryInfo memoryInfo = new MemoryInfo();
            GlobalMemoryStatus(ref memoryInfo);
            return memoryInfo;
        }

        /**/
        /// <summary> 
        /// 获取系统时间信息 
        /// </summary> 
        /// <returns></returns> 
        public SystemTimeInfo GetSystemTimeInfo()
        {
            SystemTimeInfo systemTimeInfo = new SystemTimeInfo();
            GetSystemTime(ref systemTimeInfo);
            return systemTimeInfo;
        }

        /**/
        /// <summary> 
        /// 获取系统名称 
        /// </summary> 
        /// <returns></returns> 
        public string GetOperationSystemInName()
        {
            OperatingSystem os = System.Environment.OSVersion;
            string osName = "UNKNOWN";
            switch (os.Platform)
            {
                case PlatformID.Win32Windows:
                    switch (os.Version.Minor)
                    {
                        case 0: osName = "Windows 95"; break;
                        case 10: osName = "Windows 98"; break;
                        case 90: osName = "Windows ME"; break;
                    }
                    break;
                case PlatformID.Win32NT:
                    switch (os.Version.Major)
                    {
                        case 3: osName = "Windws NT 3.51"; break;
                        case 4: osName = "Windows NT 4"; break;
                        case 5: if (os.Version.Minor == 0)
                            {
                                osName = "Windows 2000";
                            }
                            else if (os.Version.Minor == 1)
                            {
                                osName = "Windows XP";
                            }
                            else if (os.Version.Minor == 2)
                            {
                                osName = "Windows Server 2003";
                            }
                            break;
                        case 6: osName = "Longhorn"; break;
                    }
                    break;
            }
            return String.Format("{0},{1}", osName, os.Version.ToString());
        }
    }


}
