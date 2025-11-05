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

            string[] win32_cmd = new string[] { "Win32_BaseBoard", "Win32_Battery", "Win32_BIOS", "Win32_DiskDrive", "Win32_IDEController", "Win32_NetworkAdapter", "Win32_NetworkAdapterConfiguration", "Win32_Processor", "Win32_SerialPort", "Win32_USBController", "Win32_USBHub", "Win32_VideoController", "Win32_VideoSettings" };
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
                    sub_i1a.Text = (prop.Value == null) ? String.Empty : prop.Value.ToString();
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
