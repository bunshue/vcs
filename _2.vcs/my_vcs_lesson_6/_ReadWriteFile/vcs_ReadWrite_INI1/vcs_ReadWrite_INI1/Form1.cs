using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;

namespace vcs_ReadWrite_INI1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private string filename = "c:\\______test_files\\__RW\\_ini\\vcs_ReadWrite_INI1a.ini";

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern bool WritePrivateProfileString(string lpAppName, string lpKeyName, string lpString, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileString(string lpAppName, string lpKeyName, string lpDefault, StringBuilder lpReturnedString, int nSize, string lpFileName);

        [DllImport("kernel32", CharSet = CharSet.Unicode, SetLastError = true)]
        private static extern int GetPrivateProfileInt(string lpAppName, string lpKeyName, int lpDefault, string lpFileName);

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            string filename = "c:\\______test_files\\__RW\\_ini\\vcs_ReadWrite_INI1b.ini";
            richTextBox1.Text += "Write ini data to " + filename + "\n";
            WritePrivateProfileString("Demo", "abc", "123", filename);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string filename = "c:\\______test_files\\__RW\\_ini\\vcs_ReadWrite_INI1b.ini";
            richTextBox1.Text += "Read ini data from " + filename + "\n";
            StringBuilder temp = new StringBuilder();
            GetPrivateProfileString("Demo", "abc", "", temp, 255, filename);
            richTextBox1.Text += "get value = " + temp + "\n";
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
                GetPrivateProfileString(Section, Key, "", sbResult, 255, this.filename);
                return (sbResult.Length > 0) ? sbResult.ToString() : DefaultValue;
            }
            catch
            {
                return string.Empty;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string filename = "c://______test_files//__RW//_ini//vcs_ReadWrite_INI1c.ini";
            richTextBox1.Text += "Write ini data to " + filename + "\n";

            string strName;
            int nAge;
            strName = "張三";
            nAge = 12;
            WritePrivateProfileString("StudentInfo", "Name", strName, filename);
            WritePrivateProfileString("StudentInfo", "Age", nAge.ToString(), filename);
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string filename = "c://______test_files//__RW//_ini//vcs_ReadWrite_INI1c.ini";
            richTextBox1.Text += "Read ini data from " + filename + "\n";

            //TBD
        }
    }
}
