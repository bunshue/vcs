using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;   //for DllImport
using System.Diagnostics;       //for process

namespace vcs_test_all_28_ListAllProcess
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();

            // 列出系統中所有的程序
            Process[] processes = Process.GetProcesses();

            foreach (Process p in processes)
            {
                // 因為使用 Idle 的 StartTime 會造成錯誤，因此先排除
                if (!p.ProcessName.Equals("Idle"))
                {
                    // 顯示程序的名稱及啟動時間
                    listBox1.Items.Add(string.Format("{0} \t\t {1}", p.ProcessName, p.StartTime.ToString("yyyy/MM/dd hh:mm:ss")));
                }
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //C# 指定程序還原與置於前景視窗 
            // 取得目前電腦的處理程序
            listBox1.Items.Add("找到 " + Process.GetProcesses().Length + " 個程序\n\n");
            foreach (Process pTarget in Process.GetProcesses())
            {
                listBox1.Items.Add("找到 " + pTarget.ProcessName + "\n");
                if (pTarget.ProcessName == "ACDSee32")  // 取得處理序名稱並與指定程序名稱比較
                {
                    listBox1.Items.Add("\t你開啟了ACDSee32，移到前台。\n");
                    //listBox1.Items.Add(pTarget.ProcessName + "\n");
                    HandleRunningInstance(pTarget);
                }
            }
        }
        [DllImport("User32.dll")]
        private static extern bool ShowWindowAsync(IntPtr hWnd, int cmdShow);
        [DllImport("User32.dll")]
        private static extern bool SetForegroundWindow(IntPtr hWnd);
        private const int WS_SHOWNORMAL = 1;  
        public static void HandleRunningInstance(Process instance)
        {
            // 相同時透過ShowWindowAsync還原，以及SetForegroundWindow將程式至於前景
            ShowWindowAsync(instance.MainWindowHandle, WS_SHOWNORMAL);
            SetForegroundWindow(instance.MainWindowHandle);
            //Environment.SpecialFolder.
        }
    }
}
