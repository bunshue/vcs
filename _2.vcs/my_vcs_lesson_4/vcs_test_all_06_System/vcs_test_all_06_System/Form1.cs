using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;   //for DllImport
using System.Diagnostics;
using Microsoft.VisualBasic.Devices;    //for Computer
using System.Reflection;        //for Assembly
using System.Management;
using System.IO;            //for DriveInfo
using System.Net;   //for DNS
using System.IO.Ports;          //for serial ports
using System.Collections;   //for DictionaryEntry
using System.Drawing.Imaging;   //for ImageFormat
using System.Drawing.Printing;  //for PrinterSettings

using Microsoft.Win32;      //for Registry
using System.Globalization;

/*
讀取/寫入程式預設值
到
方案總管/Properties/Settings.settings裏, 加入變數
*/

namespace vcs_test_all_06_System
{
    public partial class Form1 : Form
    {
        DateTime start_time = DateTime.Now;
        static PerformanceCounter pc = new PerformanceCounter("Processor", "% Processor Time", "_Total");

        public Form1()
        {
            InitializeComponent();
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
            dx = 210;
            dy = 42;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button2.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button3.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            button4.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button5.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button6.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button7.Location = new Point(x_st + dx * 3, y_st + dy * 1);

            button8.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button10.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 3, y_st + dy * 2);

            button12.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button14.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button15.Location = new Point(x_st + dx * 3, y_st + dy * 3);

            button16.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button19.Location = new Point(x_st + dx * 3, y_st + dy * 4);

            button20.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button23.Location = new Point(x_st + dx * 3, y_st + dy * 5);

            button24.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button26.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 3, y_st + dy * 6);

            button28.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button29.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button30.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button31.Location = new Point(x_st + dx * 3, y_st + dy * 7);

            button32.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button33.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button35.Location = new Point(x_st + dx * 3, y_st + dy * 8);

            button36.Location = new Point(x_st + dx * 0, y_st + dy * 9);
            button37.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button38.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button39.Location = new Point(x_st + dx * 3, y_st + dy * 9);

            button40.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button41.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button42.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button43.Location = new Point(x_st + dx * 3, y_st + dy * 10);

            button44.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button45.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button46.Location = new Point(x_st + dx * 2, y_st + dy * 11);

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

            bt_memory.Location = new Point(x_st + dx * 1 + 70, y_st + dy * 13);
            bt_exit.Location = new Point(x_st + dx * 3, y_st + dy * 13);
            groupBox1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button0_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得軟體版本\t";
            richTextBox1.Text += "" + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開機時間 : " + (Environment.TickCount / 1000).ToString() + " 秒" + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //方案總管/專案屬性/應用程式/組件資訊 內 修改組件資訊

            //方案總管/加入/現有項目/選取AssemblyInfo.cs, 把 namespace 改成 vcs_test_all_06_System
            // Get the AssemblyInfo class.
            AssemblyInfo info = new AssemblyInfo();

            // Display the values.
            richTextBox1.Text += "Title\t" + info.Title + "\n";
            richTextBox1.Text += "Description\t" + info.Description + "\n";
            richTextBox1.Text += "Company\t" + info.Company + "\n";
            richTextBox1.Text += "Product\t" + info.Product + "\n";
            richTextBox1.Text += "Copyright\t" + info.Copyright + "\n";
            richTextBox1.Text += "Trademark\t" + info.Trademark + "\n";
            richTextBox1.Text += "Assembly Version\t" + info.AssemblyVersion + "\n";
            richTextBox1.Text += "File Version\t" + info.FileVersion + "\n";
            richTextBox1.Text += "GUID\t" + info.Guid + "\n";
            richTextBox1.Text += "Neutral Language\t" + info.NeutralLanguage + "\n";
            richTextBox1.Text += "COM Visible\t" + info.IsComVisible.ToString() + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
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
        }

        private void button4_Click(object sender, EventArgs e)
        {
            string str = System.Environment.GetEnvironmentVariable("SystemRoot");
            richTextBox1.Text += "作業系統在" + str + "\n";
            string dir = str.Substring(0, 2);
            richTextBox1.Text += "作業系統在" + dir + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            OperatingSystem myOS = Environment.OSVersion;
            richTextBox1.Text += "目前系統版本： " + myOS.ToString() + "\n";
            richTextBox1.Text += "目前系統版本： ";
            if (myOS.Version.Major == 5)
            {
                switch (myOS.Version.Minor)
                {
                    case 0:
                        richTextBox1.Text += "Windows 2000 " + myOS.ServicePack + "\n";
                        break;
                    case 1:
                        richTextBox1.Text += "Windows XP " + myOS.ServicePack + "\n";
                        break;
                    case 2:
                        richTextBox1.Text += "Windows Server 2003 " + " " + myOS.ServicePack + "\n";
                        break;
                    default:
                        richTextBox1.Text += myOS.ToString() + " " + myOS.ServicePack + "\n";
                        break;
                }
            }
            else
                richTextBox1.Text += myOS.VersionString + " " + myOS.ServicePack + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            //.Net C# 取得電腦名稱
            //Windows 及 LINUX 都正常

            richTextBox1.Text += "電腦名稱 1 : " + Environment.MachineName + "\n";
            richTextBox1.Text += "電腦名稱 2 : " + System.Net.Dns.GetHostName() + "\n";
            richTextBox1.Text += "電腦名稱 3 : " + System.Windows.Forms.SystemInformation.ComputerName + "\n";
            richTextBox1.Text += "電腦名稱 4 : " + System.Environment.GetEnvironmentVariable("COMPUTERNAME") + "\n";
        }

        //啟動螢幕保護
        private const int WM_SYSCOMMAND = 0x0112;
        private const int SC_SCREENSAVE = 0xf140;
        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);
        private void button7_Click(object sender, EventArgs e)
        {
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_SCREENSAVE, 0);
        }

        private void button8_Click(object sender, EventArgs e)
        {
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
            richTextBox1.Text += "UserName: " + Environment.UserName + "\n";    //操作系統的登錄用户名
            richTextBox1.Text += "WorkingSet: " + Environment.WorkingSet + "\n";
            richTextBox1.Text += "OSVersion: " + Environment.OSVersion.ToString() + "\n";

            richTextBox1.Text += "GetFolderPath System: " + Environment.GetFolderPath(Environment.SpecialFolder.System) + "\n";
            richTextBox1.Text += "GetFolderPath SendTo: " + Environment.GetFolderPath(Environment.SpecialFolder.SendTo) + "\n";
            richTextBox1.Text += "GetFolderPath StartMenu: " + Environment.GetFolderPath(Environment.SpecialFolder.StartMenu) + "\n";
            richTextBox1.Text += "我的文件夾位置 GetFolderPath Personal: " + Environment.GetFolderPath(Environment.SpecialFolder.Personal) + "\n";
            richTextBox1.Text += "GetFolderPath MyMusic: " + Environment.GetFolderPath(Environment.SpecialFolder.MyMusic) + "\n";
            richTextBox1.Text += "GetFolderPath MyComputer: " + Environment.GetFolderPath(Environment.SpecialFolder.MyComputer) + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + "\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "防止程序多次執行\n";
            richTextBox1.Text += "要修改 Program.cs\n";
        }

        private void button11_Click(object sender, EventArgs e)
        {
        }

        private void button12_Click(object sender, EventArgs e)
        {
            object owner_string = "", company_string = "";
            OperatingSystem os_info = System.Environment.OSVersion;
            if (os_info.Platform == PlatformID.Win32Windows)
            {
                // Windows 98?
                owner_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows\CurrentVersion\",
                    "RegisteredOwner", "Unknown");
                company_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows\CurrentVersion\",
                    "RegisteredOrganization", "Unknown");
            }
            else if (os_info.Platform == PlatformID.Win32NT)
            {
                // Windows NT.
                owner_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows NT\CurrentVersion\",
                    "RegisteredOwner", "Unknown");
                company_string = RegistryTools.GetRegistryValue(
                    Registry.LocalMachine,
                    @"SOFTWARE\Microsoft\Windows NT\CurrentVersion\",
                    "RegisteredOrganization", "Unknown");
            }

            richTextBox1.Text += "Owner :\t" + owner_string.ToString() + "\n";
            richTextBox1.Text += "Company :\t" + company_string.ToString() + "\n";
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
                richTextBox1.Text += "電腦本機IP " + IPHost.AddressList[0].ToString() + "\n";
                //MessageBox.Show(IPHost.AddressList[0].ToString(), "電腦本機IP");
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
            foreach (Screen screen in System.Windows.Forms.Screen.AllScreens)
            {
                richTextBox1.Text += "Screen " + screen.DeviceName + "\n";
                richTextBox1.Text += "\tPrimary " + screen.Primary + "\n";
                richTextBox1.Text += "\tBounds: " + screen.Bounds + "\n";
                richTextBox1.Text += "\tWorking Area: " + screen.WorkingArea + "\n";
                richTextBox1.Text += "\tBitsPerPixel: " + screen.BitsPerPixel + "\n";
            }
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //C# 如何產生 GUID?
            //可以直接透過內建方法，產生 GUID

            Guid guid = Guid.NewGuid();
            richTextBox1.Text += "GUID1 : " + guid + "\n";

            guid = Guid.NewGuid();
            richTextBox1.Text += "GUID2 : " + guid + "\n";

            guid = Guid.NewGuid();
            richTextBox1.Text += "GUID3 : " + guid + "\n";
        }

        private void button17_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\r\n主機名:" + Dns.GetHostName() + "\n"; //獲取主機名稱

            string hostName = Dns.GetHostName(); //獲取主機名稱
            IPAddress[] addresses = Dns.GetHostAddresses(hostName); //解析主機IP地址

            string[] IP = new string[addresses.Length]; //轉換為字符串形式
            for (int i = 0; i < addresses.Length; i++)
            {
                IP[i] = addresses[i].ToString();
                richTextBox1.Text += "get ip addr : " + IP[i] + "\n";
            }

            //讀取操作系統和CLR的版本
            OperatingSystem os = System.Environment.OSVersion;
            richTextBox1.Text += "Platform: " + os.Platform + "\n";
            richTextBox1.Text += "Service Pack:" + os.ServicePack + "\n";
            richTextBox1.Text += "Version: " + os.Version + "\n";
            richTextBox1.Text += "VersionString: " + os.VersionString + "\n";
            richTextBox1.Text += "CLR Version: " + System.Environment.Version + "\n";
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            //int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.Text += "目前的螢幕解析度 :" + Screen.PrimaryScreen.Bounds.Width.ToString() + " * " + Screen.PrimaryScreen.Bounds.Height.ToString() + "\n";
        }

        private void button19_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "提供磁碟上實體檔案的版本資訊\n";
            // Get the file version for the notepad.
            FileVersionInfo myFileVersionInfo = FileVersionInfo.GetVersionInfo(Environment.SystemDirectory + "\\Notepad.exe");

            // Print the file name and version number.
            richTextBox1.Text += "File: " + myFileVersionInfo.FileDescription + '\n' + "Version number: " + myFileVersionInfo.FileVersion + "\n";
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //取得目前應用程式版本
            richTextBox1.Text += "VersionInfo: " + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {
            checkSuperuser chk = new checkSuperuser();
            chk.ShowDialog();

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //取得NOTEPAD版本資訊
            richTextBox1.Text += "VersionInfo: " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n";
        }

        private void button23_Click(object sender, EventArgs e)
        {

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
                sb.Append(ei.CodePage).Append("\t")
                    .Append(ei.Name).Append("\t")
                    .Append(ei.DisplayName).Append("\r\n");
            }

            richTextBox1.Text += sb.ToString() + "\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            //(A)關於
            //方案總管/vcs_test_all_06_System/右鍵/加入/Windows Form/關於對話方塊/新增

            AboutBox1 formab = new AboutBox1();
            formab.ShowDialog();


            //方案總管空白處按右鍵/屬性/組件資訊, 修改要顯示的程式資訊
        }

        private void button29_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "找出所有的COM port, ";

            // Get a list of serial port names.
            string[] ports = SerialPort.GetPortNames();

            richTextBox1.Text += " 共有 " + ports.Length + " 個COM port\n";
            // Display each port name to the console.
            foreach (string port in ports)
            {
                richTextBox1.Text += "\t" + port + "\n";
            }
            richTextBox1.Text += "\n";
        }

        private void button36_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "詢問確定關閉表單\n";
            richTextBox1.Text += "找個地方加入WndProc()即可\n";

        }

        //關閉程式時，系統會問是否確認，只需要加下面這段就好。
        protected override void WndProc(ref Message m)
        {
            const int WM_SYSCOMMAND = 0x0112;
            const int SC_CLOSE = 0xF060;
            if (m.Msg == WM_SYSCOMMAND && (int)m.WParam == SC_CLOSE)
            {
                // 顯示MessageBox 
                DialogResult Result = MessageBox.Show("確定關閉表單", "表單訊息", MessageBoxButtons.YesNo);
                if (Result == System.Windows.Forms.DialogResult.Yes)
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

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "作業系統 : " + GetOS() + ", " + GetBit() + "\n";
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
            lv.Left = 955;
            lv.Top = 10;
            lv.Width = 330;
            lv.Height = 400;
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
            richTextBox1.Text += "目前系統目錄為：" + Environment.SystemDirectory + "\n";//顯示系統目錄
            richTextBox1.Text += "機器名稱為：" + Environment.MachineName + "\n";//顯示機器名稱
            richTextBox1.Text += "目前程式執行目錄：" + Environment.CurrentDirectory + "\n";//取得目前程式執行目錄
            richTextBox1.Text += "系統版本號：" + Environment.OSVersion.VersionString + "\n";//顯示系統版本號

            // part 3
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

            // part 4
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

        }

        private void button33_Click(object sender, EventArgs e)
        {
            //c#获取屏幕分辨率信息
            System.Windows.Forms.Screen scr = System.Windows.Forms.Screen.PrimaryScreen;//PrimaryScreen 属性：获取主显示设备
            richTextBox1.Text += "Bounds:\t\t" + scr.Bounds.ToString() + "\n"; //获取屏幕的边界。属性值是一个Rectangle结构的值
            richTextBox1.Text += "DeviceName:\t" + scr.DeviceName.ToString() + "\n"; //获取与显示关联的设备名称
            richTextBox1.Text += "Primary:\t\t" + scr.Primary.ToString() + "\n";   //该值指示某个显示是否为主设备
            richTextBox1.Text += "WorkingArea:\t" + scr.WorkingArea.ToString() + "\n";   //获取显示器的工作区, 属性值是一个Rectangle结构的值
            richTextBox1.Text += "BitsPerPixel:\t" + scr.BitsPerPixel.ToString() + "\n"; //获取与数据的一个像素相关联的内存位数
        }

        private void button23_Click_1(object sender, EventArgs e)
        {
            richTextBox1.Text += "取得目前應用程式版本\n";
            richTextBox1.Text += "Ver：" + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";

            richTextBox1.Text += "取得NOTEPAD版本資訊\n";
            richTextBox1.Text += FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n";
        }

        private void button24_Click_1(object sender, EventArgs e)
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
                stream.Read(buffer, 0, 256);

            var offset = BitConverter.ToInt32(buffer, c_PeHeaderOffset);
            var secondsSince1970 = BitConverter.ToInt32(buffer, offset + c_LinkerTimestampOffset);
            var epoch = new DateTime(1970, 1, 1, 0, 0, 0, DateTimeKind.Utc);

            var linkTimeUtc = epoch.AddSeconds(secondsSince1970);
            var tz = TimeZoneInfo.Local;
            var localTime = TimeZoneInfo.ConvertTimeFromUtc(linkTimeUtc, tz);
            return localTime;
        }

        private void button32_Click_1(object sender, EventArgs e)
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

        private void button38_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "C# 透過Win32取得滑鼠位置 GetCursorPos\n";
        }

        private void button35_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "讀取程式預設值\n";
            ReadSettings();
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

        private void bt_exit_Click(object sender, EventArgs e)
        {
            //離開
            Application.Exit();
        }

        private void timer2_Tick(object sender, EventArgs e)
        {
            Computer myComputer = new Computer();
            label1.Text = "物理內存總量(B)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory);
            label2.Text = "可用物理內存(B)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory);
            label3.Text = "虛擬內存總量(B)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory);
            label4.Text = "可用虛擬內存(B)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory);

            double cpu_usage;
            cpu_usage = (double)pc.NextValue();
            label5.Text = "CPU使用率 " + cpu_usage.ToString() + " %";
        }

        private void bt_memory_Click(object sender, EventArgs e)
        {
            timer2.Enabled = true;
        }

        private void button42_Click(object sender, EventArgs e)
        {
            save_current_program_to_local_drive();
        }

        void save_current_program_to_local_drive()
        {
            //imsLink的方法
            //本程式截圖
            Bitmap bmp = new Bitmap(this.Width, this.Height);
            Graphics g = Graphics.FromImage(bmp);
            //public void CopyFromScreen(int sourceX, int sourceY, int destinationX, int destinationY, System.Drawing.Size blockRegionSize);
            g.CopyFromScreen(this.Location, new Point(0, 0), new Size(this.Width, this.Height));
            //richTextBox1.Text += "W = " + this.Width.ToString() + "\n";
            //richTextBox1.Text += "H = " + this.Height.ToString() + "\n";
            IntPtr dc1 = g.GetHdc();
            g.ReleaseHdc(dc1);

            //存成bmp檔
            String filename = Application.StartupPath + "\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
            bmp.Save(filename, ImageFormat.Bmp);

            //存成jpg檔
            //String filename = Application.StartupPath + "\\picture\\image_this_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".jpg";
            //myImage.Save(filename, ImageFormat.Jpeg);
            richTextBox1.Text += "本程式截圖，存檔檔名：" + filename + "\n";
        }

        private void button39_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "寫入程式預設值\n";
            SaveSettings();
        }

        private void button44_Click(object sender, EventArgs e)
        {
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

        private void button45_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "WorkingArea X = " + Screen.PrimaryScreen.WorkingArea.X.ToString() + "\n";
            richTextBox1.Text += "WorkingArea Y = " + Screen.PrimaryScreen.WorkingArea.Y.ToString() + "\n";
            richTextBox1.Text += "WorkingArea Width = " + Screen.PrimaryScreen.WorkingArea.Width.ToString() + "\n";
            richTextBox1.Text += "WorkingArea Height = " + Screen.PrimaryScreen.WorkingArea.Height.ToString() + "\n";
        }

        private void button46_Click(object sender, EventArgs e)
        {
            Rectangle rect = Screen.GetBounds(Point.Empty);
            using (Bitmap bmp = new Bitmap(rect.Width, rect.Height))
            {
                using (Graphics g = Graphics.FromImage(bmp))
                    g.CopyFromScreen(Point.Empty, Point.Empty, rect.Size);

                //存成bmp檔
                String filename = Application.StartupPath + "\\image_full_screen_" + DateTime.Now.ToString("yyyyMMdd_HHmmss") + ".bmp";
                bmp.Save(filename, ImageFormat.Bmp);

                richTextBox1.Text += "全螢幕截圖，存檔檔名：" + filename + "\n";
            }

        }



        private void button43_Click(object sender, EventArgs e)
        {

        }

        // Save the current settings.
        private void SaveSettings()
        {
            string dir_name = @"C:\______test_files\peony";

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
            Process.Start(psi);
        }

        // Reboot.
        private void btnReboot_Click(object sender, EventArgs e)
        {
            var psi = new ProcessStartInfo("shutdown", "/r /t 0");
            psi.CreateNoWindow = true;
            psi.UseShellExecute = false;
            Process.Start(psi);
        }

        // Log off.
        private void btnLogOff_Click(object sender, EventArgs e)
        {
            ExitWindowsEx(0, 0);
        }

        // Lock.
        private void btnLock_Click(object sender, EventArgs e)
        {
            LockWorkStation();
        }

        // Hibernate.
        private void btnHibernate_Click(object sender, EventArgs e)
        {
            Application.SetSuspendState(PowerState.Hibernate, true, true);
        }

        // Sleep.
        private void btnSleep_Click(object sender, EventArgs e)
        {
            Application.SetSuspendState(PowerState.Suspend, true, true);
        }

        #endregion


    }
}
