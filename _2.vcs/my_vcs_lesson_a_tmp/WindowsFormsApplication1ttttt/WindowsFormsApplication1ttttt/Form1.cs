using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Management;    //for WMI
using System.Diagnostics;   //for Process

using System.Net;
using System.Net.NetworkInformation;    //for UnicastIPAddressInformation

using System.IO;

using Shell32;

/*
[C#] 調用WMI
第一步：加入參考
專案→加入參考→.Net→System.Management
第二步：引用命名空間
using System.Management;
*/

namespace WindowsFormsApplication1ttttt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        string GetProcessOwner(Process process)
        {
            var query = "Select * From Win32_Process Where ProcessID = " + process.Id;
            var searcher = new ManagementObjectSearcher(query);
            var processObj = searcher.Get().OfType<ManagementObject>().FirstOrDefault();

            if (processObj == null)
                throw new ArgumentException("Process not exists!");

            var argList = new string[2];
            int returnVal = Convert.ToInt32(processObj.InvokeMethod("GetOwner", argList));
            if (returnVal == 0)
            {
                return string.Join(@"\", argList.Reverse().ToArray());
            }

            return null;
        }


        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            //取得網卡的IPV6位置
            foreach (var ip in GetLocalIPV6IP())
            {
                richTextBox1.Text += "ip = " + ip.ToString() + "\n";
            }
        }

        private static IEnumerable<String> GetLocalIPV6IP()
        {
            return (from adapter in NetworkInterface.GetAllNetworkInterfaces()
                    where adapter.NetworkInterfaceType == NetworkInterfaceType.Ethernet
                    from AddressInfo in adapter.GetIPProperties().UnicastAddresses.OfType<UnicastIPAddressInformation>()
                    where AddressInfo.Address.AddressFamily == System.Net.Sockets.AddressFamily.InterNetworkV6
                    let ipAddress = AddressInfo.Address.ToString()
                    select ipAddress);
        }

        private void button3_Click(object sender, EventArgs e)
        {

        }


        static IEnumerable<KeyValuePair<string, int>> GetDetailColumn()
        {
            ShellClass sh = new ShellClass();
            Folder dir = sh.NameSpace(@"c:\");

            int idx = 0;
            string columnName = dir.GetDetailsOf(0, idx);
            do
            {
                yield return new KeyValuePair<string, int>(columnName, idx);
                columnName = dir.GetDetailsOf(0, ++idx);
            } while (!string.IsNullOrEmpty(columnName));
        }

        static IEnumerable<KeyValuePair<string, int>> GetDetailColumn(int offset, int count)
        {
            ShellClass sh = new ShellClass();
            Folder dir = sh.NameSpace(@"c:\");

            for (var idx = offset; idx < offset + count; ++idx)
            {
                yield return new KeyValuePair<string, int>(dir.GetDetailsOf(0, idx), idx);
            }
        }

        static void ViewDetailColumn()
        {
            var columns = GetDetailColumn();
            foreach (var item in columns)
            {
                Console.WriteLine(item.Key);
            }
        }

        static void ViewDetailColumn(int offset, int count)
        {
            var columns = GetDetailColumn(offset, count);
            foreach (var item in columns)
            {
                Console.WriteLine(item.Key);
            }
        }

        static string GetDetailValue(string file, int column)
        {
            ShellClass sh = new ShellClass();
            Folder dir = sh.NameSpace(Path.GetDirectoryName(file));
            FolderItem item = dir.ParseName(Path.GetFileName(file));
            return dir.GetDetailsOf(item, column);
        }

        static void ViewDetailValue(string file, int column)
        {
            Console.WriteLine(GetDetailValue(file, column));
        }

        static string GetDetailValue(string file, string column)
        {
            var linq = from item in GetDetailColumn()
                       where item.Key == column
                       select item.Value;
            return GetDetailValue(file, linq.FirstOrDefault());
        }

        static void ViewDetailValue(string file, string column)
        {
            Console.WriteLine(GetDetailValue(file, column));
        }


    }
}
