using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Management;    //for ManagementObject, 需加入參考System.Management
using System.IO;            //for DriveInfo

namespace vcs_test_all_06_Drive
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
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

        private void button1_Click(object sender, EventArgs e)
        {
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            /*
            //法一
            comboBox_drive.Items.Clear();
            DriveInfo[] drives = DriveInfo.GetDrives();
            foreach (DriveInfo drive in drives)
            {
                comboBox_drive.Items.Add(drive.ToString());
            }
            if (comboBox_drive.Items.Count > 0)
                comboBox_drive.Text = comboBox_drive.Items[0].ToString();
            */

            //法二
            comboBox_drive.Items.Clear();
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject disk in searcher.Get())
            {
                comboBox_drive.Items.Add(disk["Name"].ToString());
            }

            if (comboBox_drive.Items.Count > 0)
                comboBox_drive.Text = comboBox_drive.Items[0].ToString();

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //使用System.IO.DriveInfo來遍歷磁片及其分區資訊
            //引用System.IO後即可調用DriveInfo類來對磁碟空間資訊進行遍歷了，此外DriveInfo只有在普通WINFORM中可以調用，WINCE專案中未封裝此類。
            //獲取磁片設備
            DriveInfo[] allDrives = DriveInfo.GetDrives();
            richTextBox1.Text = "系統共有 " + allDrives.Length.ToString() + " 部磁碟機" + "\n";
            //遍歷磁片
            foreach (DriveInfo d in allDrives)
            {
                richTextBox1.Text += d.Name + "        ";
            }

            richTextBox1.Text += "\n";

            //取得單一磁碟資訊：
            //System.IO.DriveInfo di = new System.IO.DriveInfo(@"C:\");

            //取得所有磁碟資訊：
            foreach (DriveInfo d in allDrives)
            {
                richTextBox1.Text += "磁碟分割號:  " + d.Name + " 槽\n";
                richTextBox1.Text += "RootDirectory:  " + d.RootDirectory + "\n";
                richTextBox1.Text += "DriveType:  " + d.DriveType;
                if (d.IsReady == true)  //使用IsReady屬性判斷裝置是否就緒
                {
                    richTextBox1.Text += "\n";
                    richTextBox1.Text += "磁碟標籤:  " + d.VolumeLabel + "\n";
                    richTextBox1.Text += "磁碟類型:  " + d.DriveType.ToString() + "\n";
                    richTextBox1.Text += "磁碟格式:  " + d.DriveFormat + "\n";
                    richTextBox1.Text += "已使用空間 :\t" + (d.TotalSize - d.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(d.TotalSize - d.AvailableFreeSpace)) + "\n";
                    richTextBox1.Text += "可用空間 :\t\t" + d.AvailableFreeSpace.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(d.AvailableFreeSpace)) + "\n";
                    richTextBox1.Text += "磁碟容量 :\t\t" + d.TotalSize.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(d.TotalSize)) + "\n";
                }
                else
                {
                    richTextBox1.Text += "\n    Not ready\n";
                }
                richTextBox1.Text += "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void comboBox_drive_SelectedIndexChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "選中 : " + comboBox_drive.Text + "\n";

            DriveInfo drive = new DriveInfo(comboBox_drive.Text);

            if (drive.IsReady)
            {
                richTextBox1.Text += "磁碟 : " + drive.ToString() + "\n";
                richTextBox1.Text += "標籤 : " + drive.VolumeLabel + "\n";
                richTextBox1.Text += "名稱 : " + drive.Name + "\n";

                richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";
                richTextBox1.Text += "可用空間 :\t\t" + drive.AvailableFreeSpace.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)) + "\n";
                richTextBox1.Text += "磁碟容量 :\t\t" + drive.TotalSize.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize)) + "\n";

                richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                richTextBox1.Text += "型態 : " + drive.DriveType + "\n";
                richTextBox1.Text += "根目錄 : " + drive.RootDirectory + "\n";
            }
            else
            {
                richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒" + "\n";
            }  


        }

        private void button1_Click_1(object sender, EventArgs e)
        {
            //找資料夾所在的硬碟的標籤
            string path = String.Empty;

            path = "C:\\______test_files\\_case1";

            richTextBox1.Text += "\n資料夾路徑" + path + "\n";

            if (File.Exists(path))
            {
                // This path is a file
                richTextBox1.Text += "是個檔案\n";
            }
            else if (Directory.Exists(path))
            {
                // This path is a directory
                DirectoryInfo d = new DirectoryInfo(path);//輸入檔案夾
                /*
                richTextBox1.Text += "Name : " + d.Name + "\n";
                richTextBox1.Text += "FullName : " + d.FullName + "\n";
                richTextBox1.Text += "Parent : " + d.Parent + "\n";
                richTextBox1.Text += "Root : " + d.Root + "\n";
                */

                DriveInfo drive = new DriveInfo(d.Root.ToString());

                if (drive.IsReady)
                {
                    richTextBox1.Text += "磁碟 : " + drive.ToString() + "\n";
                    richTextBox1.Text += "標籤 : " + drive.VolumeLabel + "\n";
                    //richTextBox1.Text += "名稱 : " + drive.Name + "\n";
                    richTextBox1.Text += "已使用空間 :\t" + (drive.TotalSize - drive.AvailableFreeSpace).ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize - drive.AvailableFreeSpace)) + "\n";
                    richTextBox1.Text += "可用空間 :\t\t" + drive.AvailableFreeSpace.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.AvailableFreeSpace)) + "\n";
                    richTextBox1.Text += "磁碟容量 :\t\t" + drive.TotalSize.ToString() + " 個位元組\t" + ByteConversionGBMBKB(Convert.ToInt64(drive.TotalSize)) + "\n";

                    /*
                    richTextBox1.Text += "格式 : " + drive.DriveFormat + "\n";
                    richTextBox1.Text += "型態 : " + drive.DriveType + "\n";
                    richTextBox1.Text += "根目錄 : " + drive.RootDirectory + "\n";
                    */
                }
                else
                {
                    richTextBox1.Text += "磁碟 " + drive.ToString() + "未就緒" + "\n";
                }
            }
            else
            {
                //Console.WriteLine("{0} is not a valid file or directory.", path);
                richTextBox1.Text += "非合法路徑或檔案\n";
            }

        }

    }
}
