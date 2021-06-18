using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using Microsoft.Win32;  //for RegistryKey

using System.Reflection;    //for Assembly

namespace 真的只是一個測試1
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
            string strpath = Environment.SystemDirectory + "\\music";
            richTextBox1.Text += "strpath = " + strpath + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string sText = this.Text;
            string sFullName = string.Format("{0} %1", Application.ExecutablePath);
            // Application.ExecutablePath 是程式執行檔的完整路徑檔案名稱
            // %1 表示傳入的檔案
            //if (this.rbFile.Checked)
            {
                // 加入檔案右鍵選單
                RegFile(sText, sFullName);
            }
            //else
            {
                // 加入目錄右鍵選單
                //RegDirectory(sText, sFullName);
            }
            MessageBox.Show("作業成功");

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得專案內所有表單名稱

            Assembly a = Assembly.GetExecutingAssembly();       //取得目前組件

            richTextBox1.Text += "目前組件 : " + a.ToString() + "\n";
            richTextBox1.Text += "CodeBase : " + a.CodeBase.ToString() + "\n";
            richTextBox1.Text += "FullName : " + a.FullName.ToString() + "\n";
            richTextBox1.Text += "Location : " + a.Location.ToString() + "\n";
            richTextBox1.Text += "GetType : " + a.GetType().ToString() + "\n";
            richTextBox1.Text += "GetType : " + a.GetName() + "\n";
            richTextBox1.Text += "GetType : " + a.ImageRuntimeVersion + "\n";

            foreach (Type t in a.GetTypes())                    //找尋組件內所有類別型態
            {
                richTextBox1.Text += t.ToString() + "\n";

                if (t.IsSubclassOf(typeof(Form)))           //如果父類別是繼承自Form的話
                {
                    //richTextBox1.Text += t.ToString() + "\n"; //列出該類別資訊

                }
            }

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {

        }

        private void RegFile(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"*\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue(string.Empty, sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }
        private void RegDirectory(string sText, string sFullName)
        {
            RegistryKey shell = Registry.ClassesRoot.OpenSubKey(@"directory\shell", true);
            RegistryKey custom = shell.CreateSubKey(sText);
            RegistryKey cmd = custom.CreateSubKey("command");
            cmd.SetValue("", sFullName);
            cmd.Close();
            custom.Close();
            shell.Close();
        }


    }
}
