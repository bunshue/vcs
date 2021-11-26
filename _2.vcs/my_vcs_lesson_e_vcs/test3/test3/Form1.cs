using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Net;
using System.Xml;
using System.Xml.Linq;
using System.Management;
using System.Diagnostics;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;

using System.IO;
using System.IO.Ports;
using System.Threading;
using System.Reflection;    //for Assembly
using System.Security;
using System.Security.Cryptography;

using Shell32;
using Microsoft.Win32;  //for Registry

namespace test3
{
    public partial class Form1 : Form
    {
        /// <summary>
        /// 操作系統關閉時，關閉應用程序
        /// </summary>
        /// <param name="m">截獲系統消息</param>
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case 0x0011://WM_QUERYENDSESSION
                    //m.Result = (IntPtr)1;
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    richTextBox1.Text += "截獲作業系統關閉時發出的訊息\n";
                    break;
                default:
                    base.WndProc(ref m);
                    break;
            }
        }
        /*
        做了一個定時播放器,程序運行時最小化到任務欄托盤,可這時候關閉或重啟操作系統使如果程序沒有退出,
        則系統不能關閉.那麼如何實現關機時自動退出程序呢?其實很簡單,當windows操作系統執行關閉動作時,
        它會發送給各個正在運行的應用程序一個消息WM_QUERYENDSESSION,告訴應用程序要關機了,如果反饋回來的消息值為1,
        那麼windows操作系統就會自動關閉.因此,通過截獲WM_QUERYENDSESSION消息,就能實現自動退出程序.
        */


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

            label1.Location = new Point(x_st + dx * 2, y_st + dy * 0 + 15);
            pictureBox1.Location = new Point(x_st + dx * 3 + 100, y_st + dy * 0);

            richTextBox1.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            //控件位置
            bt_exit.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_exit.Size.Width, richTextBox1.Location.Y + 0);

            //控件位置
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //獲取文件的版本信息:
            string filename = @"C:\______test_files\_material\AForge.Video.dll";

            FileVersionInfo myFileVersionInfo1 = FileVersionInfo.GetVersionInfo(filename);
            richTextBox1.Text += "版本號: " + myFileVersionInfo1.FileVersion + "\n";

        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "今天是 : " + GetCnWeek() + "\n";
        }

        /// <summary>
        /// 獲得中文星期名稱
        /// </summary>
        /// <returns></returns>
        public static string GetCnWeek()
        {
            switch (DateTime.Now.DayOfWeek)
            {
                case DayOfWeek.Monday:
                    return "星期一";
                case DayOfWeek.Tuesday:
                    return "星期二";
                case DayOfWeek.Wednesday:
                    return "星期三";
                case DayOfWeek.Thursday:
                    return "星期四";
                case DayOfWeek.Friday:
                    return "星期五";
                case DayOfWeek.Saturday:
                    return "星期六";
                case DayOfWeek.Sunday:
                    return "星期日";
                default:
                    return "星期一";
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            //獲取百度首頁生成靜態文件
            this.DownUrltoFile("http://www.baidu.com", "baidu.htm", "GB2312");

            //DownUrltoFile("http://www.xueit.com/show.aspx?pid=1", "html/news/20091224-001.html", "GB2312");
            //其中URL：http://www.xueit.com/show.aspx?pid=1 是动态显示文章，html/news/20091224-001.html是表字段htmlFile预先保存的文件名，这样就可以生成静态文件了。

        }

        /// 獲取遠程URL並生成文件的代碼：
        /// <summary>
        /// 生成網頁文件
        /// </summary>
        /// <param name="url">遠程URL</param>
        /// <param name="filename">生成文件名路徑</param>
        /// <param name="pagecode">目標URL頁面編碼</param>
        protected void DownUrltoFile(string url, string filename, string pagecode)
        {
            try
            {
                //編碼
                Encoding encode = Encoding.GetEncoding(pagecode);
                //請求URL
                HttpWebRequest req = (HttpWebRequest)WebRequest.Create(url);
                //設置超時(10秒)
                req.Timeout = 10000;
                //this.NotFolderIsCreate(filename);
                //獲取Response
                HttpWebResponse rep = (HttpWebResponse)req.GetResponse();
                //創建StreamReader與StreamWriter文件流對象
                StreamReader sr = new StreamReader(rep.GetResponseStream(), encode);
                StreamWriter sw = new StreamWriter(filename, false, encode);
                //寫入內容
                sw.Write(sr.ReadToEnd());
                //清理當前緩存區，並將緩存寫入文件
                sw.Flush();
                //釋放相關對象資源
                sw.Close();
                sw.Dispose();
                sr.Close();
                sr.Dispose();
                //Response.Write("生成文件"   filename   "成功");
            }
            catch (Exception ex)
            {
                //Response.Write("生成文件"   filename   "失敗，原因："   ex.Message);
            }
        }

        //以上代碼關鍵知識點，通過HttpWebRequest、HttpWebResponse請求獲取遠程URL數據，之後使用StreamReader、StreamWriter文件流讀寫數據寫入文件，注意還有編碼Encoding。

        /*
        /// <summary>
        /// 文件夾不存在則創建
        /// </summary>
        /// <param name="filename">文件名所在路徑</param>
        protected void NotFolderIsCreate(string filename)
        {
            string fileAtDir = Server.MapPath(Path.GetDirectoryName(filename));
            if (!Directory.Exists(fileAtDir))
                Directory.CreateDirectory(fileAtDir);
        }
        */

        private void button3_Click(object sender, EventArgs e)
        {
            HardDiskVal hdv = new HardDiskVal();
            string result = hdv.HDVal();
            richTextBox1.Text += "獲取硬盤序列號 : " + result + "\n";
        }

        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += CaculateWeekDay(2021, 10, 28);
        }

        /*
        C#實現的根據年月日計算星期幾的函數

        基姆拉爾森計算公式

        W= (d 2*m 3*(m 1)/5 y y/4-y/100 y/400) mod 7

        在公式中d表示日期中的日數，m表示月份數，y表示年數。注意：在公式中有個與其他公式不同的地方：把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10則換算成：2003-13-10來代入公式計算。
        */

        //y－年，m－月，d－日期
        string CaculateWeekDay(int y, int m, int d)
        {
            if (m == 1) m = 13;
            if (m == 2) m = 14;
            int week = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7 + 1;

            string weekstr = "";
            switch (week)
            {
                case 1: weekstr = "星期一"; break;
                case 2: weekstr = "星期二"; break;
                case 3: weekstr = "星期三"; break;
                case 4: weekstr = "星期四"; break;
                case 5: weekstr = "星期五"; break;
                case 6: weekstr = "星期六"; break;
                case 7: weekstr = "星期日"; break;
            } return weekstr;
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //獲取硬盤相應序列號
            string result = clsIDE.GetAllSerialNumber();
            richTextBox1.Text += "獲取硬盤序列號 : " + result + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //WMI 使用
            SelectQuery query = new SelectQuery("Select * From Win32_LogicalDisk");
            ManagementObjectSearcher searcher = new ManagementObjectSearcher(query);

            foreach (ManagementBaseObject disk in searcher.Get())
            {
                richTextBox1.Text += disk["Name"] + " " + disk["DriveType"] + " " + disk["VolumeName"] + "\n";
            }
            /*
            disk["DriveType"] 的返回值意義如下:

            1 No type
            2 Floppy disk
            3 Hard disk
            4 Removable drive or network drive
            5 CD-ROM
            6 RAM disk
            */


            //3、如何用WMI獲得指定磁盤的容量？	  TBD

            //"win32_logicaldisk.deviceid=/"c:/"");
            /*
            ManagementObject disk2 = new ManagementObject("win32_logicaldisk.deviceid=C://");
            disk2.Get();
            Console.WriteLine("Logical Disk Size = " + disk2["Size"] + " bytes");
            */


            ManagementClass diskClass = new ManagementClass("Win32_LogicalDisk");
            ManagementObjectCollection disks = diskClass.GetInstances();
            ManagementObjectCollection.ManagementObjectEnumerator disksEnumerator = disks.GetEnumerator();
            while (disksEnumerator.MoveNext())
            {
                ManagementObject disk = (ManagementObject)disksEnumerator.Current;
                richTextBox1.Text += "Disk found: " + disk["deviceid"] + "\n";
            }

            richTextBox1.Text += "列出機器中所有的共享資源\n";
            ManagementObjectSearcher searcher2 = new ManagementObjectSearcher("SELECT * FROM Win32_share");
            foreach (ManagementObject share in searcher2.Get())
            {
                richTextBox1.Text += share.GetText(TextFormat.Mof) + "\n";
            }
        }

        private void button8_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "主機名稱：" + System.Net.Dns.GetHostName() + "\n";

            richTextBox1.Text += "IP地址：" + getIPAddress() + "\n";


            //本機mac地址

            string mac = "";
            ManagementClass mc = new ManagementClass("Win32_NetworkAdapterConfiguration");
            ManagementObjectCollection moc = mc.GetInstances();

            foreach (ManagementObject mo in moc)
            {
                if ((bool)mo["IPEnabled"])
                {
                    mac = mo["MacAddress"].ToString();

                    //本機MAC
                    richTextBox1.Text += "本機MAC：" + mac + "\n";
                }
            }
        }

        private static string getIPAddress()
        {
            System.Net.IPAddress addr;
            // 獲得本機局域網IP地址
            addr = new System.Net.IPAddress(Dns.GetHostByName(Dns.GetHostName()).AddressList[0].Address);
            return addr.ToString();
        }

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
        private void button9_Click(object sender, EventArgs e)
        {
            //useless
            //設定音量1 winm
            SetVol1(a);

            a += 10;
        }

        //設定音量2
        private void button10_Click(object sender, EventArgs e)
        {
            //設定音量2 user32
            SetVol2();
        }

        //設定音量1, 2  SP

        private void button11_Click(object sender, EventArgs e)
        {
            string result = appInfo();
            richTextBox1.Text += result + "\n";
        }

        public static string appInfo()
        {
            Assembly assembly = Assembly.GetExecutingAssembly();
            FileVersionInfo fvi = FileVersionInfo.GetVersionInfo(assembly.Location);
            string result = "File Version: " + fvi.FileVersion
                + Environment.NewLine + "Company Name: " + fvi.CompanyName
                + Environment.NewLine + "Comments: " + fvi.Comments
                + Environment.NewLine + "Product Name: " + fvi.ProductName
                + Environment.NewLine + "Copyright: " + fvi.LegalCopyright
                + Environment.NewLine + "File Name: " + fvi.FileName
                + Environment.NewLine + "Original File Name: " + fvi.OriginalFilename
                + Environment.NewLine + "Product Version: " + fvi.ProductVersion
                + Environment.NewLine + "Special build: " + fvi.SpecialBuild
                + Environment.NewLine + "" + fvi.CompanyName;
            return result;
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //html轉txt
            //http://www.aspphp.online/bianchen/dnet/cxiapu/cxprm/201701/184774.html
        }

        /// C#過濾html標簽
        /// 用正則表達式來做html轉txt
        public static string Html2Text(string htmlStr)
        {
            if (String.IsNullOrEmpty(htmlStr))
            {
                return "";
            }
            string regEx_style = "<style[^>]*?>[\\s\\S]*?<\\/style>"; //定義style的正則表達式
            string regEx_script = "<script[^>]*?>[\\s\\S]*?<\\/script>"; //定義script的正則表達式
            string regEx_html = "<[^>]+>"; //定義HTML標簽的正則表達式
            htmlStr = Regex.Replace(htmlStr, regEx_style, "");//刪除css
            htmlStr = Regex.Replace(htmlStr, regEx_script, "");//刪除js
            htmlStr = Regex.Replace(htmlStr, regEx_html, "");//刪除html標記
            htmlStr = Regex.Replace(htmlStr, "\\s*|\t|\r|\n", "");//去除tab、空格、空行
            htmlStr = htmlStr.Replace(" ", "");
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            htmlStr = htmlStr.Replace("\"", ""); //去除異常的引號" " "
            return htmlStr.Trim();
        }

        // 顏色模板
        //  黑、白、紅、綠、藍、黃/ 棕 、灰
        private const int BLACK = 0;
        private const int WHITE = 1;
        private const int RED1 = 2;
        private const int RED2 = 3;
        private const int GREEN1 = 4;
        private const int GREEN2 = 5;
        private const int BLUE1 = 6;
        private const int BLUE2 = 7;
        private const int YELLOW1 = 8;
        private const int YELLOW2 = 9;
        private const int BROWN = 10;
        private const int GRAY = 11;

        private void button13_Click(object sender, EventArgs e)
        {
            //顯示顏色
            int[,] colorVelue = null;
            colorVelue = new int[,] {
            {50,50,50},    //黑
            {255,255,255},  //白
            {240,80,80}, //紅小
            {240,160,160},  //紅大
            {60,180,60}, //綠小
            {160,240,160},  //綠大
            {80,80,240}, //藍小
            {160,160,240},  //藍大
            {240,190,80}, //黃小
            {240,240,160},  //黃大
            {205,133,63},   //棕/褐
            //{162,162,162},//灰，特殊
            };

            int total_colors = colorVelue.GetUpperBound(0) + 1;
            richTextBox1.Text += "total_colors = " + total_colors.ToString() + "\n";

            int i;
            for (i = 0; i < total_colors; i++)
            {
                switch (i)
                {
                    case -1:
                        richTextBox1.Text += "無此色\n";
                        break;
                    case 0:
                        richTextBox1.Text += "黑\n";
                        break;
                    case 1:
                        richTextBox1.Text += "白\n";
                        break;
                    case 2:
                        richTextBox1.Text += "紅\n";
                        break;
                    case 3:
                        richTextBox1.Text += "紅\n";
                        break;
                    case 4:
                        richTextBox1.Text += "綠\n";
                        break;
                    case 5:
                        richTextBox1.Text += "綠\n";
                        break;
                    case 6:
                        richTextBox1.Text += "藍\n";
                        break;
                    case 7:
                        richTextBox1.Text += "藍\n";
                        break;
                    case 8:
                        richTextBox1.Text += "黃\n";
                        break;
                    case 9:
                        richTextBox1.Text += "黃\n";
                        break;
                    case 10:
                        richTextBox1.Text += "棕\n";
                        break;
                    case 11:
                        richTextBox1.Text += "灰\n";
                        break;
                    default:
                        richTextBox1.Text += "其他\n";
                        break;
                }

                int R = colorVelue[i, 0];
                int G = colorVelue[i, 1];
                int B = colorVelue[i, 2];
                richTextBox1.Text += "show color " + i.ToString() + " " + R.ToString() + " " + G.ToString() + " " + B.ToString() + "\n";

                pictureBox1.BackColor = Color.FromArgb(R, G, B);
                Application.DoEvents();
                Thread.Sleep(1000);

            }

        }


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


        private void button14_Click(object sender, EventArgs e)
        {
            //取得Windows版本

            richTextBox1.Text += " Passing OSVersionInfo as class\n";

            OSVersionInfo osvi = new OSVersionInfo();
            osvi.OSVersionInfoSize = Marshal.SizeOf(osvi);


            LibWrap.GetVersionEx(osvi);

            Console.WriteLine("Class size: {0} Operation System : {1} Pack: {2}", osvi.OSVersionInfoSize, OpSysName(osvi.MajorVersion, osvi.MinorVersion, osvi.PlatformId), osvi.versionString);
            Console.WriteLine("{0}", osvi.PlatformId);

            richTextBox1.Text += " Passing OSVersionInfo as struct\n";

            OSVersionInfo2 osvi2 = new OSVersionInfo2();
            osvi2.OSVersionInfoSize = Marshal.SizeOf(osvi2);

            LibWrap.GetVersionEx2(ref osvi2);
            Console.WriteLine("Static size: {0} Operation System : {1} Pack: {2}", osvi2.OSVersionInfoSize, OpSysName(osvi2.MajorVersion, osvi2.MinorVersion, osvi2.PlatformId), osvi2.versionString);
        }

        private void button15_Click(object sender, EventArgs e)
        {
            //取得Windows版本
            string version = OSInfoMation.GetOsVersion();
            richTextBox1.Text += version + "\n";
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Close();
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            MyTempImage myTempImage = new MyTempImage();

            //myTempImage.CreateImage();
            pictureBox1.Image = Image.FromFile(myTempImage.CreateImage());



            //string thefullname = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + ".gif"; // "nowtime.gif";
            //richTextBox1.Text += thefullname + "\n";
        }
    }

    public class MyTempImage
    {
        public string CreateImage()
        {
            string str = DateTime.Now.ToString();
            Bitmap image = new Bitmap(200, 30);
            Graphics g = Graphics.FromImage(image);
            string thefullname = DateTime.Now.ToString("yyyy-MM-dd HH-mm-ss") + ".gif"; // "nowtime.gif";

            g.Clear(Color.White);
            g.DrawString(str, new Font("CourIEr New", 10), new SolidBrush(Color.Red), 20, 5);
            //Graphics 類還有很多繪圖方法可以繪制 直線、曲線、圓等等 
            image.Save(thefullname, System.Drawing.Imaging.ImageFormat.Gif);
            return thefullname;
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

    /// <summary>
    /// Summary description for clsIDE.
    /// </summary>
    public class clsIDE
    {
        /// <summary>
        /// 獲取硬盤相應分區的序列號
        /// </summary>
        /// <returns></returns>
        public static string GetAllSerialNumber()
        {
            string Dri = "";

            System.Management.ManagementClass mo = new System.Management.ManagementClass("Win32_LogicalDisk");

            System.Management.ManagementObjectCollection mc = mo.GetInstances();

            foreach (System.Management.ManagementObject m in mc)
            {
                if (Convert.ToString(m.Properties["DriveType"].Value) == "3")
                {
                    Dri = Dri + m.Properties["VolumeSerialNumber"].Value.ToString() + "/n";
                }
            }

            Dri = Dri.Substring(0, Dri.Length - 1);

            return Dri;
        }

        /// <summary>
        /// 獲取硬盤相應分區的序列號
        /// </summary>
        /// <param name="Drive">盤符（如 C）</param>
        /// <returns></returns>
        public static string GetSpecialVolumeSerialNumber(string Drive)
        {
            string Dri = "";

            System.Management.ManagementClass mo = new System.Management.ManagementClass("Win32_LogicalDisk");

            System.Management.ManagementObjectCollection mc = mo.GetInstances();

            foreach (System.Management.ManagementObject m in mc)
            {
                if (Convert.ToString(m.Properties["DriveType"].Value) == "3")
                {
                    if (m.Properties["Name"].Value.ToString().ToUpper().Trim().Substring(0, 1) == Drive.ToUpper().Trim())
                    {
                        Dri = Dri + m.Properties["VolumeSerialNumber"].Value.ToString();

                        break;
                    }
                }
            }

            return Dri;
        }
    }

    public class OSInfoMation
    {
        public static string OSBit()
        {
            try
            {
                ConnectionOptions oConn = new ConnectionOptions();
                System.Management.ManagementScope managementScope = new System.Management.ManagementScope("\\\\localhost", oConn);
                System.Management.ObjectQuery objectQuery = new System.Management.ObjectQuery("select AddressWidth from Win32_Processor");
                ManagementObjectSearcher moSearcher = new ManagementObjectSearcher(managementScope, objectQuery);
                ManagementObjectCollection moReturnCollection = null;
                string addressWidth = null;
                moReturnCollection = moSearcher.Get();
                foreach (ManagementObject oReturn in moReturnCollection)
                {
                    addressWidth = oReturn["AddressWidth"].ToString();
                } //www.heatpress123.net
                return addressWidth;
            }
            catch
            {
                return "獲取錯誤";
            }
        }

        public static string GetOsVersion()
        {
            string osBitString = OSBit();
            string osVersionString = Environment.OSVersion.ToString();
            return string.Format(@"系統：{0}。位：{1}", osVersionString, osBitString);
        }
    }

}

