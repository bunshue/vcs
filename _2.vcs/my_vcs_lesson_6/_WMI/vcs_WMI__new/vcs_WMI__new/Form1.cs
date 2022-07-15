using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

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
                catch (System.Exception er)
                {
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

        }

        private void button6_Click(object sender, EventArgs e)
        {

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

    }
}
