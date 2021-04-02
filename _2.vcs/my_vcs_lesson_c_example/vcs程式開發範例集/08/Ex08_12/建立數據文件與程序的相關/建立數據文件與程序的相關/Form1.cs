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
namespace 建立數據文件與程序的相關
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
            try
            {
                string notepath = @"C:\WINDOWS\notepad.exe";
                string extName = ".ls";
                string mtype = "我定義的類型";
                string mContent = "text/plain";
                RegistryKey mreg;
                mreg = Registry.ClassesRoot;
                mreg = mreg.CreateSubKey(extName);
                mreg.SetValue("",mtype);
                mreg.SetValue("Content Type", mContent);
                mreg = mreg.CreateSubKey("shell\\open\\command");
                mreg.SetValue("",notepath+" %1");
                mreg.Close();
                if (MessageBox.Show("設定完畢") == DialogResult.OK)
                {
                    RefreshSystem();
                }
            }
            catch(Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            RegistryKey mreg;
            string extName = ".ls";
            mreg = Registry.ClassesRoot;
            mreg = mreg.CreateSubKey(extName+"\\shell\\open");
            mreg.DeleteSubKey("command");
            mreg.Close();
            if (MessageBox.Show("設定完畢") == DialogResult.OK)
            {
                RefreshSystem();
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}
