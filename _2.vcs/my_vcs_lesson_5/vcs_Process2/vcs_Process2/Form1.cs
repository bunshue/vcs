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
            timer1.Interval = 1000;
            listBox1.DisplayMember = "ProcessName";
            listBox1.DataSource = Process.GetProcesses();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            var selectedProcess = listBox1.SelectedItem as Process;
            if (selectedProcess == null)
                return;

            textBox2.Text = selectedProcess.GetCpuUsage().ToString();
            textBox3.Text = selectedProcess.GetProcessOwner();
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {

            var selectedProcess = listBox1.SelectedItem as Process;
            if (selectedProcess == null)
                return;

            timer1.Enabled = false;

            textBox1.Text = selectedProcess.GetInstanceName();
            textBox2.Text = selectedProcess.GetCpuUsage().ToString();
            textBox3.Text = selectedProcess.GetProcessOwner();

            timer1.Enabled = true;
        }


    }

    public static class ProcessExtension
    {
        #region Private Static Var
        private static Dictionary<int, PerformanceCounter> _counterPool;
        private static Dictionary<int, DateTime> _updateTimePool;
        private static Dictionary<int, int> _cpuUsagePool;
        #endregion

        #region Private Static Property
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
        #endregion

        #region Private Static Method
        private static string GetProcessInstanceName(int pid)
        {
            var category = new PerformanceCounterCategory("Process");

            var instances = category.GetInstanceNames();
            foreach (var instance in instances)
            {

                using (var counter = new PerformanceCounter(category.CategoryName,
                     "ID Process", instance, true))
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

        #endregion

        #region Public Static Method
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

        #endregion


    }


}
