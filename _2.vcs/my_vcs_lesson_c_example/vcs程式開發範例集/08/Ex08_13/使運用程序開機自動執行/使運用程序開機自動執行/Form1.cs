using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.Win32;
using System.Diagnostics;
namespace 使運用程序開機自動執行
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        public void RefreshSystem()
        {
            Process[] mprocess;
            mprocess = Process.GetProcessesByName("explorer");
            foreach (Process mp in mprocess)
            {
                mp.Kill();
            }
        }
        private void button1_Click(object sender, EventArgs e)
        {
            if (openFileDialog1.ShowDialog() == DialogResult.OK)
            {
                textBox1.Text = openFileDialog1.FileName;
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {
                string strName = textBox1.Text.Trim();
                if (!System.IO.File.Exists(strName))
                    return;
                string strnewName = strName.Substring(strName.LastIndexOf("\\") + 1);
                RegistryKey RKey = Registry.LocalMachine.OpenSubKey("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", true);
                if (RKey == null)
                    RKey = Registry.LocalMachine.CreateSubKey("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run");
                RKey.SetValue(strnewName, strName);
                if (MessageBox.Show("設定完畢") == DialogResult.OK)
                {
                    RefreshSystem();
                }
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            if (textBox1.Text != "")
            {
                string strName = textBox1.Text.Trim();
                if (!System.IO.File.Exists(strName))
                    return;
                string strnewName = strName.Substring(strName.LastIndexOf("\\") + 1);
                RegistryKey RKey = Registry.LocalMachine.OpenSubKey("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", true);
                if (RKey == null)
                    RKey = Registry.LocalMachine.CreateSubKey("SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run");
                RKey.DeleteValue(strnewName, false);
                if (MessageBox.Show("設定完畢") == DialogResult.OK)
                {
                    RefreshSystem();
                }
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
