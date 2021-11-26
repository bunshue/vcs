using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_ListViewK_DiskInfo
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
            listView1.View = View.Details;
            ColumnHeader ch1 = new ColumnHeader();
            ch1.Text = "Disk Name";
            ch1.Width = 85;
            listView1.Columns.Add(ch1);
            ColumnHeader ch2 = new ColumnHeader();
            ch2.Text = "Type";
            ch2.Width = 85;
            listView1.Columns.Add(ch2);
            ColumnHeader ch3 = new ColumnHeader();
            ch3.Text = "All Size";
            ch3.Width = 85;
            listView1.Columns.Add(ch3);
            ColumnHeader ch4 = new ColumnHeader();
            ch4.Text = "Free Size";
            ch4.Width = 85;
            listView1.Columns.Add(ch4);
            string[] drive = Environment.GetLogicalDrives();
            for (int i = 0; i < drive.Length; i++)
            {
                //實例化一個listview對象的子項
                ListViewItem lvi1 = new ListViewItem();
                lvi1.Text = drive[i];//第一列數據
                lvi1.SubItems.Add(i.ToString());//第二列
                lvi1.SubItems.Add(GetHardDiskTotalSize(i).ToString() + " G");//第三列
                lvi1.SubItems.Add(GetHardDiskFreeSize(i).ToString() + " G");//第四列
                listView1.Items.Add(lvi1);//添加列
            }



        }

        /// <summary>
        /// 獲取磁盤總空間
        /// </summary>
        /// <param name="i">獲取磁盤需要的下標 0 c盤 1 d盤</param>
        /// <returns>磁盤總空間 long類型</returns>
        public static long GetHardDiskTotalSize(int i)
        {
            long totalSize = new long();
            System.IO.DriveInfo[] drives = System.IO.DriveInfo.GetDrives();
            if (drives[i].IsReady == true)
            {
                totalSize = drives[i].TotalSize / (1024L * 1024 * 1024);
                return totalSize;
            }
            else
                return 0;
        }
        public static long GetHardDiskFreeSize(int i)
        {
            long freeSize = new long();
            System.IO.DriveInfo[] drives = System.IO.DriveInfo.GetDrives();
            if (drives[i].IsReady == true)
            {
                freeSize = drives[i].AvailableFreeSpace / (1024 * 1024 * 1024);
                return freeSize;
            }
            else
                return 0;
        }


    }
}

