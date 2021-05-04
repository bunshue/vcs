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
namespace 隱藏桌面快捷方式圖標的小箭頭
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
            mreg = Registry.ClassesRoot;
            mreg = mreg.CreateSubKey("piffile");
            mreg.DeleteValue("IsShortcut");
            mreg.Close();
            RegistryKey mreg1;
            mreg1 = Registry.ClassesRoot;
            mreg1 = mreg1.CreateSubKey("lnkfile");
            mreg1.DeleteValue("IsShortcut");
            mreg1.Close();
            if (MessageBox.Show("設定完畢") == DialogResult.OK)
            {
                RefreshSystem();
            }
        }
    }
}
