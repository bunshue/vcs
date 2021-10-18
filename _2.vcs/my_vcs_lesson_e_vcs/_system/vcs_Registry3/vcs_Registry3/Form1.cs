using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;  //for Registry

namespace vcs_Registry3
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //讀
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //寫

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //刪除

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //判斷

        }

        /*
        C#操作註冊表
        以下從『讀』『寫』『刪除』『判斷』四個事例實現對註冊表的簡單操作
        */

        //1.讀取指定名稱的註冊表的值    
        private string GetRegistData(string name)
        {
            string registData;
            RegistryKey hkml = Registry.LocalMachine;
            RegistryKey software = hkml.OpenSubKey("SOFTWARE", true);
            RegistryKey aimdir = software.OpenSubKey("XXX", true);
            registData = aimdir.GetValue(name).ToString();
            return registData;
        }
        //以上是讀取的註冊表中HKEY_LOCAL_MACHINE\SOFTWARE目錄下的XXX目錄中名稱為name的註冊表值；    

        //2.向註冊表中寫數據    
        private void WTRegedit(string name, string tovalue)
        {
            RegistryKey hklm = Registry.LocalMachine;
            RegistryKey software = hklm.OpenSubKey("SOFTWARE", true);
            RegistryKey aimdir = software.CreateSubKey("XXX");
            aimdir.SetValue(name, tovalue);
        }
        //以上是在註冊表中HKEY_LOCAL_MACHINE\SOFTWARE目錄下新建XXX目錄並在此目錄下創建名稱為name值為tovalue的註冊表項；    

        //3.刪除註冊表中指定的註冊表項    
        private void DeleteRegist(string name)
        {
            string[] aimnames;
            RegistryKey hkml = Registry.LocalMachine;
            RegistryKey software = hkml.OpenSubKey("SOFTWARE", true);
            RegistryKey aimdir = software.OpenSubKey("XXX", true);
            aimnames = aimdir.GetSubKeyNames();
            foreach (string aimKey in aimnames)
            {
                if (aimKey == name)
                    aimdir.DeleteSubKeyTree(name);
            }
        }
        //以上是在註冊表中HKEY_LOCAL_MACHINE\SOFTWARE目錄下XXX目錄中刪除名稱為name註冊表項；    

        //4.判斷指定註冊表項是否存在    
        private bool IsRegeditExit(string name)
        {
            bool _exit = false;
            string[] subkeyNames;
            RegistryKey hkml = Registry.LocalMachine;
            RegistryKey software = hkml.OpenSubKey("SOFTWARE", true);
            RegistryKey aimdir = software.OpenSubKey("XXX", true);
            subkeyNames = aimdir.GetSubKeyNames();
            foreach (string keyName in subkeyNames)
            {
                if (keyName == name)
                {
                    _exit = true;
                    return _exit;
                }
            }
            return _exit;
        }
        //以上是在註冊表中HKEY_LOCAL_MACHINE\SOFTWARE目錄下XXX目錄中判斷名稱為name註冊表項是否存在，這一方法在刪除註冊表時已經存在，在新建一註冊表項時也應有相應判斷；
 

    }
}
