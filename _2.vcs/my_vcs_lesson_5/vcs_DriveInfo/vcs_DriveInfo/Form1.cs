using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DriveInfo

namespace vcs_DriveInfo
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void HDD_Scan()
        {
            cmbDrive.Items.Clear();   //Clear All items in Combobox
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo drive in drives)
            {
                cmbDrive.Items.Add(drive.ToString());
            }

            if (drives.Length > 0)
                cmbDrive.Text = drives[0].ToString();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            HDD_Scan();
        }

        private void cmbDrive_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            DriveInfo drive = new DriveInfo(cmbDrive.SelectedItem.ToString());
            if (drive.IsReady == true)
            {
                richTextBox1.Text += "磁碟 : " + drive.ToString() + "\n";
                richTextBox1.Text += "名稱 : " + drive.Name + "\n";
                richTextBox1.Text += "標籤 : " + drive.VolumeLabel + "\n";
                richTextBox1.Text += "類型 : " + drive.DriveType + "\n";
                richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                richTextBox1.Text += "磁碟大小 : " + drive.TotalSize.ToString() + "\n";
                richTextBox1.Text += "剩餘空間 : " + drive.AvailableFreeSpace.ToString() + "\n";
                richTextBox1.Text += "可用總空間 : " + drive.TotalFreeSpace.ToString() + "\n";
                richTextBox1.Text += "根目錄 : " + drive.RootDirectory + "\n";
            }
            else
                richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            HDD_Scan();
        }
    }
}
