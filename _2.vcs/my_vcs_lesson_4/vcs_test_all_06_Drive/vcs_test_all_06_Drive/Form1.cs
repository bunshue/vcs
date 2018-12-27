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
                    richTextBox1.Text += "磁碟大小:  " + d.TotalSize + " bytes" + "\n";
                    richTextBox1.Text += "剩餘空間:  " + d.AvailableFreeSpace.ToString() + " bytes" + "\n";
                    richTextBox1.Text += "總剩餘空間(含磁碟配碟):        " + d.TotalFreeSpace.ToString() + " bytes" + "\n";
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

    }
}
