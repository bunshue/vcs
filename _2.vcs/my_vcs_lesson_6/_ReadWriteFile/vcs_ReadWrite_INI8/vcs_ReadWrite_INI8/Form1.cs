using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport

namespace vcs_ReadWrite_INI8
{
    public partial class Form1 : Form
    {
        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);
        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);

        public void IniWriteValue(string Section, string Key, string Value, string filepath)//對ini文件進行寫操作的函數
        {
            WritePrivateProfileString(Section, Key, Value, filepath);
            richTextBox1.Text += "write to " + filepath + "\n";
        }

        public string IniReadValue(string Section, string Key, string filepath)//對ini文件進行讀操作的函數
        {
            StringBuilder temp = new StringBuilder(255);
            int i = GetPrivateProfileString(Section, Key, "", temp, 255, filepath);
            return temp.ToString();
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //read
            string filename = @"C:\______test_files1\__RW\_ini\ConnectString.ini";
            richTextBox1.Text += IniReadValue("ConnectString", "DataBase", filename) + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //write
            string filename = @"C:\______test_files1\__RW\_ini\ConnectString2.ini";
            IniWriteValue("ConnectString", "DataBase", this.textBox1.Text, filename);
        }
    }
}
