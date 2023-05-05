using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;

namespace xCh5_4_2_11
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            process1.StartInfo.UseShellExecute = false;
            process1.StartInfo.FileName = "notepad";
            process1.StartInfo.CreateNoWindow = true;
            process1.Start();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            System.Diagnostics.Process localById = System.Diagnostics.Process.GetProcessById(10196);
            MessageBox.Show("電腦名稱：" + localById.MachineName + Environment.NewLine + "處理序名稱：" + localById.ProcessName);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            // 記得先執行幾次記事本，這樣才看得到效果
            Process[] localByName = Process.GetProcessesByName("notepad");
            foreach (Process p in localByName)
            {
                ListViewItem item = new ListViewItem();

                item.Text = p.ProcessName;
                item.SubItems.Add(p.Id.ToString());
                item.SubItems.Add((p.PrivateMemorySize64 / 1024) + "Kbyte");
                item.SubItems.Add((p.VirtualMemorySize64 / 1024) + "byte");

                listView1.Items.Add(item);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            foreach (Process p in Process.GetProcesses())
            {
                ListViewItem item = new ListViewItem();

                item.Text = p.ProcessName;
                item.SubItems.Add(p.Id.ToString());
                item.SubItems.Add((p.PrivateMemorySize64 / 1024) + "Kbyte");
                item.SubItems.Add((p.VirtualMemorySize64 / 1024) + "byte");

                listView1.Items.Add(item);
            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            Process.Start("IExplore.exe", "tw.yahoo.com");
            Process.Start("chrome.exe", "C:\\Read_Cht.htm");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string fileName = @"C:\_git\vcs\_1.data\______test_files1\__RW\_word\bmp_format.docx";
            ProcessStartInfo startInfo = new ProcessStartInfo(fileName);

            if (File.Exists(fileName))
            {
                int i = 0;
                foreach (String verb in startInfo.Verbs)
                {
                    listBox1.Items.Add(string.Format("  {0}. {1}", i.ToString(), verb));
                    i++;
                }
            }
            else
            {
            }
        }
    }
}
