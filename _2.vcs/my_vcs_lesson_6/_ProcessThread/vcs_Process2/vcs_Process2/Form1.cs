using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Process
using System.Management;    //for WMI

//[C#]透過PerformanceCounter取得特定Process的CPU使用率
//[C#]如何取得Process的Owner

/*
[C#] 調用WMI
第一步：加入參考
專案→加入參考→.Net→System.Management
第二步：引用命名空間
using System.Management;
*/

namespace vcs_Process2
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

            //------------------------------------------------------------  # 60個

            timer1.Interval = 1000;
            listBox1.DisplayMember = "ProcessName";
            listBox1.DataSource = Process.GetProcesses();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;

            richTextBox1.Size = new Size(500, 500);
            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(980, 720);
            this.Text = "vcs_test_all_00_Usually";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void timer1_Tick(object sender, EventArgs e)
        {
            var selectedProcess = listBox1.SelectedItem as Process;
            if (selectedProcess == null)
            {
                return;
            }

            textBox2.Text = "CPU : " + selectedProcess.GetCpuUsage().ToString() + " %";
            textBox3.Text = "Owner : " + selectedProcess.GetProcessOwner();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

            var selectedProcess = listBox1.SelectedItem as Process;
            if (selectedProcess == null)
            {
                return;
            }

            timer1.Enabled = false;

            textBox1.Text = "Instance Name : " + selectedProcess.GetInstanceName();
            textBox2.Text = "CPU : " + selectedProcess.GetCpuUsage().ToString() + " %";
            textBox3.Text = "Owner : " + selectedProcess.GetProcessOwner();

            timer1.Enabled = true;
        }

    }

    //------------------------------------------------------------  # 60個

    //擴充方法
    public static class ProcessExtension
    {
        //#region Private Static Var
        private static Dictionary<int, PerformanceCounter> _counterPool;
        private static Dictionary<int, DateTime> _updateTimePool;
        private static Dictionary<int, int> _cpuUsagePool;
        //#endregion

        //#region Private Static Property
        private static Dictionary<int, PerformanceCounter> m_CounterPool
        {
            get
            {
                return _counterPool ?? (_counterPool = new Dictionary<int, PerformanceCounter>());
            }
        }

        private static Dictionary<int, DateTime> m_UpdateTimePool
        {
            get
            {
                return _updateTimePool ?? (_updateTimePool = new Dictionary<int, DateTime>());
            }
        }

        private static Dictionary<int, int> m_CpuUsagePool
        {
            get
            {
                return _cpuUsagePool ?? (_cpuUsagePool = new Dictionary<int, int>());
            }
        }
        //#endregion

        //#region Private Static Method
        //透過這個這個PerformanceCounter反查到Process的Instance Name
        private static string GetProcessInstanceName(int pid)
        {
            var category = new PerformanceCounterCategory("Process");

            var instances = category.GetInstanceNames();
            foreach (var instance in instances)
            {
                using (var counter = new PerformanceCounter(category.CategoryName, "ID Process", instance, true))
                {
                    int val = (int)counter.RawValue;
                    if (val == pid)
                    {
                        return instance;
                    }
                }
            }
            throw new ArgumentException("Invalid pid!");
        }

        private static int GetCpuUsage(int pid)
        {
            if (!m_CounterPool.ContainsKey(pid))
            {
                m_CounterPool.Add(pid, new PerformanceCounter("Process", "% Processor Time", GetProcessInstanceName(pid)));
            }

            var lastUpdateTime = default(DateTime);

            m_UpdateTimePool.TryGetValue(pid, out lastUpdateTime);

            var interval = DateTime.Now - lastUpdateTime;

            //取得的值必須要除以核心數才會是我們期望的值
            if (interval.TotalSeconds > 1)
            {
                m_CpuUsagePool[pid] = (int)(m_CounterPool[pid].NextValue() / Environment.ProcessorCount);
            }

            return m_CpuUsagePool[pid];
        }

        public static string GetProcessOwner(int pid)
        {
            var query = "Select * From Win32_Process Where ProcessID = " + pid;
            var searcher = new ManagementObjectSearcher(query);
            var processObj = searcher.Get().OfType<ManagementObject>().FirstOrDefault();

            if (processObj == null)
                throw new ArgumentException("Process not exists!");

            var argList = new string[2];
            int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
            if (returnVal == 0)
            {
                return string.Join(@"\", argList.Reverse().ToArray());
            }

            return null;
        }

        //#endregion

        //#region Public Static Method
        public static string GetInstanceName(this Process process)
        {
            return GetProcessInstanceName(process.Id);
        }

        public static int GetCpuUsage(this Process process)
        {
            return GetCpuUsage(process.Id);
        }

        public static string GetProcessOwner(this Process process)
        {
            return GetProcessOwner(process.Id);
        }
        //#endregion
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

