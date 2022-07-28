using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

// 導入 System.Runtime.InteropServices 名稱空間
using System.Runtime.InteropServices;   //for DllImport //DllImport 	指定 DLL 的位置

namespace vcs_System3
{
    public partial class Form1 : Form
    {
        /// <summary>
        ///取得計算機的系統信息
        /// </summary>
        public class ComputerInfo
        {
            // 聲明所要用到的API函數
            /// <summary>
            /// 取得Windows的目錄
            /// </summary>
            /// <param name="WinDir"></param>
            /// <param name="count"></param>
            [DllImport("kernel32")]
            public static extern void GetWindowsDirectory(StringBuilder WinDir, int count);

            /// <summary>
            /// 獲取系統路徑
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
            /// 取得內存狀態
            /// </summary>
            /// <param name="meminfo"></param>
            [DllImport("kernel32")]
            public static extern void GlobalMemoryStatus(ref MEMORY_INFO meminfo);

            /// <summary>
            /// 取得系統時間
            /// </summary>
            /// <param name="stinfo"></param>
            [DllImport("kernel32")]
            public static extern void GetSystemTime(ref SYSTEMTIME_INFO stinfo);
            public ComputerInfo()
            {
            }
        }
        //定義CPU的信息結構
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
        //定義內存的信息結構
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
        //定義系統時間的信息結構
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

            richTextBox1.Text += "本計算機中有" + CpuInfo.dwNumberOfProcessors.ToString() + "個CPU" + "\n";
            richTextBox1.Text += "CPU的類型為" + CpuInfo.dwProcessorType.ToString() + "\n";
            richTextBox1.Text += "CPU等級為" + CpuInfo.dwProcessorLevel.ToString() + "\n";
            richTextBox1.Text += "CPU的OEM ID為" + CpuInfo.dwOemId.ToString() + "\n";
            richTextBox1.Text += "CPU中的頁面大小為" + CpuInfo.dwPageSize.ToString() + "\n";


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

            richTextBox1.Text += MemInfo.dwMemoryLoad.ToString() + "%的內存正在使用" + "\n";
            richTextBox1.Text += "物理內存共有" + MemInfo.dwTotalPhys.ToString() + "字節" + "\n";
            richTextBox1.Text += "可使用的物理內存有" + MemInfo.dwAvailPhys.ToString() + "字節" + "\n";
            richTextBox1.Text += "交換文件總大小為" + MemInfo.dwTotalPageFile.ToString() + "字節" + "\n";
            richTextBox1.Text += "尚可交換文件大小為" + MemInfo.dwAvailPageFile.ToString() + "字節" + "\n";
            richTextBox1.Text += "總虛擬內存有" + MemInfo.dwTotalVirtual.ToString() + "字節" + "\n";
            richTextBox1.Text += "未用虛擬內存有" + MemInfo.dwAvailVirtual.ToString() + "字節" + "\n";

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


            //調用GetWindowsDirectory和GetSystemDirectory函數分別取得Windows路徑和系統路徑
            const int nChars = 128;
            StringBuilder Buff = new StringBuilder(nChars);
            ComputerInfo.GetWindowsDirectory(Buff, nChars);
            richTextBox1.Text += "Windows路徑：" + Buff.ToString() + "\n";
            ComputerInfo.GetSystemDirectory(Buff, nChars);
            richTextBox1.Text += "系統路徑：" + Buff.ToString() + "\n";

            //調用GetSystemTime函數獲取系統時間信息
            SYSTEMTIME_INFO StInfo;
            StInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref StInfo);
            richTextBox1.Text += StInfo.wYear.ToString() + "年" + StInfo.wMonth.ToString() + "月" + StInfo.wDay.ToString() + "日" + "\n";
            richTextBox1.Text += (StInfo.wHour + 8).ToString() + "點" + StInfo.wMinute.ToString() + "分" + StInfo.wSecond.ToString() + "秒" + "\n";
        }
    }
}
