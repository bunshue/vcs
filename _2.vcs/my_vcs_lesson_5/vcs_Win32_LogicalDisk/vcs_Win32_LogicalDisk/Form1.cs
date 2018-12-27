using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;

namespace vcs_Win32_LogicalDisk
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
            string drive = "C";
            richTextBox1.Text += "硬碟： " + drive + "\n";
            double dblSize = 0;
            double dblFree = 0;
            uint drive_type = 0;
            uint media_type = 0;

            if (string.IsNullOrEmpty(drive) || drive == null)
            {
                drive = "C";
            }
            //create our ManagementObject, passing it the drive letter to the
            //DevideID using WQL
            ManagementObject disk = new ManagementObject("Win32_LogicalDisk.DeviceID=\"" + drive + ":\"");
            //bind our management object
            disk.Get();

            richTextBox1.Text += "\n字串類\n";

            richTextBox1.Text += "Name: " + disk["Name"] + "\n";
            richTextBox1.Text += "Caption: " + disk["Caption"] + "\n";
            richTextBox1.Text += "FileSystem: " + disk["FileSystem"] + "\n";
            richTextBox1.Text += "CreationClassName: " + disk["CreationClassName"] + "\n";
            richTextBox1.Text += "Description: " + disk["Description"] + "\n";
            richTextBox1.Text += "DeviceID: " + disk["DeviceID"] + "\n";
            richTextBox1.Text += "SystemCreationClassName: " + disk["SystemCreationClassName"] + "\n";
            richTextBox1.Text += "SystemName: " + disk["SystemName"] + "\n";
            richTextBox1.Text += "VolumeName: " + disk["VolumeName"] + "\n";
            richTextBox1.Text += "序號VolumeSerialNumber: " + disk["VolumeSerialNumber"] + "\n";
            /*  無資料
            richTextBox1.Text += "LogicalDisk: " + disk["ProviderName"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["PNPDeviceID"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["Purpose"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["Status"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["ErrorDescription"] + "\n";
            richTextBox1.Text += "LogicalDisk: " + disk["ErrorMethodology"] + "\n";
            */

            richTextBox1.Text += "\n數字類\n";

            richTextBox1.Text += "Size: " + disk["Size"].ToString() + "\n";
            richTextBox1.Text += "FreeSpace: " + disk["FreeSpace"].ToString() + "\n";
            richTextBox1.Text += "MaximumComponentLength: " + disk["MaximumComponentLength"].ToString() + "\n";
            richTextBox1.Text += "MediaType: " + disk["MediaType"].ToString() + "\n";
            //richTextBox1.Text += "Access: " + disk["Access"].ToString() + "\n";
            richTextBox1.Text += "DriveType: " + disk["DriveType"].ToString() + "\t";

            drive_type = (uint)disk["DriveType"];

            switch (drive_type)
            {
                case 0:
                    richTextBox1.Text += "Unknown." + "\n";
                    break;
                case 1:
                    richTextBox1.Text += "No Root Directory." + "\n";
                    break;
                case 2:
                    richTextBox1.Text += "Removable Disk." + "\n";
                    break;
                case 3:
                    richTextBox1.Text += "Local Disk." + "\n";
                    break;
                case 4:
                    richTextBox1.Text += "Network Drive." + "\n";
                    break;
                case 5:
                    richTextBox1.Text += "Compact Disc." + "\n";
                    break;
                case 6:
                    richTextBox1.Text += "RAM Disk." + "\n";
                    break;
                default:
                    richTextBox1.Text += "Drive type could not be determined." + "\n";
                    break;
            }

            dblSize = Math.Round(Convert.ToDouble(disk["Size"]) / 1024 / 1024 / 1024);
            //1 KB = 1024 - KiloByte
            //1 MB = 1024 ^ 2 - MegaByte
            //1 GB = 1024 ^ 3 - GigaByte
            //1 TB = 1024 ^ 4 - TeraByte
            //1 PB = 1024 ^ 5 - PetaByte
            //1 EB = 1024 ^ 6 - ExaByte
            //1 ZB = 1024 ^ 7 - ZettaByte
            //1 YB = 1024 ^ 8 - YottaByte
            //1 BB = 1024 ^ 9 - BrontoByte
            richTextBox1.Text += "Hard Disk Size = " + dblSize.ToString() + " GB" + "\n";

            dblFree = Math.Round(Convert.ToDouble(disk["FreeSpace"]) / 1024 / 1024 / 1024);
            //1 KB = 1024 - KiloByte
            //1 MB = 1024 ^ 2 - MegaByte
            //1 GB = 1024 ^ 3 - GigaByte
            //1 TB = 1024 ^ 4 - TeraByte
            //1 PB = 1024 ^ 5 - PetaByte
            //1 EB = 1024 ^ 6 - ExaByte
            //1 ZB = 1024 ^ 7 - ZettaByte
            //1 YB = 1024 ^ 8 - YottaByte
            //1 BB = 1024 ^ 9 - BrontoByte

            richTextBox1.Text += "Hard Disk Free Space = " + dblFree.ToString() + " GB\n";

            media_type = (uint)disk["MediaType"];
            switch (media_type)
            {
                case 1:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (1), 5 1/4-Inch Floppy Disk - 1.2 MB - 512 bytes/sector." + "\n"; break;
                case 2:
                    richTextBox1.Text += "3½-Inch Floppy Disk (2), 3 1/2-Inch Floppy Disk - 1.44 MB -512 bytes/sector." + "\n"; break;
                case 3:
                    richTextBox1.Text += "3½-Inch Floppy Disk (3), 3 1/2-Inch Floppy Disk - 2.88 MB - 512 bytes/sector." + "\n"; break;
                case 4:
                    richTextBox1.Text += "3½-Inch Floppy Disk (4), 3 1/2-Inch Floppy Disk - 20.8 MB - 512 bytes/sector." + "\n"; break;
                case 5:
                    richTextBox1.Text += "3½-Inch Floppy Disk (5), 3 1/2-Inch Floppy Disk - 720 KB - 512 bytes/sector." + "\n"; break;
                case 6:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (6), 5 1/4-Inch Floppy Disk - 360 KB - 512 bytes/sector." + "\n"; break;
                case 7:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (7), 5 1/4-Inch Floppy Disk - 320 KB - 512 bytes/sector." + "\n"; break;
                case 8:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (8), 5 1/4-Inch Floppy Disk - 320 KB - 1024 bytes/sector." + "\n"; break;
                case 9:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (9), 5 1/4-Inch Floppy Disk - 180 KB - 512 bytes/sector." + "\n"; break;
                case 10:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (10), 5 1/4-Inch Floppy Disk - 160 KB - 512 bytes/sector." + "\n"; break;
                case 11:
                    richTextBox1.Text += "Removable media other than floppy (11)." + "\n"; break;
                case 12:
                    richTextBox1.Text += "Fixed hard disk media (12)." + "\n"; break;
                case 13:
                    richTextBox1.Text += "3½-Inch Floppy Disk (13), 3 1/2-Inch Floppy Disk - 120 MB - 512 bytes/sector." + "\n"; break;
                case 14:
                    richTextBox1.Text += "3½-Inch Floppy Disk (14), 3 1/2-Inch Floppy Disk - 640 KB - 512 bytes/sector." + "\n"; break;
                case 15:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (15), 5 1/4-Inch Floppy Disk - 640 KB - 512 bytes/sector." + "\n"; break;
                case 16:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (16), 5 1/4-Inch Floppy Disk - 720 KB - 512 bytes/sector." + "\n"; break;
                case 17:
                    richTextBox1.Text += "3½-Inch Floppy Disk (17), 3 1/2-Inch Floppy Disk - 1.2 MB - 512 bytes/sector." + "\n"; break;
                case 18:
                    richTextBox1.Text += "3½-Inch Floppy Disk (18), 3 1/2-Inch Floppy Disk - 1.23 MB - 1024 bytes/sector." + "\n"; break;
                case 19:
                    richTextBox1.Text += "5¼-Inch Floppy Disk (19), 5 1/4-Inch Floppy Disk - 1.23 MB - 1024 bytes/sector." + "\n"; break;
                case 20:
                    richTextBox1.Text += "3½-Inch Floppy Disk (20), 3 1/2-Inch Floppy Disk - 128 MB - 512 bytes/sector." + "\n"; break;
                case 21:
                    richTextBox1.Text += "3½-Inch Floppy Disk (21), 3 1/2-Inch Floppy Disk - 230 MB - 512 bytes/sector." + "\n"; break;
                case 22:
                    richTextBox1.Text += "8-Inch Floppy Disk (22), 8-Inch Floppy Disk - 256 KB - 128 bytes/sector." + "\n"; break;
                default:
                    richTextBox1.Text += "Media type could not be determined." + "\n"; break;
            }

            /*  無資料
            //richTextBox1.Text += "Size: " + disk["Availability"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["BlockSize"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["ConfigManagerErrorCode"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["LastErrorCode"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["NumberOfBlocks"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["PowerManagementCapabilities[]"].ToString() + "\n";
            //richTextBox1.Text += "Size: " + disk["StatusInfo"].ToString() + "\n";
            */
            /*  無資料
            richTextBox1.Text += "InstallDate: " + disk["InstallDate"] + "\n";
            */
        }
    }
}
