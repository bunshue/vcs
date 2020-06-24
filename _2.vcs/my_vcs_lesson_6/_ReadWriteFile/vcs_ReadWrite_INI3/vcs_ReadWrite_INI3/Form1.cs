using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport
using System.IO;    //for File

namespace vcs_ReadWrite_INI3
{
    public partial class Form1 : Form
    {
        public string filename = "c:\\______test_files\\__RW\\_ini\\language.ini";//要注意全域變數都是放在public Form1()上面

        SetupIniIP ini = new SetupIniIP();

        public Form1()
        {
            InitializeComponent();
        }

        public class SetupIniIP
        {
            public string path;
            [DllImport("kernel32", CharSet = CharSet.Unicode)]
            private static extern long WritePrivateProfileString(string section,
            string key, string val, string filePath);
            [DllImport("kernel32", CharSet = CharSet.Unicode)]
            private static extern int GetPrivateProfileString(string section,
            string key, string def, StringBuilder retVal,
            int size, string filePath);
            public void IniWriteValue(string Section, string Key, string Value, string inipath)
            {
                WritePrivateProfileString(Section, Key, Value, inipath);
            }
            public string IniReadValue(string Section, string Key, string inipath)
            {
                StringBuilder temp = new StringBuilder(255);
                int i = GetPrivateProfileString(Section, Key, "", temp, 255, inipath);
                return temp.ToString();
            }
        }


        private void button2_Click(object sender, EventArgs e)
        {
            try
            {
                if (File.Exists(filename))
                {
                    textBox1.Text = ini.IniReadValue("Language", "lang1", filename);
                    textBox2.Text = ini.IniReadValue("Language", "lang2", filename);
                    richTextBox1.Text += ini.IniReadValue("Language", "lang1", filename) + "\n";
                    richTextBox1.Text += ini.IniReadValue("Language", "lang2", filename) + "\n";
                }
            }
            catch (Exception)
            {
                throw;
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            ini.IniWriteValue("Language", "lang1", textBox1.Text, filename);
            ini.IniWriteValue("Language", "lang2", textBox2.Text, filename);

        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "刪除\tTBD\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            textBox1.Clear();
            textBox2.Clear();
        }
    }
}
