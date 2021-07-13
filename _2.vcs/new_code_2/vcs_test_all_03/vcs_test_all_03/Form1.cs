using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;

using System.Management;    //for ManagementObjectSearcher

using System.Diagnostics;
using System.IO;

using System.Runtime.InteropServices;   //for DllImport

using System.Text.RegularExpressions;   //for Regex

using Microsoft.VisualBasic.Devices;

using System.Collections;       //for DictionaryEntry

namespace vcs_test_all_03
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            /*
            Process p = new Process();
            p.StartInfo.FileName = "cmd.exe";
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.RedirectStandardInput = true;
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.RedirectStandardError = true;
            p.StartInfo.CreateNoWindow = true;
            p.Start();
            p.StandardInput.WriteLine(@"netstat -a -n > c:\port.txt");
            */

            show_item_location();

            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";
            Microsoft.Win32.SystemEvents.TimeChanged += new EventHandler(SystemEvents_TimeChanged); //for 設定系統時間
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
            dx = 140;
            dy = 60;

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

            button15.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 4);

            button20.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 3, y_st + dy * 4);

            button25.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button26.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button27.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button28.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button29.Location = new Point(x_st + dx * 4, y_st + dy * 4);

            button30.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 5, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 5, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 5, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 5, y_st + dy * 4);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //取得所有邏輯分區
            //取得本地磁盤目錄
            richTextBox1.Text += "取得所有邏輯分區\n";
            string[] logicdrives = System.IO.Directory.GetLogicalDrives();
            for (int i = 0; i < logicdrives.Length; i++)
            {
                richTextBox1.Text += "取得: " + logicdrives[i] + "\n";
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string name = "www.google.com";

            //透過計算機名取得IP地址
            IPAddress[] ip = null;
            try
            {
                ip = Dns.GetHostAddresses(name);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "電腦名稱 : " + name + "\n";
            richTextBox1.Text += "IP位址 : " + ip[0].ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            string ip_addr = "140.114.29.100";
            IPHostEntry hostInfo;
            try
            {
                hostInfo = Dns.Resolve(ip_addr);
            }
            catch (Exception ey)
            {
                MessageBox.Show(ey.Message);
                return;
            }
            richTextBox1.Text += "IP位址 : " + ip_addr + "\n";
            richTextBox1.Text += "電腦名稱 : " + hostInfo.HostName + "\n";

        }

        private void button3_Click(object sender, EventArgs e)
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

        private void button4_Click(object sender, EventArgs e)
        {
            this.richTextBox1.Text += "取得系統開啟的端口和狀態\n";
            try
            {
                string path = @"c:\port.txt";
                using (StreamReader sr = new StreamReader(path))
                {
                    while (sr.Peek() >= 0)
                    {
                        this.richTextBox1.Text += sr.ReadLine() + "\r\n";
                    }
                }
            }
            catch (Exception hy)
            {
                MessageBox.Show(hy.Message);
            }

        }

        private void button5_Click(object sender, EventArgs e)
        {

        }

        public string getstr(string strUrl)
        {
            string d = @"<title>(?<title>[^<]*)</title>";
            return Regex.Match(strUrl, d).ToString();
        }

        public bool ValidateDate1(string input)
        {
            return Regex.IsMatch(input, "http(s)?://([\\w-]+\\.)+[\\w-]+(//[\\w- .//?%&=]*)?");
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "提取網頁標題\n";
            string url = "https://www.youtube.com/watch?v=ViyVmAU0zgo";

            if (ValidateDate1(url))
            {
                string strl;//儲存編碼
                WebRequest wb = WebRequest.Create(url);//請求資源
                WebResponse webRed = wb.GetResponse();//響應請求
                Stream redweb = webRed.GetResponseStream();//傳回數據存入流中
                StreamReader sr = new StreamReader(redweb, Encoding.UTF8);//從流中讀出數據
                StringBuilder sb = new StringBuilder();//可變字符
                while ((strl = sr.ReadLine()) != null)
                {
                    sb.Append(strl);//讀出數據存入可變字符中
                }
                string result = getstr(sb.ToString());//呼叫正則表達式方法讀出標題
                richTextBox1.Text += "網頁標題:\t" + result + "\n";
            }
            else
            {
                MessageBox.Show("請輸入正確的網址");
                return;
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //獲得硬盤序號

            ManagementObjectSearcher mos = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            string strHardDiskID = "";
            foreach (ManagementObject mo in mos.Get())
            {
                strHardDiskID = mo["SerialNumber"].ToString().Trim();
                break;
            }
            richTextBox1.Text += "獲得硬盤序號 : " + strHardDiskID + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher mos = new ManagementObjectSearcher(selectQuery);
            foreach (ManagementObject mo in mos.Get())
            {
                string disk_name = mo["Name"].ToString();
                richTextBox1.Text += "取得硬碟 : " + disk_name + "\n";

                DriveInfo dinfo = new DriveInfo(disk_name);
                if (dinfo.IsReady == true)
                {
                    richTextBox1.Text += "驅動器總容量：" + dinfo.TotalSize + " B\n";
                    richTextBox1.Text += "驅動器剩餘容量：" + dinfo.TotalFreeSpace + " B\n"; ;
                }
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            DriveInfo dinfo = new DriveInfo(@"C:\");
            float tsize = dinfo.TotalSize;
            float fsize = dinfo.TotalFreeSpace;
            Graphics g = this.pictureBox1.CreateGraphics();
            g.Clear(Color.White);
            Pen pen1 = new Pen(Color.Red);
            Brush brush1 = new SolidBrush(Color.WhiteSmoke);
            Brush brush2 = new SolidBrush(Color.LimeGreen);
            Brush brush3 = new SolidBrush(Color.RoyalBlue);
            Font font1 = new Font("Courier New", 16, FontStyle.Bold);
            Font font2 = new Font("細明體", 9);
            g.DrawString("磁盤容量分析", font1, brush2, new Point(60, 50));
            float angle1 = Convert.ToSingle((360 * (Convert.ToSingle(fsize / 100000000000) / Convert.ToSingle(tsize / 100000000000))));
            float angle2 = Convert.ToSingle((360 * (Convert.ToSingle((tsize - fsize) / 100000000000) / Convert.ToSingle(tsize / 100000000000))));
            g.FillPie(brush2, 60, 80, 150, 150, 0, angle1);
            g.FillPie(brush3, 60, 80, 150, 150, angle1, angle2);
            g.DrawRectangle(pen1, 30, 235, 200, 50);
            g.FillRectangle(brush2, 35, 245, 20, 10);
            g.DrawString("磁盤剩餘容量:" + dinfo.TotalFreeSpace / 1000 + "KB", font2, brush2, 55, 245);
            g.FillRectangle(brush3, 35, 265, 20, 10);
            g.DrawString("磁盤已用容量:" + (dinfo.TotalSize - dinfo.TotalFreeSpace) / 1000 + "KB", font2, brush3, 55, 265);

        }


        [DllImport("shell32.dll")]
        private static extern int SHFormatDrive(IntPtr hWnd, int drive, long fmtID, int Options);
        public const long SHFMT_ID_DEFAULT = 0xFFFF;
        private void button10_Click(object sender, EventArgs e)
        {
            int drive_id = 4;   //A: 0, B: 1, C: 2, D: 3, E: 4.....

            //格式化磁盤
            try
            {
                //偽執行
                //SHFormatDrive(this.Handle, drive_id, SHFMT_ID_DEFAULT, 0);
                MessageBox.Show("格式化完成", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            catch
            {
                MessageBox.Show("格式化失敗", "訊息", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("確定要休眠計算機嗎？") == DialogResult.OK)
            {
                //偽執行
                //Application.SetSuspendState(PowerState.Hibernate, true, true);
            }

        }

        [DllImport("kernel32.dll", CharSet = CharSet.Ansi)]
        public extern static bool SetSystemTime(ref SYSTEMTIME time);
        [StructLayout(LayoutKind.Sequential)]
        public struct SYSTEMTIME
        {
            public short Year;
            public short Month;
            public short DayOfWeek;
            public short Day;
            public short Hour;
            public short Minute;
            public short Second;
            public short Miliseconds;
        }

        private void SystemEvents_TimeChanged(object sender, EventArgs e)
        {
            MessageBox.Show("系統日期修改成功！", "提示", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //設定系統時間 為 12:34:56
            int setup_hour = 12;
            int setup_minute = 34;
            int setup_second = 56;
            SYSTEMTIME t = new SYSTEMTIME();
            t.Year = (short)DateTime.Now.Year;
            t.Month = (short)DateTime.Now.Month;
            t.Day = (short)DateTime.Now.Day;
            t.Hour = (short)(setup_hour - 8);//這個函數使用的是0時區的時間,例如，要設12點，則為12-8   
            t.Minute = (short)setup_minute;
            t.Second = (short)setup_second;
            //偽執行
            //bool v = SetSystemTime(ref t);
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            //參考/加入參考/.Net/Microsoft.VisualBasic
            Computer myComputer = new Computer();
            label1.Text = "物理內存總量（M）：" + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024);
            label2.Text = "可用物理內存（M）：" + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024);
            label3.Text = "虛擬內存總量（M）：" + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024);
            label4.Text = "可用虛擬內存（M）：" + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024);

            label5.Text = "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + " 秒";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from Win32_VideoController");
            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "顯示設備訊息\n";
                richTextBox1.Text += "顯示設備名稱：" + mo["Name"].ToString() + "\n";//顯示設備名稱
                richTextBox1.Text += "顯示設備PNPDeviceID：" + mo["PNPDeviceID"].ToString() + "\n";//顯示設備的PNPDeviceID
                richTextBox1.Text += "顯示設備驅動程序文件：" + mo["InstalledDisplayDrivers"].ToString() + "\n";//顯示設備的驅動程序文件
                richTextBox1.Text += "顯示設備驅動版本號：" + mo["DriverVersion"].ToString() + "\n";//顯示設備的驅動版本號
                richTextBox1.Text += "顯示設備的顯示處理器：" + mo["VideoProcessor"].ToString() + "\n";//顯示設備的顯示處理器
                richTextBox1.Text += "顯示設備的最大更新率：" + mo["MaxRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "顯示設備的最小更新率：" + mo["MinRefreshRate"].ToString() + "\n";//顯示設備的最大更新率
                richTextBox1.Text += "顯示設備目前顯示模式：" + mo["VideoModeDescription"].ToString() + "\n";//顯示設備目前顯示模式
            }
        }

        private void button14_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "環境變數" + "\t\t\t" + "變數值" + "\n";
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += DEntry.Key.ToString() + "\t" + DEntry.Value.ToString() + "\n";
            }
        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "系統版本：\t";

            OperatingSystem myOS = Environment.OSVersion;
            if (myOS.Version.Major == 5)
            {
                switch (myOS.Version.Minor)
                {
                    case 0:
                        richTextBox1.Text += "Windows 2000 " + myOS.ServicePack;
                        break;
                    case 1:
                        richTextBox1.Text += "Windows XP " + myOS.ServicePack;
                        break;
                    case 2:
                        richTextBox1.Text += "Windows Server 2003 " + " " + myOS.ServicePack;
                        break;
                    default:
                        richTextBox1.Text += myOS.ToString() + " " + myOS.ServicePack;
                        break;
                }
            }
            else
                richTextBox1.Text += myOS.VersionString + " " + myOS.ServicePack;

            richTextBox1.Text += "\n";




        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text = "檢索系統中正在執行的任務\n";
            Process[] myProcesses = Process.GetProcesses();
            foreach (Process myProcess in myProcesses)
            {
                if (myProcess.MainWindowTitle.Length > 0)
                    richTextBox1.Text += "任務名：" + myProcess.MainWindowTitle + "\n";
            }


        }

        private void button17_Click(object sender, EventArgs e)
        {
            //取得顯示設備相關資訊
            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from win32_VideoController");//声明一个用于检索设备管理信息的对象
            foreach (ManagementObject mo in mos.Get())//循环遍历WMI实例中的每一个对象
            {
                richTextBox1.Text += "顯示設備名稱 : " + mo["name"].ToString() + "\n";  //在文本框中显示显示设备的名称
                richTextBox1.Text += "PNPDeviceID : " + mo["PNPDeviceID"].ToString() + "\n"; //在文本框中显示显示设备的PNPDeviceID

                richTextBox1.Text += "最大更新率 : " + mo["MaxRefreshRate"].ToString() + "\n"; //在当前文本框中显示最大刷新率
                richTextBox1.Text += "最小更新率 : " + mo["MinRefreshRate"].ToString() + "\n"; //在当前文本框中显示最小刷新率
                richTextBox1.Text += "目前更新率 : " + mo["CurrentRefreshRate"].ToString() + "\n"; //在当前文本框中显示当前刷新率

                richTextBox1.Text += "顯示模式 : " + mo["VideoModeDescription"].ToString() + "\n"; //在文本框中显示设备的当前显示模式
            }
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //取得音效設備相關資訊
            ManagementObjectSearcher mos = new ManagementObjectSearcher("select * from Win32_SoundDevice");//声明一个用于检索设备管理信息的对象
            foreach (ManagementObject mo in mos.Get())//循环遍历WMI实例中的每一个对象
            {
                richTextBox1.Text += "音效設備名稱 : " + mo["ProductName"].ToString() + "\n"; //在当前文本框中显示声音设备的名称
                richTextBox1.Text += "PNPDeviceID : " + mo["PNPDeviceID"].ToString() + "\n";//在当前文本框中显示声音设备的PNPDeviceID
            }
        }

        private void button19_Click(object sender, EventArgs e)
        {
        }

        private void button20_Click(object sender, EventArgs e)
        {
            string foldername = @"C:\______test_files";
            string[] files = Directory.GetFiles(foldername);
            for (int i = 0; i < files.Length; i++)
            {
                richTextBox1.Text += files[i] + "\n";
                //textBox2.Lines = files;
            }
        }

        private void button21_Click(object sender, EventArgs e)
        {
            string filename1 = @"C:\______test_files\compare\aaaa.txt";
            string filename2 = @"C:\______test_files\compare\bbbb.txt";

            StreamReader sr1 = new StreamReader(filename1);
            StreamReader sr2 = new StreamReader(filename2);
            if (object.Equals(sr1.ReadToEnd(), sr2.ReadToEnd()))
            {
                MessageBox.Show("兩個文件相等");
            }
            else
            {
                MessageBox.Show("兩個文件不相等");
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //映射驅動器 = 網路芳鄰硬碟的連結

            SelectQuery selectQuery = new SelectQuery("select * from win32_logicaldisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(selectQuery);
            int i = 0;
            foreach (ManagementObject disk in searcher.Get())
            {
                string DriveType;
                DriveType = disk["DriveType"].ToString();
                if (DriveType == "4")
                {
                    richTextBox1.Text += "取得 : " + disk["Name"].ToString() + "\n";
                }
                i++;
            }


        }

        private void button23_Click(object sender, EventArgs e)
        {
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

        private void button24_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "臨時文件目錄 : " + Path.GetTempPath() + "\n";

            //string temp_filename = Path.GetTempFileName();
            //richTextBox1.Text += temp_filename + "\n";


            richTextBox1.Text += "取得運用程序所在目錄 : " + Application.StartupPath + "\n";

            richTextBox1.Text += "取得系統目前目錄 : " + System.Environment.CurrentDirectory + "\n";

            string foldername = @"C:\______test_files";

            richTextBox1.Text += "設定新的系統目前目錄\n";
            System.Environment.CurrentDirectory = foldername;
            richTextBox1.Text += "取得系統目前目錄 : " + System.Environment.CurrentDirectory + "\n";
        }
    }
}
