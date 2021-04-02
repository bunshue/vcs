using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;
namespace 禁止修改IE瀏覽器主頁
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Policies\Microsoft\Internet Explorer\Control Panel");
            reg.SetValue("HomePage",1,RegistryValueKind.DWord);
            MessageBox.Show("禁止修改IE主頁設定成功");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Policies\Microsoft\Internet Explorer\Control Panel");
            reg.SetValue("HomePage", 0, RegistryValueKind.DWord);
            MessageBox.Show("啟動IE主頁設定成功");
        }
    }
}