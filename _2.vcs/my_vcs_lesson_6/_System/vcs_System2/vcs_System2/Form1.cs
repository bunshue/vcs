using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;   //for Dns
using System.Runtime.InteropServices;   //for DllImport //DllImport 	指定 DLL 的位置
using System.Diagnostics;   //for Process
using System.Net.NetworkInformation;    //for Ping & PingReply

using System.ServiceProcess;    //for ServiceController     參考/加入參考/.NET/System.ServiceProcess

namespace vcs_System2
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
            x_st = 10;
            y_st = 10;
            dx = 210;
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

            label1.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            label1.Text = "aaaaaa";

            label2.Location = new Point(x_st + dx * 5, y_st + dy * 0);
            bt_exit.Location = new Point(x_st + dx * 5, y_st + dy * 0 + 35);

            richTextBox1.Size = new Size(400, 460);
            richTextBox1.Location = new Point(x_st + dx * 4, y_st + dy * 2);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1400, 660);
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

        //是否安裝音效卡 ST
        [DllImport("winmm.dll", EntryPoint = "waveOutGetNumDevs")]
        public static extern int waveOutGetNumDevs();
        private void button12_Click(object sender, EventArgs e)
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

        //光碟機開關 ST
        [DllImport("winmm.dll", EntryPoint = "mciSendString")]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, System.UInt16 uReturnLength, System.IntPtr HwndCallback);
        private void button13_Click(object sender, EventArgs e)
        {
            //打開光碟機
            int result = mciSendString("Set cdaudio door open wait", "", 0, this.Handle);
            if (result == 0)
            {
                richTextBox1.Text += "光碟機打開\n";
            }
        }

        private void button14_Click(object sender, EventArgs e)
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


        //取得任務欄尺寸大小 ST

        [DllImport("user32.dll")]
        public static extern int FindWindow(string lpClassName, string lpWindowName);

        [DllImport("user32.dll")]
        public static extern int GetWindowRect(int hwnd, ref Rectangle lpRect);

        Rectangle myrect;


        private void button15_Click(object sender, EventArgs e)
        {
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

        private void button16_Click(object sender, EventArgs e)
        {
            //隱藏任務欄
            ShowWindow(FindWindow("Shell_TrayWnd", null), SW_HIDE);
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //顯示任務欄
            ShowWindow(FindWindow("Shell_TrayWnd", null), SW_RESTORE);
        }
        //隱藏任務欄, 顯示任務欄 SP

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

        private void button25_Click(object sender, EventArgs e)
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

        private void button26_Click(object sender, EventArgs e)
        {
        }

        private void button27_Click(object sender, EventArgs e)
        {
        }

        private void button28_Click(object sender, EventArgs e)
        {
            //檢測系統啟動模式
            string mode = SystemInformation.BootMode.ToString();
            string str = "目前系統的啟動模式是：";
            switch (mode)
            {
                case "FailSafe":
                    MessageBox.Show(str + "不具有網絡支援的安全模式");
                    break;
                case "FailSafeWithNetwork":
                    MessageBox.Show(str + "具有網絡支援的安全模式");
                    break;
                case "Normal":
                    MessageBox.Show(str + "標準模式");
                    break;
            }
        }

        private void button29_Click(object sender, EventArgs e)
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
            //打開控制面板中的程序_桌面設定
            System.Diagnostics.Process.Start("desk.cpl");
        }

        private void button33_Click(object sender, EventArgs e)
        {
            //打開控制面板中的程序_滑鼠游標設定
            System.Diagnostics.Process.Start("main.cpl");
        }

        private void button34_Click(object sender, EventArgs e)
        {
            //打開控制面板中的程序_網路連接
            System.Diagnostics.Process.Start("ncpa.cpl");
        }

        private void button35_Click(object sender, EventArgs e)
        {
            //打開控制面板中的程序_聲音設定
            System.Diagnostics.Process.Start("mmsys.cpl");
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

        private void button36_Click(object sender, EventArgs e)
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

        private void button37_Click(object sender, EventArgs e)
        {
        }

        private void button38_Click(object sender, EventArgs e)
        {
        }

        private void button39_Click(object sender, EventArgs e)
        {
            //使用Class取得系統資訊
            SYSTEMTIME_INFO SystemInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref SystemInfo);

            richTextBox1.Text += "date : " + SystemInfo.wYear.ToString() + "/" + SystemInfo.wMonth.ToString() + "/" + SystemInfo.wDay.ToString() + " " + SystemInfo.wHour.ToString() + ":" + SystemInfo.wMinute.ToString() + ":" + SystemInfo.wSecond.ToString() + "." + SystemInfo.wMilliseconds.ToString() + "\n";

            //調用GetSystemInfo函數獲取CPU的相關訊息
            CPU_INFO CpuInfo = new CPU_INFO();
            ComputerInfo.GetSystemInfo(ref CpuInfo);
            richTextBox1.Text += "dwOemId = " + CpuInfo.dwOemId.ToString() + "\n";
            richTextBox1.Text += "dwPageSize = " + CpuInfo.dwPageSize.ToString() + "\n";
            richTextBox1.Text += "lpMinimumApplicationAddress = " + CpuInfo.lpMinimumApplicationAddress.ToString() + "\n";
            richTextBox1.Text += "lpMaximumApplicationAddress = " + CpuInfo.lpMaximumApplicationAddress.ToString() + "\n";
            richTextBox1.Text += "dwActiveProcessorMask = " + CpuInfo.dwActiveProcessorMask.ToString() + "\n";
            richTextBox1.Text += "dwNumberOfProcessors = " + CpuInfo.dwNumberOfProcessors.ToString() + "\n";
            richTextBox1.Text += "dwProcessorType = " + CpuInfo.dwProcessorType.ToString() + "\n";
            richTextBox1.Text += "dwAllocationGranularity = " + CpuInfo.dwAllocationGranularity.ToString() + "\n";
            richTextBox1.Text += "dwProcessorLevel = " + CpuInfo.dwProcessorLevel.ToString() + "\n";
            richTextBox1.Text += "dwProcessorRevision = " + CpuInfo.dwProcessorRevision.ToString() + "\n";

            richTextBox1.Text += "本計算機中有" + CpuInfo.dwNumberOfProcessors.ToString() + "個CPU" + "\n";
            richTextBox1.Text += "CPU的類型為" + CpuInfo.dwProcessorType.ToString() + "\n";
            richTextBox1.Text += "CPU等級為" + CpuInfo.dwProcessorLevel.ToString() + "\n";
            richTextBox1.Text += "CPU的OEM ID為" + CpuInfo.dwOemId.ToString() + "\n";
            richTextBox1.Text += "CPU中的頁面大小為" + CpuInfo.dwPageSize.ToString() + "\n";


            //調用GlobalMemoryStatus函數獲取記憶體的相關訊息
            MEMORY_INFO MemInfo = new MEMORY_INFO();
            ComputerInfo.GlobalMemoryStatus(ref MemInfo);
            richTextBox1.Text += "dwLength = " + MemInfo.dwLength.ToString() + "\n";
            richTextBox1.Text += "dwMemoryLoad = " + MemInfo.dwMemoryLoad.ToString() + "\n";
            richTextBox1.Text += "dwTotalPhys = " + (MemInfo.dwTotalPhys / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwAvailPhys = " + (MemInfo.dwAvailPhys / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwTotalPageFile = " + (MemInfo.dwTotalPageFile / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwAvailPageFile = " + (MemInfo.dwAvailPageFile / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwTotalVirtual = " + (MemInfo.dwTotalVirtual / 1024 / 1024).ToString().ToString() + "\n";
            richTextBox1.Text += "dwAvailVirtual = " + (MemInfo.dwAvailVirtual / 1024 / 1024).ToString().ToString() + "\n";

            richTextBox1.Text += MemInfo.dwMemoryLoad.ToString() + "%的內存正在使用" + "\n";
            richTextBox1.Text += "物理內存共有" + MemInfo.dwTotalPhys.ToString() + "字節" + "\n";
            richTextBox1.Text += "可使用的物理內存有" + MemInfo.dwAvailPhys.ToString() + "字節" + "\n";
            richTextBox1.Text += "交換文件總大小為" + MemInfo.dwTotalPageFile.ToString() + "字節" + "\n";
            richTextBox1.Text += "尚可交換文件大小為" + MemInfo.dwAvailPageFile.ToString() + "字節" + "\n";
            richTextBox1.Text += "總虛擬內存有" + MemInfo.dwTotalVirtual.ToString() + "字節" + "\n";
            richTextBox1.Text += "未用虛擬內存有" + MemInfo.dwAvailVirtual.ToString() + "字節" + "\n";

            //調用GetSystemTime函數獲取系統時間訊息
            SYSTEMTIME_INFO SysInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref SysInfo);
            richTextBox1.Text += "wYear = " + SysInfo.wYear.ToString() + "\n";
            richTextBox1.Text += "wMonth = " + SysInfo.wMonth.ToString() + "\n";
            richTextBox1.Text += "wDayOfWeek = " + SysInfo.wDayOfWeek.ToString() + "\n";
            richTextBox1.Text += "wDay = " + SysInfo.wDay.ToString() + "\n";
            richTextBox1.Text += "wHour = " + SysInfo.wHour.ToString() + "\n";
            richTextBox1.Text += "wMinute = " + SysInfo.wMinute.ToString() + "\n";
            richTextBox1.Text += "wSecond = " + SysInfo.wSecond.ToString() + "\n";
            richTextBox1.Text += "wMilliseconds = " + SysInfo.wMilliseconds.ToString() + "\n";


            //調用GetWindowsDirectory和GetSystemDirectory函數分別取得Windows路徑和系統路徑
            const int nChars = 128;
            StringBuilder Buff = new StringBuilder(nChars);
            ComputerInfo.GetWindowsDirectory(Buff, nChars);
            richTextBox1.Text += "Windows路徑：" + Buff.ToString() + "\n";
            ComputerInfo.GetSystemDirectory(Buff, nChars);
            richTextBox1.Text += "系統路徑：" + Buff.ToString() + "\n";

            //調用GetSystemTime函數獲取系統時間信息
            SYSTEMTIME_INFO StInfo;
            StInfo = new SYSTEMTIME_INFO();
            ComputerInfo.GetSystemTime(ref StInfo);
            richTextBox1.Text += StInfo.wYear.ToString() + "年" + StInfo.wMonth.ToString() + "月" + StInfo.wDay.ToString() + "日" + "\n";
            richTextBox1.Text += (StInfo.wHour + 8).ToString() + "點" + StInfo.wMinute.ToString() + "分" + StInfo.wSecond.ToString() + "秒" + "\n";
        }


        /// <summary>
        ///取得計算機的系統信息
        /// </summary>
        public class ComputerInfo
        {
            // 聲明所要用到的API函數
            /// <summary>
            /// 取得Windows的目錄
            /// </summary>
            /// <param name="WinDir"></param>
            /// <param name="count"></param>
            [DllImport("kernel32")]
            public static extern void GetWindowsDirectory(StringBuilder WinDir, int count);

            /// <summary>
            /// 獲取系統路徑
            /// </summary>
            /// <param name="SysDir"></param>
            /// <param name="count"></param>
            [DllImport("kernel32")]
            public static extern void GetSystemDirectory(StringBuilder SysDir, int count);

            /// <summary>
            /// 取得CPU信息
            /// </summary>
            /// <param name="cpuinfo"></param>
            [DllImport("kernel32")]
            public static extern void GetSystemInfo(ref CPU_INFO cpuinfo);

            /// <summary>
            /// 取得內存狀態
            /// </summary>
            /// <param name="meminfo"></param>
            [DllImport("kernel32")]
            public static extern void GlobalMemoryStatus(ref MEMORY_INFO meminfo);

            /// <summary>
            /// 取得系統時間
            /// </summary>
            /// <param name="stinfo"></param>
            [DllImport("kernel32")]
            public static extern void GetSystemTime(ref SYSTEMTIME_INFO stinfo);
            public ComputerInfo()
            {
            }
        }
        //定義CPU的信息結構
        [StructLayout(LayoutKind.Sequential)]
        public struct CPU_INFO
        {
            public uint dwOemId;
            public uint dwPageSize;
            public uint lpMinimumApplicationAddress;
            public uint lpMaximumApplicationAddress;
            public uint dwActiveProcessorMask;
            public uint dwNumberOfProcessors;
            public uint dwProcessorType;
            public uint dwAllocationGranularity;
            public uint dwProcessorLevel;
            public uint dwProcessorRevision;
        }
        //定義內存的信息結構
        [StructLayout(LayoutKind.Sequential)]
        public struct MEMORY_INFO
        {
            public uint dwLength;
            public uint dwMemoryLoad;
            public uint dwTotalPhys;
            public uint dwAvailPhys;
            public uint dwTotalPageFile;
            public uint dwAvailPageFile;
            public uint dwTotalVirtual;
            public uint dwAvailVirtual;
        }
        //定義系統時間的信息結構
        [StructLayout(LayoutKind.Sequential)]
        public struct SYSTEMTIME_INFO
        {
            public ushort wYear;
            public ushort wMonth;
            public ushort wDayOfWeek;
            public ushort wDay;
            public ushort wHour;
            public ushort wMinute;
            public ushort wSecond;
            public ushort wMilliseconds;
        }


    }
}
