using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// 导入 System.Runtime.InteropServices 名称空间
using System.Runtime.InteropServices;   //for DllImport //DllImport 	指定 DLL 的位置

namespace vcs_Class1
{
    public partial class Form1 : Form
    {
        //建立 Animal 類別
        public class Animal
        {
            public string recorder;
            public int number;
            public string name;
            public string type;
            //A class被實例化時，會立即執行建構子內容，並且可以傳入參數
            public string Show
            {
                // 可以透過 get 存取子，將字串進行判斷、處理.... 再返回結果
                get { return name; }

                // set含有特殊的keyword: value, 當有值傳入時，都會存入value中
                set
                {
                    name = type;
                    recorder = value;
                    //Console.WriteLine("I am " + value);
                }
            }
        }


        /// <summary>
        ///取得计算机的系统信息
        /// </summary>
        public class ComputerInfo
        {
            // 声明所要用到的API函数
            /// <summary>
            /// 取得Windows的目录
            /// </summary>
            /// <param name="WinDir"></param>
            /// <param name="count"></param>
            [DllImport("kernel32")]
            public static extern void GetWindowsDirectory(StringBuilder WinDir, int count);

            /// <summary>
            /// 获取系统路径
            /// </summary>
            /// <param name="SysDir"></param>
            /// <param name="count"></param>
            [DllImport("kernel32")]
            public static extern void GetSystemDirectory(StringBuilder SysDir, int count);

            /// <summary>
            /// 取得CPU信息
            /// </summary>
            /// <param name="cpuinfo"></param>
            [DllImport("kernel32")]
            public static extern void GetSystemInfo(ref CPU_INFO cpuinfo);

            /// <summary>
            /// 取得内存状态
            /// </summary>
            /// <param name="meminfo"></param>
            [DllImport("kernel32")]
            public static extern void GlobalMemoryStatus(ref MEMORY_INFO meminfo);

            /// <summary>
            /// 取得系统时间
            /// </summary>
            /// <param name="stinfo"></param>
            [DllImport("kernel32")]
            public static extern void GetSystemTime(ref SYSTEMTIME_INFO stinfo);
            public ComputerInfo()
            {
            }
        }
        //定义CPU的信息结构
        [StructLayout(LayoutKind.Sequential)]
        public struct CPU_INFO
        {
            public uint dwOemId;
            public uint dwPageSize;
            public uint lpMinimumApplicationAddress;
            public uint lpMaximumApplicationAddress;
            public uint dwActiveProcessorMask;
            public uint dwNumberOfProcessors;
            public uint dwProcessorType;
            public uint dwAllocationGranularity;
            public uint dwProcessorLevel;
            public uint dwProcessorRevision;
        }
        //定义内存的信息结构
        [StructLayout(LayoutKind.Sequential)]
        public struct MEMORY_INFO
        {
            public uint dwLength;
            public uint dwMemoryLoad;
            public uint dwTotalPhys;
            public uint dwAvailPhys;
            public uint dwTotalPageFile;
            public uint dwAvailPageFile;
            public uint dwTotalVirtual;
            public uint dwAvailVirtual;
        }
        //定义系统时间的信息结构
        [StructLayout(LayoutKind.Sequential)]
        public struct SYSTEMTIME_INFO
        {
            public ushort wYear;
            public ushort wMonth;
            public ushort wDayOfWeek;
            public ushort wDay;
            public ushort wHour;
            public ushort wMinute;
            public ushort wSecond;
            public ushort wMilliseconds;
        }



        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SYSTEMTIME_INFO SystemInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref SystemInfo);

            richTextBox1.Text += "date : " + SystemInfo.wYear.ToString() + "/" + SystemInfo.wMonth.ToString() + "/" + SystemInfo.wDay.ToString() + " " + SystemInfo.wHour.ToString() + ":" + SystemInfo.wMinute.ToString() + ":" + SystemInfo.wSecond.ToString() + "." + SystemInfo.wMilliseconds.ToString() + "\n";

            //調用GetSystemInfo函數獲取CPU的相關訊息
            CPU_INFO CpuInfo = new CPU_INFO();
            ComputerInfo.GetSystemInfo(ref CpuInfo);
            richTextBox1.Text += "dwOemId = " + CpuInfo.dwOemId.ToString() + "\n";
            richTextBox1.Text += "dwPageSize = " + CpuInfo.dwPageSize.ToString() + "\n";
            richTextBox1.Text += "lpMinimumApplicationAddress = " + CpuInfo.lpMinimumApplicationAddress.ToString() + "\n";
            richTextBox1.Text += "lpMaximumApplicationAddress = " + CpuInfo.lpMaximumApplicationAddress.ToString() + "\n";
            richTextBox1.Text += "dwActiveProcessorMask = " + CpuInfo.dwActiveProcessorMask.ToString() + "\n";
            richTextBox1.Text += "dwNumberOfProcessors = " + CpuInfo.dwNumberOfProcessors.ToString() + "\n";
            richTextBox1.Text += "dwProcessorType = " + CpuInfo.dwProcessorType.ToString() + "\n";
            richTextBox1.Text += "dwAllocationGranularity = " + CpuInfo.dwAllocationGranularity.ToString() + "\n";
            richTextBox1.Text += "dwProcessorLevel = " + CpuInfo.dwProcessorLevel.ToString() + "\n";
            richTextBox1.Text += "dwProcessorRevision = " + CpuInfo.dwProcessorRevision.ToString() + "\n";

            richTextBox1.Text += "本计算机中有" + CpuInfo.dwNumberOfProcessors.ToString() + "个CPU" + "\n";
            richTextBox1.Text += "CPU的类型为" + CpuInfo.dwProcessorType.ToString() + "\n";
            richTextBox1.Text += "CPU等级为" + CpuInfo.dwProcessorLevel.ToString() + "\n";
            richTextBox1.Text += "CPU的OEM ID为" + CpuInfo.dwOemId.ToString() + "\n";
            richTextBox1.Text += "CPU中的页面大小为" + CpuInfo.dwPageSize.ToString() + "\n";


            //調用GlobalMemoryStatus函數獲取記憶體的相關訊息
            MEMORY_INFO MemInfo = new MEMORY_INFO();
            ComputerInfo.GlobalMemoryStatus(ref MemInfo);
            richTextBox1.Text += "dwLength = " + MemInfo.dwLength.ToString() + "\n";
            richTextBox1.Text += "dwMemoryLoad = " + MemInfo.dwMemoryLoad.ToString() + "\n";
            richTextBox1.Text += "dwTotalPhys = " + (MemInfo.dwTotalPhys / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwAvailPhys = " + (MemInfo.dwAvailPhys / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwTotalPageFile = " + (MemInfo.dwTotalPageFile / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwAvailPageFile = " + (MemInfo.dwAvailPageFile / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwTotalVirtual = " + (MemInfo.dwTotalVirtual / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwAvailVirtual = " + (MemInfo.dwAvailVirtual / 1024 / 1024).ToString().ToString() + "\n";

            richTextBox1.Text += MemInfo.dwMemoryLoad.ToString() + "%的内存正在使用" + "\n";
            richTextBox1.Text += "物理内存共有" + MemInfo.dwTotalPhys.ToString() + "字节" + "\n";
            richTextBox1.Text += "可使用的物理内存有" + MemInfo.dwAvailPhys.ToString() + "字节" + "\n";
            richTextBox1.Text += "交换文件总大小为" + MemInfo.dwTotalPageFile.ToString() + "字节" + "\n";
            richTextBox1.Text += "尚可交换文件大小为" + MemInfo.dwAvailPageFile.ToString() + "字节" + "\n";
            richTextBox1.Text += "总虚拟内存有" + MemInfo.dwTotalVirtual.ToString() + "字节" + "\n";
            richTextBox1.Text += "未用虚拟内存有" + MemInfo.dwAvailVirtual.ToString() + "字节" + "\n";

            //調用GetSystemTime函數獲取系統時間訊息
            SYSTEMTIME_INFO SysInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref SysInfo);
            richTextBox1.Text += "wYear = " + SysInfo.wYear.ToString() + "\n";
            richTextBox1.Text += "wMonth = " + SysInfo.wMonth.ToString() + "\n";
            richTextBox1.Text += "wDayOfWeek = " + SysInfo.wDayOfWeek.ToString() + "\n";
            richTextBox1.Text += "wDay = " + SysInfo.wDay.ToString() + "\n";
            richTextBox1.Text += "wHour = " + SysInfo.wHour.ToString() + "\n";
            richTextBox1.Text += "wMinute = " + SysInfo.wMinute.ToString() + "\n";
            richTextBox1.Text += "wSecond = " + SysInfo.wSecond.ToString() + "\n";
            richTextBox1.Text += "wMilliseconds = " + SysInfo.wMilliseconds.ToString() + "\n";


            //调用GetWindowsDirectory和GetSystemDirectory函数分别取得Windows路径和系统路径
            const int nChars = 128;
            StringBuilder Buff = new StringBuilder(nChars);
            ComputerInfo.GetWindowsDirectory(Buff, nChars);
            richTextBox1.Text += "Windows路径：" + Buff.ToString() + "\n";
            ComputerInfo.GetSystemDirectory(Buff, nChars);
            richTextBox1.Text += "系统路径：" + Buff.ToString() + "\n";

            //调用GetSystemTime函数获取系统时间信息
            SYSTEMTIME_INFO StInfo;
            StInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref StInfo);
            richTextBox1.Text += StInfo.wYear.ToString() + "年" + StInfo.wMonth.ToString() + "月" + StInfo.wDay.ToString() + "日" + "\n";
            richTextBox1.Text += (StInfo.wHour + 8).ToString() + "点" + StInfo.wMinute.ToString() + "分" + StInfo.wSecond.ToString() + "秒" + "\n";




        }

        private void button2_Click(object sender, EventArgs e)
        {
            //實例化A類別
            Animal people = new Animal();

            people.type = "zzz";
            people.name = "Brown";
            people.Show = "Joe";
            richTextBox1.Text += people.Show + "\n";

            richTextBox1.Text += "ttt = " + people.recorder + "\n";

        }

    }
}
