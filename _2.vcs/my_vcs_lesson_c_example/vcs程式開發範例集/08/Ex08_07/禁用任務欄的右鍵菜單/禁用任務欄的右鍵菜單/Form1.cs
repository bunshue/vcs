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
namespace 禁用任務欄的右鍵菜單
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
                RegistryKey mreg;
                mreg = Registry.CurrentUser;
                mreg = mreg.CreateSubKey(@"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer");
                mreg.SetValue("notraycontextmenu", 1);
                mreg.Close();
                if (MessageBox.Show("設定完畢！") == DialogResult.OK)
                {
                    RefreshSystem();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                RegistryKey mreg;
                mreg = Registry.CurrentUser;
                mreg = mreg.CreateSubKey(@"Software\Microsoft\Windows\CurrentVersion\Policies\Explorer");
                mreg.DeleteValue("notraycontextmenu");
                mreg.Close();
                if (MessageBox.Show("設定完畢！") == DialogResult.OK)
                {
                    RefreshSystem();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }
    }
}
