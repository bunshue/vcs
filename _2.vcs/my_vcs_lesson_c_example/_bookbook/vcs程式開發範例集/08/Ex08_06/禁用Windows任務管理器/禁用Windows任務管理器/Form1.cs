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
namespace 禁用Windows任務管理器
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
            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey(@"SOFTWARE\Microsoft\Windows\CurrentVersion\policies\system");
            mreg.SetValue("DisableTaskMgr", 1);
            mreg.Close();

            mreg = Registry.CurrentUser;
            mreg = mreg.CreateSubKey(@"SOFTWARE\Microsoft\Windows\CurrentVersion\policies\system");
            mreg.SetValue("DisableTaskMgr", 1);
            mreg.Close();
            if (MessageBox.Show("設定完畢！") == DialogResult.OK)
            {
                RefreshSystem();
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey(@"SOFTWARE\Microsoft\Windows\CurrentVersion\policies\system");
            mreg.SetValue("DisableTaskMgr", 0);
            mreg.Close();

            mreg = Registry.CurrentUser;
            mreg = mreg.CreateSubKey(@"SOFTWARE\Microsoft\Windows\CurrentVersion\policies\system");
            mreg.SetValue("DisableTaskMgr", 0);
            mreg.Close();
            if (MessageBox.Show("設定完畢！") == DialogResult.OK)
            {
                RefreshSystem();
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
