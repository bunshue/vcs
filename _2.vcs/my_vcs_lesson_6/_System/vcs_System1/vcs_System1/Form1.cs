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
using System.ServiceProcess;    //for ServiceController     參考/加入參考/.NET/System.ServiceProcess

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

        Thread td;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            CheckForIllegalCrossThreadCalls = false;

            GetMemoryInfo();
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

            button40.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 4, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 4, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 4, y_st + dy * 4);
            button45.Location = new Point(x_st + dx * 4, y_st + dy * 5);
            button46.Location = new Point(x_st + dx * 4, y_st + dy * 6);
            button47.Location = new Point(x_st + dx * 4, y_st + dy * 7);
            button48.Location = new Point(x_st + dx * 4, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 4, y_st + dy * 9);

            groupBox1.Size = new Size(200, 150);//Windows 開關機(偽執行)
            groupBox2.Size = new Size(320, 150);
            groupBox3.Size = new Size(320, 100);
            groupBox4.Size = new Size(320, 100);

            groupBox2.Location = new Point(x_st + dx * 5, y_st + dy * 0);//記憶體狀態
            groupBox3.Location = new Point(x_st + dx * 5, y_st + dy * 2 + 20);//物理內存
            groupBox4.Location = new Point(x_st + dx * 5, y_st + dy * 4);//虛擬內存
            groupBox1.Location = new Point(x_st + dx * 5, y_st + dy * 6);

            richTextBox1.Size = new Size(300, 640);
            richTextBox1.Location = new Point(x_st + dx * 6 + 130, y_st + dy * 0);
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

            this.Size = new Size(1710, 700);
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
            //Environment 屬性

            richTextBox1.Text += "電腦名稱 : " + Environment.MachineName + "\n";
            richTextBox1.Text += "電腦名稱 : " + Environment.GetEnvironmentVariable("COMPUTERNAME") + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "處理序的命令列：" + Environment.CommandLine + "\n";
            richTextBox1.Text += "工作目錄的完整路徑：" + Environment.CurrentDirectory + "\n";
            richTextBox1.Text += "目前程式執行目錄：" + Environment.CurrentDirectory + "\n";//取得目前程式執行目錄
            richTextBox1.Text += "處理序的結束代碼：" + Environment.ExitCode + "\n";
            richTextBox1.Text += "是否正常關機：" + Environment.HasShutdownStarted + "\n";
            richTextBox1.Text += "環境定義的新字串：" + Environment.NewLine + "\n";
            richTextBox1.Text += "作業系統平台：" + Environment.OSVersion.Platform + "\n";

            richTextBox1.Text += "Service Pack版本：" + Environment.OSVersion.ServicePack + "\n";
            richTextBox1.Text += "作業系統版本：" + Environment.OSVersion.Version + "\n";
            richTextBox1.Text += "串連字串表示：" + Environment.OSVersion.VersionString + "\n";
            richTextBox1.Text += "系統版本號：" + Environment.OSVersion.VersionString + "\n";//顯示系統版本號
            richTextBox1.Text += "OSVersion： " + Environment.OSVersion + "\n";
            richTextBox1.Text += "OSVersion: " + Environment.OSVersion.ToString() + "\n";

            string osVersionString = Environment.OSVersion.ToString();
            richTextBox1.Text += "取得Windows版本 : " + osVersionString + "\n";

            richTextBox1.Text += "處理器數目(邏輯處理器)：" + Environment.ProcessorCount + "\n";

            richTextBox1.Text += "堆疊追蹤資訊：" + Environment.StackTrace + "\n";
            richTextBox1.Text += "系統目錄完整路徑：" + Environment.SystemDirectory + "\n";

            richTextBox1.Text += "使用者網域名稱：" + Environment.UserDomainName + "\n";
            richTextBox1.Text += "處理序是否與使用者互動：" + Environment.UserInteractive + "\n";
            richTextBox1.Text += "使用者名稱：" + Environment.UserName + "\n";//操作系統的登錄用戶名

            richTextBox1.Text += "組件元件值：" + Environment.Version.Build + "\n";
            richTextBox1.Text += "主要元件值：" + Environment.Version.Major + "\n";
            richTextBox1.Text += "修訂編號的高 16 位元：" + Environment.Version.MajorRevision + "\n";
            richTextBox1.Text += "次要元件值：" + Environment.Version.Minor + "\n";
            richTextBox1.Text += "修訂編號的低 16 位元：" + Environment.Version.MinorRevision + "\n";
            richTextBox1.Text += "修訂元件值：" + Environment.Version.Revision + "\n";
            richTextBox1.Text += "實際記憶體數量：" + Environment.WorkingSet + "\n";

            richTextBox1.Text += "系統啟動後的毫秒數：" + Environment.TickCount + "\t系統啟動後經過的Tick數, 1個tick為1msec\n";
            richTextBox1.Text += "系統啟動後經過的時間(電腦開機時間)： " + (Environment.TickCount / 1000).ToString() + " 秒\n";

            richTextBox1.Text += "SystemPageSize： " + Environment.SystemPageSize + "\n";

            richTextBox1.Text += "Is64BitOperatingSystem： " + Environment.Is64BitOperatingSystem + "\n";
            if (Environment.Is64BitOperatingSystem == true)
            {
                richTextBox1.Text += "64位元作業系統\n";
            }
            else
            {
                richTextBox1.Text += "32位元作業系統\n";
            }

            richTextBox1.Text += "Is64BitProcess： " + Environment.Is64BitProcess + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "系統特殊資料夾的路徑：" + Environment.GetFolderPath(Environment.SpecialFolder.System) + "\n";
            richTextBox1.Text += "[傳送到]資料夾位置 GetFolderPath SendTo: " + Environment.GetFolderPath(Environment.SpecialFolder.SendTo) + "\n";
            richTextBox1.Text += "GetFolderPath StartMenu: " + Environment.GetFolderPath(Environment.SpecialFolder.StartMenu) + "\n";
            richTextBox1.Text += "[我的文件夾]位置 GetFolderPath Personal: " + Environment.GetFolderPath(Environment.SpecialFolder.Personal) + "\n";
            richTextBox1.Text += "GetFolderPath MyMusic: " + Environment.GetFolderPath(Environment.SpecialFolder.MyMusic) + "\n";
            richTextBox1.Text += "GetFolderPath MyComputer: " + Environment.GetFolderPath(Environment.SpecialFolder.MyComputer) + "\n";

            //Environment.SpecialFolder
            foreach (Environment.SpecialFolder folder_type in Enum.GetValues(typeof(Environment.SpecialFolder)))
            {
                //many
                //richTextBox1.AppendText(String.Format("{0,-25}", folder_type.ToString()) + Environment.GetFolderPath(folder_type) + "\r\n");
            }

            //------------------------------------------------------------  # 60個

            //環境參數
            string RootPath = Environment.GetEnvironmentVariable("HOMEDRIVE") + Environment.GetEnvironmentVariable("HOMEPATH") + @"\ScreenCapture";

            richTextBox1.Text += "HOMEDRIVE :\t" + Environment.GetEnvironmentVariable("HOMEDRIVE") + "\n";
            richTextBox1.Text += "HOMEPATH :\t" + Environment.GetEnvironmentVariable("HOMEPATH") + "\n";
            richTextBox1.Text += "my path :\t" + RootPath + "\n";

            //------------------------------------------------------------  # 60個

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

            /*
            string strFinal;
            string strQuery = "系統磁碟機：%SystemDrive% 與 系統根目錄：%SystemRoot%";
            strFinal = Environment.ExpandEnvironmentVariables(strQuery);
            richTextBox1.Text += strFinal + "\n";

            string[] arguments = Environment.GetCommandLineArgs();
            richTextBox1.Text += string.Format("取得命令列的Args: {0}", string.Join(", ", arguments)) + "\n";
            */

            //------------------------------------------------------------  # 60個

            //取得系統相關資訊

            //取得系統環境變數及對應的變數值
            foreach (DictionaryEntry DEntry in Environment.GetEnvironmentVariables())
            {
                richTextBox1.Text += "環境變數 : " + DEntry.Key.ToString() + "\t";
                richTextBox1.Text += "變數值 : " + DEntry.Value.ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //取得目前Windows版本

            OperatingSystem myOS = Environment.OSVersion;

            if (myOS.Version.Major == 5)
            {
                switch (myOS.Version.Minor)
                {
                    case 0:
                        richTextBox1.Text += "系統版本：" + "Windows 2000 " + myOS.ServicePack + "\n";
                        break;
                    case 1:
                        richTextBox1.Text += "系統版本：" + "Windows XP " + myOS.ServicePack + "\n";
                        break;
                    case 2:
                        richTextBox1.Text += "系統版本：" + "Windows Server 2003 " + " " + myOS.ServicePack + "\n";
                        break;
                    default:
                        richTextBox1.Text += "系統版本：" + myOS.ToString() + " " + myOS.ServicePack + "\n";
                        break;
                }
            }
            else
            {
                richTextBox1.Text += "系統版本：" + myOS.VersionString + " " + myOS.ServicePack + "\n";
            }

            //檢視目前系統版本

            //讀取操作系統和CLR的版本
            OperatingSystem os = Environment.OSVersion;
            richTextBox1.Text += "Platform: " + os.Platform + "\n";
            richTextBox1.Text += "Service Pack:" + os.ServicePack + "\n";
            richTextBox1.Text += "Version: " + os.Version + "\n";
            richTextBox1.Text += "VersionString: " + os.VersionString + "\n";
            richTextBox1.Text += "CLR Version: " + System.Environment.Version + "\n";
            richTextBox1.Text += "Version：" + Environment.Version + "\n";
            richTextBox1.Text += "Version： " + Environment.Version + "\n";
            richTextBox1.Text += "Version:\t" + Environment.Version + "\n";

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
            richTextBox1.Text += "Windows 作業系統 : \n";

            //定義系統版本
            Version ver = Environment.OSVersion.Version;
            //Major主版本號,Minor副版本號
            string version_name = string.Empty;
            if (ver.Major == 5 && ver.Minor == 0)
            {
                version_name = "Windows 2000";
            }
            else if (ver.Major == 5 && ver.Minor == 1)
            {
                version_name = "Windows XP";
            }
            else if (ver.Major == 5 && ver.Minor == 2)
            {
                version_name = "Windows 2003";
            }
            else if (ver.Major == 6 && ver.Minor == 0)
            {
                version_name = "Windows Vista";
            }
            else if (ver.Major == 6 && ver.Minor == 1)
            {
                version_name = "Windows7";
            }
            else if (ver.Major == 6 && ver.Minor == 2)
            {
                version_name = "Windows10";
            }
            else
            {
                version_name = "未知";
            }

            richTextBox1.Text += "Windows 作業系統 : " + version_name + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // 獲取系統名稱, ex : 操作系統：Longhorn,6.2.9200.0
            os = Environment.OSVersion;
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
            string result = String.Format("{0},{1}", osName, os.Version.ToString());

            richTextBox1.Text += "操作系統：" + result + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            OperatingSystem os_info = Environment.OSVersion;
            richTextBox1.Text += "os_info : " + os_info + "\n";
            richTextBox1.Text += os_info.VersionString + "\n";

            //取得作業系統名稱
            richTextBox1.Text += "os_info : " + os_info + "\n";

            string version = os_info.Version.Major.ToString() + "." + os_info.Version.Minor.ToString();

            version_name = string.Empty;
            switch (version)
            {
                case "10.0":
                    version_name = "10/Server 2016";
                    break;
                case "6.3":
                    version_name = "8.1/Server 2012 R2";
                    break;
                case "6.2":
                    version_name = "8/Server 2012";
                    break;
                case "6.1":
                    version_name = "7/Server 2008 R2";
                    break;
                case "6.0":
                    version_name = "Server 2008/Vista";
                    break;
                case "5.2":
                    version_name = "Server 2003 R2/Server 2003/XP 64-Bit Edition";
                    break;
                case "5.1":
                    version_name = "XP";
                    break;
                case "5.0":
                    version_name = "2000";
                    break;
                default:
                    version_name = "Unknown";
                    break;
            }
            richTextBox1.Text += "Windows名稱 : " + version_name + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個



            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

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
            //取得目前的Process
            using (Process curProcess = Process.GetCurrentProcess())
            {
                richTextBox1.Text += "aaaa = " + curProcess.ProcessName + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.MainModule + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.MainWindowTitle + "\n";
                richTextBox1.Text += "aaaa = " + curProcess.ProcessorAffinity + "\n";
                richTextBox1.Text += "處理序的名稱 :\t" + curProcess.ProcessName.ToString().Trim() + "\n";//取得處理序的名稱
                richTextBox1.Text += "主視窗標題 :\t" + curProcess.MainWindowTitle + "\n";   //取得處理序的主視窗標題
                richTextBox1.Text += "處理序啟動的時間 :\t" + curProcess.StartTime.ToString() + "\n";   //取得處理序的主視窗標題
                richTextBox1.Text += "這個處理序的總處理器時間 :\t" + curProcess.TotalProcessorTime.ToString() + "\n";   //取得處理序的主視窗標題

                //程序的退出
                //Process.GetCurrentProcess().Kill();
            }

            Process proc = Process.GetCurrentProcess();

            richTextBox1.Text += "aaa : " + proc.MinWorkingSet + " 拜\n";
            richTextBox1.Text += "bbb : " + proc.MaxWorkingSet + " 拜\n";
            richTextBox1.Text += "ccc : " + proc.NonpagedSystemMemorySize64 + " 拜\n";
            richTextBox1.Text += "ddd : " + proc.PagedMemorySize64 + " 拜\n";
            richTextBox1.Text += "eee : " + proc.PagedSystemMemorySize64 + " 拜\n";

            richTextBox1.Text += "aaa : " + proc.PeakPagedMemorySize64 + " 拜\n";
            richTextBox1.Text += "bbb : " + proc.PeakVirtualMemorySize64 + " 拜\n";
            richTextBox1.Text += "ccc : " + proc.PeakWorkingSet64 + " 拜\n";
            richTextBox1.Text += "ddd : " + proc.VirtualMemorySize64 + " 拜\n";
            richTextBox1.Text += "eee : " + proc.WorkingSet64 + " 拜\n";

            //取得記憶體使用狀態

            richTextBox1.Text += "Property\t\t\tValue\n";
            richTextBox1.Text += "Min Working Set" + "\t" + ((double)proc.MinWorkingSet).ToFileSize() + "\n";
            richTextBox1.Text += "Max Working Set" + "\t" + ((double)proc.MaxWorkingSet).ToFileSize() + "\n";
            richTextBox1.Text += "Non-paged Memory Size" + "\t" + ((double)proc.NonpagedSystemMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Paged Memory Size" + "\t" + ((double)proc.PagedMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Paged System Memory Size" + "\t" + ((double)proc.PagedSystemMemorySize64).ToFileSize() + "\n";

            richTextBox1.Text += "Peak Paged Memory Size" + "\t" + ((double)proc.PeakPagedMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Peak Virtual Memory Size" + "\t" + ((double)proc.PeakVirtualMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Peak Working Set" + "\t" + ((double)proc.PeakWorkingSet64).ToFileSize() + "\n";
            richTextBox1.Text += "Virtual Memory Size" + "\t" + ((double)proc.VirtualMemorySize64).ToFileSize() + "\n";
            richTextBox1.Text += "Working Set" + "\t" + ((double)proc.WorkingSet64).ToFileSize() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //自建類別 SystemInfo
            //取得系統有關環境、屬性

            SystemInfo systemInfo = new SystemInfo();

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


            return;

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
            //取得程式編譯時間
            richTextBox1.Text += "編譯時間 : " + GetLinkerTime() + "\n";

            //取得程式啟動時間
            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + " 秒\n";
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

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "詢問確定關閉表單\n";
            richTextBox1.Text += "找個地方加入WndProc()即可\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //Application, Path, 物件

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "目前應用程式路徑: \t" + Path.GetDirectoryName(System.Reflection.Assembly.GetExecutingAssembly().Location) + "\n";

            //------------------------------------------------------------  # 60個

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
            //測試防火牆
            // Create the firewall type.
            Type FWManagerType = Type.GetTypeFromProgID("HNetCfg.FwMgr");

            // Use the firewall type to create a firewall manager object.
            dynamic FWManager = Activator.CreateInstance(FWManagerType);

            // Check the status of the firewall.

            if (FWManager.LocalPolicy.CurrentProfile.FirewallEnabled == true)
                richTextBox1.Text += "防火牆已開啟\n";
            else
                richTextBox1.Text += "防火牆未開啟\n";
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

        [DllImport("user32.dll", EntryPoint = "GetSystemMetrics")]
        private static extern int GetSystemMetrics(int mVal);

        private void button13_Click(object sender, EventArgs e)
        {
            //取得螢幕大小

            richTextBox1.Text += "使用 Screen.PrimaryScreen.Bounds\n";
            int W = Screen.PrimaryScreen.Bounds.Width;
            int H = Screen.PrimaryScreen.Bounds.Height;

            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "使用 GetSystemMetrics\n";
            W = GetSystemMetrics(0);
            H = GetSystemMetrics(1);
            richTextBox1.Text += "W = " + W.ToString() + ", H = " + H.ToString() + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
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
        }

        private void button20_Click(object sender, EventArgs e)
        {
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

            //Kilo / Romeo可用, Sugar不可用

            SystemTime MySystemTime = new SystemTime();

            richTextBox1.Text += "取得本機電腦時間 :\n";
            SetSystemDateTime.GetLocalTime(MySystemTime);
            richTextBox1.Text += "年 : " + MySystemTime.vYear + "\n";
            richTextBox1.Text += "月 : " + MySystemTime.vMonth + "\n";
            richTextBox1.Text += "日 : " + MySystemTime.vDay + "\n";
            richTextBox1.Text += "星 : " + MySystemTime.vDayOfWeek + "\n";
            richTextBox1.Text += "時 : " + MySystemTime.vHour + "\n";
            richTextBox1.Text += "分 : " + MySystemTime.vMinute + "\n";
            richTextBox1.Text += "秒 : " + MySystemTime.vSecond + "\n";

            richTextBox1.Text += "要設定的本機電腦時間 :\n";
            MySystemTime.vYear = 2025;
            MySystemTime.vMonth = 11;
            MySystemTime.vDay = 22;
            MySystemTime.vHour = 12;
            MySystemTime.vMinute = 34;
            MySystemTime.vSecond = 56;

            richTextBox1.Text += "年 : " + MySystemTime.vYear + "\n";
            richTextBox1.Text += "月 : " + MySystemTime.vMonth + "\n";
            richTextBox1.Text += "日 : " + MySystemTime.vDay + "\n";
            //richTextBox1.Text += "星 : " + MySystemTime.vDayOfWeek + "\n";
            richTextBox1.Text += "時 : " + MySystemTime.vHour + "\n";
            richTextBox1.Text += "分 : " + MySystemTime.vMinute + "\n";
            richTextBox1.Text += "秒 : " + MySystemTime.vSecond + "\n";

            richTextBox1.Text += "設定本機電腦時間(偽執行)\n";
            //SetSystemDateTime.SetLocalTime(MySystemTime);
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
            Graphics graphics = this.CreateGraphics();
            float dpiX = graphics.DpiX;
            float dpiY = graphics.DpiY;
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

            string systemName1 = CultureInfo.CurrentCulture.Name;
            string systemName2 = CultureInfo.CurrentCulture.NativeName;
            richTextBox1.Text += "Name : " + systemName1 + "\n";
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
            foreach (string mPrinterName in PrinterSettings.InstalledPrinters)
            {
                richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
                richTextBox1.Text += "打印機名稱：" + mPrinterName + "\n";
                PrinterSettings mprinter = new PrinterSettings();
                mprinter.PrinterName = mPrinterName;
                if (mprinter.IsValid)
                {
                    foreach (PrinterResolution resolution in mprinter.PrinterResolutions)
                    {
                        richTextBox1.Text += "分  辨  率：" + resolution.ToString() + "\n";
                    }
                    string prinsize = "";
                    foreach (PaperSize size in mprinter.PaperSizes)
                    {
                        if (Enum.IsDefined(size.Kind.GetType(), size.Kind))
                        {
                            prinsize += size.ToString() + "\n";
                        }
                    }
                    //many
                    //richTextBox1.AppendText("打 印 尺寸：\n" + prinsize + "\n");
                }
                else
                {
                    richTextBox1.Text += "XXXXXXXX\n";
                }
            }
            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button34_Click(object sender, EventArgs e)
        {
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

        //取得任務欄尺寸大小 ST

        [DllImport("user32.dll")]
        public static extern int FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll")]
        public static extern int GetWindowRect(int hwnd, ref Rectangle lpRect);

        Rectangle myrect;

        private void button37_Click(object sender, EventArgs e)
        {
            //取得任務欄尺寸大小
            if (GetWindowRect(FindWindow("Shell_TrayWnd", null), ref myrect) == 0)
            {
                return;
            }
            else
            {
                richTextBox1.Text += "取得任務欄尺寸大小\n";
                richTextBox1.Text += "上 : \t" + Convert.ToString(myrect.Top) + "\n";
                richTextBox1.Text += "下 : \t" + Convert.ToString(myrect.Bottom) + "\n";
                richTextBox1.Text += "左 : \t" + Convert.ToString(myrect.Left) + "\n";
                richTextBox1.Text += "右 : \t" + Convert.ToString(myrect.Right) + "\n";
            }
        }
        //取得任務欄尺寸大小 SP

        //隱藏任務欄, 顯示任務欄 ST
        private const int SW_HIDE = 0;
        private const int SW_RESTORE = 9;

        /*
        [DllImport("user32.dll")]
        public static extern int FindWindow(string lpClassName, string lpWindowName);
        */

        [DllImport("user32.dll")]
        public static extern int ShowWindow(int hwnd, int nCmdShow);

        private void button38_Click(object sender, EventArgs e)
        {
            //隱藏任務欄
            ShowWindow(FindWindow("Shell_TrayWnd", null), SW_HIDE);
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //顯示任務欄
            ShowWindow(FindWindow("Shell_TrayWnd", null), SW_RESTORE);
        }
        //隱藏任務欄, 顯示任務欄 SP

        private void button40_Click(object sender, EventArgs e)
        {
            //使用 SystemInformation

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "電腦名稱 3 : " + SystemInformation.ComputerName + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
            richTextBox1.Text += "檢測系統啟動模式\n";

            string mode = SystemInformation.BootMode.ToString();
            richTextBox1.Text += "目前系統的啟動模式是：";
            switch (mode)
            {
                case "FailSafe":
                    richTextBox1.Text += "不具有網絡支援的安全模式\n";
                    break;
                case "FailSafeWithNetwork":
                    richTextBox1.Text += "具有網絡支援的安全模式\n";
                    break;
                case "Normal":
                    richTextBox1.Text += "標準模式\n";
                    break;
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
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

            richTextBox1.Text += "------------------------------\n";  // 30個

            status = SystemInformation.PowerStatus;

            int percents = (int)(status.BatteryLifePercent * 100);
            richTextBox1.Text += "充電百分比 : " + percents.ToString() + "%" + "\n";

            richTextBox1.Text += "充電百分比:\t\t" + status.BatteryLifePercent.ToString("P0") + "\n";
            richTextBox1.Text += "BatteryLifePercent : " + status.BatteryLifePercent.ToString() + "\n";

            richTextBox1.Text += "電源線狀態 : " + status.PowerLineStatus.ToString() + "\n";
            richTextBox1.Text += "電池充電狀態 : " + status.BatteryChargeStatus.ToString() + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "BatteryFullLifetime : " + status.BatteryFullLifetime.ToString() + "\n";
            if (status.BatteryFullLifetime == -1)
            {
                richTextBox1.Text += "Full Lifetime:\t" + "Unknown" + "\n";
            }
            else
            {
                richTextBox1.Text += "Full Lifetime (sec):\t" + status.BatteryFullLifetime.ToString() + "\n";
            }

            richTextBox1.Text += "BatteryLifeRemaining : " + status.BatteryLifeRemaining.ToString() + "\n";
            if (status.BatteryLifeRemaining == -1)
            {
                richTextBox1.Text += "Life Remaining:\t" + "Unknown" + "\n";
            }
            else
            {
                richTextBox1.Text += "Life Remaining (sec):\t" + status.BatteryLifeRemaining.ToString() + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button41_Click(object sender, EventArgs e)
        {
            //判斷電腦中是否安裝了SQL軟體
            if (ExitSQL())
            {
                richTextBox1.Text += "本機電腦中已經安裝SQL軟體\n";
            }
            else
            {
                richTextBox1.Text += "本機電腦中沒有安裝SQL軟體\n";
            }
        }

        public bool ExitSQL()
        {
            bool sqlFlag = false;
            ServiceController[] services = ServiceController.GetServices();
            for (int i = 0; i < services.Length; i++)
            {
                if (services[i].DisplayName.ToString() == "MSSQLSERVER")
                    sqlFlag = true;
            }
            return sqlFlag;
        }


        private void button42_Click(object sender, EventArgs e)
        {
            //獲取本機所有SQLServer引擎

            //获得主机名称
            string HostName = Dns.GetHostName();
            ServiceController[] services = ServiceController.GetServices();

            //从机器服务列表中找到本机的SqlServer引擎

            richTextBox1.Text += "services len = " + services.Length.ToString() + "\n";

            foreach (ServiceController s in services)
            {
                richTextBox1.Text += "s = " + s.ServiceName + "\n";
                if (s.ServiceName.ToLower().IndexOf("mssql$") != -1)
                {
                    //ddlServerName.Items.Add(HostName + "\\" + s.ServiceName.Substring(s.ServiceName.IndexOf("$") + 1));     
                    richTextBox1.Text += HostName + "\\" + s.ServiceName.Substring(s.ServiceName.IndexOf("$") + 1) + "\n";
                }
                else if (s.ServiceName.ToLower() == "mssqlserver")
                {
                    //ddlServerName.Items.Add(HostName);
                    richTextBox1.Text += "bbbb " + HostName + "\n";
                }
            }
        }

        private void button43_Click(object sender, EventArgs e)
        {
            //使用 Application.DoEvents
            int i;
            for (i = 0; i <= 7777; i++)
            {
                //do something lb_DoEvents.Text = i.ToString();
                Application.DoEvents();//實時響應文本框中的值
                //Application.DoEvents()的作用：处理当前在消息队列中的所有 Windows 消息。
                //加Application.DoEvents可以防止界面停止响应
            }

        }

        private void button44_Click(object sender, EventArgs e)
        {
            //不使用 Application.DoEvents
            int i;
            for (i = 0; i <= 7777; i++)
            {
                //do something lb_DoEvents.Text = i.ToString();
                //Application.DoEvents();//實時響應文本框中的值
            }
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

        private void button48_Click(object sender, EventArgs e)
        {

        }

        private void button49_Click(object sender, EventArgs e)
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

        private void GetMemoryInfo()
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

            td = new Thread(new ThreadStart(GetMemoryInfo));
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
        /// <summary>
        /// OEM ID
        /// </summary>
        public uint dwOemId;
        /// <summary>
        /// 頁面大小
        /// </summary>
        public uint dwPageSize;
        public uint lpMinimumApplicationAddress;
        public uint lpMaximumApplicationAddress;
        public uint dwActiveProcessorMask;
        /// <summary>
        /// CPU個數
        /// </summary>
        public uint dwNumberOfProcessors;
        /// <summary>
        /// CPU類型
        /// </summary>
        public uint dwProcessorType;
        public uint dwAllocationGranularity;
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
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個
//------------------------------------------------------------

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

//1515
//---------------  # 15個


/*  可搬出

*/

