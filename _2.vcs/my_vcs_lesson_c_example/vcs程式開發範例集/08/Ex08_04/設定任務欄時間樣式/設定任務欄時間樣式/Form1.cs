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
namespace 設定任務欄時間樣式
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
            if (comboBox1.Text != "")
            {
                RegistryKey mreg;
                mreg = Registry.CurrentUser;
                mreg = mreg.CreateSubKey(@"Control Panel\International");
                mreg.SetValue("sTimeFormat",comboBox1.Text.Trim());
                mreg.Close();
                if (MessageBox.Show("設定完畢") == DialogResult.OK)
                {
                    RefreshSystem();
                }
            }
        }
    }
}
