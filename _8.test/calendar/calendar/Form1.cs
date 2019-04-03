using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.IO;    //for Stream

using System.Management;    //for ManagementObjectSearcher

using System.Globalization; //for 民國 農曆


namespace calendar
{
    public partial class Form1 : Form
    {
        //天干
        private static string[] TianGan = { "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸" };

        //地支
        private static string[] DiZhi = { "子", "醜", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥" };

        //十二生肖
        private static string[] ShengXiao = { "鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬" };

        //農曆日期
        private static string[] DayName = {"*","初一","初二","初三","初四","初五",
"初六","初七","初八","初九","初十",
"十一","十二","十三","十四","十五",
"十六","十七","十八","十九","二十",
"廿一","廿二","廿三","廿四","廿五",
"廿六","廿七","廿八","廿九","三十"};

        //農曆月份
        private static string[] MonthName = { "*", "正", "二", "三", "四", "五", "六", "七", "八", "九", "十", "十一", "臘" };

        //西曆月計數天
        private static int[] MonthAdd = { 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334 };

        //農曆資料
        private static int[] LunarData = {2635,333387,1701,1748,267701,694,2391,133423,1175,396438
,3402,3749,331177,1453,694,201326,2350,465197,3221,3402
,400202,2901,1386,267611,605,2349,137515,2709,464533,1738
,2901,330421,1242,2651,199255,1323,529706,3733,1706,398762
,2741,1206,267438,2647,1318,204070,3477,461653,1386,2413
,330077,1197,2637,268877,3365,531109,2900,2922,398042,2395
,1179,267415,2635,661067,1701,1748,398772,2742,2391,330031
,1175,1611,200010,3749,527717,1452,2742,332397,2350,3222
,268949,3402,3493,133973,1386,464219,605,2349,334123,2709
,2890,267946,2773,592565,1210,2651,395863,1323,2707,265877};





        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            string lunar_date;
            lunar_date = GetLunarCalendar(dt);
            richTextBox1.Text += "result : " + lunar_date + "\n";
            

        }

        /// <summary>
        /// 獲取對應日期的農曆
        /// </summary>
        /// <param name="dtDay">西曆日期</param>
        /// <returns></returns>

        public string GetLunarCalendar(DateTime dtDay)
        {
            string sYear = dtDay.Year.ToString();
            string sMonth = dtDay.Month.ToString();
            string sDay = dtDay.Day.ToString();
            int year;
            int month;
            int day;
            try
            {
                year = int.Parse(sYear);
                month = int.Parse(sMonth);
                day = int.Parse(sDay);
            }
            catch
            {
                year = DateTime.Now.Year;
                month = DateTime.Now.Month;
                day = DateTime.Now.Day;
            }

            int nTheDate;
            int nIsEnd;
            int k, m, n, nBit, i;
            string calendar = string.Empty;
            //計算到初始時間1921年2月8日的天數：1921-2-8(正月初一)
            nTheDate = (year - 1921) * 365 + (year - 1921) / 4 + day + MonthAdd[month - 1] - 38;
            if ((year % 4 == 0) && (month > 2))
                nTheDate += 1;
            //計算天干，地支，月，日
            nIsEnd = 0;
            m = 0;
            k = 0;
            n = 0;
            while (nIsEnd != 1)
            {
                if (LunarData[m] < 4095)
                    k = 11;
                else
                    k = 12;
                n = k;
                while (n >= 0)
                {
                    //獲取LunarData[m]的第n個二進位位的值
                    nBit = LunarData[m];
                    for (i = 1; i < n + 1; i++)
                        nBit = nBit / 2;
                    nBit = nBit % 2;
                    if (nTheDate <= (29 + nBit))
                    {
                        nIsEnd = 1;
                        break;
                    }
                    nTheDate = nTheDate - 29 - nBit;
                    n = n - 1;
                }
                if (nIsEnd == 1)
                    break;
                m = m + 1;
            }
            year = 1921 + m;
            month = k - n + 1;
            day = nTheDate;
            //return year + "-" + month + "-" + day;

            if (k == 12)
            {
                if (month == LunarData[m] / 65536 + 1)
                    month = 1 - month;
                else if (month > LunarData[m] / 65536 + 1)
                    month = month - 1;
            }
            //年
            calendar = year + "年";
            //生肖
            calendar += ShengXiao[(year - 4) % 60 % 12].ToString() + "年 ";
            // //天干
            calendar += TianGan[(year - 4) % 60 % 10].ToString();
            // //地支
            calendar += DiZhi[(year - 4) % 60 % 12].ToString() + " ";

            //農曆月
            if (month < 1)
                calendar += "閏" + MonthName[-1 * month].ToString() + "月";
            else
                calendar += MonthName[month].ToString() + "月";

            //農曆日
            calendar += DayName[day].ToString() + "日";

            return calendar;
        }

        string[] SolarTerm = new string[] { 
            "小寒", "大寒", "立春", "雨水", 
            "驚蟄", "春分", "清明", "穀雨", 
            "立夏", "小滿", "芒種", "夏至", 
            "小暑", "大暑", "立秋", "處暑", 
            "白露", "秋分", "寒露", "霜降", 
            "立冬", "小雪", "大雪", "冬至" };

        string[] LunarHolDayName =
                  {
                  "小寒", "大寒", "立春", "雨水",
                  "驚蟄", "春分", "清明", "谷雨",
                  "立夏", "小滿", "芒種", "夏至",
                  "小暑", "大暑", "立秋", "處暑",
                  "白露", "秋分", "寒露", "霜降",
                  "立冬", "小雪", "大雪", "冬至"};

        private void button2_Click(object sender, EventArgs e)
        {
            foreach (string str in SolarTerm)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";

            foreach (string str in LunarHolDayName)
            {
                richTextBox1.Text += str + " ";
            }
            richTextBox1.Text += "\n";
        }


        public struct Mp3Info
        {
            public string identify;//TAG，三個位元組
            public string Title;//歌曲名,30個位元組
            public string Artist;//歌手名,30個位元組
            public string Album;//所屬唱片,30個位元組
            public string Year;//年,4個字元
            public string Comment;//注釋,28個位元組
            public char reserved1;//保留位，一個位元組
            public char reserved2;//保留位，一個位元組
            public char reserved3;//保留位，一個位元組
        }

        /// <summary>
        /// mp3類
        /// </summary>
        //public class clsMP3

        //C# 獲取MP3 資訊
            //所以，我們只要把MP3檔的最後128個位元組分段讀出來並保存到該結構裡就可以了。函式定義如下：
            private byte[] getLast128(string FileName)
            {
                FileStream fs = new FileStream(FileName, FileMode.Open, FileAccess.Read);
                Stream stream = fs;
                stream.Seek(-128, SeekOrigin.End);
                const int seekPos = 128;
                int rl = 0;
                byte[] Info = new byte[seekPos];
                rl = stream.Read(Info, 0, seekPos);
                fs.Close();
                stream.Close();
                return Info;
            }
            //再對上面返回的位元組陣列分段取出，並保存到Mp3Info結構中返回:
            private Mp3Info getMp3Info(byte[] Info)
            {
                Mp3Info mp3Info = new Mp3Info();
                string str = null;
                int i;
                int position = 0;//迴圈的起始值
                int currentIndex = 0;//Info的當前索引值
                //獲取TAG標識(陣列前3個)
                for (i = currentIndex; i < currentIndex + 3; i++)
                {
                    str = str + (char)Info[i];
                    position++;
                }
                currentIndex = position;
                mp3Info.identify = str;
                //獲取歌名（陣列3-32）
                str = null;
                byte[] bytTitle = new byte[30];//將歌名部分讀到一個單獨的陣列中
                int j = 0;
                for (i = currentIndex; i < currentIndex + 30; i++)
                {
                    bytTitle[j] = Info[i];
                    position++;
                    j++;
                }
                currentIndex = position;
                mp3Info.Title = this.byteToString(bytTitle);
                //獲取歌手名（陣列33-62）
                str = null;
                j = 0;
                byte[] bytArtist = new byte[30];//將歌手名部分讀到一個單獨的陣列中
                for (i = currentIndex; i < currentIndex + 30; i++)
                {
                    bytArtist[j] = Info[i];
                    position++;
                    j++;
                }
                currentIndex = position;
                mp3Info.Artist = this.byteToString(bytArtist);
                //獲取唱片名（陣列63-92）
                str = null;
                j = 0;
                byte[] bytAlbum = new byte[30];//將唱片名部分讀到一個單獨的陣列中
                for (i = currentIndex; i < currentIndex + 30; i++)
                {
                    bytAlbum[j] = Info[i];
                    position++;
                    j++;
                }
                currentIndex = position;
                mp3Info.Album = this.byteToString(bytAlbum);
                //獲取年 （陣列93-96）
                str = null;
                j = 0;
                byte[] bytYear = new byte[4];//將年部分讀到一個單獨的陣列中
                for (i = currentIndex; i < currentIndex + 4; i++)
                {
                    bytYear[j] = Info[i];
                    position++;
                    j++;
                }
                currentIndex = position;
                mp3Info.Year = this.byteToString(bytYear);
                //獲取注釋（陣列97-124）
                str = null;
                j = 0;
                byte[] bytComment = new byte[28];//將注釋部分讀到一個單獨的陣列中
                for (i = currentIndex; i < currentIndex + 25; i++)
                {
                    bytComment[j] = Info[i];
                    position++;
                    j++;
                }
                currentIndex = position;
                mp3Info.Comment = this.byteToString(bytComment);
                //以下獲取保留位（陣列125-127）
                mp3Info.reserved1 = (char)Info[++position];
                mp3Info.reserved2 = (char)Info[++position];
                mp3Info.reserved3 = (char)Info[++position];

                richTextBox1.Text += "Title = " + mp3Info.Title + "\n";
                richTextBox1.Text += "Artist = " + mp3Info.Artist + "\n";
                richTextBox1.Text += "Album = " + mp3Info.Album + "\n";
                richTextBox1.Text += "Year = " + mp3Info.Year + "\n";
                richTextBox1.Text += "Comment = " + mp3Info.Comment + "\n";
                richTextBox1.Text += "identify = " + mp3Info.identify + "\n";
                richTextBox1.Text += "reserved1 = " + mp3Info.reserved1 + "\n";
                richTextBox1.Text += "reserved2 = " + mp3Info.reserved2 + "\n";
                richTextBox1.Text += "reserved3 = " + mp3Info.reserved3 + "\n";

                return mp3Info;
            }


            //上面程式用到下面的方法：
            /// <summary>
            /// 將位元組陣列轉換成字串
            /// </summary>
            /// <param name = "b">位元組陣列</param>
            /// <returns>返回轉換後的字串</returns>
            private string byteToString(byte[] b)
            {
                //Encoding enc = Encoding.GetEncoding("GB2312");
                //Encoding enc = Encoding.GetEncoding("Big5");
                //Encoding enc = Encoding.GetEncoding("utf-8");
                Encoding enc = Encoding.GetEncoding("GB2312");

                string str = enc.GetString(b);
                //str = str.Substring(0, str.IndexOf('\0') >= 0 ? str.IndexOf('\0') : str.Length);//去掉無用字元
                return str;
            }


        private void button3_Click(object sender, EventArgs e)
        {

            //string filename = @"C:\______test_vcs\aaaa.mp3";
            string filename = @"C:\______test_vcs\07    都はろみ--妻戀道中(他鄉思妻兒).mp3";
            richTextBox1.Text += "filename = " + filename + "\n";
            getMp3Info(getLast128(filename));




        }

        private void Form1_Load(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
        }

        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            /*
            //monthCalendar1.Visible = false;
            label1.Text = monthCalendar1.TodayDate.Year.ToString();
            label1.Text += "/" + monthCalendar1.TodayDate.Month.ToString();
            label1.Text += "/" + monthCalendar1.TodayDate.Day.ToString();


            label1.Text += " " + DateTime.Now.Hour;
            label1.Text += ":" + DateTime.Now.Minute;
            label1.Text += ":" + DateTime.Now.Second;
            */


        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            label1.Text = dateTimePicker1.Value.Year.ToString();
            label1.Text += "/" + dateTimePicker1.Value.Month.ToString();
            label1.Text += "/" + dateTimePicker1.Value.Day.ToString();


            label1.Text += " " + DateTime.Now.Hour;
            label1.Text += ":" + DateTime.Now.Minute;
            label1.Text += ":" + DateTime.Now.Second;

        }

        private void button5_Click(object sender, EventArgs e)
        {
            string text = "測試一下";
            byte[] byt = System.Text.UnicodeEncoding.Unicode.GetBytes(text);
            richTextBox1.Text += System.Text.UnicodeEncoding.Unicode.GetString(byt) + "\n";

            //如果要自行指定BIG5編碼的話:
            string text2 = "測試一下";
            byte[] byt2 = System.Text.Encoding.GetEncoding("Big5").GetBytes(text2);
            richTextBox1.Text += System.Text.Encoding.GetEncoding("Big5").GetString(byt2) + "\n";

        }

        private void button6_Click(object sender, EventArgs e)
        {
            /*
            C# 調用WMI

            第一步：加入參考
            專案→加入參考→.Net→System.Management
            第二步：引用命名空間
            using System.Management;
            第三步：調用WMI Class
            1：類別實體化
            例：
              ManagementClass mClass = new ManagementClass("Win32_Share");
            2：引用類別方法(Methods)
              例1：
              ManagementBaseObject mMethod = mClass.GetMethodParameters("Create");
            */

            /*
            1. 專案請先加入參考 System.Management
            2. 透過 ManagementObjectSearcher 查詢 
            */

            // 透過 ManagementObjectSearcher 類別用類似 SQL 的語法查詢

            ManagementObjectSearcher wmiSearcher
                        = new ManagementObjectSearcher("SELECT * FROM Win32_Processor");

            int i = 0;



            // 使用 ManagementObjectSearcher 的 Get 方法取得所有集合

            foreach (ManagementObject obj in wmiSearcher.Get())
            {

                // 取得CPU 序號

                //Console.WriteLine("CPU{0} ID:\t{1}", i++, obj["ProcessorId"].ToString());
                richTextBox1.Text += "CPU [" + i.ToString() + "] ID : " + obj["ProcessorId"].ToString() + "\n";
                i++;

            }


            // 或透過 ManagementObject 類別直接存取特定 CPU 序號

            ManagementObject wmiObj = new ManagementObject("Win32_Processor.DeviceID='CPU0'");
            //Console.WriteLine("CPU{0} ID:\t{1}", 0, wmiObj.GetPropertyValue("ProcessorId").ToString());
            richTextBox1.Text += "CPU [0] ID : " + wmiObj.GetPropertyValue("ProcessorId").ToString() + "\n";


        }

        private void button7_Click(object sender, EventArgs e)
        {

            DateTime dd = new DateTime(2006, 3, 11);
            TaiwanCalendar tc = new TaiwanCalendar();


            int year = tc.GetYear(dd);

            int month = tc.GetMonth(dd);

            int dayOfMonth = tc.GetDayOfMonth(dd);             //日

            int daysInMonth = tc.GetDaysInMonth(year, month);   //整個月的天數

            richTextBox1.Text += "民國" + year.ToString() + "年" + month.ToString() + "月" + dayOfMonth.ToString() + "日\n";


            TaiwanLunisolarCalendar tlc = new TaiwanLunisolarCalendar();

            // 取得目前支援的農曆日曆到幾年幾月幾日( 2051-02-10 )
            tlc.MaxSupportedDateTime.ToShortDateString();

            // 取得今天的農曆年月日
            /*
            txtContent.Text =
            tlc.GetYear(DateTime.Now).ToString() + "-" +
            tlc.GetMonth(DateTime.Now).ToString() + "-" +
            tlc.GetDayOfMonth(DateTime.Now).ToString();
            */
            richTextBox1.Text += "農曆" + tlc.GetYear(DateTime.Now).ToString() + "年" + tlc.GetMonth(DateTime.Now).ToString() + "月" + tlc.GetDayOfMonth(DateTime.Now).ToString() + "日\n";


        }



    }
}
