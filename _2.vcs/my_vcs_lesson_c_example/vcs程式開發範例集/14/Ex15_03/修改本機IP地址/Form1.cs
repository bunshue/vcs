using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Security.Permissions;
using Microsoft.Win32;
namespace 修改本機IP地址
{
    
    public partial class Form1 : Form
    {
        static string strnew = null;
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                RegistryKey reg = Registry.LocalMachine.OpenSubKey(@"System\CurrentControlSet\Services\Tcpip\Linkage");
                string []str= (String[])reg.GetValue("Route");
                strnew = str[0].Substring(1, str[0].Length - 2);
                string path = @"System\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\" + strnew;
                RegistryKey regIp = Registry.LocalMachine.OpenSubKey(path);
                string[] strIP = (String[])regIp.GetValue("IPAddress", "Null", RegistryValueOptions.None);
                this.textBox1.Text = strIP[0];
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            if (this.textBox1.Enabled == false)
            {
                this.button1.Text = "確定";
                this.textBox1.Enabled=true;
                return;
            }
            if (this.textBox1.Enabled == true)
            {
                string[] str = new string[1];
                str[0] = this.textBox1.Text;
                string path = @"System\CurrentControlSet\Services\Tcpip\Parameters\Interfaces\" + strnew;
                Registry.LocalMachine.CreateSubKey(path).SetValue("IPAddress", str, RegistryValueKind.MultiString);
                this.textBox1.Enabled = false;
                this.button1.Text = "設定";
                MessageBox.Show("修改成功--請重新啟動計算機");

            }
        }
    }
}