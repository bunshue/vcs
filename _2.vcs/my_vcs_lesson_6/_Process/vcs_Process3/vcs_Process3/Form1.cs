using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;

namespace vcs_Process3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
            list_all_processes();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        void list_all_processes()
        {
            listBox1.Items.Clear();

            richTextBox1.Text += "取得所有程序\n";
            Process[] processes = Process.GetProcesses(); //取得所有程序
            richTextBox1.Text += "系統中有： " + processes.Length.ToString() + " 個程序\n";

            foreach (Process process in processes)
            {
                //richTextBox1.Text += "A\t" + process.ProcessName + "\t";
                if (process.MainWindowTitle.Length > 0)
                {
                    //僅列出 有視窗 的Process
                    listBox1.Items.Add(process.ProcessName.ToString().Trim());
                    richTextBox1.Text += "取得 有視窗 的Process : " + process.ProcessName.ToString().Trim() + "\n";
                }
                else
                {
                    //richTextBox1.Text += "取得 無視窗 的Process : " + process.ProcessName.ToString().Trim() + "\n";
                }
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem == null)
                return;
            richTextBox1.Text += "欲關閉程序名稱 : " + listBox1.SelectedItem.ToString().Trim() + "\n";
            Process[] processes = Process.GetProcessesByName(listBox1.SelectedItem.ToString().Trim());
            foreach (Process process in processes)
            {
                process.CloseMainWindow();
            }
            listBox1.Items.Remove(listBox1.SelectedItem);//從listBox1中移除listBox1中選定的項

            richTextBox1.Text += "程序已關閉\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            list_all_processes();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (listBox1.SelectedItem == null)
                return;
            richTextBox1.Text += "selected = " + listBox1.SelectedItem.ToString() + "\n";
        }

    }
}
