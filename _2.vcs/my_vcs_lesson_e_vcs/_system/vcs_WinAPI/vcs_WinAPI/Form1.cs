using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;   //for Process
using System.IO;

using System.Runtime.InteropServices;   //for DllImport

//Windows API是對Windows操作系統的API函數，在C#中調用Windows API的實質是托管代碼對非托管代碼的調用。

namespace vcs_WinAPI
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
            dx = 180;
            dy = 90;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);

            button8.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button9.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button10.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button11.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button12.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button13.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button14.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button15.Location = new Point(x_st + dx * 1, y_st + dy * 7);

            button16.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button17.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button18.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button19.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button20.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button21.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button22.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button23.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            richTextBox1.Location = new Point(x_st + dx * 3, y_st + dy * 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }


        //Beep ST
        [DllImport("kernel32", CharSet = CharSet.Ansi)]
        //[DllImport("kernel32.dll")]
        public static extern bool Beep(int frequency, int duration);

        public enum BeepType
        {
            SimpleBeep = -1,
            IconAsterisk = 0x00000040,
            IconExclamation = 0x00000030,
            IconHand = 0x00000010,
            IconQuestion = 0x00000020,
            Ok = 0x00000000,
        }
        [DllImport("user32.dll")]
        public static extern bool MessageBeep(BeepType beepType);

        private void button0_Click(object sender, EventArgs e)
        {
            Beep(500, 300);
            //其中的Beep就是Win API的調用，使用[DllImport("kernel32")]屬性進行調用。

            //雜音Beep
            Random random = new Random();
            for (int i = 0; i < 10; i++)
            {
                Beep(random.Next(10000), 100);
            }

        }
        //Beep SP

        //鼠標 ST
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern bool GetCursorPos(ref Point point);

        [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
        public static extern IntPtr GetCursor();

        [DllImport("user32.dll")]
        private static extern bool SetCursorPos(int X, int Y);

        private void button1_Click(object sender, EventArgs e)
        {
            //以下是用WinAPI 模擬鼠標定位和單機左鍵的操作：

            Point point = new Point();
            bool getResult = GetCursorPos(ref point);
            bool setRight = SetCursorPos(1920 / 2, 1080 / 2);
        }
        //鼠標 SP

        private void button2_Click(object sender, EventArgs e)
        {
            //獲取硬盤序列號
            HardDiskVal hddval = new HardDiskVal();
            richTextBox1.Text += "C : " + hddval.HDVal("C") + "\n";
            richTextBox1.Text += "D : " + hddval.HDVal("D") + "\n";

            //獲取硬盤序列號
            HardDiskVal hdv = new HardDiskVal();
            string result = hdv.HDVal();
            richTextBox1.Text += "獲取硬盤序列號 : " + result + "\n";
        }

        //C#如何獲得 WINDOWS 版本 ST

        [StructLayout(LayoutKind.Sequential)]
        public class OSVersionInfo
        {
            public int OSVersionInfoSize;
            public int MajorVersion;
            public int MinorVersion;
            public int BuildNumber;
            public int PlatformId;


            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 128)]
            public String versionString;
        }


        [StructLayout(LayoutKind.Sequential)]
        public struct OSVersionInfo2
        {
            public int OSVersionInfoSize;
            public int MajorVersion;
            public int MinorVersion;
            public int BuildNumber;
            public int PlatformId;


            [MarshalAs(UnmanagedType.ByValTStr, SizeConst = 128)]
            public String versionString;
        }


        public class LibWrap
        {
            [DllImport("kernel32")]
            public static extern bool GetVersionEx([In, Out] OSVersionInfo osvi);


            [DllImport("kernel32", EntryPoint = "GetVersionEx")]
            public static extern bool GetVersionEx2(ref OSVersionInfo2 osvi);
        }


        public static String OpSysName(int MajorVersion, int MinorVersion, int PlatformId)
        {
            String str_opn = String.Format("{0}.{1}", MajorVersion, MinorVersion);

            switch (str_opn)
            {
                case "4.0":
                    return win95_nt40(PlatformId);
                case "4.10":
                    return "Windows 98";
                case "4.90":
                    return "Windows Me";
                case "3.51":
                    return "Windows NT 3.51";
                case "5.0":
                    return "Windwos 2000";
                case "5.1":
                    return "Windwos XP";
                case "5.2":
                    return "Windows Server 2003 family";
                default:
                    return "This windows version is not distinguish!";
            }
        }

        public static String win95_nt40(int PlatformId)
        {
            switch (PlatformId)
            {
                case 1:
                    return "Windows 95";
                case 2:
                    return "Windows NT 4.0";
                default:
                    return "This windows version is not distinguish!";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            ////取得Windows版本
            richTextBox1.Text += " Passing OSVersionInfo as class" + "\n";

            OSVersionInfo osvi = new OSVersionInfo();
            osvi.OSVersionInfoSize = Marshal.SizeOf(osvi);

            LibWrap.GetVersionEx(osvi);

            richTextBox1.Text += "Class size: " + osvi.OSVersionInfoSize + "\tOperation System : " + OpSysName(osvi.MajorVersion, osvi.MinorVersion, osvi.PlatformId) + "\tPack: " + osvi.versionString + "\n";
            richTextBox1.Text += osvi.PlatformId + "\n";

            richTextBox1.Text += " Passing OSVersionInfo as struct" + "\n";
            OSVersionInfo2 osvi2 = new OSVersionInfo2();
            osvi2.OSVersionInfoSize = Marshal.SizeOf(osvi2);

            LibWrap.GetVersionEx2(ref osvi2);
            richTextBox1.Text += "Static size: " + osvi2.OSVersionInfoSize + "\tOperation System : " + OpSysName(osvi2.MajorVersion, osvi2.MinorVersion, osvi2.PlatformId) + "\tPack: " + osvi2.versionString + "\n";
        }
        //C#如何獲得 WINDOWS 版本 SP

        //設定音量1, 2  ST

        //winmm控制方式，涉及Xp系統波形聲音的左右聲道，高位為左聲道，低位為右聲道：
        //winmm

        [DllImport("winmm.dll", EntryPoint = "waveOutSetVolume")]
        public static extern int WaveOutSetVolume(IntPtr hwo, uint dwVolume);

        private void SetVol1(double arg)
        {
            double newVolume = ushort.MaxValue * arg / 10.0;

            uint v = ((uint)newVolume) & 0xffff;
            uint vAll = v | (v << 16);

            richTextBox1.Text += "setup " + vAll.ToString() + "\n";
            int retVal = WaveOutSetVolume(IntPtr.Zero, vAll);
        }

        //user32控制方式：
        //user32

        [DllImport("user32.dll")]
        public static extern IntPtr SendMessageW(IntPtr hWnd, int Msg, IntPtr wParam, IntPtr lParam);

        public void SetVol2()
        {
            p = Process.GetCurrentProcess();
            for (int i = 0; i < 5; i++)
            {
                SendMessageW(p.Handle, WM_APPCOMMAND, p.Handle, (IntPtr)APPCOMMAND_VOLUME_UP);
            }
        }

        private Process p;
        private const int APPCOMMAND_VOLUME_MUTE = 0x80000;
        private const int APPCOMMAND_VOLUME_UP = 0x0a0000;
        private const int APPCOMMAND_VOLUME_DOWN = 0x090000;
        private const int WM_APPCOMMAND = 0x319;

        double a = 0;

        private void button4_Click(object sender, EventArgs e)
        {
            //useless
            //設定音量1 winm
            SetVol1(a);

            a += 10;
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //設定音量2 user32
            SetVol2();
        }
        //設定音量1, 2  SP

        //切換鼠標左右鍵 ST
        //C#切換鼠標左右鍵習慣無需控制面板中修改

        [DllImport("user32.dll")]
        private extern static bool SwapMouseButton(bool fSwap);

        [DllImport("user32.dll")]
        private extern static int GetSystemMetrics(int index);

        private void button6_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "你按了 切換鼠標左右鍵\n";

            int flag = GetSystemMetrics(23);//獲取當前鼠標設置狀態
            if (flag == 0)//右手習慣
            {
                SwapMouseButton(true);//設置成左手
                richTextBox1.Text += "換成左手\n";
            }
            else//左手習慣
            {
                SwapMouseButton(false);//設置成右手
                richTextBox1.Text += "換成右手\n";
            }

        }

        //切換鼠標左右鍵 SP

        //長檔名轉短檔名 ST
        [DllImport("Kernel32.dll")]//声明API函数
        private static extern Int16 GetShortPathName(string lpszLongPath, StringBuilder lpszShortPath, Int16 cchBuffer);

        private void button7_Click(object sender, EventArgs e)
        {
            string filename_long = @"C:\______test_files\__RW\_word\word_for_vcs_ReadWrite_WORD.doc";
            StringBuilder filename_short = new System.Text.StringBuilder(256);//创建StringBuilder对象
            GetShortPathName(filename_long, filename_short, 256);//调用API函数转换成短文件名
            richTextBox1.Text += "長檔名：" + filename_long + "\n";
            richTextBox1.Text += "短檔名：" + filename_short + "\n";
        }
        //長檔名轉短檔名 SP

        //格式化磁盤 ST

        [DllImport("shell32.dll")]
        private static extern int SHFormatDrive(IntPtr hWnd, int drive, long fmtID, int Options);
        public const long SHFMT_ID_DEFAULT = 0xFFFF;

        private void button8_Click(object sender, EventArgs e)
        {
            int drive_id = 1;   //A: 0, B: 1, C: 2, D: 3, E: 4.....

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
        //格式化磁盤 SP

        //取得mp3播放長度 ST

        #region  获取文件的播放时间，并在列表中进行显示
        /// <summary>
        /// 获取文件的播放时间，并在列表中进行显示
        /// </summary>
        /// <param Millisecond="int">毫秒数</param>
        //添加using System.Runtime.InteropServices;API函数的命名空间
        [DllImport("kernel32.dll", CharSet = CharSet.Auto)]
        public static extern int GetShortPathName(string lpszLongPath, string shortFile, int cchBuffer);//获取指定文件的短路径名

        [DllImport("winmm.dll", EntryPoint = "mciSendString", CharSet = CharSet.Auto)]
        public static extern int mciSendString(string lpstrCommand, string lpstrReturnString, int uReturnLength, int hwndCallback);//播放多媒体文件

        public int LongTime(string Spath)
        {
            richTextBox1.Text += "Spath = " + Spath + "\n";
            string Pname = "";//用来保存多媒体文件的命令       
            string TemStr = "";//用来保存处理后的字符串
            int ilong = 0;//用来保存短路径文件名
            string tem_str = "";//用来保存最终的文件名
            int t = 0;//声明一个用来保存时间的变量
            TemStr = TemStr.PadLeft(128, Convert.ToChar(" "));//右对齐此实例中的字符，在左边用空格或指定的 Unicode 字符填充以达到指定的总长度
            ilong = GetShortPathName(Spath, TemStr, TemStr.Length);//获取指定路径下的短路径文件名
            Pname = "open " + Convert.ToChar(34) + Spath + Convert.ToChar(34) + " alias media";//为变量Pname赋值
            t = mciSendString(Pname, TemStr, TemStr.Length, 0);//打开指定的多媒体文件
            t = mciSendString("status " + Spath + " length", TemStr, 128, 0);//获取当前多媒体文件的状态
            tem_str = TemStr.Substring(0, TemStr.IndexOf("\0"));//为变量tem_str赋值
            if (tem_str.Trim() == "")//当变量tem_str的值为空时
                t = 0;//设定变量t的值为0
            else//当变量tem_str的值为非空时
                t = Convert.ToInt32(tem_str);//重新设定变量t的值
            return t;//返回变量t的值
        }
        #endregion

        #region  获取文件的播放时间，并按指定格式进行显示
        /// <summary>
        /// 获取文件的播放时间，并按指定格式进行显示
        /// </summary>
        /// <param Millisecond="int">毫秒数</param>
        public string GetFileTime(int Millisecond)
        {
            string Tem_Time = ""; //用来保存歌曲的播放时间
            double Tem_min = 0;  //用来保存歌曲播放的分钟部分
            double Tem_sec = 0;  //用来保存歌曲播放时间的秒
            double Tem_millisec = 0; //用来保存歌曲播放时间的毫秒

            Tem_min = Millisecond / 1000;//将当前时间转化为以秒为单位的数据类型
            Tem_min = Tem_min / 60.0; //将当前时间转化为以分为单位的数据类型

            Tem_sec = Tem_min - (int)Tem_min; //保存歌曲播放时间的小数部分（当以分为单位时）
            Tem_min = (int)Tem_min; //将double型变量Tem_min转化为int型变量
            Tem_sec = (60 * Tem_sec) / 100.0; //将获得的小数转化为以秒为单位的数据
            Tem_sec = (int)(Tem_sec * 100);//将数据类型转化为int型
            Tem_millisec = (int)((Millisecond - Tem_min * 60 * 1000 - Tem_sec * 1000) / 1000 * 100);//将歌曲播放的时间转换为以秒为单位存储
            if (Tem_min >= 100)//当Tem_min的值大于等于100时
            {
                Tem_Time = Tem_min.ToString("000") + ":" + Tem_sec.ToString("00");//设置时间的显示格式
            }
            else//当Tem_min的值小于100时
                Tem_Time = Tem_min.ToString("00") + ":" + Tem_sec.ToString("00"); //设置事件的显示格式
            return Tem_Time;//返回变量Tem_Time
        }
        #endregion



        private void button9_Click(object sender, EventArgs e)
        {
            //取得mp3播放長度
            string filename = @"C:\______test_files\_mp3\16.監獄風雲.mp3";

            richTextBox1.Text += "filename = " + filename + "\n";
            richTextBox1.Text += "播放時間 : " + GetFileTime(LongTime(filename)) + "\n";
        }
        //取得mp3播放長度 SP


        private const uint WM_SYSCOMMAND = 0x112;                    //系统消息
        private const int SC_MONITORPOWER = 0xF170;                  //关闭显示器的系统命令
        private const int MonitorPowerOn = -1;                       //2为PowerOff, 1为省电状态，-1为开机
        private const int MonitorPowerSaving = 1;                    //2为PowerOff, 1为省电状态，-1为开机
        private const int MonitorPowerOff = 2;                       //2为PowerOff, 1为省电状态，-1为开机
        private static readonly IntPtr HWND_BROADCAST = new IntPtr(0xffff);//广播消息，所有顶级窗体都会接收

        [DllImport("user32.dll")]
        private static extern IntPtr SendMessage(IntPtr hWnd, uint Msg, int wParam, int lParam);

        private void button10_Click(object sender, EventArgs e)
        {
            //關閉顯示器, 但打開顯示器無效, 要自己動手按
            richTextBox1.Text += "關閉顯示器, 偽執行\n";
            //SendMessage(HWND_BROADCAST, WM_SYSCOMMAND, SC_MONITORPOWER, MonitorPowerOff);
            //SendMessage(this.Handle, WM_SYSCOMMAND,SC_MONITORPOWER, 2);     // 2 为关闭显示器, －1则打开显示器, same

            //same
            //关闭
            //SendMessage(this.Handle, WM_SYSCOMMAND, SC_MONITORPOWER, 2);
            //打开
            //SendMessage(this.Handle, WM_SYSCOMMAND, SC_MONITORPOWER, -1);
        }

        //使用API即時判斷當前的網絡的連接方式 ST

        [DllImport("wininet.dll")]
        private extern static bool InternetGetConnectedState(out int connectionDescription, int reservedValue);

        [DllImport("sensapi.dll")]
        private extern static bool IsNetworkAlive(out int connectionDescription);

        static string Fun_InternetGetConnectedState()
        {
            int INTERNET_CONNECTION_MODEM = 1;
            int INTERNET_CONNECTION_LAN = 2;
            int INTERNET_CONNECTION_PROXY = 4;
            int INTERNET_CONNECTION_MODEM_BUSY = 8;

            string outPut = null;
            int flags;//上網方式
            bool m_bOnline = true;//是否在線 

            m_bOnline = InternetGetConnectedState(out flags, 0);
            if (m_bOnline)//在線  
            {
                if ((flags & INTERNET_CONNECTION_MODEM) == INTERNET_CONNECTION_MODEM)
                {
                    outPut = "在線：撥號上網 ";
                }
                if ((flags & INTERNET_CONNECTION_LAN) == INTERNET_CONNECTION_LAN)
                {
                    outPut = "在線：通過局域網 ";
                }
                if ((flags & INTERNET_CONNECTION_PROXY) == INTERNET_CONNECTION_PROXY)
                {
                    outPut = "在線：代理 ";
                }
                if ((flags & INTERNET_CONNECTION_MODEM_BUSY) == INTERNET_CONNECTION_MODEM_BUSY)
                {
                    outPut = "MODEM被其他非INTERNET連接占用 ";
                }
            }
            else
            {
                outPut = "不在線 ";
            }

            return outPut;
        }

        static string Fun_IsNetworkAlive()
        {
            int NETWORK_ALIVE_LAN = 0;
            int NETWORK_ALIVE_WAN = 2;
            int NETWORK_ALIVE_AOL = 4;

            string outPut = null;
            int flags;//上網方式
            bool m_bOnline = true;//是否在線 

            m_bOnline = IsNetworkAlive(out flags);
            if (m_bOnline)//在線  
            {
                if ((flags & NETWORK_ALIVE_LAN) == NETWORK_ALIVE_LAN)
                {
                    outPut = "在線：NETWORK_ALIVE_LAN ";
                }
                if ((flags & NETWORK_ALIVE_WAN) == NETWORK_ALIVE_WAN)
                {
                    outPut = "在線：NETWORK_ALIVE_WAN ";
                }
                if ((flags & NETWORK_ALIVE_AOL) == NETWORK_ALIVE_AOL)
                {
                    outPut = "在線：NETWORK_ALIVE_AOL ";
                }
            }
            else
            {
                outPut = "不在線\n";
            }

            return outPut;
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //使用API即時判斷當前的網絡的連接方式
            Console.WriteLine("使用InternetGetConnectedState對網絡連接方式進行判斷");
            Console.WriteLine(Fun_InternetGetConnectedState());
            Console.WriteLine("使用IsNetworkAlive對網絡連接方式進行判斷");
            Console.WriteLine(Fun_IsNetworkAlive());
        }

        //使用API即時判斷當前的網絡的連接方式 SP


        [DllImport("User32.dll")]
        public extern static System.IntPtr GetDC(System.IntPtr hWnd);
        private void button12_Click(object sender, EventArgs e)
        {
            //在螢幕上畫東西1

            IntPtr DesktopHandle = GetDC(IntPtr.Zero);
            Graphics g = Graphics.FromHdc(DesktopHandle);
            Rectangle ScreenArea = Screen.GetBounds(this);
            for (; ; )
            {
                g.DrawRectangle(new Pen(Color.Red), new Rectangle(ScreenArea.Width / 2, ScreenArea.Height / 2, 1, 1));


                g.DrawRectangle(new Pen(Color.Red), new Rectangle(ScreenArea.Width / 2 - 50, ScreenArea.Height / 2 - 50, 100, 100));
            }
        }

        [DllImport("user32.dll")]
        private static extern int GetDC(int hwnd);
        private void button13_Click(object sender, EventArgs e)
        {
            //在螢幕上畫東西2
            IntPtr p = (IntPtr)GetDC(0);// '取得屏幕
            Graphics g = Graphics.FromHdc(p);
            g.DrawRectangle(new Pen(Color.Red, 10), new Rectangle(1920 / 2 - 100, 1080 / 2 - 100, 200, 200));
        }

        [DllImport("user32.dll", CharSet = CharSet.Auto, ExactSpelling = true)]
        public static extern IntPtr GetDesktopWindow();
        [DllImport("user32.dll", EntryPoint = "GetDCEx", CharSet = CharSet.Auto, ExactSpelling = true)]
        private static extern IntPtr GetDCEx(IntPtr hWnd, IntPtr hrgnClip, int flags);
        private void button14_Click(object sender, EventArgs e)
        {
            //在螢幕上畫東西3
            IntPtr desk = GetDesktopWindow();
            IntPtr deskDC = GetDCEx(desk, IntPtr.Zero, 0x403);
            Graphics g = Graphics.FromHdc(deskDC);
            g.FillEllipse(new SolidBrush(Color.Red), 0, 0, 100, 100);
        }

        private void button15_Click(object sender, EventArgs e)
        {

        }
    }

    /// <summary>
    /// HardDiskVal 的摘要說明。
    /// 讀取指定盤符的硬盤序列號
    /// 功能：讀取指定盤符的硬盤序列號
    /// </summary>
    public class HardDiskVal
    {
        [DllImport("kernel32.dll")]
        private static extern int GetVolumeInformation(
        string lpRootPathName,
        string lpVolumeNameBuffer,
        int nVolumeNameSize,
        ref int lpVolumeSerialNumber,
        int lpMaximumComponentLength,
        int lpFileSystemFlags,
        string lpFileSystemNameBuffer,
        int nFileSystemNameSize
        );

        /// <summary>
        /// 獲得盤符為drvID的硬盤序列號，缺省為C
        /// </summary>
        /// <param name="drvID"></param>
        /// <returns></returns>
        public string HDVal(string drvID)
        {
            const int MAX_FILENAME_LEN = 256;
            int retVal = 0;
            int a = 0;
            int b = 0;
            string str1 = null;
            string str2 = null;
            int i = GetVolumeInformation(
            drvID + @":/",
            str1,
            MAX_FILENAME_LEN,
            ref retVal,
            a,
            b,
            str2,
            MAX_FILENAME_LEN
            );
            return retVal.ToString();
        }

        public string HDVal()
        {
            const int MAX_FILENAME_LEN = 256;
            int retVal = 0;
            int a = 0;
            int b = 0;
            string str1 = null;
            string str2 = null;
            int i = GetVolumeInformation(
            "c://",
            str1,
            MAX_FILENAME_LEN,
            ref retVal,
            a,
            b,
            str2,
            MAX_FILENAME_LEN
            );
            return retVal.ToString();
        }
    }


}

