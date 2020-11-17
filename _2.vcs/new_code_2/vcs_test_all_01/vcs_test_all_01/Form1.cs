using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

//參考 / 加入參考 / .NET  System.Management

using System.Management;

using System.Runtime.InteropServices;

namespace vcs_test_all_01
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "Get HDD serial\n";
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");

            foreach (ManagementObject info in searcher.Get())
            {
                richTextBox1.Text += info["DeviceID"].ToString() + "\t";
                richTextBox1.Text += "Model: " + info["Model"].ToString() + "\t";
                richTextBox1.Text += "Interface: " + info["InterfaceType"].ToString() + "\t";
                richTextBox1.Text += "Serial#: " + info["SerialNumber"].ToString() + "\n";

            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            OperatingSystem os_info = System.Environment.OSVersion;
            richTextBox1.Text += os_info.VersionString + "\n\nWindows " + GetOsName(os_info) + "\n";

        }
        // Return the OS name.
        private string GetOsName(OperatingSystem os_info)
        {
            string version =
                os_info.Version.Major.ToString() + "." +
                os_info.Version.Minor.ToString();
            switch (version)
            {
                case "10.0": return "10/Server 2016";
                case "6.3": return "8.1/Server 2012 R2";
                case "6.2": return "8/Server 2012";
                case "6.1": return "7/Server 2008 R2";
                case "6.0": return "Server 2008/Vista";
                case "5.2": return "Server 2003 R2/Server 2003/XP 64-Bit Edition";
                case "5.1": return "XP";
                case "5.0": return "2000";
            }
            return "Unknown";
        }

        [DllImport("kernel32.dll")]
        private static extern long GetVolumeInformation(
            string PathName,
            StringBuilder VolumeNameBuffer,
            UInt32 VolumeNameSize,
            ref UInt32 VolumeSerialNumber,
            ref UInt32 MaximumComponentLength,
            ref UInt32 FileSystemFlags,
            StringBuilder FileSystemNameBuffer,
            UInt32 FileSystemNameSize);

        private void button3_Click(object sender, EventArgs e)
        {
            string drive_letter = drive_letter = "c:\\";

            uint serial_number = 0;
            uint max_component_length = 0;
            StringBuilder sb_volume_name = new StringBuilder(256);
            UInt32 file_system_flags = new UInt32();
            StringBuilder sb_file_system_name = new StringBuilder(256);

            if (GetVolumeInformation(drive_letter, sb_volume_name,
                (UInt32)sb_volume_name.Capacity, ref serial_number,
                ref max_component_length, ref file_system_flags,
                sb_file_system_name,
                (UInt32)sb_file_system_name.Capacity) == 0)
            {
                MessageBox.Show("Error getting volume information.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
            else
            {


                //richTextBox1.Text +=
                richTextBox1.Text += "Volume Name\t" + sb_volume_name.ToString() + "\n";
                richTextBox1.Text += "Serial Number\t" + serial_number.ToString() + "\n";
                richTextBox1.Text += "Max Component Length\t" + max_component_length.ToString() + "\n";
                richTextBox1.Text += "File System\t" + sb_file_system_name.ToString() + "\n";
                richTextBox1.Text += "Flags\t" + "&&H" + file_system_flags.ToString("x") + "\n";


            }

        }

        // List the folder types.
        private void button4_Click(object sender, EventArgs e)
        {
            foreach (Environment.SpecialFolder folder_type
                in Enum.GetValues(typeof(Environment.SpecialFolder)))
            {
                DescribeFolder(folder_type);
            }
            richTextBox1.Select(0, 0);
        }

        // Add a folder's information to the txtFolders TextBox.
        private void DescribeFolder(Environment.SpecialFolder folder_type)
        {
            richTextBox1.AppendText(
                String.Format("{0,-25}", folder_type.ToString()) +
                Environment.GetFolderPath(folder_type) + "\r\n");
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //尋找13號星期五
            int year_st = 2020;
            int year_sp = 2030;

            // Loop over the selected years.
            for (int year = year_st; year <= year_sp; year++)
            {
                // Loop over the months in the year.
                for (int month = 1; month <= 12; month++)
                {
                    // See if this month's 13th is a Friday.
                    DateTime dt = new DateTime(year, month, 13);

                    // See if this is a Friday.
                    if (dt.DayOfWeek == DayOfWeek.Friday)
                    {
                        richTextBox1.Text += dt.ToShortDateString() + "\n";
                    }
                }
            }


        }

        private void button6_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

            //?日?時?分?秒 後
            DateTime dt_new = dt + new TimeSpan(365 * 10, 12, 34, 56);


            richTextBox1.Text += "now time : " + dt.ToString() + "\n";
            richTextBox1.Text += "new time : " + dt_new.ToString() + "\n";


        }

        private void Form1_Paint(object sender, PaintEventArgs e)
        {
            Graphics g = e.Graphics; //創建畫板,這裡的畫板是由Form提供的.
            Pen p = new Pen(Color.Blue, 2);//定義了一個藍色,寬度為的畫筆
            g.DrawLine(p, 10, 10, 100, 100);//在畫板上畫直線,起始坐標為(10,10),終點坐標為(100,100)
            g.DrawRectangle(p, 10, 10, 100, 100);//在畫板上畫矩形,起始坐標為(10,10),寬為,高為
            g.DrawEllipse(p, 10, 10, 100, 100);//在畫板上畫橢圓,起始坐標為(10,10),外接矩形的寬為,高為

        }



    }
}
