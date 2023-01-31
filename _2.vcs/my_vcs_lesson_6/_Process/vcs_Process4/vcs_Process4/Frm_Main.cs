using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;
using System.Management;
using System.Runtime.InteropServices;

namespace vcs_Process4
{
    public partial class Frm_Main : Form
    {
        public Frm_Main()
        {
            InitializeComponent();
        }

        private void getProcessInfo()
        {
            try
            {
                listView1.Items.Clear();
                Process[] MyProcesses = Process.GetProcesses();
                tsslInfo.Text = "進程總數：" + MyProcesses.Length.ToString();
                string[] Minfo = new string[6];
                foreach (Process MyProcess in MyProcesses)
                {
                    Minfo[0] = MyProcess.ProcessName;
                    Minfo[1] = MyProcess.MainModule.ModuleName;
                    Minfo[2] = MyProcess.Threads.Count.ToString();
                    Minfo[3] = MyProcess.BasePriority.ToString();
                    Minfo[4] = Convert.ToString(MyProcess.WorkingSet / 1024) + "K";
                    Minfo[5] = Convert.ToString(MyProcess.VirtualMemorySize / 1024) + "K";
                    ListViewItem lvi = new ListViewItem(Minfo, "process");
                    listView1.Items.Add(lvi);
                }
            }
            catch { }
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            getProcessInfo();
        }

        private void 刷新ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            getProcessInfo();
        }

        private void 結束進程ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                if (MessageBox.Show("警告:終止進程會導致不希望發生的結果，\r包括數據丟失和系統不穩定。在被終止前，\r進程將沒有機會保存其狀態和數據。確實\r想終止該進程嗎?", "任務管理器警告", MessageBoxButtons.YesNo, MessageBoxIcon.Exclamation) == DialogResult.Yes)
                {
                    string ProcessName = listView1.SelectedItems[0].Text;
                    Process[] MyProcess = Process.GetProcessesByName(ProcessName);
                    MyProcess[0].Kill();
                    getProcessInfo();
                }
                else
                { }
            }
            catch
            {
                string ProcessName = listView1.SelectedItems[0].Text;
                Process[] MyProcess1 = Process.GetProcessesByName(ProcessName);
                Process MyProcess = new Process();
                //設定程序名
                MyProcess.StartInfo.FileName = "cmd.exe";
                //關閉Shell的使用
                MyProcess.StartInfo.UseShellExecute = false;
                //重定向標準輸入
                MyProcess.StartInfo.RedirectStandardInput = true;
                //重定向標準輸出
                MyProcess.StartInfo.RedirectStandardOutput = true;
                //重定向錯誤輸出
                MyProcess.StartInfo.RedirectStandardError = true;
                //設置不顯示窗口
                MyProcess.StartInfo.CreateNoWindow = true;
                //執行強制結束命令
                MyProcess.Start();
                MyProcess.StandardInput.WriteLine("ntsd -c q -p " + (MyProcess1[0].Id).ToString());
                MyProcess.StandardInput.WriteLine("Exit");
                getProcessInfo();
            }
        }

        private void SetBasePriority(int i)
        {
            string ProcessName = listView1.SelectedItems[0].Text;
            Process[] MyProcess = Process.GetProcessesByName(ProcessName);
            switch (i)
            {
                case 0: MyProcess[0].PriorityClass = ProcessPriorityClass.Idle; break;//低
                case 1: MyProcess[0].PriorityClass = ProcessPriorityClass.Normal; break;//標準
                case 2: MyProcess[0].PriorityClass = ProcessPriorityClass.High; break;//高
                case 3: MyProcess[0].PriorityClass = ProcessPriorityClass.RealTime; break;//實時
                case 4: MyProcess[0].PriorityClass = ProcessPriorityClass.AboveNormal; break;//高于標準
                case 5: MyProcess[0].PriorityClass = ProcessPriorityClass.BelowNormal; break;//低于標準
            }
            getProcessInfo();
        }
        private void 實時ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetBasePriority(3);
        }

        private void 高ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetBasePriority(2);
        }

        private void 高于標準ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetBasePriority(4);
        }

        private void 標準ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetBasePriority(1);
        }

        private void 低于標準ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetBasePriority(5);
        }

        private void 低ToolStripMenuItem_Click(object sender, EventArgs e)
        {
            SetBasePriority(0);
        }
    }
}