using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using Microsoft.Win32;

namespace 進入Windows前發出警告
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            RegistryKey rkey = Registry.LocalMachine;
            RegistryKey rkeyInfo = rkey.CreateSubKey(@"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon");
            rkeyInfo.SetValue("LegalNoticeCaption", textBox1.Text, RegistryValueKind.String);
            rkeyInfo.SetValue("LegalNoticeText", textBox2.Text, RegistryValueKind.String);
            MessageBox.Show("已完成設定，請重新啟動計算機！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}