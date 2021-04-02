using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;
namespace 設定IE瀏覽器的預設主頁
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            object strInfo=reg.GetValue("Start Page", "沒有值");
            this.textBox1.Text = (string)strInfo;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg.SetValue("Start Page", this.textBox2.Text, RegistryValueKind.String);
            MessageBox.Show("IE 目前的預設頁為\r\n" + this.textBox2.Text);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg.SetValue("Start Page", "about:blank", RegistryValueKind.String);
            MessageBox.Show("IE 目前的預設頁為\r\n" + "空白頁");
        }
    }
}