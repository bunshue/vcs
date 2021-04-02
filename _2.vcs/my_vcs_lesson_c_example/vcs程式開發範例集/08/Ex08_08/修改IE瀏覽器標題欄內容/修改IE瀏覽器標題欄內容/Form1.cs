using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;
namespace 修改IE瀏覽器標題欄內容
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg.SetValue("Window Title", this.textBox1.Text, RegistryValueKind.String);
            MessageBox.Show("修改成功");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            RegistryKey reg = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg.DeleteValue("Window Title",false);
            MessageBox.Show("恢復成功");
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }
}