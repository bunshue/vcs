using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;   //for DllImport

namespace vcs_test_all_24_DllImport_HDD
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        [DllImport("kernel32.dll")]
        private static extern bool GetDiskFreeSpaceEx(
        string lpDirectoryName, out ulong lpFreeBytesAvailable, out ulong lpTotalNumberOfBytes, out ulong lpTotalNumberOfFreeBytes);

        private void button1_Click(object sender, EventArgs e)
        {
            ulong freesize;
            freesize = GetFreeSpace("C");
            richTextBox1.Text += "磁碟C剩餘空間: " + freesize.ToString() + " bytes\n";
            freesize = GetFreeSpace("D");
            richTextBox1.Text += "磁碟D剩餘空間: " + freesize.ToString() + " bytes\n";
            freesize = GetFreeSpace("G");
            richTextBox1.Text += "磁碟G剩餘空間: " + freesize.ToString() + " bytes\n";
        }

        /// <summary>
        /// 取得磁碟剩餘空間
        /// </summary>
        /// <param name="driveDirectoryName">驅動器名</param>
        /// <returns>剩餘空間</returns>
        private static ulong GetFreeSpace(string driveDirectoryName)
        {
            ulong freeBytesAvailable, totalNumberOfBytes, totalNumberOfFreeBytes;
            if (!driveDirectoryName.EndsWith(":\\"))
            {
                driveDirectoryName += ":\\";
            }
            GetDiskFreeSpaceEx(driveDirectoryName, out freeBytesAvailable, out totalNumberOfBytes, out totalNumberOfFreeBytes);
            return freeBytesAvailable;
        }

    }
}
