using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_DriveInfo2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo drive in drives)
            {
                cmbDrive.Items.Add(drive.ToString());
                richTextBox1.Text += "抓到磁碟分割區 : " + drive.ToString() + "\n";
            }
        }

        private void cmbDrive_SelectedIndexChanged(object sender, EventArgs e)
        {
            lbDriveInfo.Items.Clear();
            DriveInfo drive = new DriveInfo(cmbDrive.SelectedItem.ToString());
            if (drive.IsReady)
            {
                lbDriveInfo.Items.Add("磁碟 : " + drive.ToString());
                lbDriveInfo.Items.Add("標籤 : " + drive.VolumeLabel);
                lbDriveInfo.Items.Add("名稱 : " + drive.Name);
                lbDriveInfo.Items.Add("可用空間 : " + drive.AvailableFreeSpace);
                lbDriveInfo.Items.Add("可用大小 : " + drive.TotalSize);
                lbDriveInfo.Items.Add("可用總空間 : " + drive.TotalFreeSpace);
                lbDriveInfo.Items.Add("格式 : " + drive.DriveFormat);
                lbDriveInfo.Items.Add("型態 : " + drive.DriveType);
                lbDriveInfo.Items.Add("根目錄 : " + drive.RootDirectory);
            }
            else
            {
                lbDriveInfo.Items.Add("磁碟 " + drive.ToString() + "未就緒");
            }
        }
    }
}
