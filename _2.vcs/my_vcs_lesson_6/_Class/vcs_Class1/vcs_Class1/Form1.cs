using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

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

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SYSTEMTIME_INFO SystemInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref SystemInfo);

            richTextBox1.Text += "date : " + SystemInfo.wYear.ToString() + "/" + SystemInfo.wMonth.ToString() + "/" + SystemInfo.wDay.ToString() + " " + SystemInfo.wHour.ToString() + ":" + SystemInfo.wMinute.ToString() + ":" + SystemInfo.wSecond.ToString() + "." + SystemInfo.wMilliseconds.ToString() + "\n";
        }


        /// <summary>
        ///取得计算机的系统信息
        /// </summary>
        public class ComputerInfo
        {
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
