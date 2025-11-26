using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for DriveInfo
using System.Net;   //for DNS
using System.IO.Ports;  //for serial ports
using System.Collections;   //for DictionaryEntry
using System.Globalization;
using System.Runtime.InteropServices;   //for DllImport, StructLayout
using System.Diagnostics;       //for Process
using System.Reflection;        //for Assembly
using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Printing;  //for PrinterSettings
using System.Threading;

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

        Process[] MyProcesses;
        Thread td;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            CheckForIllegalCrossThreadCalls = false;
            MyProcesses = Process.GetProcesses();
            lb_processes.Text = "進程數 : " + MyProcesses.Length.ToString();
            myUser();
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
            dx = 200 + 5;
            dy = 60 + 5;

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

            button20.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 2, y_st + dy * 9);

            button30.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            lb_processes.Location = new Point(x_st + dx * 4, y_st + dy * 9);//進程數

            groupBox1.Size = new Size(200, 150);//Windows 開關機(偽執行)
            groupBox2.Size = new Size(320, 150);
            groupBox3.Size = new Size(320, 100);
            groupBox4.Size = new Size(320, 100);

            groupBox2.Location = new Point(x_st + dx * 4, y_st + dy * 0);//記憶體狀態
            groupBox3.Location = new Point(x_st + dx * 4, y_st + dy * 2 + 20);//物理內存
            groupBox4.Location = new Point(x_st + dx * 4, y_st + dy * 4);//虛擬內存
            groupBox1.Location = new Point(x_st + dx * 4, y_st + dy * 6);

            richTextBox1.Size = new Size(400, 740);
            richTextBox1.Location = new Point(x_st + dx * 5 + 130, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            dy = 30;
            label1.Location = new Point(x_st + dx * 0, y_st + 12 + dy * 0);
            label2.Location = new Point(x_st + dx * 0, y_st + 12 + dy * 1);
            label3.Location = new Point(x_st + dx * 0, y_st + 12 + dy * 2);
            label4.Location = new Point(x_st + dx * 0, y_st + 12 + dy * 3);
            label1.Text = "";
            label2.Text = "";
            label3.Text = "";
            label4.Text = "";

            this.Size = new Size(1600, 800);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        //是否安裝音效卡 ST
        [DllImport("winmm.dll", EntryPoint = "waveOutGetNumDevs")]
        public static extern int waveOutGetNumDevs();
        private void button1_Click(object sender, EventArgs e)
        {
            if (waveOutGetNumDevs() != 0)
            {
                richTextBox1.Text += "已安裝音效卡\n";
            }
            else
            {
                richTextBox1.Text += "未安裝音效卡\n";
            }
        }
        //是否安裝音效卡 SP

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
            //取得系統有關環境、屬性

            SystemInfo systemInfo = new SystemInfo();
            richTextBox1.Text += "操作系統：" + systemInfo.GetOperationSystemInName() + "\n";
            richTextBox1.Text += "Windows目錄所在位置：" + systemInfo.GetSysDirectory() + "\n";
            richTextBox1.Text += "系統目錄所在位置：" + systemInfo.GetWinDirectory() + "\n";

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

            MemoryInfo memoryInfo = systemInfo.GetMemoryInfo();
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
            richTextBox1.Text += "讀取程式預設值\n";
            ReadSettings();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "詢問確定關閉表單\n";
            richTextBox1.Text += "找個地方加入WndProc()即可\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Environment 大全

            richTextBox1.Text += "電腦開機時間 : " + (Environment.TickCount / 1000).ToString() + " 秒\n";

            //------------------------------------------------------------  # 60個

            //Environment屬性

            //Environment 類別
            richTextBox1.Text += "Environment 類別\n";

            richTextBox1.Text += "處理序的命令列：" + Environment.CommandLine + "\n";
            richTextBox1.Text += "工作目錄的完整路徑：" + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "目前程式執行目錄：" + Environment.CurrentDirectory + "\n";//取得目前程式執行目錄
            richTextBox1.Text += "處理序的結束代碼：" + Environment.ExitCode + "\n";
            richTextBox1.Text += "是否正常關機：" + Environment.HasShutdownStarted + "\n";
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
            richTextBox1.Text += "使用者名稱：" + Environment.UserName + "\n";//操作系統的登錄用戶名
            richTextBox1.Text += "Version：" + Environment.Version + "\n";
            richTextBox1.Text += "組件元件值：" + Environment.Version.Build + "\n";
            richTextBox1.Text += "主要元件值：" + Environment.Version.Major + "\n";
            richTextBox1.Text += "修訂編號的高 16 位元：" + Environment.Version.MajorRevision + "\n";
            richTextBox1.Text += "次要元件值：" + Environment.Version.Minor + "\n";
            richTextBox1.Text += "修訂編號的低 16 位元：" + Environment.Version.MinorRevision + "\n";
            richTextBox1.Text += "修訂元件值：" + Environment.Version.Revision + "\n";
            richTextBox1.Text += "實際記憶體數量：" + Environment.WorkingSet + "\n";

            richTextBox1.Text += "系統啟動後經過的時間： " + (Environment.TickCount / 1000).ToString() + "秒" + "\n";
            richTextBox1.Text += "系統版本號：" + Environment.OSVersion.VersionString + "\n";//顯示系統版本號
            richTextBox1.Text += "OSVersion： " + Environment.OSVersion + "\n";
            richTextBox1.Text += "OSVersion: " + Environment.OSVersion.ToString() + "\n";
            richTextBox1.Text += "Version： " + Environment.Version + "\n";
            richTextBox1.Text += "SystemPageSize： " + Environment.SystemPageSize + "\n";

            richTextBox1.Text += "電腦名稱 : " + Environment.MachineName + "\n";

            richTextBox1.Text += "Is64BitOperatingSystem： " + Environment.Is64BitOperatingSystem + "\n";
            richTextBox1.Text += "Is64BitProcess： " + Environment.Is64BitProcess + "\n";
            richTextBox1.Text += "ProcessorCount： " + Environment.ProcessorCount + "\n";

            richTextBox1.Text += "TickCount: " + Environment.TickCount + "\t系統啟動後經過的Tick數, 1個tick為1msec\n";

            richTextBox1.Text += "WorkingSet: " + Environment.WorkingSet + "\n";

            richTextBox1.Text += "GetFolderPath System: " + Environment.GetFolderPath(Environment.SpecialFolder.System) + "\n";
            richTextBox1.Text += "[傳送到]資料夾位置 GetFolderPath SendTo: " + Environment.GetFolderPath(Environment.SpecialFolder.SendTo) + "\n";
            richTextBox1.Text += "GetFolderPath StartMenu: " + Environment.GetFolderPath(Environment.SpecialFolder.StartMenu) + "\n";
            richTextBox1.Text += "[我的文件夾]位置 GetFolderPath Personal: " + Environment.GetFolderPath(Environment.SpecialFolder.Personal) + "\n";
            richTextBox1.Text += "GetFolderPath MyMusic: " + Environment.GetFolderPath(Environment.SpecialFolder.MyMusic) + "\n";
            richTextBox1.Text += "GetFolderPath MyComputer: " + Environment.GetFolderPath(Environment.SpecialFolder.MyComputer) + "\n";

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

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "TickCount:\t" + Environment.TickCount + "\n";
            richTextBox1.Text += "Version:\t" + Environment.Version + "\n";
            richTextBox1.Text += "WorkingSet:\t" + Environment.WorkingSet + "\n";

            richTextBox1.Text += "列出所有環境變數\n";
            foreach (DictionaryEntry var in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += var.Key + "\t" + var.Value + "\n";
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "取得系統目前目錄 : " + Environment.CurrentDirectory + "\n";

            string foldername = @"D:\_git\vcs\_1.data\______test_files1";

            richTextBox1.Text += "設定新的系統目前目錄\n";
            Environment.CurrentDirectory = foldername;
            richTextBox1.Text += "取得系統目前目錄 : " + Environment.CurrentDirectory + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "# of processors (logical): " + Environment.ProcessorCount + "\n";
            //richTextBox1.Text += "# of processors (physical): " + CountPhysicalProcessors() + "\n";
            //richTextBox1.Text += "RAM installed:   bytes" + CountPhysicalMemory() + "\n";
            richTextBox1.Text += "Is OS 64-bit? " + Environment.Is64BitOperatingSystem + "\n";
            richTextBox1.Text += "Is process 64-bit? " + Environment.Is64BitProcess + "\n";
            richTextBox1.Text += "Little-endian: " + BitConverter.IsLittleEndian + "\n";

            //------------------------------------------------------------  # 60個

            string strFinal;
            string strQuery = "系統磁碟機：%SystemDrive% 與 系統根目錄：%SystemRoot%";
            strFinal = Environment.ExpandEnvironmentVariables(strQuery);
            richTextBox1.Text += strFinal + "\n";

            //------------------------------------------------------------  # 60個

            string[] arguments = Environment.GetCommandLineArgs();
            richTextBox1.Text += "取得命令列的Args: " + string.Join(", ", arguments) + "\n";

            int i = 0;
            richTextBox1.Text += "啟動程式, 參數:\n";
            foreach (string arg in Environment.GetCommandLineArgs())
            {
                richTextBox1.Text += "第 " + i.ToString() + " 項 : " + arg + "\n";
                i++;
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "系統特殊資料夾的路徑：" + Environment.GetFolderPath(Environment.SpecialFolder.System) + "\n";

            //作業系統位置
            string str = Environment.GetEnvironmentVariable("SystemRoot");
            richTextBox1.Text += "作業系統在" + str + "\n";
            string dir = str.Substring(0, 2);
            richTextBox1.Text += "作業系統在" + dir + "\n";

            //------------------------------------------------------------  # 60個

            //取得系統環境變數
            richTextBox1.Text += "環境變數" + "\t\t\t" + "變數值" + "\n";
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += DEntry.Key.ToString() + "\t" + DEntry.Value.ToString() + "\n";
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "Environment 類別使用\n";
            richTextBox1.Text += "處理序的命令列：" + Environment.CommandLine + "\n";
            richTextBox1.Text += "工作目錄的完整路徑：" + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "處理序的結束代碼：" + Environment.ExitCode + "\n";
            richTextBox1.Text += "是否正常關機：" + Environment.HasShutdownStarted + "\n";
            richTextBox1.Text += "NetBIOS名稱：" + Environment.MachineName + "\n";
            richTextBox1.Text += "環境定義的新字串：" + Environment.NewLine + "\n";
            richTextBox1.Text += "作業系統平台：" + Environment.OSVersion.Platform + "\n";
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
            /*
            string strFinal;
            string strQuery = "系統磁碟機：%SystemDrive% 與 系統根目錄：%SystemRoot%";
            strFinal = Environment.ExpandEnvironmentVariables(strQuery);
            richTextBox1.Text += strFinal + "\n";

            string[] arguments = Environment.GetCommandLineArgs();
            richTextBox1.Text += string.Format("取得命令列的Args: {0}", string.Join(", ", arguments)) + "\n";

            richTextBox1.Text += "系統特殊資料夾的路徑：" + Environment.GetFolderPath(Environment.SpecialFolder.System);
            */
            //------------------------------------------------------------  # 60個

            string osVersionString = Environment.OSVersion.ToString();
            richTextBox1.Text += "取得Windows版本 : " + osVersionString + "\n";

            //取得電腦名稱
            string ComputerName = Environment.GetEnvironmentVariable("ComputerName");
            richTextBox1.Text += "ComputerName\t" + ComputerName + "\n";


            //取得系統相關資訊

            //取得系統環境變數及對應的變數值
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += "環境變數 : " + DEntry.Key.ToString() + "\t";
                richTextBox1.Text += "變數值 : " + DEntry.Value.ToString() + "\n";
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個





        }

        // List the folder types.
        private void button8_Click(object sender, EventArgs e)
        {
            //Environment.SpecialFolder
            foreach (Environment.SpecialFolder folder_type in Enum.GetValues(typeof(Environment.SpecialFolder)))
            {
                DescribeFolder(folder_type);
            }
            richTextBox1.Select(0, 0);
        }

        // Add a folder's information to the txtFolders TextBox.
        private void DescribeFolder(Environment.SpecialFolder folder_type)
        {
            richTextBox1.AppendText(String.Format("{0,-25}", folder_type.ToString()) + Environment.GetFolderPath(folder_type) + "\r\n");
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //Application, Path, 物件
            richTextBox1.Text += "系統預設路徑\n";
            richTextBox1.Text += "StartupPath :\t" + Application.StartupPath + "\n";
            richTextBox1.Text += "Form1.cs所在位置 :\t" + Path.GetFullPath(Path.Combine(Application.StartupPath, "..\\..")) + "\n";

            //------------------------------------------------------------  # 60個

            //程式所在位置
            string appPath = Application.ExecutablePath;
            richTextBox1.Text += "程式所在位置" + appPath + "\n";

            //------------------------------------------------------------  # 60個

            //系統路徑

            richTextBox1.Text += "臨時文件目錄 : " + Path.GetTempPath() + "\n";

            //string temp_filename = Path.GetTempFileName();
            //richTextBox1.Text += temp_filename + "\n";

            richTextBox1.Text += "取得運用程序所在目錄 : " + Application.StartupPath + "\n";


            //------------------------------------------------------------  # 60個


            //------------------------------------------------------------  # 60個

        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "防止程序多次執行\n";
            richTextBox1.Text += "要修改 Program.cs\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //get os version
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

        [DllImport("kernel32.dll")]
        private static extern long GetVolumeInformation(
            string PathName,
            StringBuilder VolumeNameBuffer,
            UInt32 VolumeNameSize,
            ref UInt32 VolumeSerialNumber,
            ref UInt32 MaximumComponentLength,
            ref UInt32 FileSystemFlags,
            StringBuilder FileSystemNameBuffer,
            UInt32 FileSystemNameSize
        );

        private void button13_Click(object sender, EventArgs e)
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
            richTextBox1.Text += "C# 透過Win32取得滑鼠位置 GetCursorPos\n";
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
            richTextBox1.Text += "電腦名稱 2 : " + Dns.GetHostName() + "\n";
            richTextBox1.Text += "電腦名稱 3 : " + SystemInformation.ComputerName + "\n";
            richTextBox1.Text += "電腦名稱 4 : " + Environment.GetEnvironmentVariable("COMPUTERNAME") + "\n";


            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //主機名稱
            richTextBox1.Text += "主機名稱 : " + Dns.GetHostName() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            IPAddress addr;
            // 獲得本機局域網IP地址
            addr = new IPAddress(Dns.GetHostByName(Dns.GetHostName()).AddressList[0].Address);
            string cc = addr.ToString();

            richTextBox1.Text += "IP地址：" + cc + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        [DllImport("kernel32.dll")]
        private static extern int SetComputerName(string ipComputerName);//重寫API函數

        private void button18_Click(object sender, EventArgs e)
        {
            //取得並修改電腦名(偽執行)
            Computer computer = new Computer();//創建計算機對象
            richTextBox1.Text += "取得原計算機名 : " + computer.Name + "\n";

            richTextBox1.Text += "偽執行 計算機名稱修改, 須重啟計算機使之生效\n";
            //SetComputerName("lion-mouse");//修改計算機名稱
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫入程式預設值\n";
            SaveSettings();
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

        //設置系統日期和時間 ST
        public class SetSystemDateTime
        {
            [DllImportAttribute("Kernel32.dll")]
            public static extern void GetLocalTime(SystemTime st);
            [DllImportAttribute("Kernel32.dll")]
            public static extern void SetLocalTime(SystemTime st);
        }

        [StructLayoutAttribute(LayoutKind.Sequential)]
        public class SystemTime
        {
            public ushort vYear;
            public ushort vMonth;
            public ushort vDayOfWeek;
            public ushort vDay;
            public ushort vHour;
            public ushort vMinute;
            public ushort vSecond;
        }

        private void button22_Click(object sender, EventArgs e)
        {
            //設置系統日期和時間
            //Romeo可用 Sugar不可用
            //DateTime Year = this.dateTimePicker1.Value;
            SystemTime MySystemTime = new SystemTime();
            SetSystemDateTime.GetLocalTime(MySystemTime);
            /*
            MySystemTime.vYear = (ushort)this.dateTimePicker1.Value.Year;
            MySystemTime.vMonth = (ushort)this.dateTimePicker1.Value.Month;
            MySystemTime.vDay = (ushort)this.dateTimePicker1.Value.Day;
            MySystemTime.vHour = (ushort)this.dateTimePicker2.Value.Hour;
            MySystemTime.vMinute = (ushort)this.dateTimePicker2.Value.Minute;
            MySystemTime.vSecond = (ushort)this.dateTimePicker2.Value.Second;
            */
            MySystemTime.vYear = 2021;
            MySystemTime.vMonth = 11;
            MySystemTime.vDay = 3;
            MySystemTime.vHour = 23;
            MySystemTime.vMinute = 37;
            MySystemTime.vSecond = 00;

            SetSystemDateTime.SetLocalTime(MySystemTime);
        }
        //設置系統日期和時間 SP

        private void button23_Click(object sender, EventArgs e)
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

        [DllImport("user32.dll", EntryPoint = "ExitWindowsEx", CharSet = CharSet.Ansi)]
        private static extern int ExitWindowsEx(int uFlags, int dwReserved);

        private void button28_Click(object sender, EventArgs e)
        {
            //電腦重新啟動
            ExitWindowsEx(0, 0);//注销计算机            
        }

        private void button29_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取語系區域\n";

            string systemName = CultureInfo.CurrentCulture.Name;
            string systemName2 = CultureInfo.CurrentCulture.NativeName;
            richTextBox1.Text += "Name : " + systemName + "\n";
            richTextBox1.Text += "NativeName : " + systemName2 + "\n";
        }

        private void button30_Click(object sender, EventArgs e)
        {
            //打開控制面板中的程序_桌面設定
            System.Diagnostics.Process.Start("desk.cpl");

            //打開控制面板中的程序_滑鼠游標設定
            System.Diagnostics.Process.Start("main.cpl");

            //打開控制面板中的程序_網路連接
            System.Diagnostics.Process.Start("ncpa.cpl");

            //打開控制面板中的程序_聲音設定
            System.Diagnostics.Process.Start("mmsys.cpl");
        }

        //光碟機開關 ST
        [DllImport("winmm.dll", EntryPoint = "mciSendString")]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, System.UInt16 uReturnLength, System.IntPtr HwndCallback);
        private void button31_Click(object sender, EventArgs e)
        {
            //打開光碟機
            int result = mciSendString("Set cdaudio door open wait", "", 0, this.Handle);
            if (result == 0)
            {
                richTextBox1.Text += "光碟機打開\n";
            }
        }

        private void button32_Click(object sender, EventArgs e)
        {
            //關閉光碟機
            int result = mciSendString("Set cdaudio door Closed wait", "", 0, this.Handle);
            if (result == 0)
            {
                richTextBox1.Text += "光碟機關閉\n";
            }
        }
        //光碟機開關 SP

        /* 另外的寫法
        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnstring, int uReturnLength, int hwndCallback);

        public static void 彈出光驅()
        {
            mciSendString("set CDAudio door open", null, 127, 0);
        }

        public static void 關閉光驅()
        {
            mciSendString("set CDAudio door closed", null, 127, 0);
        }
        */

        private void button33_Click(object sender, EventArgs e)
        {
            //系統已經安裝的打印機訊息
            foreach (string mPrinterName in System.Drawing.Printing.PrinterSettings.InstalledPrinters)
            {
                richTextBox1.Text += "打印機名稱：" + mPrinterName + "\n";
                System.Drawing.Printing.PrinterSettings mprinter = new System.Drawing.Printing.PrinterSettings();
                mprinter.PrinterName = mPrinterName;
                if (mprinter.IsValid)
                {
                    foreach (System.Drawing.Printing.PrinterResolution resolution in mprinter.PrinterResolutions)
                    {
                        richTextBox1.Text += "分  辨  率：" + resolution.ToString() + "\n";
                    }
                    string prinsize = "";
                    foreach (System.Drawing.Printing.PaperSize size in mprinter.PaperSizes)
                    {
                        if (Enum.IsDefined(size.Kind.GetType(), size.Kind))
                        {
                            prinsize += size.ToString() + "\n";
                        }
                    }
                    richTextBox1.AppendText("打 印 尺寸：\n" + prinsize + "\n");
                }
                else
                {
                    richTextBox1.Text += "XXXXXXXX\n";
                }
            }
        }

        [DllImport("kernel32.dll", EntryPoint = "GetDiskFreeSpaceEx")]
        public static extern int GetDiskFreeSpaceEx(string lpDirectoryName, out long lpFreeBytesAvailable, out long lpTotalNumberOfBytes, out long lpTotalNumberOfFreeBytes);
        private void button34_Click(object sender, EventArgs e)
        {
            //取得本機或網路磁碟機的磁碟訊息
            //取得本機或網路磁碟機的磁碟訊息, 選擇磁碟或目錄
            FolderBrowserDialog fbd = new FolderBrowserDialog();
            if (fbd.ShowDialog() == DialogResult.OK)
            {
                long fb, ftb, tfb;
                string str = fbd.SelectedPath;
                richTextBox1.Text += "path : " + str + "\n";
                if (GetDiskFreeSpaceEx(str, out fb, out ftb, out tfb) != 0)
                {
                    string strfb = Convert.ToString(fb / 1024 / 1024 / 1024) + " G";
                    string strftb = Convert.ToString(ftb / 1024 / 1024 / 1024) + " G";
                    string strtfb = Convert.ToString(tfb / 1024 / 1024 / 1024) + " G";
                    richTextBox1.Text += "總空間" + strfb + "\n";
                    richTextBox1.Text += "可用空間" + strftb + "\n";
                    richTextBox1.Text += "總剩餘空間" + strtfb + "\n";
                }
                else
                {
                    MessageBox.Show("NO");
                }
            }
        }

        private void button35_Click(object sender, EventArgs e)
        {
            //(偽)將計算機設定為休眠狀態

            if (MessageBox.Show("確定要休眠計算機嗎？") == DialogResult.OK)
            {
                //偽執行
                //Application.SetSuspendState(PowerState.Hibernate, true, true);
            }
        }

        private void button36_Click(object sender, EventArgs e)
        {

        }

        private void button37_Click(object sender, EventArgs e)
        {

        }

        private void button38_Click(object sender, EventArgs e)
        {

        }

        private void button39_Click(object sender, EventArgs e)
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

        private void myUser()
        {
            Memory();
        }

        private void Memory()
        {
            Microsoft.VisualBasic.Devices.Computer myInfo = new Microsoft.VisualBasic.Devices.Computer();
            //获取物理内存总量
            pbMemorySum.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemorySum.Value = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            lblSum.Text = (myInfo.Info.TotalPhysicalMemory / 1024).ToString();
            //获取可用物理内存总量
            pbMemoryUse.Maximum = Convert.ToInt32(myInfo.Info.TotalPhysicalMemory / 1024 / 1024);
            pbMemoryUse.Value = Convert.ToInt32(myInfo.Info.AvailablePhysicalMemory / 1024 / 1024);
            lblMuse.Text = (myInfo.Info.AvailablePhysicalMemory / 1024).ToString();
            //获取虚拟内存总量
            pbVmemorysum.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemorysum.Value = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            lblVinfo.Text = (myInfo.Info.TotalVirtualMemory / 1024).ToString();
            //获取可用虚拟内存总量
            pbVmemoryuse.Maximum = Convert.ToInt32(myInfo.Info.TotalVirtualMemory / 1024 / 1024);
            pbVmemoryuse.Value = Convert.ToInt32(myInfo.Info.AvailableVirtualMemory / 1024 / 1024);
            lblVuse.Text = (myInfo.Info.AvailableVirtualMemory / 1024).ToString();
        }

        private void timer_memory_Tick(object sender, EventArgs e)
        {
            //使用Computer()讀得記憶體狀態

            //1. 參考 -> 加入參考 -> .NET/Microsoft.VisualBasic
            //2. using Microsoft.VisualBasic.Devices;

            Computer myComputer = new Computer();

            //Bytes
            label1.Text = "物理內存總量(B)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory);
            label2.Text = "可用物理內存(B)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory);
            label3.Text = "虛擬內存總量(B)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory);
            label4.Text = "可用虛擬內存(B)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory);

            //MB
            label1.Text = "物理內存總量(MB)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024) + " MB";
            label2.Text = "可用物理內存(MB)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024) + " MB";
            label3.Text = "虛擬內存總量(MB)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024) + " MB";
            label4.Text = "可用虛擬內存(MB)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024) + " MB";

            //------------------------------------------------------------  # 60個

            MyProcesses = Process.GetProcesses();
            lb_processes.Text = "進程數 : " + MyProcesses.Length.ToString();
            td = new Thread(new ThreadStart(myUser));
            td.Start();
        }

        private void Form1_FormClosed(object sender, FormClosedEventArgs e)
        {
            if (td != null)
            {
                td.Abort();
            }
        }
    }

    /*
    * LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
    * 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
    * LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
    * LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
    */

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

    /*
    * LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
    * 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
    * LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
    * LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
    */
    /// <summary>
    /// 定義內存的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct MemoryInfo
    {
        /// <summary>
        ///
        /// </summary>
        public uint dwLength;
        /// <summary>
        /// 已經使用的內存
        /// </summary>
        public uint dwMemoryLoad;
        /// <summary>
        /// 總物理內存大小
        /// </summary>
        public uint dwTotalPhys;
        /// <summary>
        /// 可用物理內存大小
        /// </summary>
        public uint dwAvailPhys;
        /// <summary>
        /// 交換文件總大小
        /// </summary>
        public uint dwTotalPageFile;
        /// <summary>
        /// 可用交換文件大小
        /// </summary>
        public uint dwAvailPageFile;
        /// <summary>
        /// 總虛擬內存大小
        /// </summary>
        public uint dwTotalVirtual;
        /// <summary>
        /// 可用虛擬內存大小
        /// </summary>
        public uint dwAvailVirtual;
    }

    /*
    * LayoutKind.Automatic：為了提高效率允許運行態對類型成員重新排序
    * 注意：永遠不要使用這個選項來調用不受管轄的動態鏈接庫函數。
    * LayoutKind.Explicit：對每個域按照FIEldOffset屬性對類型成員排序
    * LayoutKind.Sequential：對出現在受管轄類型定義地方的不受管轄內存中的類型成員進行排序。
    */
    /// <summary>
    /// 定義系統時間的信息結構
    /// </summary>
    [StructLayout(LayoutKind.Sequential)]
    public struct SystemTimeInfo
    {
        /// <summary>
        /// 年
        /// </summary>
        public ushort wYear;
        /// <summary>
        /// 月
        /// </summary>
        public ushort wMonth;
        /// <summary>
        /// 星期
        /// </summary>
        public ushort wDayOfWeek;
        /// <summary>
        /// 天
        /// </summary>
        public ushort wDay;
        /// <summary>
        /// 小時
        /// </summary>
        public ushort wHour;
        /// <summary>
        /// 分鐘
        /// </summary>
        public ushort wMinute;
        /// <summary>
        /// 秒
        /// </summary>
        public ushort wSecond;
        /// <summary>
        /// 毫秒
        /// </summary>
        public ushort wMilliseconds;
    }

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


//6060
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//------------------------------  # 30個

//1515
//---------------  # 15個

//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//richTextBox1.Text += "------------------------------\n";  // 30個
//richTextBox1.Text += "---------------\n";  // 15個


/*  可搬出

*/



