using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_ReadWrite_INI
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string _FilePath = "c:\\______test_vcs\\sample.ini";

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern bool WritePrivateProfileString(
        string lpAppName, string lpKeyName, string lpString, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileString(
        string lpAppName, string lpKeyName, string lpDefault, StringBuilder lpReturnedString,
        int nSize, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileInt(
        string lpAppName, string lpKeyName, int lpDefault, string lpFileName);

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "write data to test_ini.ini.\n";
            WritePrivateProfileString("Demo", "abc", "123", "c:\\______test_vcs\\test_ini.ini");

        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "read data from test_ini.ini.\n";
            StringBuilder temp = new StringBuilder();
            GetPrivateProfileString("Demo", "abc", "", temp, 255, "c:\\______test_vcs\\test_ini.ini");
            richTextBox1.Text += "get value = " + temp + "\n";

            //Console.WriteLine(temp);
            //Console.ReadLine();


        }

        /// <summary>
        /// 取得 Key 相對的 Value 值，若沒有則使用預設值(DefaultValue)。
        /// </summary>
        /// <param name="Section">Section。</param>
        /// <param name="Key">Key。</param>
        /// <param name="DefaultValue">DefaultValue。</param>        
        public string getKeyValue(string Section, string Key, string DefaultValue)
        {
            StringBuilder sbResult = null;
            try
            {
                sbResult = new StringBuilder(255);
                GetPrivateProfileString(Section, Key, "", sbResult, 255, this._FilePath);
                return (sbResult.Length > 0) ? sbResult.ToString() : DefaultValue;
            }
            catch
            {
                return string.Empty;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "write data to student.ini.\n";
            string strName, strTemp;
            int nAge;
            strName = "張三";
            nAge = 12;
            WritePrivateProfileString("StudentInfo", "Name", strName, "c://______test_vcs//student.ini");
            WritePrivateProfileString("StudentInfo", "Age", nAge.ToString(), "c://______test_vcs//student.ini");


        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "read data from student.ini.\n";





        }

    }
}
