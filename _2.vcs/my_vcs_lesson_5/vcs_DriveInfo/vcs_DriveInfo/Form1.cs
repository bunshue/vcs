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

        const Int64 TB = (Int64)GB * 1024;//定義TB的計算常量
        const int GB = 1024 * 1024 * 1024;//定義GB的計算常量
        const int MB = 1024 * 1024;//定義MB的計算常量
        const int KB = 1024;//定義KB的計算常量
        public string ByteConversionGBMBKB(Int64 KSize)
        {
            if (KSize / TB >= 1)//如果目前Byte的值大於等於1TB
                return (Math.Round(KSize / (float)TB, 2)).ToString() + " TB";//將其轉換成TB
            else if (KSize / GB >= 1)//如果目前Byte的值大於等於1GB
                return (Math.Round(KSize / (float)GB, 2)).ToString() + " GB";//將其轉換成GB
            else if (KSize / MB >= 1)//如果目前Byte的值大於等於1MB
                return (Math.Round(KSize / (float)MB, 2)).ToString() + " MB";//將其轉換成MB
            else if (KSize / KB >= 1)//如果目前Byte的值大於等於1KB
                return (Math.Round(KSize / (float)KB, 2)).ToString() + " KB";//將其轉換成KGB
            else
                return KSize.ToString() + " Byte";//顯示Byte值
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

                richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";
                richTextBox1.Text += "可用空間 :\t\t" + drive.AvailableFreeSpace.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)) + "\n";
                richTextBox1.Text += "磁碟容量 :\t\t" + drive.TotalSize.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize)) + "\n";

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
