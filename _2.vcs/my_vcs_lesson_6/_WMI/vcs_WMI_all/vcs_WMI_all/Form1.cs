using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_all
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();

            listView1.Columns.Add("項目", 300, HorizontalAlignment.Center);
            listView1.Columns.Add("內容", 300, HorizontalAlignment.Center);

            string[] win32_cmd = new string[] { "Win32_BaseBoard", "Win32_Battery", "Win32_BIOS", "Win32_DiskDrive", "Win32_IDEController", "Win32_NetworkAdapter", "Win32_NetworkAdapterConfiguration", "Win32_Processor", "Win32_SerialPort", "Win32_USBController", "Win32_USBHub", "Win32_VideoController", "Win32_VideoSettings"};
           comboBox1.Items.AddRange(win32_cmd);
           comboBox1.Text = win32_cmd[0];
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            listView1.Clear();
            listView1.Columns.Add("項目", 300, HorizontalAlignment.Center);
            listView1.Columns.Add("內容", 300, HorizontalAlignment.Center);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //CPU ID/Board SerialNumber
            // Display the CPU IDs and the mother board serial numbers.
            GetCpuIds();
            GetBoardSerialNumbers();
        }

        // Use WMI to return the CPUs' IDs.
        private List<string> GetCpuIds()
        {
            List<string> results = new List<string>();

            string query = "Select * FROM Win32_Processor";
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(query);
            foreach (ManagementObject info in searcher.Get())
            {
                results.Add(info.GetPropertyValue("ProcessorId").ToString());
                richTextBox1.Text += "CPU ID:\t" + info.GetPropertyValue("ProcessorId").ToString() + "\n";
            }
            return results;
        }

        // Use WMI to return the system's base board serial numbers.
        private List<string> GetBoardSerialNumbers()
        {
            List<string> results = new List<string>();

            string query = "SELECT * FROM Win32_BaseBoard";
            ManagementObjectSearcher searcher =
                new ManagementObjectSearcher(query);
            foreach (ManagementObject info in searcher.Get())
            {
                results.Add(info.GetPropertyValue("SerialNumber").ToString());
                richTextBox1.Text += "Board SerialNumber:\t" + info.GetPropertyValue("SerialNumber").ToString() + "\n";
            }
            return results;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int num_physical_processors, num_cores, num_logical_processors;
            GetProcessorCounts(out num_physical_processors, out num_cores, out num_logical_processors);

            richTextBox1.Text += "PhysicalProcessors\t" + num_physical_processors.ToString() + "\n";
            richTextBox1.Text += "Cores\t" + num_cores.ToString() + "\n";
            richTextBox1.Text += "LogicalProcessors\t" + num_logical_processors.ToString() + "\n";
        }

        // Return the numbers of physical processors, cores,
        // and logical processors.
        private void GetProcessorCounts(out int num_physical_processors,
            out int num_cores, out int num_logical_processors)
        {
            string query;
            ManagementObjectSearcher searcher;

            // Get the number of physical processors.
            num_physical_processors = 0;
            query = "SELECT * FROM Win32_ComputerSystem";
            searcher = new ManagementObjectSearcher(query);
            foreach (ManagementObject sys in searcher.Get())
                num_physical_processors =
                    int.Parse(sys["NumberOfProcessors"].ToString());

            // Get the number of cores.
            query = "SELECT * FROM Win32_Processor";
            num_cores = 0;
            searcher = new ManagementObjectSearcher(query);
            foreach (ManagementObject proc in searcher.Get())
                num_cores += int.Parse(proc["NumberOfCores"].ToString());

            num_logical_processors = Environment.ProcessorCount;
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取硬碟資訊\n";
            richTextBox1.Text += "\nWin32_DiskDrive\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject mo in mos.Get())
            {
                //印出所有參數名稱及內容
                foreach (var prop in mo.Properties)
                {
                    richTextBox1.Text += prop.Name + ": " + prop.Value + "\n";

                    ListViewItem i1 = new ListViewItem(prop.Name);
                    ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                    sub_i1a.Text = (prop.Value==null)?String.Empty:prop.Value.ToString();
                    i1.SubItems.Add(sub_i1a);
                    listView1.Items.Add(i1);
                }
            }
            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            string win32_command;

            richTextBox1.Text += "選擇了： " + comboBox1.SelectedItem + "\n";

            win32_command = "SELECT * FROM " + comboBox1.SelectedItem;

            //richTextBox1.Text += "\n獲取硬碟資訊\n";
            //richTextBox1.Text += "\nWin32_DiskDrive\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher(win32_command);

            foreach (ManagementObject mo in mos.Get())
            {
                //印出所有參數名稱及內容
                foreach (var prop in mo.Properties)
                {
                    richTextBox1.Text += prop.Name + ": " + prop.Value + "\n";

                    ListViewItem i1 = new ListViewItem(prop.Name);
                    ListViewItem.ListViewSubItem sub_i1a = new ListViewItem.ListViewSubItem();
                    sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
                    i1.SubItems.Add(sub_i1a);
                    listView1.Items.Add(i1);
                }
            }
            //設置ListView最後一行可見
            listView1.Items[listView1.Items.Count - 1].EnsureVisible();
        }
    }
}
