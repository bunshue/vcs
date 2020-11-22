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

using System.Net.NetworkInformation;

using System.IO;    //for Stream
using System.Net;   //for WebClient


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

        private void button7_Click(object sender, EventArgs e)
        {
            String host;

            host = "www.google.com";

            if (IsInternetConnected(host))
                richTextBox1.Text += host + "\t連線OK\n";
            else
                richTextBox1.Text += host+ "\t無法連線\n";

            host = "http://csharphelper.com/";

            if (IsInternetConnected(host))
                richTextBox1.Text += host + "\t連線OK\n";
            else
                richTextBox1.Text += host + "\t無法連線\n";
        }

        // Return true if a ping to Google works.
        private bool IsInternetConnected(String host)
        {
            return IsInternetConnected(host, 1000);
        }
        private bool IsInternetConnected(String host, int timeout)
        {
            try
            {
                Ping ping = new Ping();
                PingReply reply = ping.Send(host, timeout);
                return (reply.Status == IPStatus.Success);
            }
            catch
            {
                return false;
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            // Get the current charge percent.
            PowerStatus status = SystemInformation.PowerStatus;
            int percent = (int)(status.BatteryLifePercent * 100);

            richTextBox1.Text += percent.ToString() + "%" + "\n";
            richTextBox1.Text += status.PowerLineStatus.ToString() + "\n";
            richTextBox1.Text += status.BatteryChargeStatus.ToString() + "\n";
            richTextBox1.Text += status.BatteryFullLifetime.ToString() + "\n";
            richTextBox1.Text += status.BatteryLifePercent.ToString() + "\n";
            richTextBox1.Text += status.BatteryLifeRemaining.ToString() + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            string url = "file:///C:/_git/vcs/_1.data/_html/My_Link.html";
            // Get the response.
            try
            {
                // Get the web response.
                string result = GetWebResponse(url);
                //Console.WriteLine(result.Replace("\\r\\n", "\r\n"));
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Read Error",
                    MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            }
        }

        // Get a web response.
        private string GetWebResponse(string url)
        {
            // Make a WebClient.
            WebClient web_client = new WebClient();

            // Get the indicated URL.
            Stream response = web_client.OpenRead(url);

            // Read the result.
            using (StreamReader stream_reader = new StreamReader(response))
            {
                // Get the results.
                string result = stream_reader.ReadToEnd();

                // Close the stream reader and its underlying stream.
                stream_reader.Close();

                // Return the result.

                richTextBox1.Text += result + "\n";

                string filename = Application.StartupPath + "\\html_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".html";
                StreamWriter sw = File.CreateText(filename);
                sw.Write(result);
                sw.Close();

                return result;
            }
        }


        private void button10_Click(object sender, EventArgs e)
        {
            string[] words = {
                "Alabama",
                "Alaska",
                "American Samoa",
                "Arizona",
                "Arkansas",
                "California",
                "Colorado",
                "Connecticut",
                "Delaware",
                "District of Columbia",
                "Florida",
                "Georgia",
                "Guam",
                "Hawaii",
                "Idaho",
                "Illinois",
                "Indiana",
                "Iowa",
                "Kansas",
                "Kentucky",
                "Louisiana",
                "Maine",
                "Maryland",
                "Massachusetts",
                "Michigan",
                "Minnesota",
                "Mississippi",
                "Missouri",
                "Montana",
                "Nebraska",
                "Nevada",
                "New Hampshire",
                "New Jersey",
                "New Mexico",
                "New York",
                "North Carolina",
                "North Dakota",
                "Northern Marianas Islands    ",
                "Ohio",
                "Oklahoma",
                "Oregon",
                "Pennsylvania",
                "Puerto Rico",
                "Rhode Island",
                "South Carolina",
                "South Dakota",
                "Tennessee",
                "Texas",
                "Utah",
                "Vermont",
                "Virginia ",
                "Virgin Islands ",
                "Washington",
                "West Virginia",
                "Wisconsin",
                "Wyoming"
            };

            // Get a list holding each word's unique letter count and name.
            var count_query =
                from string word in words
                orderby word.ToCharArray().Distinct().Count()
                select word.ToCharArray().Distinct().Count() + ", " + word;
            //listView1.DataSource = count_query.ToArray();

            richTextBox1.Text += count_query.ToArray().Length.ToString() + "\n";

            int len = count_query.ToArray().Length;
            for (int i = 0; i < len; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + (count_query.ToArray())[i].ToString() + "\n";


            }

        }

        private void button11_Click(object sender, EventArgs e)
        {
            string text =
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse lobortis blandit mauris, a sagittis libero. Proin a posuere justo, vel scelerisque risus.\n" +
    "Sed condimentum suscipit est in sagittis. Maecenas ac nulla in metus gravida feugiat nec vel odio. Aenean vulputate urna vel gravida rhoncus.\n" +
    "Etiam vel lacinia urna, non ultrices arcu. Curabitur eget neque nec felis facilisis lacinia. Donec sit amet neque vel ligula scelerisque cursus et quis nisl.\n" +
    "Proin convallis metus elit, eu condimentum nunc ultrices vel. Maecenas elementum orci tellus, quis pretium risus fringilla non.\n" +
    "Quisque eget diam a erat vestibulum cursus ut nec nisi. Duis non velit quis augue mattis consectetur pharetra sed dolor.\n" +
    "Pellentesque luctus tempor ornare.\n" +
    "Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Proin pellentesque dolor in leo porttitor, dignissim sollicitudin nulla bibendum.\n" +
    "Nullam sit amet faucibus nunc, nec laoreet orci. Etiam nec rutrum mauris. Integer sapien felis, placerat id orci eu, fermentum porta dui.\n" +
    "Nam in pharetra orci, sed sollicitudin urna. Suspendisse sit amet tellus sagittis, lobortis ante quis, consectetur est.\n" +
    "Aliquam tempor ligula in augue facilisis, vehicula fermentum sem elementum. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.";

            // Split the text into paragraphs.
            string[] paragraphs = text.Split('\n');

            int i = 1;
            // Draw each paragraph.
            foreach (string paragraph in paragraphs)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 行\t" + paragraph + "\n";
                // Break the text into words.
                string[] words = paragraph.Split(' ');
                foreach (string word in words)
                {
                    richTextBox1.Text += word + "_";

                }
                richTextBox1.Text += "\n";


                i++;
            }


        }



    }
}
