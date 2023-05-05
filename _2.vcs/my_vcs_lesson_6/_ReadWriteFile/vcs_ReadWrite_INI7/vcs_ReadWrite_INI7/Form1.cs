using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;
using System.IO;


/*
    ini內容

    [session name]

    key1 = value1

    key2 = value2
*/

namespace vcs_ReadWrite_INI7
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
            string filename = @"C:\_git\vcs\_1.data\______test_files1\__RW\_ini\vcs_ReadWrite_INI1a.ini";
            IniFile ini = new IniFile(filename);

            string session_name = "SearchFolders";
            string key = "Folder0";
            string data = ini.ReadIni(session_name, key);
            richTextBox1.Text += "get result : " + data + "\n";

        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }
    }

    public class IniFile
    {
        [DllImport("kernel32")]
        private static extern long WritePrivateProfileString(string section, string key, string val, string filePath);

        [DllImport("kernel32")]
        private static extern int GetPrivateProfileString(string section, string key, string def, StringBuilder retVal, int size, string filePath);

        private string filepath;

        public IniFile(string fileName)
        {
            this.filepath = Path.GetFullPath(fileName);
        }

        public void WriteIni(string section, string key, string val)
        {
            WritePrivateProfileString(section, key, val, filepath);
        }

        public string ReadIni(string section, string key)
        {
            StringBuilder temp = new StringBuilder(255);
            GetPrivateProfileString(section, key, "", temp, 255, filepath);
            return temp.ToString();
        }
    }
}

