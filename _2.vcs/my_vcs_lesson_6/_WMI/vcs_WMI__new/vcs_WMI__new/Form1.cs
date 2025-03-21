﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;
using System.Management;    //for WMI

namespace vcs_WMI__new
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
            x_st = 12;
            y_st = 12;
            dx = 200;
            dy = 65;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            button10.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 9);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\nWMI寫法一：\n";
            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDisk");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += mo["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo["VolumeSerialNumber"] + "\n";
            }

            richTextBox1.Text += "\nWMI寫法二：\n";
            SelectQuery sq = new SelectQuery("SELECT * FROM Win32_LogicalDisk");
            ManagementObjectSearcher mos2 = new ManagementObjectSearcher(sq);
            foreach (ManagementObject mo2 in mos2.Get())
            {
                richTextBox1.Text += mo2["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo2["VolumeSerialNumber"] + "\n";
            }

            richTextBox1.Text += "\nWMI寫法三：\n";
            String strQry = "SELECT * FROM Win32_LogicalDisk"; // 指定查詢Win32_LogicalDisk ( 邏輯磁碟)
            // ManagementObjectSearcher 類別, 根據指定的查詢擷取管理物件的集合。
            ManagementObjectSearcher mos3 = new ManagementObjectSearcher(strQry);
            // 使用Foreach 陳述式存取集合類別中物件(元素), Get 方法, 叫用指定的WMI 查詢, 並傳回產生的集合。
            foreach (ManagementObject mo3 in mos3.Get())
            {
                // 取得磁碟Volumne 名稱跟序號
                richTextBox1.Text += mo3["Name"].ToString() + "\t";
                richTextBox1.Text += "VolumeSerialNumber: " + mo3["VolumeSerialNumber"] + "\n";
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            //使用WMI取得USB資訊


            string strServiceName = string.Empty;

            string location = System.Reflection.Assembly.GetExecutingAssembly().Location;
            //string serviceFileName = location.Substring(0, location.LastIndexOf('\\')) + "\\" + serviceName + ".exe";


            //Cursor myCursor = new Cursor(@"C:\WINDOWS\Cursors\cross_r.cur"); //自定義鼠標 

            //使用WMI取得USB資訊

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_USBHub");
            ManagementObjectCollection collection = mos.Get();
            var usbList = from u in collection.Cast<ManagementBaseObject>()
                          select new
                          {
                              id = u.GetPropertyValue("DeviceID"),
                              name = u.GetPropertyValue("Name"),
                              status = u.GetPropertyValue("Status"),
                              system = u.GetPropertyValue("SystemName"),
                              caption = u.GetPropertyValue("Caption"),
                              pnp = u.GetPropertyValue("PNPDeviceID"),
                              description = u.GetPropertyValue("Description")
                          };
            foreach (var u in usbList)
            {
                richTextBox1.Text += String.Format("{0}{7}{1}{7}{2}{7}{3}{7}{4}{7}{5}{7}{6}{7}{7}{7}", u.id, u.name, u.status, u.system, u.caption, u.pnp, u.description, Environment.NewLine);
            }





        }
        private void button2_Click(object sender, EventArgs e)
        {


            _serialNumber.Clear();
            matchDriveLetterWithSerial();
            richTextBox1.Text += "len = " + _serialNumber.Count.ToString() + "\n";

            int len = _serialNumber.Count;
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "取得序號 : " + _serialNumber[i] + "\n";

            }
        }

        //讀取U盤序列號
        private List<string> _serialNumber = new List<string>();

        /// <summary>
        /// 調用這個函數將本機所有U盤序列號存儲到_serialNumber中
        /// </summary>
        private void matchDriveLetterWithSerial()
        {
            string[] diskArray;
            string driveNumber;
            var searcher = new ManagementObjectSearcher("SELECT * FROM Win32_LogicalDiskToPartition");
            foreach (ManagementObject dm in searcher.Get())
            {
                getValueInQuotes(dm["Dependent"].ToString());
                diskArray = getValueInQuotes(dm["Antecedent"].ToString()).Split(',');
                driveNumber = diskArray[0].Remove(0, 6).Trim();
                var disks = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
                foreach (ManagementObject disk in disks.Get())
                {
                    if (disk["Name"].ToString() == ("\\\\.\\PHYSICALDRIVE" + driveNumber) & disk["InterfaceType"].ToString() == "USB")
                    {
                        _serialNumber.Add(parseSerialFromDeviceID(disk["PNPDeviceID"].ToString()));
                    }
                }
            }
        }

        private static string parseSerialFromDeviceID(string deviceId)
        {
            var splitDeviceId = deviceId.Split('\\');
            var arrayLen = splitDeviceId.Length - 1;
            var serialArray = splitDeviceId[arrayLen].Split('&');
            var serial = serialArray[0];
            return serial;
        }

        private static string getValueInQuotes(string inValue)
        {
            var posFoundStart = inValue.IndexOf("\"");
            var posFoundEnd = inValue.IndexOf("\"", posFoundStart + 1);
            var parsedValue = inValue.Substring(posFoundStart + 1, (posFoundEnd - posFoundStart) - 1);
            return parsedValue;
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //獲得處理器參數程序代碼
            get_ProcessorInfo();
        }

        void get_ProcessorInfo()
        {
            string[] 制造商;
            string[] 型號;
            string[] 序列號;

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");
            制造商 = new string[mos.Get().Count];
            型號 = new string[mos.Get().Count];
            序列號 = new string[mos.Get().Count];
            int i = 0;
            foreach (ManagementObject mo in mos.Get())
            {
                try
                {
                    制造商[i] = mo.GetPropertyValue("Manufacturer").ToString();
                    序列號[i] = mo.GetPropertyValue("ProcessorId").ToString();

                    richTextBox1.Text += "制造商[" + i.ToString() + "] : " + 制造商[i].ToString() + "\n";
                    richTextBox1.Text += "序列號[" + i.ToString() + "] : " + 序列號[i].ToString() + "\n";
                }
                catch (System.Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //獲得硬盤空間
            richTextBox1.Text += "獲得硬盤空間 : " + GetDiskSpace() + "\n";
        }

        //獲得硬盤空間
        public System.UInt64 GetDiskSpace()
        {
            ManagementClass diskClass = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection disks = diskClass.GetInstances();
            System.UInt64 space = UInt64.MinValue;
            foreach (ManagementObject disk in disks)
            {
                if ((disk["Name"]).ToString() == "C:")
                    space = (System.UInt64)(disk["FreeSpace"]);
            }
            return space;
        }


        private void button5_Click(object sender, EventArgs e)
        {
            //取得本機MAC地址
            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from Win32_NetworkAdapterConfiguration");
            foreach (ManagementObject mo in mos.Get())
            {
                if (Convert.ToBoolean(mo["ipEnabled"]) == true)
                {
                    richTextBox1.Text += "取得本機MAC地址 : " + Convert.ToString(mo["MACAddress"]) + "\n";
                }
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //獲得硬盤參數

        }

        //C# 獲得硬盤參數程序代碼如下：
        public void HardDisk(out string[] 制造商, out string[] 型號, out string[] 序列號)
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_DiskDrive");
            制造商 = new string[searcher.Get().Count];
            型號 = new string[searcher.Get().Count];
            序列號 = new string[searcher.Get().Count];
            int i = 0;
            foreach (ManagementObject share in searcher.Get())
            {
                try
                {
                    制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                    型號[i] = share.GetPropertyValue("Model").ToString();
                    序列號[i] = share.GetPropertyValue("Signature").ToString();
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //獲得網卡參數

        }

        //C# 獲得網卡參數程序代碼如下：
        public void NetworkAdapter(out string[] 制造商, out string[] MAC地址)
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_NetworkAdapter");
            制造商 = new string[searcher.Get().Count];
            MAC地址 = new string[searcher.Get().Count];
            int i = 0;
            foreach (ManagementObject share in searcher.Get())
            {
                try
                {
                    制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                    MAC地址[i] = share.GetPropertyValue("MACAddress").ToString();
                }
                catch (Exception ex)
                {
                    richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
                }
                i++;
            }
        }


        private void button8_Click(object sender, EventArgs e)
        {
            //獲得主板序列號

        }

        //C# 獲得主板序列號程序代碼如下：
        public static void MainboardSerialNumber(out string[] 序列號)
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("Select * From Win32_BIOS");
            序列號 = new string[searcher.Get().Count];
            int i = 0;
            foreach (ManagementObject share in searcher.Get())
            {
                序列號[i] = share.GetPropertyValue("SerialNumber").ToString();
                i++;
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //獲得主板參數

        }

        //C# 獲得主板參數程序代碼如下：
        public static void Mainboard(out string[] 制造商, out string[] 型號)
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_BaseBoard");
            制造商 = new string[searcher.Get().Count];
            型號 = new string[searcher.Get().Count];
            int i = 0;
            foreach (ManagementObject share in searcher.Get())
            {
                制造商[i] = share.GetPropertyValue("Manufacturer").ToString();
                型號[i] = share.GetPropertyValue("Product").ToString();
                i++;
            }
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //判斷驅動器類型
            richTextBox1.Text += "判斷驅動器類型\n";

            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject disk in searcher.Get())
            {
                //comboBox1.Items.Add(disk["Name"].ToString());
                richTextBox1.Text += "取得驅動器 : " + disk["Name"].ToString() + "\t" + get_drive_type(disk["Name"].ToString()) + "\n";
            }
        }

        string get_drive_type(string drive)
        {
            string DriveType;
            string type = string.Empty;
            DriveInfo dinfo = new DriveInfo(drive);
            try
            {
                DriveType = dinfo.DriveType.ToString();
                switch (DriveType)
                {
                    case "Unknown":
                        type = "這是未知設備";
                        break;
                    case "NoRootDirectory":
                        type = "這是未分區";
                        break;
                    case "Removable":
                        type = "這是可移動磁盤";
                        break;
                    case "Fixed":
                        type = "這是硬盤";
                        break;
                    case "Network":
                        type = "這是網絡驅動器";
                        break;
                    case "CDRom":
                        type = "這是光驅";
                        break;
                }
            }
            catch
            {
                type = "這是未知類型";
            }
            return type;
        }


        private void button11_Click(object sender, EventArgs e)
        {
            //取得系統其他進程的啟動參數
            //使用WMI來查詢得到數據

            foreach (ManagementObject p in new ManagementObjectSearcher(new SelectQuery("SELECT * FROM Win32_Process")).Get())
            {
                richTextBox1.Text += p.Properties["commandLine"].Value + "\n";
            }
        }

        private void button12_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {

        }

        private void button14_Click(object sender, EventArgs e)
        {

        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {

        }

        private void button17_Click(object sender, EventArgs e)
        {

        }

        private void button18_Click(object sender, EventArgs e)
        {

        }

        private void button19_Click(object sender, EventArgs e)
        {

        }
    }
}
