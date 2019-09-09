using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI

namespace vcs_WMI_Win32_PageFile
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n獲取頁面文檔\n";
            richTextBox1.Text += "\nWin32_PageFile\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PageFile");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "FileName: " + mo["Name"].ToString() + "\n";　　//頁面文檔
                //richTextBox1.Text += "FileName: " + mo["Manufacturer"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Status"].ToString() + "\n";
                //richTextBox1.Text += "FileName: " + mo["Version"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Caption"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Description"].ToString() + "\n";
                //richTextBox1.Text += "FileName: " + mo["CompressionMethod"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["CSCreationClassName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["CSName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Drive"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["CreationClassName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["EightDotThreeFileName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FileType"].ToString() + "\n";
                //richTextBox1.Text += "FileName: " + mo["EncryptionMethod"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Extension"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FileName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FSCreationClassName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["FSName"].ToString() + "\n";
                richTextBox1.Text += "FileName: " + mo["Path"].ToString() + "\n";


                long FileSize = mo["FileSize"] == null ? 0 : long.Parse(mo["FileSize"].ToString());//頁面文檔大小
                //計算
                richTextBox1.Text += "FileSize: " + (FileSize / 1024 / 1024).ToString("#0.00") + "G" + "\n";

                richTextBox1.Text += "FileSize: " + mo["FileSize"].ToString() + "\n";
                //richTextBox1.Text += "InUseCount: " + mo["InUseCount"].ToString() + "\n";
                //richTextBox1.Text += "AccessMask: " + mo["AccessMask"].ToString() + "\n";
                //richTextBox1.Text += "FreeSpace: " + mo["FreeSpace"].ToString() + "\n";
                richTextBox1.Text += "InitialSize: " + mo["InitialSize"].ToString() + "\n";
                richTextBox1.Text += "MaximumSize: " + mo["MaximumSize"].ToString() + "\n";

                richTextBox1.Text += "InstallDate: " + mo["InstallDate"].ToString() + "\n";
                richTextBox1.Text += "CreationDate: " + mo["CreationDate"].ToString() + "\n";
                richTextBox1.Text += "LastAccessed: " + mo["LastAccessed"].ToString() + "\n";
                richTextBox1.Text += "LastModified: " + mo["LastModified"].ToString() + "\n";

            }


        }
    }
}
