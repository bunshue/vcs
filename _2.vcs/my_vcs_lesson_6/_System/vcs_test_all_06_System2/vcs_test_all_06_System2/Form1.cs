using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Runtime.InteropServices;   //for DllImport
using System.Diagnostics;   //for Process
using System.Net.NetworkInformation;    //for Ping & PingReply

using System.ServiceProcess;    //for ServiceController     參考/加入參考/.NET/System.ServiceProcess

using Microsoft.Win32;      //for RegistryKey

namespace vcs_test_all_06_System2
{
    public partial class Form1 : Form
    {

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

            label1.Location = new Point(x_st + dx * 4, y_st + dy * 1 / 2 + 5);
            label1.Text = "";

            label2.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 5 + 140, y_st + dy * 0 + 35);

            richTextBox1.Location = new Point(x_st + dx * 4 + dx / 2, y_st + dy * 0 + 80);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        //禁用視窗上的關閉按鈕
        protected override void WndProc(ref Message m)
        {
            const int WM_SYSCOMMAND = 0x0112;
            const int SC_CLOSE = 0xF060;
            if ((m.Msg == WM_SYSCOMMAND) && ((int)m.WParam == SC_CLOSE))
            {
                return;
            }
            base.WndProc(ref m);
        }

        private void button0_Click(object sender, EventArgs e)
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
            UInt32 FileSystemNameSize
        );

        private void button1_Click(object sender, EventArgs e)
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
        private void button2_Click(object sender, EventArgs e)
        {
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

        private void button3_Click(object sender, EventArgs e)
        {
            int i;
            for (i = 0; i <= 7777; i++)
            {
                label1.Text = i.ToString();
                Application.DoEvents();//實時響應文本框中的值
                //Application.DoEvents()的作用：处理当前在消息队列中的所有 Windows 消息。
                //加Application.DoEvents可以防止界面停止响应
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //取得記憶體使用狀態

            richTextBox1.Text += "Property\t\t\tValue\n";
            Process proc = Process.GetCurrentProcess();

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

        private void button5_Click(object sender, EventArgs e)
        {
            //C# Ping a hostname on the network
            //C# Ping a hostname on the network

            Ping ping = new Ping();

            PingReply reply = ping.Send("www.google.com");
            if (reply.Status == IPStatus.Success)
            {
                MessageBox.Show("ok");
            }

        }

        private void button6_Click(object sender, EventArgs e)
        {
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

            string strFinal;
            string strQuery = "系統磁碟機：%SystemDrive% 與 系統根目錄：%SystemRoot%";
            strFinal = Environment.ExpandEnvironmentVariables(strQuery);
            richTextBox1.Text += strFinal + "\n";

            string[] arguments = Environment.GetCommandLineArgs();
            richTextBox1.Text += string.Format("取得命令列的Args: {0}", string.Join(", ", arguments)) + "\n";

            richTextBox1.Text += "系統特殊資料夾的路徑：" + Environment.GetFolderPath(Environment.SpecialFolder.System);

            string[] drives = Environment.GetLogicalDrives();
            richTextBox1.Text += string.Format("系統磁碟機：{0}", string.Join(", ", drives)) + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            int i;
            for (i = 0; i <= 7777; i++)
            {
                label1.Text = i.ToString();
                //Application.DoEvents();//實時響應文本框中的值
            }
        }

        private void button8_Click(object sender, EventArgs e)
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

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {

        }

        private void button11_Click(object sender, EventArgs e)
        {

        }

        private void button12_Click(object sender, EventArgs e)
        {
            //列出所有的Process
            Process[] all = Process.GetProcesses();
            int length = all.Length;
            for (int index = 0; index < length; index++)
            {
                richTextBox1.Text += String.Format("{0} \tID:{1}", all[index].ProcessName, all[index].Id) + "\n";
            }
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
            //列出firefox的Process
            Process[] ps = Process.GetProcessesByName("firefox");
            foreach (Process p in ps)
            {
                richTextBox1.Text += String.Format("{0} \tID:{1}", p.ProcessName, p.Id) + "\n";
            }
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

        private void button20_Click(object sender, EventArgs e)
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

        private void button21_Click(object sender, EventArgs e)
        {

        }

        private void button22_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click(object sender, EventArgs e)
        {

        }

        private void button24_Click(object sender, EventArgs e)
        {

        }

        private void button25_Click(object sender, EventArgs e)
        {
        }

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //取得各瀏覽器版本訊息

            RegistryKey mreg;
            mreg = Registry.LocalMachine;
            mreg = mreg.CreateSubKey("software\\Microsoft\\Internet Explorer");
            string IEVersion = "目前IE瀏覽器的版本訊息：\t" + (String)mreg.GetValue("Version");
            mreg.Close();

            richTextBox1.Text += IEVersion + "\n";

            RegistryKey mreg2;
            mreg2 = Registry.LocalMachine;
            mreg2 = mreg2.CreateSubKey("software\\mozilla.org\\Mozilla");
            string FirefoxVersion = "目前Firefox瀏覽器的版本訊息：\t" + (String)mreg2.GetValue("CurrentVersion");
            mreg2.Close();

            richTextBox1.Text += FirefoxVersion + "\n";


        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        //啟動螢幕保護 ST

        private const int WM_SYSCOMMAND = 0x0112;
        private const int SC_SCREENSAVE = 0xf140;

        [DllImport("user32.dll")]
        public static extern bool SendMessage(IntPtr hwnd, int wMsg, int wParam, int lParam);

        private void button36_Click(object sender, EventArgs e)
        {
            //啟動螢幕保護
            SendMessage(this.Handle, WM_SYSCOMMAND, SC_SCREENSAVE, 0);

        }
        //啟動螢幕保護 SP

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {

        }

        private void button32_Click(object sender, EventArgs e)
        {

        }

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button23_Click_1(object sender, EventArgs e)
        {
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

        private void button24_Click_1(object sender, EventArgs e)
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

        private void button32_Click_1(object sender, EventArgs e)
        {
            //設定IE瀏覽器的預設主頁

            //1.讀取目前IE的首頁
            RegistryKey reg1 = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            object strInfo = reg1.GetValue("Start Page", "沒有值");
            //this.textBox1.Text = (string)strInfo;
            richTextBox1.Text += "IE目前的首頁:\t" + (string)strInfo + "\n";

            //2.設定IE的首頁為空白頁
            RegistryKey reg2 = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg2.SetValue("Start Page", "about:blank", RegistryValueKind.String);
            richTextBox1.Text += "IE 目前的預設頁為\t空白頁\n";

            //3.設定IE的首頁為Google首頁
            string url = @"https://www.google.com.tw/";
            RegistryKey reg3 = Registry.CurrentUser.CreateSubKey(@"SoftWare\Microsoft\Internet Explorer\Main");
            reg3.SetValue("Start Page", url, RegistryValueKind.String);
            richTextBox1.Text += "IE 目前的預設頁為\t" + url + "\n";
        }

        private void button34_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
        }

        private void button35_Click(object sender, EventArgs e)
        {
        }

        private void button40_Click(object sender, EventArgs e)
        {
        }

        private void button41_Click(object sender, EventArgs e)
        {
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
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

        private void button42_Click(object sender, EventArgs e)
        {
        }

        private void button39_Click(object sender, EventArgs e)
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

        private void button43_Click(object sender, EventArgs e)
        {
        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }
    }
}
