using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;

namespace vcs_GetLogicalDrives
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 140;
            dy = 70;

            button00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button04.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button05.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button06.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button07.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            richTextBox1.Size = new Size(600, 600);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(800, 680);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button00_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "列出Logical Drives\n";
            foreach (string drive in Environment.GetLogicalDrives())
            {
                richTextBox1.Text += "\t" + drive + "\n";
            }

            string[] drives = Environment.GetLogicalDrives();
            richTextBox1.Text += "系統磁碟機：" + string.Join(", ", drives) + "\n";

            richTextBox1.Text += string.Format("系統磁碟機：{0}", string.Join(", ", drives)) + "\n";

            //取得所有邏輯分區
            //取得所有邏輯分區
            //取得本地磁盤目錄
            richTextBox1.Text += "取得所有邏輯分區\n";
            string[] logicdrives = Directory.GetLogicalDrives();
            for (int i = 0; i < logicdrives.Length; i++)
            {
                richTextBox1.Text += "取得: " + logicdrives[i] + "\n";
            }

        }

        private void button01_Click(object sender, EventArgs e)
        {
            //顯示所有邏輯磁碟機
            GetLogicalDrives();
        }

        // Print out all logical drives on the system.
        void GetLogicalDrives()
        {
            try
            {
                string[] drives = System.IO.Directory.GetLogicalDrives();

                foreach (string str in drives)
                {
                    System.Console.WriteLine(str);
                    richTextBox1.Text += "drive : " + str + "\n";
                }
            }
            catch (System.IO.IOException)
            {
                System.Console.WriteLine("An I/O error occurs.");
            }
            catch (System.Security.SecurityException)
            {
                System.Console.WriteLine("The caller does not have the " +
                    "required permission.");
            }
        }

        private void button02_Click(object sender, EventArgs e)
        {
            string[] drive = Environment.GetLogicalDrives();
            for (int i = 0; i < drive.Length; i++)
            {
                richTextBox1.Text += "磁碟名稱 :" + drive[i] + "\n";
                richTextBox1.Text += "全部大小 :" + GetHardDiskTotalSize(i).ToString() + " G" + "\n";
                richTextBox1.Text += "可用大小 :" + GetHardDiskFreeSize(i).ToString() + " G" + "\n";
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
            {
                return 0;
            }
        }

        private void button03_Click(object sender, EventArgs e)
        {
        }

        private void button04_Click(object sender, EventArgs e)
        {
        }
        private void button05_Click(object sender, EventArgs e)
        {
        }

        private void button06_Click(object sender, EventArgs e)
        {

        }

        private void button07_Click(object sender, EventArgs e)
        {

        }
    }
}
