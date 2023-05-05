using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;


using System.Diagnostics;
//using Microsoft.Win32;
using System.IO;
using System.Runtime.InteropServices;

namespace vcs_ReadWrite_INI4
{
    public partial class Form1 : Form
    {
        string ini_filename = @"C:/_git/vcs/_1.data/______test_files1/__RW/_ini/vcs_ReadWrite_INI4.ini";

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Read ini data from " + ini_filename + "\n";

            textBox1.Text = GetPrivateProfileString("version", "ver");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Write ini data to " + ini_filename + "\n";

            string iniValue = textBox1.Text;
            if (iniValue != "")
            {
                WritePrivateProfileString("version", "ver", iniValue);
                if (WritePrivateProfileString("version", "ver", iniValue) != 0)
                {
                    richTextBox1.Text += "寫入INI檔完成\n";
                }
            }
            else
            {
                richTextBox1.Text += "請輸入版本號\n";
            }
        }

        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);

        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(string section, string key, string value, string filePath);

        /// <summary>
        /// 从Ini文件获取数据
        /// </summary>
        /// <param name="section">应用程序</param>
        /// <param name="key">键的名称</param>
        /// <returns>键的值</returns>
        private string GetPrivateProfileString(string section, string key)
        {
            int nCapacity = 255;
            StringBuilder temp = new StringBuilder(nCapacity);
            int i = GetPrivateProfileString(section, key, "", temp, nCapacity, ini_filename);

            if (i < 0)
                return "";

            return temp.ToString();
        }

        /// <summary>
        /// 向Ini文件中写入值
        /// </summary>
        /// <param name="section">应用程序</param>
        /// <param name="key">键的名称</param>
        /// <param name="value">键的值</param>
        /// <returns>执行成功为True，失败为False。</returns>
        public long WritePrivateProfileString(string section, string key, string value)
        {
            if (section.Trim().Length <= 0 || key.Trim().Length <= 0 || value.Trim().Length <= 0)
                return 0;

            return WritePrivateProfileString(section, key, value, ini_filename);
        } 




    }
}
