using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Diagnostics;
using System.Text.RegularExpressions;

using System.Management;

namespace WindowsFormsApplication0106e
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
            //C# 獲取磁盤空間大小的方法 1
        }

        //方法一：利用System.IO.DriveInfo.GetDrives方法來獲取

        ///   
        /// 獲取指定驅動器的空間總大小(單位為B) 
        ///   
        ///  只需輸入代表驅動器的字母即可 （大寫） 
        ///    
        public static long GetHardDiskSpace(string str_HardDiskName)
        {
            long totalSize = new long();
            str_HardDiskName = str_HardDiskName + ":\\";
            System.IO.DriveInfo[] drives = System.IO.DriveInfo.GetDrives();
            foreach (System.IO.DriveInfo drive in drives)
            {
                if (drive.Name == str_HardDiskName)
                {
                    totalSize = drive.TotalSize / (1024 * 1024 * 1024);
                }
            }
            return totalSize;
        }

        ///   
        /// 獲取指定驅動器的剩余空間總大小(單位為B) 
        ///   
        ///  只需輸入代表驅動器的字母即可  
        ///    
        public static long GetHardDiskFreeSpace(string str_HardDiskName)
        {
            long freeSpace = new long();
            str_HardDiskName = str_HardDiskName + ":\\";
            System.IO.DriveInfo[] drives = System.IO.DriveInfo.GetDrives();
            foreach (System.IO.DriveInfo drive in drives)
            {
                if (drive.Name == str_HardDiskName)
                {
                    freeSpace = drive.TotalFreeSpace / (1024 * 1024 * 1024);
                }
            }
            return freeSpace;
        }




        private void button2_Click(object sender, EventArgs e)
        {
            //C# 獲取磁盤空間大小的方法 2
            //方法二：利用ManagementClass("Win32_LogicalDisk")來獲取

            List<Dictionary<string, string>> diskInfoDic = new List<Dictionary<string, string>>();
            ManagementClass diskClass = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection disks = diskClass.GetInstances();
            foreach (ManagementObject disk in disks)
            {
                Dictionary<string, string> diskInfo = new Dictionary<string, string>();
                try
                {
                    // 磁盤名稱
                    diskInfo["Name"] = disk["Name"].ToString();
                    // 磁盤描述
                    diskInfo["Description"] = disk["Description"].ToString();
                    // 磁盤總容量，可用空間，已用空間
                    if (System.Convert.ToInt64(disk["Size"]) > 0)
                    {
                        long totalSpace = System.Convert.ToInt64(disk["Size"]); // MB;
                        long freeSpace = System.Convert.ToInt64(disk["FreeSpace"]); // MB;
                        long usedSpace = totalSpace - freeSpace;
                        diskInfo["totalSpace"] = totalSpace.ToString();
                        diskInfo["usedSpace"] = usedSpace.ToString();
                        diskInfo["freeSpace"] = freeSpace.ToString();
                    }
                    diskInfoDic.Add(diskInfo);
                }
                catch (Exception ex)
                {
                    //Throw ex;
                }
            }
        }



        private void button3_Click(object sender, EventArgs e)
        {

        }








    }
}

