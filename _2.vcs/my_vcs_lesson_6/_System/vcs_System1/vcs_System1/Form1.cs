using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;            //for DriveInfo
using System.Net;   //for DNS
using System.IO.Ports;          //for serial ports
using System.Collections;   //for DictionaryEntry
using System.Globalization;
using System.Runtime.InteropServices;   //for DllImport, StructLayout
using System.Diagnostics;       //for Process
using System.Reflection;        //for Assembly
using System.Management;
using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Printing;  //for PrinterSettings

using Microsoft.VisualBasic.Devices;    //for Computer

/*
讀取/寫入程式預設值
到
方案總管/Properties/Settings.settings裏, 加入變數
*/

namespace vcs_System1
{
    public partial class Form1 : Form
    {
        DateTime start_time = DateTime.Now;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int i = 0;
            richTextBox1.Text += "啟動程式, 參數:\n";
            foreach (string arg in Environment.GetCommandLineArgs())
            {
                richTextBox1.Text += "第 " + i.ToString() + " 項 : " + arg + "\n";
                i++;
            }
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
            dx = 250;
            dy = 55;

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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);

            button12.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 11);

            button24.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 11);

            button36.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button40.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button41.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button42.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button43.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button44.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button45.Location = new Point(x_st + dx * 3, y_st + dy * 9);
            button46.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            button47.Location = new Point(x_st + dx * 3, y_st + dy * 11);

            groupBox1.Location = new Point(x_st + dx * 0, y_st + dy * 14);
            groupBox2.Location = new Point(x_st + dx * 1, y_st + dy * 14);

            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            richTextBox1.Size = new Size(660, 1040);

            dy = 0;

            bt_memory.Location = new Point(x_st + dx * 1 + 70, y_st + dy * 13 + 50);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 12 + 25);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 12 + 50);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 12 + 75);
            label5.Location = new Point(x_st + dx * 0 + 280, y_st + dy * 12);
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";
            label5.Text = "";

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        //關閉程式時，系統會問是否確認，只需要加下面這段就好 ST
        protected override void WndProc(ref Message m)
        {
            const int WM_SYSCOMMAND = 0x0112;
            const int SC_CLOSE = 0xF060;
            if (m.Msg == WM_SYSCOMMAND && (int)m.WParam == SC_CLOSE)
            {
                // 顯示MessageBox 
                DialogResult Result = MessageBox.Show("確定關閉表單", "表單訊息", MessageBoxButtons.YesNo);
                if (Result == DialogResult.Yes)
                {
                    // 關閉Form 
                    this.Close();
                }
                else
                {
                    return;
                }
            }
            base.WndProc(ref m);
        }
        //關閉程式時，系統會問是否確認，只需要加下面這段就好 SP

        private void button0_Click(object sender, EventArgs e)
        {
            //讀取電源狀態

            richTextBox1.Text += "讀取電源狀態\n";
            PowerStatus status = SystemInformation.PowerStatus;
            float percent = status.BatteryLifePercent;

            string percent_text = percent.ToString("P0");

            richTextBox1.Text += percent_text + "\n";
            if (status.PowerLineStatus == PowerLineStatus.Online)
            {
                if (percent < 1.0f)
                    richTextBox1.Text += percent_text + ", charging\n";
                else
                    richTextBox1.Text += "Online fully charged\n";
            }
            else
            {
                richTextBox1.Text += "Offline, " + percent_text + " remaining\n";
            }


            ShowPowerStatus1();
            ShowPowerStatus2();
        }

        private void ShowPowerStatus1()
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

        private void ShowPowerStatus2()
        {
            PowerStatus status = SystemInformation.PowerStatus;
            richTextBox1.Text += "Charge Status:\t" + status.BatteryChargeStatus.ToString() + "\n";

            if (status.BatteryFullLifetime == -1)
            {
                richTextBox1.Text += "Full Lifetime:\t" + "Unknown" + "\n";
            }
            else
            {
                richTextBox1.Text += "Full Lifetime (sec):\t" + status.BatteryFullLifetime.ToString() + "\n";
            }
            richTextBox1.Text += "Charge:\t\t" + status.BatteryLifePercent.ToString("P0") + "\n";
            if (status.BatteryLifeRemaining == -1)
            {
                richTextBox1.Text += "Life Remaining:\t" + "Unknown" + "\n";
            }
            else
            {
                richTextBox1.Text += "Life Remaining (sec):\t" + status.BatteryLifeRemaining.ToString() + "\n";
            }
            richTextBox1.Text += "Line Status:\t" + status.PowerLineStatus.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "電腦開機時間 : " + (Environment.TickCount / 1000).ToString() + " 秒\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //取得目前Windows版本

            OperatingSystem myOS = Environment.OSVersion;
            if (myOS.Version.Major == 5)
            {
                switch (myOS.Version.Minor)
                {
                    case 0:
                        MessageBox.Show("系統版本：" + "Windows 2000 " + myOS.ServicePack);
                        break;
                    case 1:
                        MessageBox.Show("系統版本：" + "Windows XP " + myOS.ServicePack);
                        break;
                    case 2:
                        MessageBox.Show("系統版本：" + "Windows Server 2003 " + " " + myOS.ServicePack);
                        break;
                    default:
                        MessageBox.Show("系統版本：" + myOS.ToString() + " " + myOS.ServicePack);
                        break;
                }
            }
            else
            {
                MessageBox.Show("系統版本：" + myOS.VersionString + " " + myOS.ServicePack);
            }

            //檢視目前系統版本
            OperatingSystem os = Environment.OSVersion;
            richTextBox1.Text += "目前系統版本： " + os.ToString() + "\n";
            richTextBox1.Text += "目前系統版本.Version： " + os.Version.ToString() + "\n";
            richTextBox1.Text += "目前系統版本.Platform： " + os.Platform.ToString() + "\n";
            richTextBox1.Text += "目前系統版本： ";
            if (os.Version.Major == 5)
            {
                switch (os.Version.Minor)
                {
                    case 0:
                        richTextBox1.Text += "Windows 2000 " + os.ServicePack + "\n";
                        break;
                    case 1:
                        richTextBox1.Text += "Windows XP " + os.ServicePack + "\n";
                        break;
                    case 2:
                        richTextBox1.Text += "Windows Server 2003 " + " " + os.ServicePack + "\n";
                        break;
                    default:
                        richTextBox1.Text += os.ToString() + " " + os.ServicePack + "\n";
                        break;
                }
            }
            else
            {
                richTextBox1.Text += os.VersionString + " " + os.ServicePack + "\n";
            }

            //判斷 User 電腦作業系統與位元數
            richTextBox1.Text += "Windows 作業系統 : " + GetOS() + ", " + GetBit() + "\n";








        }


        private static string GetOS()
        {
            //定義系統版本
            Version ver = Environment.OSVersion.Version;
            //Major主版本號,Minor副版本號
            if (ver.Major == 5 && ver.Minor == 0)
            {
                return "Windows 2000";
            }
            else if (ver.Major == 5 && ver.Minor == 1)
            {
                return "Windows XP";
            }
            else if (ver.Major == 5 && ver.Minor == 2)
            {
                return "Windows 2003";
            }
            else if (ver.Major == 6 && ver.Minor == 0)
            {
                return "Windows Vista";
            }
            else if (ver.Major == 6 && ver.Minor == 1)
            {
                return "Windows7";
            }
            else if (ver.Major == 6 && ver.Minor == 2)
            {
                return "Windows10";
            }
            else
            {
                return "未知";
            }
        }

        private static string GetBit()
        {
            if (Environment.Is64BitOperatingSystem)
                return "64bit";
            else
                return "32bit";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //取得CPU編號、硬盤編號等系統有關環境、屬性
            SystemInfo systemInfo = new SystemInfo();
            richTextBox1.Text += "操作系統：" + systemInfo.GetOperationSystemInName() + "\n";
            richTextBox1.Text += "CPU編號：" + systemInfo.GetCpuId() + "\n";
            richTextBox1.Text += "硬盤編號：" + systemInfo.GetMainHardDiskId() + "\n";
            richTextBox1.Text += "Windows目錄所在位置：" + systemInfo.GetSysDirectory() + "\n";
            richTextBox1.Text += "系統目錄所在位置：" + systemInfo.GetWinDirectory() + "\n";
            MemoryInfo memoryInfo = systemInfo.GetMemoryInfo();
            CpuInfo cpuInfo = systemInfo.GetCpuInfo();
            richTextBox1.Text += "dwActiveProcessorMask" + cpuInfo.dwActiveProcessorMask + "\n";
            richTextBox1.Text += "dwAllocationGranularity" + cpuInfo.dwAllocationGranularity + "\n";
            richTextBox1.Text += "CPU個數：" + cpuInfo.dwNumberOfProcessors + "\n";
            richTextBox1.Text += "OEM ID：" + cpuInfo.dwOemId + "\n";
            richTextBox1.Text += "頁面大小" + cpuInfo.dwPageSize + "\n";
            richTextBox1.Text += "CPU等級" + cpuInfo.dwProcessorLevel + "\n";
            richTextBox1.Text += "dwProcessorRevision" + cpuInfo.dwProcessorRevision + "\n";
            richTextBox1.Text += "CPU類型" + cpuInfo.dwProcessorType + "\n";
            richTextBox1.Text += "lpMaximumApplicationAddress" + cpuInfo.lpMaximumApplicationAddress + "\n";
            richTextBox1.Text += "lpMinimumApplicationAddress" + cpuInfo.lpMinimumApplicationAddress + "\n";
            richTextBox1.Text += "CPU類型：" + cpuInfo.dwProcessorType + "\n";
            richTextBox1.Text += "可用交換文件大小：" + memoryInfo.dwAvailPageFile + "\n";
            richTextBox1.Text += "可用物理內存大小：" + memoryInfo.dwAvailPhys + "\n";
            richTextBox1.Text += "可用虛擬內存大小" + memoryInfo.dwAvailVirtual + "\n";
            richTextBox1.Text += "操作系統位數：" + memoryInfo.dwLength + "\n";
            richTextBox1.Text += "已經使用內存大小：" + memoryInfo.dwMemoryLoad + "\n";
            richTextBox1.Text += "交換文件總大小：" + memoryInfo.dwTotalPageFile + "\n";
            richTextBox1.Text += "總物理內存大小：" + memoryInfo.dwTotalPhys + "\n";
            richTextBox1.Text += "總虛擬內存大小：" + memoryInfo.dwTotalVirtual + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得程式啟動時間
            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + " 秒\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //取得作業系統安裝時間
            ObjectQuery MyQuery = new ObjectQuery("SELECT * FROM Win32_OperatingSystem");
            ManagementScope MyScope = new ManagementScope();
            ManagementObjectSearcher MySearch = new ManagementObjectSearcher(MyScope, MyQuery);
            ManagementObjectCollection MyCollection = MySearch.Get();
            string StrInfo = "";
            foreach (ManagementObject MyObject in MyCollection)
            {
                StrInfo = MyObject.GetText(TextFormat.Mof);
            }
            string InstallDate = StrInfo.Substring(StrInfo.LastIndexOf("InstallDate") + 15, 14);

            richTextBox1.Text += "取得作業系統安裝時間 :\t" + InstallDate + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //取得記憶體狀態2
            ManagementObjectSearcher os_searcher = new ManagementObjectSearcher("SELECT * FROM Win32_OperatingSystem");

            foreach (ManagementObject mobj in os_searcher.Get())
            {
                GetInfo(mobj, "FreePhysicalMemory");
                GetInfo(mobj, "FreeSpaceInPagingFiles");
                GetInfo(mobj, "FreeVirtualMemory");
                GetInfo(mobj, "SizeStoredInPagingFiles");
                GetInfo(mobj, "TotalSwapSpaceSize");
                GetInfo(mobj, "TotalVirtualMemorySize");
                GetInfo(mobj, "TotalVisibleMemorySize");
            }
        }

        // Add information about the property to the ListView.
        private void GetInfo(ManagementObject mobj, string property_name)
        {
            object property_obj = mobj[property_name];
            if (property_obj == null)
            {
                //lvwInfo.AddRow(property_name, "???");
                richTextBox1.Text += property_name + "\t\t???\n";
            }
            else
            {
                ulong property_value = (ulong)property_obj * 1024;
                //lvwInfo.AddRow(property_name, property_value.ToFileSizeApi());
                richTextBox1.Text += property_name + "\t\t" + property_value.ToFileSizeApi() + "\n";
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Environment屬性
            richTextBox1.Text += "顯示系統資訊\n";
            richTextBox1.Text += "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + "秒" + "\n";
            richTextBox1.Text += "OSVersion： " + Environment.OSVersion + "\n";
            richTextBox1.Text += "Version： " + Environment.Version + "\n";
            richTextBox1.Text += "SystemPageSize： " + Environment.SystemPageSize + "\n";
            richTextBox1.Text += "UserDomainName： " + Environment.UserDomainName + "\n";
            richTextBox1.Text += "UserName： " + Environment.UserName + "\n";
            richTextBox1.Text += "MachineName： " + Environment.MachineName + "\n";
            richTextBox1.Text += "Is64BitOperatingSystem： " + Environment.Is64BitOperatingSystem + "\n";
            richTextBox1.Text += "Is64BitProcess： " + Environment.Is64BitProcess + "\n";
            richTextBox1.Text += "ProcessorCount： " + Environment.ProcessorCount + "\n";
            richTextBox1.Text += "SystemDirectory： " + Environment.SystemDirectory + "\n";
            richTextBox1.Text += "CurrentDirectory： " + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "CommandLine： " + Environment.CommandLine + "\n";

            richTextBox1.Text += "\n";
            richTextBox1.Text += "Environment屬性：\n";
            richTextBox1.Text += "CommandLine: " + Environment.CommandLine + "\n";
            richTextBox1.Text += "CurrentDirectory: " + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "ExitCode: " + Environment.ExitCode + "\n";
            richTextBox1.Text += "MachineName: " + Environment.MachineName + "\n";  //計算機名
            richTextBox1.Text += "SystemDirectory: " + Environment.SystemDirectory + "\n";
            richTextBox1.Text += "TickCount: " + Environment.TickCount + "\t系統啟動後經過的Tick數, 1個tick為1msec\n";
            richTextBox1.Text += "UserDomainName: " + Environment.UserDomainName + "\n";
            richTextBox1.Text += "UserInteractive: " + Environment.UserInteractive + "\n";
            richTextBox1.Text += "UserName: " + Environment.UserName + "\n";    //操作系統的登錄用戶名
            richTextBox1.Text += "WorkingSet: " + Environment.WorkingSet + "\n";
            richTextBox1.Text += "OSVersion: " + Environment.OSVersion.ToString() + "\n";

            richTextBox1.Text += "GetFolderPath System: " + Environment.GetFolderPath(Environment.SpecialFolder.System) + "\n";
            richTextBox1.Text += "[傳送到]資料夾位置 GetFolderPath SendTo: " + Environment.GetFolderPath(Environment.SpecialFolder.SendTo) + "\n";
            richTextBox1.Text += "GetFolderPath StartMenu: " + Environment.GetFolderPath(Environment.SpecialFolder.StartMenu) + "\n";
            richTextBox1.Text += "[我的文件夾]位置 GetFolderPath Personal: " + Environment.GetFolderPath(Environment.SpecialFolder.Personal) + "\n";
            richTextBox1.Text += "GetFolderPath MyMusic: " + Environment.GetFolderPath(Environment.SpecialFolder.MyMusic) + "\n";
            richTextBox1.Text += "GetFolderPath MyComputer: " + Environment.GetFolderPath(Environment.SpecialFolder.MyComputer) + "\n";

            richTextBox1.Text += "\n取得系統相關資訊\n";
            richTextBox1.Text += "目前系統目錄為：" + Environment.SystemDirectory + "\n";//顯示系統目錄
            richTextBox1.Text += "機器名稱為：" + Environment.MachineName + "\n";//顯示機器名稱
            richTextBox1.Text += "目前程式執行目錄：" + Environment.CurrentDirectory + "\n";//取得目前程式執行目錄
            richTextBox1.Text += "系統版本號：" + Environment.OSVersion.VersionString + "\n";//顯示系統版本號

            //讀取操作系統和CLR的版本
            OperatingSystem os = Environment.OSVersion;
            richTextBox1.Text += "Platform: " + os.Platform + "\n";
            richTextBox1.Text += "Service Pack:" + os.ServicePack + "\n";
            richTextBox1.Text += "Version: " + os.Version + "\n";
            richTextBox1.Text += "VersionString: " + os.VersionString + "\n";
            richTextBox1.Text += "CLR Version: " + System.Environment.Version + "\n";

            //環境參數
            string RootPath = Environment.GetEnvironmentVariable("HOMEDRIVE") + Environment.GetEnvironmentVariable("HOMEPATH") + @"\ScreenCapture";

            richTextBox1.Text += "HOMEDRIVE :\t" + Environment.GetEnvironmentVariable("HOMEDRIVE") + "\n";
            richTextBox1.Text += "HOMEPATH :\t" + Environment.GetEnvironmentVariable("HOMEPATH") + "\n";
            richTextBox1.Text += "my path :\t" + RootPath + "\n";

            string sys_dir = Environment.SystemDirectory;
            richTextBox1.Text += "SystemDirectory :\t" + sys_dir + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Environment參數
            richTextBox1.Text += "Environment參數\n";
            richTextBox1.Text += "CommandLine:\t" + Environment.CommandLine + "\n";
            richTextBox1.Text += "CurrentDirectory:\t" + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "MachineName:\t" + Environment.MachineName + "\n";
            richTextBox1.Text += "OSVersion:\t" + Environment.OSVersion + "\n";
            //richTextBox1.Text += "StackTrace:\t" + Environment.StackTrace + "\n";
            richTextBox1.Text += "SystemDirectory:\t" + Environment.SystemDirectory + "\n";
            richTextBox1.Text += "TickCount:\t" + Environment.TickCount + "\n";
            richTextBox1.Text += "Version:\t" + Environment.Version + "\n";
            richTextBox1.Text += "WorkingSet:\t" + Environment.WorkingSet + "\n";

            richTextBox1.Text += "列出所有環境變數\n";
            foreach (DictionaryEntry var in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += var.Key + "\t" + var.Value + "\n";
            }

            richTextBox1.Text += "列出Logical Drives\n";
            foreach (string drive in Environment.GetLogicalDrives())
            {
                richTextBox1.Text += "\t" + drive + "\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //temp資料 系統路徑

            richTextBox1.Text += "臨時文件目錄 : " + Path.GetTempPath() + "\n";

            //string temp_filename = Path.GetTempFileName();
            //richTextBox1.Text += temp_filename + "\n";

            richTextBox1.Text += "取得運用程序所在目錄 : " + Application.StartupPath + "\n";

            richTextBox1.Text += "取得系統目前目錄 : " + Environment.CurrentDirectory + "\n";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            richTextBox1.Text += "設定新的系統目前目錄\n";
            Environment.CurrentDirectory = foldername;
            richTextBox1.Text += "取得系統目前目錄 : " + Environment.CurrentDirectory + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "防止程序多次執行\n";
            richTextBox1.Text += "要修改 Program.cs\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "系統預設路徑\n";
            richTextBox1.Text += "CurrentDirectory :\t" + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "StartupPath :\t" + Application.StartupPath + "\n";
            richTextBox1.Text += "Form1.cs所在位置 :\t" + Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..")) + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //GetExecutingAssembly() 使用

            //取得目前應用程式版本
            richTextBox1.Text += "VersionInfo: " + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";

            richTextBox1.Text += "取得目前應用程式版本\n";
            richTextBox1.Text += FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";

            richTextBox1.Text += "提供磁碟上實體檔案的版本資訊\n";
            // Get the file version for the notepad.
            FileVersionInfo myFileVersionInfo = FileVersionInfo.GetVersionInfo(Environment.SystemDirectory + "\\Notepad.exe");

            // Print the file name and version number.
            richTextBox1.Text += "File: " + myFileVersionInfo.FileDescription + '\n' + "Version number: " + myFileVersionInfo.FileVersion + "\n";

            richTextBox1.Text += "取得NOTEPAD版本資訊\n";
            richTextBox1.Text += "VersionInfo: " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n";
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //程式所在位置
            string appPath = Application.ExecutablePath;
            richTextBox1.Text += "程式所在位置" + appPath + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            System.Net.IPHostEntry IPHost = System.Net.Dns.GetHostEntry(Environment.MachineName);
            if (IPHost.AddressList.Length > 0)
            {
                richTextBox1.Text += "1電腦本機IP : " + IPHost.AddressList[0].ToString() + "\n";
                //MessageBox.Show(IPHost.AddressList[0].ToString(), "電腦本機IP");
            }


            string hostName = Dns.GetHostName(); //獲取主機名稱
            IPAddress[] addresses = Dns.GetHostAddresses(hostName); //解析主機IP地址

            string[] IP = new string[addresses.Length]; //轉換為字符串形式
            for (int i = 0; i < addresses.Length; i++)
            {
                IP[i] = addresses[i].ToString();
                richTextBox1.Text += "2電腦本機IP : " + IP[i] + "\n";
            }

        }

        private void button15_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "MachineName: " + Environment.MachineName + "\n";
            richTextBox1.Text += "# of processors (logical): " + Environment.ProcessorCount + "\n";
            //richTextBox1.Text += "# of processors (physical): " + CountPhysicalProcessors() + "\n";
            //richTextBox1.Text += "RAM installed:   bytes" + CountPhysicalMemory() + "\n";
            richTextBox1.Text += "Is OS 64-bit? " + Environment.Is64BitOperatingSystem + "\n";
            richTextBox1.Text += "Is process 64-bit? " + Environment.Is64BitProcess + "\n";
            richTextBox1.Text += "Little-endian: " + BitConverter.IsLittleEndian + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "C# 產生 GUID 1\n";
            //可以直接透過內建方法，產生 GUID

            Guid guid = Guid.NewGuid();
            richTextBox1.Text += "GUID1 : " + guid + "\n";

            guid = Guid.NewGuid();
            richTextBox1.Text += "GUID2 : " + guid + "\n";

            guid = Guid.NewGuid();
            richTextBox1.Text += "GUID3 : " + guid + "\n";

            richTextBox1.Text += "C# 產生 GUID 2\n";
            richTextBox1.Text += "GUID N :\t" + Guid.NewGuid().ToString("N") + "\n";//結果為：38bddf48f43c48588e0d78761eaa1ce6
            richTextBox1.Text += "GUID N :\t" + Guid.NewGuid().ToString("D") + "\n";//結果為：57d99d89-caab-482a-a0e9-a0a803eed3ba (默認的為第2種效果)
            richTextBox1.Text += "GUID N :\t" + Guid.NewGuid().ToString("B") + "\n";//結果為：{09f140d5-af72-44ba-a763-c861304b46f8}
            richTextBox1.Text += "GUID N :\t" + Guid.NewGuid().ToString("P") + "\n";//結果為：(778406c2-efff-4262-ab03-70a77d09c2b5)

            string newName = Guid.NewGuid().ToString();

            richTextBox1.Text += "C# 產生 GUID 3\n";
            richTextBox1.Text += newName + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //取得電腦名稱
            richTextBox1.Text += "電腦名稱 1 : " + Environment.MachineName + "\n";
            richTextBox1.Text += "電腦名稱 2 : " + Dns.GetHostName() + "\n";
            richTextBox1.Text += "電腦名稱 3 : " + SystemInformation.ComputerName + "\n";
            richTextBox1.Text += "電腦名稱 4 : " + Environment.GetEnvironmentVariable("COMPUTERNAME") + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            Environment 類別
            rihTextBox1.Text += "Environment 類別\n";

            richTextBox1.Text += "處理序的命令列：" + Environment.CommandLine + "\n";
            richTextBox1.Text += "工作目錄的完整路徑：" + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "處理序的結束代碼：" + Environment.ExitCode + "\n";
            richTextBox1.Text += "是否正常關機：" + Environment.HasShutdownStarted + "\n";
            richTextBox1.Text += "NetBIOS名稱：" + Environment.MachineName + "\n";
            richTextBox1.Text += "環境定義的新字串：" + Environment.NewLine + "\n";
            richTextBox1.Text += "作業系統平臺：" + Environment.OSVersion.Platform + "\n";
            richTextBox1.Text += "Service Pack版本：" + Environment.OSVersion.ServicePack + "\n";
            richTextBox1.Text += "作業系統版本：" + Environment.OSVersion.Version + "\n";
            richTextBox1.Text += "串連字串表示：" + Environment.OSVersion.VersionString + "\n";
            richTextBox1.Text += "處理器數目：" + Environment.ProcessorCount + "\n";
            richTextBox1.Text += "堆疊追蹤資訊：" + Environment.StackTrace + "\n";
            richTextBox1.Text += "系統目錄完整路徑：" + Environment.SystemDirectory + "\n";
            richTextBox1.Text += "系統啟動後的毫秒數：" + Environment.TickCount + "\n";
            richTextBox1.Text += "使用者網域名稱：" + Environment.UserDomainName + "\n";
            richTextBox1.Text += "處理序是否與使用者互動：" + Environment.UserInteractive + "\n";
            richTextBox1.Text += "使用者名稱：" + Environment.UserName + "\n";
            richTextBox1.Text += "Version：" + Environment.Version + "\n";
            richTextBox1.Text += "組件元件值：" + Environment.Version.Build + "\n";
            richTextBox1.Text += "主要元件值：" + Environment.Version.Major + "\n";
            richTextBox1.Text += "修訂編號的高 16 位元：" + Environment.Version.MajorRevision + "\n";
            richTextBox1.Text += "次要元件值：" + Environment.Version.Minor + "\n";
            richTextBox1.Text += "修訂編號的低 16 位元：" + Environment.Version.MinorRevision + "\n";
            richTextBox1.Text += "修訂元件值：" + Environment.Version.Revision + "\n";
            richTextBox1.Text += "實際記憶體數量：" + Environment.WorkingSet + "\n";

            string strFinal;
            string strQuery = "系統磁碟機：%SystemDrive% 與 系統根目錄：%SystemRoot%";
            strFinal = Environment.ExpandEnvironmentVariables(strQuery);
            richTextBox1.Text += strFinal + "\n";

            string[] arguments = Environment.GetCommandLineArgs();
            richTextBox1.Text += "取得命令列的Args: " + string.Join(", ", arguments) + "\n";

            richTextBox1.Text += "系統特殊資料夾的路徑：" + Environment.GetFolderPath(Environment.SpecialFolder.System) + "\n";

            string[] drives = Environment.GetLogicalDrives();
            richTextBox1.Text += "系統磁碟機：" + string.Join(", ", drives) + "\n";

            //作業系統位置
            string str = Environment.GetEnvironmentVariable("SystemRoot");
            richTextBox1.Text += "作業系統在" + str + "\n";
            string dir = str.Substring(0, 2);
            richTextBox1.Text += "作業系統在" + dir + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            //取得系統環境變數
            richTextBox1.Text += "環境變數" + "\t\t\t" + "變數值" + "\n";
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += DEntry.Key.ToString() + "\t" + DEntry.Value.ToString() + "\n";
            }
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //UserAppDataRegistry使用
            richTextBox1.Text += "UserAppDataRegistry使用\n";

            richTextBox1.Text += "把數值寫進系統變數AAAA\n";
            Application.UserAppDataRegistry.SetValue("AAAA", 123);

            richTextBox1.Text += "把系統變數AAAA的內容讀出來\n";
            int result;
            result = (int)Application.UserAppDataRegistry.GetValue("AAAA");
            richTextBox1.Text += "結果 : " + result.ToString() + "\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            checkSuperuser chk = new checkSuperuser();
            chk.ShowDialog();
        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {
        }

        private void button24_Click(object sender, EventArgs e)
        {
            //取得程式的編譯時間
            richTextBox1.Text += "編譯時間 : " + GetLinkerTime() + "\n";
        }

        //取得程式的編譯時間
        DateTime GetLinkerTime()
        {
            var filePath = Assembly.GetExecutingAssembly().Location;

            const int c_PeHeaderOffset = 60;
            const int c_LinkerTimestampOffset = 8;

            var buffer = new byte[256];

            using (var stream = new FileStream(filePath, FileMode.Open, FileAccess.Read))
            {
                stream.Read(buffer, 0, 256);
            }

            var offset = BitConverter.ToInt32(buffer, c_PeHeaderOffset);
            var secondsSince1970 = BitConverter.ToInt32(buffer, offset + c_LinkerTimestampOffset);
            var epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);

            var linkTimeUtc = epoch.AddSeconds(secondsSince1970);
            var tz = TimeZoneInfo.Local;
            var localTime = TimeZoneInfo.ConvertTimeFromUtc(linkTimeUtc, tz);
            return localTime;
        }

        private void button25_Click(object sender, EventArgs e)
        {
            //列印出所有的編碼方式
            StringBuilder sb = new StringBuilder();
            foreach (EncodingInfo ei in Encoding.GetEncodings())
            {
                sb.Append(ei.CodePage).Append("\t").Append(ei.Name).Append("\t").Append(ei.DisplayName).Append("\r\n");
            }

            richTextBox1.Text += sb.ToString() + "\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //(A)關於
            //方案總管/vcs_System1/右鍵/加入/Windows Form/關於對話方塊/新增

            AboutBox1 formab = new AboutBox1();
            formab.ShowDialog();

            //方案總管空白處按右鍵/屬性/組件資訊, 修改要顯示的程式資訊
        }

        private void button27_Click(object sender, EventArgs e)
        {
            // 找出字體大小,並算出比例
            // 取出螢幕DPI值
            float dpiX, dpiY;
            Graphics graphics = this.CreateGraphics();
            dpiX = graphics.DpiX;
            dpiY = graphics.DpiY;
            richTextBox1.Text += "dpiX = " + dpiX.ToString() + "\n";
            richTextBox1.Text += "dpiY = " + dpiY.ToString() + "\n";
        }

        private void button28_Click(object sender, EventArgs e)
        {
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //C# 讀取語系區域
            string systemName = System.Globalization.CultureInfo.CurrentCulture.Name;
            string systemName2 = System.Globalization.CultureInfo.CurrentCulture.NativeName;
            richTextBox1.Text += systemName + "\n";
            richTextBox1.Text += systemName2 + "\n";
        }

        private void button31_Click(object sender, EventArgs e)
        {
            // part 1
            ListView lv = new ListView();
            lv.Left = 900;
            lv.Top = 680;
            lv.Width = 360;
            lv.Height = 380;
            lv.BackColor = Color.Pink;
            this.Controls.Add(lv);
            this.Size = new Size(this.Size.Width + 330, this.Size.Height);

            lv.View = View.Details;//設定控制元件顯示方式
            lv.GridLines = true;//是否顯示網格
            lv.Columns.Add("環境變數", 150, HorizontalAlignment.Left);//新增列標頭
            lv.Columns.Add("變數值", 150, HorizontalAlignment.Left);//新增列標頭
            ListViewItem myItem;//建立ListViewItem對像
            //取得系統環境變數及對應的變數值，並顯示在ListView控制元件中
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                myItem = new ListViewItem(DEntry.Key.ToString(), 0);//建立ListViewItem對像
                myItem.SubItems.Add(DEntry.Value.ToString());//新增子項集合
                lv.Items.Add(myItem);//將子項集合新增到控制元件中
            }

            // part 2
            ManagementClass mc = new ManagementClass("win32_processor"); //建立ManagementClass物件
            ManagementObjectCollection moc = mc.GetInstances();          //取得CPU訊息

            foreach (ManagementObject mo in moc)
            {
                richTextBox1.Text += "CPU編號\t\t" + mo["processorid"].ToString() + "\n";//取得CPU編號
            }

            ManagementObjectSearcher mos = new ManagementObjectSearcher("Select * From Win32_Processor"); //查詢CPU訊息

            foreach (ManagementObject mo in mos.Get())
            {
                richTextBox1.Text += "CPU製造商名稱\t\t" + mo["Manufacturer"].ToString() + "\n";//取得CPU製造商名稱
                richTextBox1.Text += "CPU版本號\t\t" + mo["Version"].ToString() + "\n";     //取得CPU版本號
                richTextBox1.Text += "CPU產品名稱\t\t" + mo["Name"].ToString() + "\n";        //取得CPU產品名稱
            }

            // part 3
            SelectQuery query = new SelectQuery("Select * from Win32_BaseBoard"); // 查詢主板
            ManagementObjectSearcher dev = new ManagementObjectSearcher(query);   // 執行query
            ManagementObjectCollection.ManagementObjectEnumerator enumerator = dev.Get().GetEnumerator();
            enumerator.MoveNext();
            ManagementBaseObject mbo = enumerator.Current;                    // 取得目前主板
            richTextBox1.Text += "主板編號\t\t" + mbo.GetPropertyValue("SerialNumber").ToString() + "\n";  //取得主板編號
            richTextBox1.Text += "主板製造商\t\t" + mbo.GetPropertyValue("Manufacturer").ToString() + "\n";  //取得主板製造商
            richTextBox1.Text += "主板型號\t\t" + mbo.GetPropertyValue("Name").ToString() + "\n";          //取得主板型號

        }

        private void button32_Click(object sender, EventArgs e)
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

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "到 【偵錯】→【視窗】→【即時運算】 看結果\n\r";
            richTextBox1.Text += "要勾選 【工具】→【選項】→【偵錯】→【將所有輸出視窗文字重新導向到即時運算視窗】\n\r";

            int a = 123;
            int b = 456;

            System.Diagnostics.Debug.Print("即時運算視窗輸出除錯訊息 測試訊息！！！Form1！！！" + a.ToString());
            System.Diagnostics.Debug.WriteLine("即時運算視窗輸出除錯訊息 測試訊息！！！Form1！！！" + b.ToString());

            Debug.Print("aaaaaaaaaaaaaaaaaaaaaaaaaa無換行符號1");
            Debug.Print("aaaaaaaaaaaaaaaaaaaaaaaaaa無換行符號2");
            Debug.Print("aaaaaaaaaaaaaaaaaaaaaaaaaa無換行符號3");
        }

        private void button35_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取程式預設值\n";
            ReadSettings();
        }

        private void button36_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "詢問確定關閉表單\n";
            richTextBox1.Text += "找個地方加入WndProc()即可\n";
        }

        [DllImport("kernel32.dll")]
        private static extern int SetComputerName(string ipComputerName);//重寫API函數

        private void button37_Click(object sender, EventArgs e)
        {
            //取得並修改電腦名(偽執行)
            Computer computer = new Computer();//創建計算機對象
            richTextBox1.Text += "取得原計算機名 : " + computer.Name + "\n";

            richTextBox1.Text += "偽執行 計算機名稱修改, 須重啟計算機使之生效\n";
            //SetComputerName("lion-mouse");//修改計算機名稱
        }

        private void button38_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "C# 透過Win32取得滑鼠位置 GetCursorPos\n";
        }

        private void button39_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫入程式預設值\n";
            SaveSettings();
        }

        private void button40_Click(object sender, EventArgs e)
        {
            //1. 參考 -> 加入參考 -> .NET/Microsoft.VisualBasic
            //2. using Microsoft.VisualBasic.Devices;

            Computer myComputer = new Computer();
            richTextBox1.Text += "物理內存總量(M)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024) + "\n";
            richTextBox1.Text += "可用物理內存(M)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024) + "\n";
            richTextBox1.Text += "虛擬內存總量(M)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024) + "\n";
            richTextBox1.Text += "可用虛擬內存(M)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024) + "\n";
        }

        private void button41_Click(object sender, EventArgs e)
        {
        }

        private void button42_Click(object sender, EventArgs e)
        {
        }

        private void button43_Click(object sender, EventArgs e)
        {
        }

        private void button44_Click(object sender, EventArgs e)
        {
        }

        private void button45_Click(object sender, EventArgs e)
        {
        }

        private void button46_Click(object sender, EventArgs e)
        {
        }

        private void button47_Click(object sender, EventArgs e)
        {
        }

        [DllImport("User32")]
        internal extern static bool GetCursorPos(out MousePoint point);

        internal struct MousePoint
        {
            public int x;
            public int y;
        };

        private void timer1_Tick(object sender, EventArgs e)
        {
            MousePoint point;
            GetCursorPos(out point);
            this.Text = point.x.ToString() + ", " + point.y.ToString();
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            Computer myComputer = new Computer();
            label1.Text = "物理內存總量(B)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory);
            label2.Text = "可用物理內存(B)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory);
            label3.Text = "虛擬內存總量(B)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory);
            label4.Text = "可用虛擬內存(B)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory);

            label1.Text = "物理內存總量(B)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024) + " MB";
            label2.Text = "可用物理內存(B)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024) + " MB";
            label3.Text = "虛擬內存總量(B)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024) + " MB";
            label4.Text = "可用虛擬內存(B)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024) + " MB";

            timer2.Interval = 2000;
        }

        private void bt_memory_Click(object sender, EventArgs e)
        {
            timer2.Enabled = true;
        }

        // Save the current settings.
        private void SaveSettings()
        {
            string dir_name = @"D:\_git\vcs\_1.data\______test_files1\__pic\_書畫字圖\_peony2";

            Properties.Settings.Default.PictureDirectory = dir_name;
            Properties.Settings.Default.UpdateRegistry = true;
            Properties.Settings.Default.Location = Location;
            Properties.Settings.Default.Size = Size;
            Properties.Settings.Default.Delay = 123;
            Properties.Settings.Default.Save();
        }

        private void ReadSettings()
        {
            richTextBox1.Text += "Default.PictureDirectory" + "\t" + Properties.Settings.Default.PictureDirectory + "\n";
            richTextBox1.Text += "Default.UpdateRegistry" + "\t" + Properties.Settings.Default.UpdateRegistry + "\n";
            richTextBox1.Text += "Default.Location" + "\t" + Properties.Settings.Default.Location + "\n";
            richTextBox1.Text += "Default.Size" + "\t" + Properties.Settings.Default.Size.ToString() + "\n";
            richTextBox1.Text += "Default.Delay" + "\t" + Properties.Settings.Default.Delay.ToString() + "\n";
        }

        #region Windows 開關機
        [DllImport("user32")]
        public static extern bool ExitWindowsEx(uint uFlags, uint dwReason);

        [DllImport("user32")]
        public static extern void LockWorkStation();

        // Shutdown.
        private void btnShutdown_Click(object sender, EventArgs e)
        {
            var psi = new ProcessStartInfo("shutdown", "/s /t 0");
            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            //偽執行
            //Process.Start(psi);
        }

        // Reboot.
        private void btnReboot_Click(object sender, EventArgs e)
        {
            var psi = new ProcessStartInfo("shutdown", "/r /t 0");
            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            //偽執行
            //Process.Start(psi);
        }

        // Log off.
        private void btnLogOff_Click(object sender, EventArgs e)
        {
            //偽執行
            //ExitWindowsEx(0, 0);
        }

        // Lock.
        private void btnLock_Click(object sender, EventArgs e)
        {
            //偽執行
            //LockWorkStation();
        }

        // Hibernate.
        private void btnHibernate_Click(object sender, EventArgs e)
        {
            //偽執行
            //Application.SetSuspendState(PowerState.Hibernate, true, true);
        }

        // Sleep.
        private void btnSleep_Click(object sender, EventArgs e)
        {
            //偽執行
            //Application.SetSuspendState(PowerState.Suspend, true, true);
        }

        #endregion

        private void timer3_Tick(object sender, EventArgs e)
        {
        }
    }


    /**/
    /**
* LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
* 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
* LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
* LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
*/
    /**/
    /// <summary>
    /// 定義CPU的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct CpuInfo
    {
        /**/
        /// <summary>
        /// OEM ID
        /// </summary>
        public uint dwOemId;
        /**/
        /// <summary>
        /// 頁面大小
        /// </summary>
        public uint dwPageSize;
        public uint lpMinimumApplicationAddress;
        public uint lpMaximumApplicationAddress;
        public uint dwActiveProcessorMask;
        /**/
        /// <summary>
        /// CPU個數
        /// </summary>
        public uint dwNumberOfProcessors;
        /**/
        /// <summary>
        /// CPU類型
        /// </summary>
        public uint dwProcessorType;
        public uint dwAllocationGranularity;
        /**/
        /// <summary>
        /// CPU等級
        /// </summary>
        public uint dwProcessorLevel;
        public uint dwProcessorRevision;
    }


    /**/
    /**
* LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
* 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
* LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
* LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
*/
    /**/
    /// <summary>
    /// 定義內存的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct MemoryInfo
    {
        /**/
        /// <summary>
        ///
        /// </summary>
        public uint dwLength;
        /**/
        /// <summary>
        /// 已經使用的內存
        /// </summary>
        public uint dwMemoryLoad;
        /**/
        /// <summary>
        /// 總物理內存大小
        /// </summary>
        public uint dwTotalPhys;
        /**/
        /// <summary>
        /// 可用物理內存大小
        /// </summary>
        public uint dwAvailPhys;
        /**/
        /// <summary>
        /// 交換文件總大小
        /// </summary>
        public uint dwTotalPageFile;
        /**/
        /// <summary>
        /// 可用交換文件大小
        /// </summary>
        public uint dwAvailPageFile;
        /**/
        /// <summary>
        /// 總虛擬內存大小
        /// </summary>
        public uint dwTotalVirtual;
        /**/
        /// <summary>
        /// 可用虛擬內存大小
        /// </summary>
        public uint dwAvailVirtual;
    }

    /**/
    /**
* LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
* 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
* LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
* LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
*/
    /**/
    /// <summary>
    /// 定義系統時間的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct SystemTimeInfo
    {
        /**/
        /// <summary>
        /// 年
        /// </summary>
        public ushort wYear;
        /**/
        /// <summary>
        /// 月
        /// </summary>
        public ushort wMonth;
        /**/
        /// <summary>
        /// 星期
        /// </summary>
        public ushort wDayOfWeek;
        /**/
        /// <summary>
        /// 天
        /// </summary>
        public ushort wDay;
        /**/
        /// <summary>
        /// 小時
        /// </summary>
        public ushort wHour;
        /**/
        /// <summary>
        /// 分鐘
        /// </summary>
        public ushort wMinute;
        /**/
        /// <summary>
        /// 秒
        /// </summary>
        public ushort wSecond;
        /**/
        /// <summary>
        /// 毫秒
        /// </summary>
        public ushort wMilliseconds;
    }





    /**/
    /// <summary> 
    /// SystemInfo 的摘要說明 
    /// </summary> 
    public class SystemInfo
    {
        private const int CHAR_COUNT = 128;
        public SystemInfo()
        {

        }
        [DllImport("kernel32")]
        private static extern void GetWindowsDirectory(StringBuilder WinDir, int count);

        [DllImport("kernel32")]
        private static extern void GetSystemDirectory(StringBuilder SysDir, int count);

        [DllImport("kernel32")]
        private static extern void GetSystemInfo(ref CpuInfo cpuInfo);

        [DllImport("kernel32")]
        private static extern void GlobalMemoryStatus(ref MemoryInfo memInfo);

        [DllImport("kernel32")]
        private static extern void GetSystemTime(ref SystemTimeInfo sysInfo);

        /**/
        /// <summary> 
        /// 查詢CPU編號 
        /// </summary> 
        /// <returns></returns> 
        public string GetCpuId()
        {
            ManagementClass mClass = new ManagementClass("Win32_Processor");
            ManagementObjectCollection moc = mClass.GetInstances();
            string cpuId = null;
            foreach (ManagementObject mo in moc)
            {
                cpuId = mo.Properties["ProcessorId"].Value.ToString();
                break;
            }
            return cpuId;
        }

        /**/
        /// <summary> 
        /// 查詢硬盤編號 
        /// </summary> 
        /// <returns></returns> 
        public string GetMainHardDiskId()
        {
            ManagementObjectSearcher searcher = new ManagementObjectSearcher("SELECT * FROM Win32_PhysicalMedia");
            String hardDiskID = null;
            foreach (ManagementObject mo in searcher.Get())
            {
                hardDiskID = mo["SerialNumber"].ToString().Trim();
                break;
            }
            return hardDiskID;
        }

        /**/
        /// <summary> 
        /// 獲取Windows目錄 
        /// </summary> 
        /// <returns></returns> 
        public string GetWinDirectory()
        {
            StringBuilder sBuilder = new StringBuilder(CHAR_COUNT);
            GetWindowsDirectory(sBuilder, CHAR_COUNT);
            return sBuilder.ToString();
        }

        /**/
        /// <summary> 
        /// 獲取系統目錄 
        /// </summary> 
        /// <returns></returns> 
        public string GetSysDirectory()
        {
            StringBuilder sBuilder = new StringBuilder(CHAR_COUNT);
            GetSystemDirectory(sBuilder, CHAR_COUNT);
            return sBuilder.ToString();
        }

        /**/
        /// <summary> 
        /// 獲取CPU信息 
        /// </summary> 
        /// <returns></returns> 
        public CpuInfo GetCpuInfo()
        {
            CpuInfo cpuInfo = new CpuInfo();
            GetSystemInfo(ref cpuInfo);
            return cpuInfo;
        }

        /**/
        /// <summary> 
        /// 獲取系統內存信息 
        /// </summary> 
        /// <returns></returns> 
        public MemoryInfo GetMemoryInfo()
        {
            MemoryInfo memoryInfo = new MemoryInfo();
            GlobalMemoryStatus(ref memoryInfo);
            return memoryInfo;
        }

        /**/
        /// <summary> 
        /// 獲取系統時間信息 
        /// </summary> 
        /// <returns></returns> 
        public SystemTimeInfo GetSystemTimeInfo()
        {
            SystemTimeInfo systemTimeInfo = new SystemTimeInfo();
            GetSystemTime(ref systemTimeInfo);
            return systemTimeInfo;
        }

        /**/
        /// <summary> 
        /// 獲取系統名稱 
        /// </summary> 
        /// <returns></returns> 
        public string GetOperationSystemInName()
        {
            OperatingSystem os = System.Environment.OSVersion;
            string osName = "UNKNOWN";
            switch (os.Platform)
            {
                case PlatformID.Win32Windows:
                    switch (os.Version.Minor)
                    {
                        case 0: osName = "Windows 95"; break;
                        case 10: osName = "Windows 98"; break;
                        case 90: osName = "Windows ME"; break;
                    }
                    break;
                case PlatformID.Win32NT:
                    switch (os.Version.Major)
                    {
                        case 3: osName = "Windws NT 3.51"; break;
                        case 4: osName = "Windows NT 4"; break;
                        case 5: if (os.Version.Minor == 0)
                            {
                                osName = "Windows 2000";
                            }
                            else if (os.Version.Minor == 1)
                            {
                                osName = "Windows XP";
                            }
                            else if (os.Version.Minor == 2)
                            {
                                osName = "Windows Server 2003";
                            }
                            break;
                        case 6: osName = "Longhorn"; break;
                    }
                    break;
            }
            return String.Format("{0},{1}", osName, os.Version.ToString());
        }
    }
}
