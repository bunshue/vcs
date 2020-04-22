using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for FileVersionInfo

using System.Reflection;    //for Assembly

namespace WindowsFormsApplication1tmp
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //取得軟體版本
            richTextBox1.Text += "" + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //提供磁碟上實體檔案的版本資訊
            // Get the file version for the notepad.
            FileVersionInfo myFileVersionInfo = FileVersionInfo.GetVersionInfo(Environment.SystemDirectory + "\\Notepad.exe");

            // Print the file name and version number.
            richTextBox1.Text += "File: " + myFileVersionInfo.FileDescription + '\n' + "Version number: " + myFileVersionInfo.FileVersion + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得目前應用程式版本
            richTextBox1.Text += "Ver：" + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";

            //取得NOTEPAD版本資訊

            richTextBox1.Text += FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n";

        }


    }
}
