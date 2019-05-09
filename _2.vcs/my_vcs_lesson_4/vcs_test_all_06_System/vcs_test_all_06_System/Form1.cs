using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Runtime.InteropServices;   //for DllImport
using System.Diagnostics;   //for process
using Microsoft.Win32;  //for Registry
using Microsoft.VisualBasic.Devices;    //for Computer
using System.Drawing.Text;  //for InstalledFontCollection
using System.Reflection;        //for Assembly
using System.Management;
using System.IO;            //for DriveInfo
using System.Net;   //for DNS
using System.IO.Ports;          //for serial ports

namespace vcs_test_all_06_System
{
    public partial class Form1 : Form
    {
        DateTime start_time = DateTime.Now;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "開機時間 : " + (Environment.TickCount / 1000).ToString() + " 秒" + "\n";
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
            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey("software\\Microsoft\\Internet Explorer");
            string IEVersion = "目前IE瀏覽器的版本訊息：" + (String)mreg.GetValue("Version");
            mreg.Close();
            richTextBox1.Text += IEVersion + "\n";

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
            richTextBox1.Text = string.Empty;
            Process[] myProcesses = Process.GetProcesses();
            foreach (Process myProcess in myProcesses)
            {
                if (myProcess.MainWindowTitle.Length > 0)
                    richTextBox1.Text += "任務名： " + myProcess.MainWindowTitle + "\n";
            }

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
            richTextBox1.Text += "TickCount: " + Environment.TickCount + "\n";
            richTextBox1.Text += "UserDomainName: " + Environment.UserDomainName + "\n";
            richTextBox1.Text += "UserInteractive: " + Environment.UserInteractive + "\n";
            richTextBox1.Text += "UserName: " + Environment.UserName + "\n";    //操作系統的登錄用户名
            richTextBox1.Text += "WorkingSet: " + Environment.WorkingSet + "\n";

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
            InstalledFontCollection myFonts = new InstalledFontCollection();
            foreach (FontFamily family in myFonts.Families)
            {
                richTextBox1.AppendText(family.Name + "\n");
            }

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //1. 參考 -> 加入參考 -> .NET/Microsoft.VisualBasic
            //2. using Microsoft.VisualBasic.Devices;

            Computer myComputer = new Computer();
            richTextBox1.Text += "物理內存總量(M)： " + Convert.ToString(myComputer.Info.TotalPhysicalMemory / 1024 / 1024) + "\n";
            richTextBox1.Text += "可用物理內存(M)： " + Convert.ToString(myComputer.Info.AvailablePhysicalMemory / 1024 / 1024) + "\n";
            richTextBox1.Text += "虛擬內存總量(M)： " + Convert.ToString(myComputer.Info.TotalVirtualMemory / 1024 / 1024) + "\n";
            richTextBox1.Text += "可用虛擬內存(M)： " + Convert.ToString(myComputer.Info.AvailableVirtualMemory / 1024 / 1024) + "\n";

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button13_Click(object sender, EventArgs e)
        {
            System.Diagnostics.ProcessStartInfo processStartInfo = new System.Diagnostics.ProcessStartInfo();
            processStartInfo.FileName = "explorer.exe";  //资源管理器
            processStartInfo.Arguments = @"C:\";
            System.Diagnostics.Process.Start(processStartInfo);

        }

        private void button14_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            String pathname = "C:\\";
            System.Diagnostics.Process.Start(pathname);
            /*
            if (Directory.Exists(this.FolderPath))
            {
                System.Diagnostics.Process.Start(this.FolderPath);
                return true;
            }
            else
                return false;
             */

        }

        private void button15_Click(object sender, EventArgs e)
        {
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

        private void button20_Click(object sender, EventArgs e)
        {
            //取得目前應用程式版本
            richTextBox1.Text += "VersionInfo: " + FileVersionInfo.GetVersionInfo(Assembly.GetExecutingAssembly().Location).FileVersion.ToString() + "\n";

        }

        private void button22_Click(object sender, EventArgs e)
        {
            //取得NOTEPAD版本資訊
            richTextBox1.Text += "VersionInfo: " + FileVersionInfo.GetVersionInfo(@"C:\WINDOWS\NOTEPAD.EXE").FileVersion.ToString() + "\n";

        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {

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

        private void button18_Click(object sender, EventArgs e)
        {
            //int screenWidth = Screen.PrimaryScreen.Bounds.Width;
            //int screenHeight = Screen.PrimaryScreen.Bounds.Height;
            richTextBox1.Text += "目前的螢幕解析度 :" + Screen.PrimaryScreen.Bounds.Width.ToString() + " * " + Screen.PrimaryScreen.Bounds.Height.ToString() + "\n";
        }

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button27_Click(object sender, EventArgs e)
        {

        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button37_Click(object sender, EventArgs e)
        {
            //C#專案中常常要獲取系統字型
            InstalledFontCollection fontCol = new InstalledFontCollection();
            foreach (FontFamily temp in fontCol.Families)
            { comboBox_font.Items.Add(temp.Name); }
            //在Visual Studio 2012下編譯執行後就會在comboBox中顯示目前安裝的所有字體。

        }


        private void button19_Click(object sender, EventArgs e)
        {
            //[C#]取得本機端上，執行中有 GUI 介面的應用程式
            //Environment.MachineName 屬性 : 取得這個本機電腦的 NetBIOS 名稱。
            //Process.GetProcesses 方法 (String) : 為指定電腦上的每個處理序資源建立新的 Process 元件。
            //Process.MainWindowHandle 屬性 : 取得相關處理序主視窗的視窗控制代碼。
            foreach (Process p in Process.GetProcesses(System.Environment.MachineName))
            {
                if (p.MainWindowHandle != IntPtr.Zero)  // 判斷 MainWindowHandle 為非零值的應用程式，表示有主視窗
                {
                    //listBox1.Items.Add(p.ToString());
                    richTextBox1.Text += p.ToString() + "\n";
                }
            }

        }

        private void button28_Click(object sender, EventArgs e)
        {
            //開啟檔案總管
            String pathname = "C:\\";
            System.Diagnostics.Process.Start(pathname);
            /*
            if (Directory.Exists(this.FolderPath))
            {
                System.Diagnostics.Process.Start(this.FolderPath);
                return true;
            }
            else
                return false;
             */

        }

        private void button25_Click(object sender, EventArgs e)
        {
            //用預設的程式開啟檔案
            String pathname = "C:\\______test_vcs\\aaaaaaa.txt";

            if (File.Exists(pathname) == false)
            {
                MessageBox.Show("檔案: " + pathname + "不存在，無法開啟。\n");
                return;
            }
            else
                System.Diagnostics.Process.Start(pathname);
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //離開
            Application.Exit();
        }

        private void button32_Click(object sender, EventArgs e)
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

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //呼叫系統內建小鍵盤     fail
            //System.Diagnostics.Process.Start("" + System.Environment.SystemDirectory + "/osk.exe");

            //開啟特定程式
            //Process.Start(@"C:\___small\imagesweeper5.1影像清潔工.exe");

            //開啟計算機程式
            //Process.Start(@"C:\WINDOWS\system32\calc.exe");

            //開啟檔案 由預設程式開啟
            //System.Diagnostics.Process.Start("C:\\______test_vcs\\my_text_file.txt");
            
            //開啟記事本程式
            //System.Diagnostics.Process.Start("notepad.exe");

            //開啟程式
            //System.Diagnostics.Process.Start("rundll32.exe", "shell32.dll,Control_RunDLL");
            System.Diagnostics.Process.Start("winver.exe ");              //--打开Windows版本信息

        }

    }
}
