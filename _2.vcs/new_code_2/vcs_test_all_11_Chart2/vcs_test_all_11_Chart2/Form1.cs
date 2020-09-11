using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


using System.Runtime.InteropServices;   //for DllImport

using System.Diagnostics;   //for PerformanceCounter

using System.Windows.Forms.DataVisualization.Charting;  //for Series



//using System.Data.SqlClient;    //for SqlConnection

namespace vcs_test_all_11_Chart2
{
    public partial class Form1 : Form
    {
        static PerformanceCounter pc = new PerformanceCounter("Processor", "% Processor Time", "_Total");

        public Form1()
        {
            InitializeComponent();
        }


        private void button1_Click(object sender, EventArgs e)
        {
            drawLine();

            /*
            double[] data1 = new double[360];
            double[] data2 = new double[360];
            //double[] data3 = new double[360];
            for (int i = 0; i < 360; i++)
            {
                data1[i] = Math.Sin(i * 2 * Math.PI / 360);
                data2[i] = Math.Cos(i * 2 * Math.PI / 360);
                //data3[i] = data1[i] + data2[i];
            }
            // 建立好資料

            // 匯入Chart1
            for (int i = 0; i < 360; i++)
            {
                chart1.Series[0].Points.AddXY(i, data1[i]);
                chart1.Series[1].Points.AddXY(i, data2[i]);
                //chart1.Series[2].Points.AddXY(i, data3[i]);
            }
            */


        }

        private void drawLine() //繪圖
        {
            //---------------------
            chart1.Series.Clear();  //每次使用此function前先清除圖表
            Series series1 = new Series("Di0", 500); //初始畫線條(名稱，最大值)
            series1.Color = Color.Blue; //設定線條顏色
            series1.Font = new System.Drawing.Font("新細明體", 10); //設定字型
            series1.ChartType = SeriesChartType.Line; //設定線條種類
            chart1.ChartAreas[0].AxisY.Minimum = 0;//設定Y軸最小值
            chart1.ChartAreas[0].AxisY.Maximum = 500;//設定Y軸最大值
            //chart1.ChartAreas[0].AxisY.Enabled= AxisEnabled.False; //隱藏Y 軸標示
            //chart1.ChartAreas[0].AxisY.MajorGrid.Enabled= true;  //隱藏Y軸標線
            series1.IsValueShownAsLabel = true; //是否把數值顯示在線上
            //把值加入X 軸Y 軸
            series1.Points.AddXY("A", 200);
            series1.Points.AddXY("B", 100);
            series1.Points.AddXY("C", 100);
            series1.Points.AddXY("D", 30);
            series1.Points.AddXY("E", 300);
            series1.Points.AddXY("F", 70);
            this.chart1.Series.Add(series1);//將線畫在圖上
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            MEMORY_INFO MemInfo = new MEMORY_INFO();
            ComputerInfo.GlobalMemoryStatus(ref MemInfo);

            /*
            SYSTEMTIME_INFO SystemInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref SystemInfo);

            //richTextBox1.Text += "date : " + SystemInfo.wYear.ToString() + "/" + SystemInfo.wMonth.ToString() + "/" + SystemInfo.wDay.ToString() + " " + SystemInfo.wHour.ToString() + ":" + SystemInfo.wMinute.ToString() + ":" + SystemInfo.wSecond.ToString() + "\n";
            //label3.Text = SystemInfo.wMilliseconds.ToString();
            */

            //UseMemory
            Series series = ChartMemory.Series[0];
            richTextBox1.Text += "Count = " + series.Points.Count.ToString() + "\n";
            int xCount = series.Points.Count == 0 ? 0 : series.Points.Count - 1;
            double lastXValue = series.Points.Count == 0 ? 1 : series.Points[xCount].XValue + 1;

            //richTextBox1.Text += "lastXValue = " + lastXValue.ToString() + "\n";

            double lastYValue = (double)(MemInfo.dwTotalPhys - MemInfo.dwAvailPhys) / 1024 / 1024;
            //double lastYValue = SystemInfo.wMilliseconds;

            series.Points.AddXY(lastXValue, lastYValue);
            //Total Memory
            //series = ChartMemory.Series[1];
            lastYValue = (double)(MemInfo.dwTotalVirtual + MemInfo.dwTotalPhys - MemInfo.dwAvailPhys - MemInfo.dwAvailVirtual) / 1024 / 1024;
            //richTextBox1.Text += "lastYValue = " + lastYValue.ToString() + "\n";
            label1.Text = lastYValue.ToString();
            series.Points.AddXY(lastXValue, lastYValue);
            //CPU
            //series = ChartMemory.Series[2];

            lastYValue = (double)pc.NextValue();
            label2.Text = lastYValue.ToString();
            series.Points.AddXY(lastXValue, lastYValue);
            // Remove points from the left chart side if number of points exceeds 100.
            while (this.ChartMemory.Series[0].Points.Count > 150)
            {
                // Remove series points
                foreach (Series s in this.ChartMemory.Series)
                {
                    s.Points.RemoveAt(0);
                }
            }
            // Adjust categorical scale
            double axisMinimum = this.ChartMemory.Series[0].Points[0].XValue;
            //richTextBox1.Text += "axisMinimum = " + axisMinimum.ToString() + "\n";
            this.ChartMemory.ChartAreas[0].AxisX.Minimum = axisMinimum;
            this.ChartMemory.ChartAreas[0].AxisX.Maximum = axisMinimum + 99;

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




    }
}
