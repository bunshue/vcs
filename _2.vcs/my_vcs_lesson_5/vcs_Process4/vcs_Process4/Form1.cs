using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Threading.Tasks;

namespace vcs_Process4
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            listBox1.DisplayMember = "ProcessName";
            listBox1.DataSource = Process.GetProcesses();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            var selectedProcess = listBox1.SelectedItem as Process;
            if (selectedProcess == null)
                return;

            textBox2.Text = "CPU : " + selectedProcess.GetCpuUsage().ToString() + " %";
        }

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            var selectedProcess = listBox1.SelectedItem as Process;
            if (selectedProcess == null)
                return;

            timer1.Enabled = false;
            textBox1.Text = "Instance Name : " + selectedProcess.GetInstanceName();
            textBox2.Text = "CPU : " + selectedProcess.GetCpuUsage().ToString() + " %";
            timer1.Enabled = true;
        }
    }

    //擴充方法
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
        //透過這個這個PerformanceCounter反查到Process的Instance Name
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

            //取得的值必須要除以核心數才會是我們期望的值
            if (interval.TotalSeconds > 1)
            {
                m_CpuUsagePool[pid] = (int)(m_CounterPool[pid].NextValue() / Environment.ProcessorCount);
            }

            return m_CpuUsagePool[pid];
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
        #endregion
    }

}
