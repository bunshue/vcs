using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Diagnostics;  // for Stopwatch
using System.Collections;  // for IEnumerable
using System.Globalization;  // for CultureInfo, TaiwanCalendar, TaiwanLunisolarCalendar, 民國記年 農曆   //for DateTimeStyles
using Microsoft.VisualBasic;  // for DateAndTime, 需要 參考/加入參考/.NET/Microsoft.VisualBasic

// DateTime範圍 AD 0001/1/1 00:00:00 ~ 9999/12/31 23:59:59, 無法處理西元前的時間
// 時間值是以刻度（Tick）為最小單位, 每個 Tick 等於 100 奈秒, 就是一秒有1千萬個Ticks
// Tick 值由 0001/1/1 12:00:00 AM 開始累加計算, 每 100 奈秒, Tick 值加一

/* DateTime 的方法
DateTime.Now
DateTime.Now.Date
DateTime.Now.Ticks;
DateTime.Now.DayOfWeek
DateTime.Today
DateTime.Today.DayOfWeek
DateTime.MinValue  // vcs史上最早時間
DateTime.MaxValue  // vcs史上最晚時間
DateTime.Parse()
DateTime.ParseExact()
DateTime.TryParse()
DateTime.TryParseExact()
DateTime.IsLeapYear()
DateTime.Compare()
DateTime.DaysInMonth()  // 某個月的天數
DateTime.FromOADate()
*/

namespace vcs_test_all_01_DateTime
{
    public partial class Form1 : Form
    {
        DateTime bootup_time = DateTime.Now;  // 程式啟動時間

        DateTime LoginTime = DateTime.Now;
        DateTime dt_timer_st = DateTime.Now;
        DateTime dtTarget;

        string string_datetime1 = "3/11/2006 9:15:30 AM";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            //------------------------------------------------------------  # 60個

            LoginTime = DateTime.Now; //取得目前登入的時間
            richTextBox1.Text += "登入時間 : " + LoginTime.ToString() + "\n";

            timer1.Interval = 1000;
            timer1.Enabled = true;

            DateTime dt = DateTime.Now;
            this.ShowMoon(dt.Year, dt.Month, dt.Day);

            //設定倒數計時
            //dtTarget = DateTime.Now.AddHours(2);  //設定兩小時後
            dtTarget = new DateTime(2026, 9, 30, 12, 0, 0);   //設定特定時間
            timer_countdown.Start();
        }

        void show_item_location()
        {
            //button
            int x_st = 10;
            int y_st = 10;
            int dx = 200 + 10;
            int dy = 60 + 10;
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
            comboBox1.Location = new Point(x_st + dx * 1, y_st + dy * 9);
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

            groupBox13.Size = new Size(300, 200);
            groupBox13.Location = new Point(x_st + dx * 3, y_st + dy * 0);  // 月相

            groupBox9.Size = new Size(300, 360);
            groupBox9.Location = new Point(x_st + dx * 3, y_st + dy * 3);  // Timer顯示時間

            richTextBox1.Size = new Size(520, 690);
            richTextBox1.Location = new Point(x_st + dx * 4 + 100, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            lb_time.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 10);

            this.Size = new Size(1500, 750);
            this.Text = "vcs_test_all_01_DateTime";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        //------------------------------------------------------------  # 60個

        private void button0_Click(object sender, EventArgs e)
        {
            //各種建立DateTime物件的方法
            //DateTime dt = DateTime.Now;
            //DateTime dt = new DateTime(年, 月, 日);  // 指定時間, 年月日
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒);  // 指定時間, 年月日時分秒
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒, 毫秒);  // 指定時間, 年月日時分秒毫秒
            //DateTime dt = DateTime.Parse(string_datetime1);

            DateTime dt = DateTime.Now;
            DateTime dt2 = new DateTime(2025, 12, 25);  // 指定時間, 年月日
            DateTime dt3 = new DateTime(2019, 11, 22, 12, 34, 56);  // 指定時間, 年月日時分秒
            DateTime dt4 = new DateTime(2037, 12, 30, 12, 34, 56, 15);  // 指定時間, 年月日時分秒毫秒
            DateTime dt5 = new DateTime(2006, 03, 11, 09, 15, 23, 34);  // 指定時間, 年月日時分秒毫秒

            richTextBox1.Text += "當前時間 :\n";
            richTextBox1.Text += "時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "現在日期 : " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "現在時間 : " + dt.ToLongTimeString() + "\n";
            richTextBox1.Text += "ToLongDateString : " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "ToLongTimeString : " + dt.ToLongTimeString() + "\n";
            richTextBox1.Text += "ToShortDateString : " + dt.ToShortDateString() + "\n";
            richTextBox1.Text += "ToShortTimeString : " + dt.ToShortTimeString() + "\n";
            richTextBox1.Text += dt.ToFileTime().ToString() + "\n";
            richTextBox1.Text += dt.ToFileTimeUtc().ToString() + "\n";
            richTextBox1.Text += dt.ToLocalTime().ToString() + "\n";
            richTextBox1.Text += dt.ToOADate().ToString() + "\n";
            richTextBox1.Text += dt.ToShortDateString().ToString() + "\n";
            richTextBox1.Text += dt.ToShortTimeString().ToString() + "\n";
            richTextBox1.Text += dt.ToUniversalTime().ToString() + "\n";
            richTextBox1.Text += "全部格式4 : " + dt.ToBinary().ToString() + "\n";

            richTextBox1.Text += "當前是否公曆閏年 : " + DateTime.IsLeapYear(dt.Year) + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "全部日期 : " + dt.ToString() + "\n";
            richTextBox1.Text += "D\t完整日期 : " + dt.ToString("D") + "\n";
            richTextBox1.Text += "d\t簡短日期 : " + dt.ToString("d") + "\n";
            richTextBox1.Text += "F\t完整日期及時間 : " + dt.ToString("F") + "\n";
            richTextBox1.Text += "G\t一般日期 : " + dt.ToString("G") + "\n";
            richTextBox1.Text += dt.ToString("g") + "\n";
            richTextBox1.Text += "Y\t年月格式 : " + dt.ToString("Y") + "\n";
            richTextBox1.Text += dt.ToString("y") + "\n";
            richTextBox1.Text += "M\t月日格式 : " + dt.ToString("M") + "\n";
            richTextBox1.Text += dt.ToString("m") + "\n";
            richTextBox1.Text += "T\t完整時間 : " + dt.ToString("T") + "\n";
            richTextBox1.Text += "t\t簡短時間 : " + dt.ToString("t") + "\n";
            richTextBox1.Text += "簡短日期時間 : " + dt.ToString("f") + "\n";

            richTextBox1.Text += dt.ToString("R") + "\n";
            richTextBox1.Text += dt.ToString("r") + "\n";
            richTextBox1.Text += dt.ToString("U") + "\n";
            richTextBox1.Text += dt.ToString("u") + "\n";

            richTextBox1.Text += dt.ToString("O") + "\n";
            richTextBox1.Text += dt.ToString("o") + "\n";

            richTextBox1.Text += dt.ToString("s") + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "Now : " + DateTime.Now + "\n";
            richTextBox1.Text += "Today : " + DateTime.Today + "\n";//當天時間

            richTextBox1.Text += "Date : " + dt.Date.ToString() + "\n";

            richTextBox1.Text += "年 : " + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月 : " + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日 : " + dt.Day.ToString() + "\n";
            richTextBox1.Text += "天 : " + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "英文星期名稱 : " + dt.DayOfWeek + "\n";
            richTextBox1.Text += "星 : " + dt.DayOfWeek.ToString() + "\n";  // 星期幾
            richTextBox1.Text += "時 : " + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分 : " + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒 : " + dt.Second.ToString() + "\n";
            richTextBox1.Text += "毫秒 : " + dt.Millisecond.ToString() + "\n";
            richTextBox1.Text += "Ticks : " + dt.Ticks.ToString() + "\n";
            richTextBox1.Text += "TimeOfDay : " + dt.TimeOfDay.ToString() + "\n";
            richTextBox1.Text += "日期 1 : " + dt.Date.ToString() + "\n";//2005-11-5 0:00:00

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //yyyymmdd用法
            //DateTime轉字串需顯示毫秒
            //DateTime.ToString("yyyyMMddhhmmssfff")，fff 格式包含毫秒值中任何結尾的零。
            richTextBox1.Text += "顯示毫秒 : " + dt.ToString("yyyy_MMdd_hhmmss.fff") + "\n";
            richTextBox1.Text += "日期 : " + dt.ToString("yyyy-MM-dd") + "\n";

            richTextBox1.Text += dt.ToString("yyyy/MM/dd", DateTimeFormatInfo.InvariantInfo) + "\n";
            richTextBox1.Text += dt.ToString("yyyy年MM月dd日") + "\n";

            richTextBox1.Text += "現在時間 :\n";
            richTextBox1.Text += dt.ToString("hh:mm:ss.fff") + "\n";
            richTextBox1.Text += dt.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
            richTextBox1.Text += dt.ToString("yyyy-MM-dd HH:mm:ss") + "\n";
            richTextBox1.Text += dt.ToString("yyyy" + '-' + "MM" + '-' + "dd" + " HH" + ':' + "mm" + ':' + "ss") + "\n";

            //2007-04-24 15:52:19
            richTextBox1.Text += dt.ToString("yyyy-MM-dd HH：mm：ss：ffff") + "\n";
            //2007年04月24 15時56分48秒
            richTextBox1.Text += dt.ToString("yyyy年MM月dd HH時mm分ss秒") + "\n";
            //星期二, 四月 24 2007
            richTextBox1.Text += dt.ToString("dddd, MMMM dd yyyy") + "\n";
            //二, 四月 24 '07
            richTextBox1.Text += dt.ToString("ddd, MMM d \"'\"yy") + "\n";
            //星期二, 四月 24
            richTextBox1.Text += dt.ToString("dddd, MMMM dd") + "\n";
            //4-07
            richTextBox1.Text += dt.ToString("M/yy") + "\n";
            //24-04-07
            richTextBox1.Text += dt.ToString("dd-MM-yy") + "\n";

            /*
            或者dt.ToString("yyyy年MM月dd*");//2005年11月5*
            dt.ToString("yyyy-MM-dd");//2005-11-5*
            以此類推……
            */

            dt = DateTime.Now;
            richTextBox1.Text += "DateTime.Now.ToString(\"yyyyMMdd\")                       20080923\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"yyyy/MM/dd\")                     2008/09/23\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"yyyy/M/d\")                          2008/9/23\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"yyyy/MM/dd HH:mm:ss\")    2008/09/23 13:03:03\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"T\")                                      下午 01:04:43\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"t\")                                       下午 01:05\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"tt\")                                      下午\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"yyyy/MM/dd tt hh:mm:ss\")  2008/09/23 下午 01:07:27\n";
            richTextBox1.Text += "DateTime.Now.ToString(\"yyyyMMddhhmmss\")          20080923010921\n";
            richTextBox1.Text += "HH為24小時制，hh為12小時制\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //string.Format 格式化日期

            richTextBox1.Text += "日期 1 : " + dt.CompareTo(dt).ToString() + "\n";//0
            //richTextBox1.Text +="日期 2 : "+ dt.Add(?).ToString()+"\n";//問號為一個時間段
            richTextBox1.Text += "日期 3 : " + dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            richTextBox1.Text += "日期 4 : " + dt.Equals(dt).ToString() + "\n";//True
            richTextBox1.Text += "日期 5 : " + dt.GetHashCode().ToString() + "\n";//1474088234
            richTextBox1.Text += "日期 6 : " + dt.GetType().ToString() + "\n";//DateTime
            richTextBox1.Text += "日期 7 : " + dt.GetTypeCode().ToString() + "\n";//DateTime

            /*
            richTextBox1.Text += "日期 01 : " + dt.GetDateTimeFormats(s)[0].ToString() + "\n";//2005-11-05T14:06:25
            richTextBox1.Text += "日期 02 : " + dt.GetDateTimeFormats(t)[0].ToString() + "\n";//14:06
            richTextBox1.Text += "日期 03 : " + dt.GetDateTimeFormats(y)[0].ToString() + "\n";//2005年11月
            richTextBox1.Text += "日期 04 : " + dt.GetDateTimeFormats(D)[0].ToString() + "\n";//2005年11月5*
            richTextBox1.Text += "日期 05 : " + dt.GetDateTimeFormats(D)[1].ToString() + "\n";//2005 11 05
            richTextBox1.Text += "日期 06 : " + dt.GetDateTimeFormats(D)[2].ToString() + "\n";//星期六 2005 11 05
            richTextBox1.Text += "日期 07 : " + dt.GetDateTimeFormats(D)[3].ToString() + "\n";//星期六 2005年11月5*
            richTextBox1.Text += "日期 08 : " + dt.GetDateTimeFormats(M)[0].ToString() + "\n";//11月5*
            richTextBox1.Text += "日期 09 : " + dt.GetDateTimeFormats(f)[0].ToString() + "\n";//2005年11月5* 14:06
            richTextBox1.Text += "日期 10 : " + dt.GetDateTimeFormats(g)[0].ToString() + "\n";//2005-11-5 14:06
            richTextBox1.Text += "日期 11 : " + dt.GetDateTimeFormats(r)[0].ToString() + "\n";//Sat, 05 Nov 2005 14:06:25 GMT
            */

            richTextBox1.Text += dt.GetDateTimeFormats('s')[0].ToString() + "\n";//2005-11-05T14:06:25
            richTextBox1.Text += dt.GetDateTimeFormats('t')[0].ToString() + "\n";//14:06
            richTextBox1.Text += dt.GetDateTimeFormats('y')[0].ToString() + "\n";//2005年11月
            richTextBox1.Text += dt.GetDateTimeFormats('D')[0].ToString() + "\n";//2005年11月5日
            richTextBox1.Text += dt.GetDateTimeFormats('D')[1].ToString() + "\n";//2005 11 05
            //richTextBox1.Text += dt.GetDateTimeFormats('D')[2].ToString() + "\n";//星期六 2005 11 05
            //richTextBox1.Text += dt.GetDateTimeFormats('D')[3].ToString() + "\n";//星期六 2005年11月5日
            richTextBox1.Text += dt.GetDateTimeFormats('M')[0].ToString() + "\n";//11月5日
            richTextBox1.Text += dt.GetDateTimeFormats('f')[0].ToString() + "\n";//2005年11月5日 14:06
            richTextBox1.Text += dt.GetDateTimeFormats('g')[0].ToString() + "\n";//2005-11-5 14:06
            richTextBox1.Text += dt.GetDateTimeFormats('r')[0].ToString() + "\n";//Sat, 05 Nov 2005 14:06:25 GMT

            richTextBox1.Text += "日期 01 : " + string.Format("{0:d}", dt) + "\n";//2005-11-5
            richTextBox1.Text += "日期 02 : " + string.Format("{0:D}", dt) + "\n";//2005年11月5*
            richTextBox1.Text += "日期 03 : " + string.Format("{0:f}", dt) + "\n";//2005年11月5* 14:23
            richTextBox1.Text += "日期 04 : " + string.Format("{0:F}", dt) + "\n";//2005年11月5* 14:23:23
            richTextBox1.Text += "日期 05 : " + string.Format("{0:g}", dt) + "\n";//2005-11-5 14:23
            richTextBox1.Text += "日期 06 : " + string.Format("{0:G}", dt) + "\n";//2005-11-5 14:23:23
            richTextBox1.Text += "日期 07 : " + string.Format("{0:M}", dt) + "\n";//11月5*
            richTextBox1.Text += "日期 08 : " + string.Format("{0:R}", dt) + "\n";//Sat, 05 Nov 2005 14:23:23 GMT
            richTextBox1.Text += "日期 09 : " + string.Format("{0:s}", dt) + "\n";//2005-11-05T14:23:23
            richTextBox1.Text += "日期 10 : " + string.Format("{0:t}", dt) + "\n";//14:23
            richTextBox1.Text += "日期 11 : " + string.Format("{0:T}", dt) + "\n";//14:23:23
            richTextBox1.Text += "日期 12 : " + string.Format("{0:u}", dt) + "\n";//2005-11-05 14:23:23Z
            richTextBox1.Text += "日期 13 : " + string.Format("{0:U}", dt) + "\n";//2005年11月5* 6:23:23
            richTextBox1.Text += "日期 14 : " + string.Format("{0:Y}", dt) + "\n";//2005年11月
            richTextBox1.Text += "日期 15 : " + string.Format("{0}", dt) + "\n";//2005-11-5 14:23:23?
            richTextBox1.Text += "日期 16 : " + string.Format("{0:yyyyMMddHHmmssffff}", dt) + "\n";
            //yyyymm等可以設置,比如Label16.Text = string.Format("{0:yyyyMMdd}",dt)+"\n";
            //綁定也適用:例:<%# string.Format("{0:yyyy.MM.dd}",eval_r("sj"))%>

            //日期時間輸出
            richTextBox1.Text += string.Format("{0:dddd, MMM d yyyy}", dt) + "\n";
            richTextBox1.Text += string.Format("{0:HH:mm:ss}", dt) + "\n";
            richTextBox1.Text += string.Format("{0:hh:mm:ss tt}", dt) + "\n";
            richTextBox1.Text += string.Format("{0:h:m:s}", dt) + "\n";

            //-------- same
            richTextBox1.Text += dt.CompareTo(dt).ToString() + "\n";//0

            //richTextBox1.Text += dt.Add(?).ToString() + "\n";//問號為一個時間段

            richTextBox1.Text += dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            richTextBox1.Text += dt.Equals(dt).ToString() + "\n";//True
            richTextBox1.Text += dt.GetHashCode().ToString() + "\n";//1474088234
            richTextBox1.Text += dt.GetType().ToString() + "\n";//DateTime
            richTextBox1.Text += dt.GetTypeCode().ToString() + "\n";//DateTime

        }

        //------------------------------------------------------------  # 60個

        void show_time_span(TimeSpan ts)
        {
            //richTextBox1.Text += "時間間隔 : " + ts.ToString() + "\n";
            richTextBox1.Text += "時間間隔 : " + String.Format("{0} 日 {1} 時 {2} 分 {3} 秒 {4} 毫秒", ts.Days, ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds) + "\n";
            //richTextBox1.Text += "時間間隔 : " + ts.Days.ToString() + " 日 " + ts.Hours.ToString() + " 時 " + ts.Minutes.ToString() + " 分 " + ts.Seconds.ToString() + " 秒\n";
            richTextBox1.Text += "總日數 : " + ts.TotalDays.ToString() + "\n";
            richTextBox1.Text += "總時數 : " + ts.TotalHours.ToString() + "\n";
            richTextBox1.Text += "總分數 : " + ts.TotalMinutes.ToString() + "\n";
            richTextBox1.Text += "總秒數 : " + ts.TotalSeconds.ToString() + "\n";
            richTextBox1.Text += "總毫秒數 : " + ts.TotalMilliseconds.ToString() + "\n";
            return;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

            // TimeSpan 取 時間間隔，只能取到天數，不能算月數、年數
            // 計算時間間隔 TimeSpan = 兩個dt相減

            DateTime dt1 = new DateTime(2006, 3, 11, 9, 15, 15); //指定時間, 年月日 時分秒
            DateTime dt2 = DateTime.Now;

            TimeSpan ts = dt2 - dt1;
            //TimeSpan ts = new TimeSpan(dt2.Ticks - dt1.Ticks);  // same

            show_time_span(ts);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //時間相隔

            dt1 = new DateTime(2006, 3, 11, 9, 15, 30);
            // dt1 = new DateTime(2021, 5, 21, 9, 15, 30);
            dt2 = DateTime.Now;

            //計算耗時任務所需的秒數
            string diff_time = DateDiff(dt1, dt2);
            richTextBox1.Text += "相隔 : " + diff_time.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            //計算時間間隔

            dt1 = new DateTime(2017, 1, 31);
            dt2 = new DateTime(2017, 2, 1, 2, 3, 4, 15);
            DateTime dt3 = DateTime.Now;
            TimeSpan ts1 = dt2 - dt1;
            TimeSpan ts2 = dt3 - dt1;
            richTextBox1.Text += "兩個時間相距 : " + ts1.ToString() + "\n";
            richTextBox1.Text += "與現在相距 : " + ts2.ToString() + "\n";

            //------------------------------------------------------------  # 60個

            //計算時間間隔, 使用 TimeSpan
            dt1 = new DateTime(2019, 1, 1, 0, 0, 0);
            dt2 = new DateTime(2037, 12, 30, 12, 34, 56, 15);
            dt3 = DateTime.Now;

            //TimeSpan
            ts1 = dt2 - dt1;
            //TimeSpan
            ts2 = dt3 - dt1;

            richTextBox1.Text += "時間間隔 : " + ts1.ToString() + "\n";
            richTextBox1.Text += "與現在相距 : " + ts2.ToString() + "\n";

            ts = DateTime.Now - DateTime.Now.Date;
            //richTextBox1.Text += DateTime.Now.ToString() + "\n";
            //richTextBox1.Text += DateTime.Now.Date.ToString() + "\n";
            richTextBox1.Text += "今天經過時間 : " + ts.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;
            ts = DateTime.Now - bootup_time;
            richTextBox1.Text += "程式啟動時間: " + bootup_time.ToString() + " 秒\n";
            richTextBox1.Text += "至今經歷時間: " + ts.ToString() + " 時分秒\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算時間間隔
            //Timestamp 與 DateTime 互轉
            // 現在時間轉秒數
            //double timestamp = (DateTime.Now.AddHours(-8) - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
            double timestamp = (DateTime.Now.AddHours(-0) - new DateTime(2016, 5, 5, 23, 0, 0)).TotalSeconds;

            richTextBox1.Text += "從某時間距今秒數 : " + timestamp.ToString() + "\n";

            // 秒數轉 DateTime
            timestamp = 2400;
            dt = (new DateTime(2016, 5, 5, 23, 0, 0)).AddHours(0).AddSeconds(timestamp);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算時間間隔

            string string_datetime3 = "2006/03/11";
            int year = 0;
            int month = 0;
            int day = 0;
            dt = DateTime.ParseExact(string_datetime3, "yyyy/MM/dd", null, DateTimeStyles.AllowWhiteSpaces);

            year = dt.Year;
            month = dt.Month;
            day = dt.Day;

            richTextBox1.Text += year.ToString() + "  " + month.ToString() + "   " + day.ToString() + "\n\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;
            ts = dt.Subtract(LoginTime);  // dt減dt得到ts

            richTextBox1.Text += "登出時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "您在此停留了" + ts.Hours + "小時" + ts.Minutes + "分鐘" + ts.Seconds + "秒" + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //倒數計時, 2027年距今還有多久
            DateTime dt_target = new DateTime(2027, 1, 1, 0, 0, 0);
            dt = DateTime.Now;
            ts = dt_target.Subtract(dt);  // dt減dt得到ts
            ts = dt_target - dt;//same

            if (ts.TotalSeconds < 0)
            {
                richTextBox1.Text += "時間 " + dt_target + " 已過\n";
            }
            else
            {
                richTextBox1.Text += "時間 " + dt_target + " 距今:\n";
                show_time_span(ts);
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算兩個日期的時間間隔
            dt1 = new DateTime(2006, 3, 11, 9, 15, 20);
            dt2 = DateTime.Now;

            string diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";

            ts = dt2 - dt1;
            show_time_span(ts);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "計算時間往回推 1天 2小時 3分 4秒\n";

            uint elapssed_time_msec = 1000 * (60 * 60 * 24 * 1 + 60 * 60 * 2 + 60 * 3 + 4);  // msec

            // 換算成 DateTime
            TimeSpan uptime = TimeSpan.FromMilliseconds(elapssed_time_msec);
            richTextBox1.Text += "已開機時間 : " + uptime.Days.ToString() + "天" + uptime.Hours.ToString() + "小時" + uptime.Minutes.ToString() + "分鐘\n";

            DateTime before_time = DateTime.Now - TimeSpan.FromMilliseconds(elapssed_time_msec);

            richTextBox1.Text += "計算時間往回推 : " + before_time + "\n";

            richTextBox1.Text += "計算時間往回推 1天 2小時 3分 4秒\n";

            uint elapssed_time = 60 * 60 * 24 * 1 + 60 * 60 * 2 + 60 * 3 + 4;  // sec

            before_time = DateTime.Now - TimeSpan.FromSeconds(elapssed_time);

            richTextBox1.Text += "計算時間往回推 : " + before_time + "\n";
        }

        //計算時間間隔, 傳回時間差的絕對值
        private string DateDiff(DateTime dt1, DateTime dt2)
        {
            TimeSpan ts1 = new TimeSpan(dt1.Ticks);
            TimeSpan ts2 = new TimeSpan(dt2.Ticks);
            TimeSpan ts = ts2.Subtract(ts1).Duration();  // dt減dt得到ts 取秒數
            string dateDiff = ts.Days.ToString() + "天" + ts.Hours.ToString() + "小時" + ts.Minutes.ToString() + "分鐘" + ts.Seconds.ToString() + "秒";
            return dateDiff;
        }

        //------------------------------------------------------------  # 60個

        long ticks_old = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            long seconds = DateTime.Now.Ticks / TimeSpan.TicksPerSecond;

            richTextBox1.Text += "現在時間用Ticks表示 : " + DateTime.Now.Ticks.ToString() + "\n";  // 一秒 1千萬 個 Ticks
            richTextBox1.Text += "每秒有幾個Ticks(TicksPerSecond) : " + TimeSpan.TicksPerSecond.ToString() + "\n";

            richTextBox1.Text += "現在時間用秒表示 : " + seconds.ToString() + "\n";

            richTextBox1.Text += DateTime.Now.ToString() + "\n";
            richTextBox1.Text += "diff = " + (DateTime.Now.Ticks - ticks_old).ToString() + "\n";

            ticks_old = DateTime.Now.Ticks;
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // DateTime.Compare() 比較時間早晚

            richTextBox1.Text += "比較時間早晚\n";

            DateTime dt1 = new DateTime(2016, 12, 9, 0, 0, 0);
            DateTime dt2 = new DateTime(2016, 12, 9, 11, 0, 0);

            richTextBox1.Text += "時間1 : " + dt1.ToString() + "\n";
            richTextBox1.Text += "時間2 : " + dt2.ToString() + "\n";

            int result = DateTime.Compare(dt1, dt2);

            string relationship = string.Empty;
            if (result < 0)
                relationship = " 早於 ";
            else if (result == 0)
                relationship = " 同時 ";
            else
                relationship = " 晚於 ";

            richTextBox1.Text += dt1 + " " + relationship + " " + dt2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            //時間比較
            DateTime.Compare(dt1, dt2) > 0 : dt1 > dt2
            DateTime.Compare(dt1, dt2) == 0 : dt1 == dt2
            DateTime.Compare(dt1, dt2) < 0 : dt1 < dt2       
            */
        }

        private void button5_Click(object sender, EventArgs e)
        {
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 時間加減
            /*
            dt.AddYears()
            dt.AddDays()
            dt.AddHours()
            dt.AddMilliseconds()
            dt.AddMonths()
            dt.AddSeconds()
            dt.AddMinutesv
            dt.AddTicks()
            */

            DateTime dt = DateTime.Now;

            DateTime ThisMonBeginDay = new DateTime(dt.Year, dt.Month, 1);
            DateTime ThisMonEndDay = ThisMonBeginDay.AddMonths(1).AddDays(-1);
            richTextBox1.Text += "本月月底日期:" + ThisMonEndDay.Day.ToString() + "\n";
            richTextBox1.Text += "本月月底日期:" + DateTime.DaysInMonth(dt.Year, dt.Month).ToString() + "\n";

            richTextBox1.Text += "日期 1 : " + dt.AddYears(1).ToString() + "\n";//2006-11-5 13:47:04
            richTextBox1.Text += "日期 2 : " + dt.AddDays(1.1).ToString() + "\n";//2005-11-6 16:11:04
            richTextBox1.Text += "日期 3 : " + dt.AddHours(1.1).ToString() + "\n";//2005-11-5 14:53:04
            richTextBox1.Text += "日期 4 : " + dt.AddMilliseconds(1.1).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 5 : " + dt.AddMonths(1).ToString() + "\n";//2005-12-5 13:47:04
            richTextBox1.Text += "日期 6 : " + dt.AddSeconds(1.1).ToString() + "\n";//2005-11-5 13:47:05
            richTextBox1.Text += "日期 7 : " + dt.AddMinutes(1.1).ToString() + "\n";//2005-11-5 13:48:10
            richTextBox1.Text += "日期 8 : " + dt.AddTicks(1000).ToString() + "\n";//2005-11-5 13:47:04

            //現在日期加天數寫法(本例為加5天):
            DateTime Add5Day = dt.AddDays(5);
            richTextBox1.Text += "現在日期加5天 : " + Add5Day.ToLongDateString() + "\n";

            //現在時間加小時寫法(本例為加12個小時):
            DateTime Add12Hours = dt.AddHours(12);
            richTextBox1.Text += "現在時間加12小時 : " + Add12Hours.ToLongTimeString() + "\n";

            //現在時間減分鐘寫法(本例為減30分鐘):
            DateTime Minus30Minutes = dt.AddMinutes(-30);
            richTextBox1.Text += "現在時間減30分鐘 : " + Minus30Minutes.ToLongTimeString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = new DateTime(2019, 1, 1);

            richTextBox1.Text += "2019/1/1 加一段時間後 : " + dt.AddDays(3125).AddSeconds(14653 * 2).ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            int yy = -280;
            int dd = -1250;
            richTextBox1.Text += "2019/1/1 減一段時間後 : " + dt.AddYears(yy).AddDays(dd).AddSeconds(14653 * 2).ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //一段時間以後的寫法
            dt = DateTime.Now;

            //?日?時?分?秒 後
            DateTime dt_new = dt + new TimeSpan(365 * 10, 12, 34, 56);

            richTextBox1.Text += "現在時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "一段時間以後 : " + dt_new.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //一段時間以後的寫法
            dt = DateTime.Now;

            //?日?時?分?秒 後
            DateTime dt_target = dt + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            richTextBox1.Text += "現在時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "現在時間 + 1天13時42分59秒 = " + dt_target.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;

            DateTime LastSalaryDay = new DateTime(dt.Year, dt.Month, 5);
            DateTime NextSalaryDay = new DateTime(dt.AddMonths(1).Year, dt.AddMonths(1).Month, 5);

            richTextBox1.Text += "上次發薪日 : " + LastSalaryDay.ToString("yyyy/MM/dd") + "\n";
            TimeSpan ts1 = dt - LastSalaryDay;

            richTextBox1.Text += "經過了 : " + ts1.Days + " 天\n";

            richTextBox1.Text += "下次發薪日 : " + NextSalaryDay.ToString("yyyy/MM/dd") + "\n";

            //用 大的日期 減 小的日期
            TimeSpan ts2 = dt - NextSalaryDay;    //小的日期減大的日期

            richTextBox1.Text += "距離下次發薪日還有" + Math.Abs(ts2.Days) + " 天\n"; //距離幾天一定是正的 用Math.Abs取絕對值

            //------------------------------------------------------------  # 60個

            dt = DateTime.Now;

            //後一天
            DateTime nextDay = dt.AddDays(1);
            richTextBox1.Text += "後一天 : " + nextDay + "\n";

            //前一天
            DateTime pervDay = dt.AddDays(-1);
            richTextBox1.Text += "前一天 : " + pervDay + "\n";

            /*
            DateTime dt3 = new DateTime(1900, 1, 6, 2, 5, 0); //#1/6/1900 2:05:00 AM#
            DateTime dt4;
            num = 525948.76 * (y - 1900) + sTermInfo[i - 1];
            dt4 = dt3.AddMinutes(num);//按分鐘計算
            */

            dt = DateTime.Now;
            string message = "";
            message += string.Format("{0}", dt.Year) + "\n";
            message += ("西元年:" + dt.Year.ToString()) + "\n";
            message += (string.Format("西元:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";

            dt = DateTime.Now;
            richTextBox1.Text += "現在日期 : " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "現在時間 : " + dt.ToLongTimeString() + "\n";

            //6060

            //時間相關
            //中時間相關知識點小結

            //二、當月第一天和最後一天

            DateTime ThisMonth_Frist = dt.AddDays(1 - dt.Day).Date;
            richTextBox1.Text += "當月第一天\t" + ThisMonth_Frist + "\n";

            DateTime ThisMOnth_Last = dt.AddDays(1 - dt.Day).Date.AddMonths(1).AddSeconds(-1);
            richTextBox1.Text += "當月最後一天\t" + ThisMOnth_Last + "\n";

            //三、上月第一天和最後一天

            DateTime Today = DateTime.Today;//當天時間
            DateTime ThisMonth = new DateTime(Today.Year, Today.Month, 1);//當前月第一天時間

            DateTime LastMonth_First = ThisMonth.AddMonths(-1);//上月第一天時間
            richTextBox1.Text += "上月第一天\t" + LastMonth_First + "\n";

            DateTime LastMonth_Last = ThisMonth.AddDays(-1);//上月最後一天時間
            richTextBox1.Text += "上月最後一天\t" + LastMonth_Last + "\n";

            //四、本周第幾天

            int daysInWeek1 = (int)dt.DayOfWeek;//注意 : 此處周日時回傳0
            richTextBox1.Text += "本周第幾天\t" + daysInWeek1.ToString() + "\n";

            int daysInWeek2 = (int)dt.DayOfWeek == 0 ? 7 : (int)dt.DayOfWeek;//當前周第幾天,注釋:周日為0
            richTextBox1.Text += "本周第幾天\t" + daysInWeek2.ToString() + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //VB的DateAndTime, 需要 參考/加入參考/.NET/Microsoft.VisualBasic

            //使用VisualBasic的DateDiff方法獲取日期間隔

            DateTime dt1 = new DateTime(2006, 3, 11, 9, 15, 30);
            //DateTime dt1 = new DateTime(2021, 5, 21, 9, 15, 30);
            DateTime dt2 = DateTime.Now;
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Year, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 年\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Month, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 月\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Day, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 天\n";

            //------------------------------------------------------------  # 60個

            DateTime get_time1 = Convert.ToDateTime(DateTime.Now.ToString());
            DateTime sta_ontime1 = Convert.ToDateTime(Convert.ToDateTime("2028-07-14 20:00:00"));

            richTextBox1.Text += "距離2028年洛杉磯奧運會開幕還有\n";
            richTextBox1.Text += DateAndTime.DateDiff("yyyy", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 年\n";
            richTextBox1.Text += DateAndTime.DateDiff("m", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 月\n";
            richTextBox1.Text += DateAndTime.DateDiff("d", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 日\n";
            richTextBox1.Text += DateAndTime.DateDiff("h", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 時\n";
            richTextBox1.Text += DateAndTime.DateDiff("n", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 分\n";
            richTextBox1.Text += DateAndTime.DateDiff("s", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 秒\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
        }

        //6060

        private void button9_Click(object sender, EventArgs e)
        {
        }

        //6060

        private void button10_Click(object sender, EventArgs e)
        {
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //依時間建立檔案
            DateTime dt = DateTime.Now;

            string filename = String.Format("{0}-{1}-{2}_{3}-{4}-{5}", dt.Year, dt.Month, dt.Day, dt.Hour, dt.Minute, dt.Second);

            richTextBox1.Text += "依時間建立檔案 :" + filename + "\n";

            string m_fileName = dt.ToFileTime().ToString() + ".jpg";
            richTextBox1.Text += "依時間建立檔案 :" + m_fileName + "\n";

            richTextBox1.Text += "Conversion finished @ " + dt.ToString() + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
            //Parse 大全
            //DateTime.Parse   DateTime.TryParse	在處理西元1~99年會處理成20XX年

            richTextBox1.Text += "DateTime.Parse, 字串轉DateTime物件\n";

            string string_datetime1 = "3/11/2006 9:15:30 AM";
            string string_datetime2 = "11 March 2006, 9:15";

            DateTime dt;
            richTextBox1.Text += "日期1 : " + string_datetime1 + "\n";
            try
            {   //可能會產生錯誤的程式區段
                dt = DateTime.Parse(string_datetime1);
                richTextBox1.Text += "日期轉序數 : " + dt.ToOrdinal() + "\n";
                richTextBox1.Text += dt.ToString() + "\n";
            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
                richTextBox1.Text += "DateTime.Parse完成\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "日期2 : " + string_datetime2 + "\n";

            if (DateTime.TryParse(string_datetime2, out dt) == true)
            {
                richTextBox1.Text += "取得DateTime : " + dt.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "取得DateTime失敗 1\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string string_datetime3 = "20100504";
            dt = DateTime.ParseExact(string_datetime3, "yyyyMMdd", null, DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間 : " + dt.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string string_datetime4 = "3/11/2006 9:15:30 AM";
            dt = DateTime.Parse(string_datetime4);
            richTextBox1.Text += "生日: " + dt.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            DateTime dt1 = DateTime.ParseExact("2006/03/11", "yyyy/MM/dd", null);
            DateTime dt2 = DateTime.ParseExact("2018/02/01", "yyyy/MM/dd", null);
            dt1 = DateTime.Parse("628年7月21日");
            dt2 = DateTime.Parse("683年12月27日");

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string str1 = "20091014223600";
            IFormatProvider ifp = new CultureInfo("zh-TW", true);
            dt1 = DateTime.ParseExact(str1, "yyyyMMddHHmmss", ifp);

            richTextBox1.Text += "原字串 : " + str1 + "\n";
            richTextBox1.Text += "解讀後 : " + dt1.ToString() + "\n";

            string str2 = "20091014223600";
            dt = DateTime.Now;
            richTextBox1.Text += "原字串 : " + str2 + "\n";
            //IFormatProvider ifp = new CultureInfo("zh-TW", true);
            if (DateTime.TryParseExact(str2, "yyyyMMddHHmmss", ifp, DateTimeStyles.None, out dt2) == true)
            {
                richTextBox1.Text += "解讀後1 : " + dt2.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "解讀後2 : " + dt.ToString() + "\n";
                richTextBox1.Text += "取得DateTime失敗 2\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string date_time1 = "21 July 1969, 20:17:40";
            string date_time2 = "14 December 1972, 19:54:57";
            richTextBox1.Text += "時間1 : " + date_time1 + "\n";
            richTextBox1.Text += "時間2 : " + date_time2 + "\n";

            if (DateTime.TryParse(date_time1, out dt1) == true)
            {
                richTextBox1.Text += "dt1 : " + dt1.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "取得DateTime失敗 4a\n";
                return;
            }

            if (DateTime.TryParse(date_time2, out dt2) == true)
            {
                richTextBox1.Text += "dt2 : " + dt2.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "取得DateTime失敗 4b\n";
                return;
            }

            int years, months, days, hours, minutes, seconds, milliseconds;

            GetElapsedTime(dt1, dt2, out years, out months, out days, out hours, out minutes, out seconds, out milliseconds);

            string txt = "";
            if (years != 0)
            {
                txt += ", " + years.ToString() + " years";
            }
            if (months != 0)
            {
                txt += ", " + months.ToString() + " months";
            }
            if (days != 0)
            {
                txt += ", " + days.ToString() + " days";
            }
            if (hours != 0)
            {
                txt += ", " + hours.ToString() + " hours";
            }
            if (minutes != 0)
            {
                txt += ", " + minutes.ToString() + " minutes";
            }
            if (seconds != 0)
            {
                txt += ", " + seconds.ToString() + " seconds";
            }
            if (milliseconds != 0)
            {
                txt += ", " + milliseconds.ToString() + " milliseconds";
            }
            if (txt.Length > 0)
            {
                txt = txt.Substring(2);
            }
            if (txt.Length == 0)
            {
                txt = "Same";
            }
            richTextBox1.Text += "時間間隔 : " + txt + "\n";

            //------------------------------------------------------------  # 60個

            //新進

            // 時間格式轉換 pppp
            // 各種取得 DateTime 的方法

            dt1 = Convert.ToDateTime("2010-10-15 15:50:39");
            dt1 = Convert.ToDateTime("2010/05/30 12:13:50");
            dt2 = Convert.ToDateTime("1953/07/27");

            dt1 = new DateTime(2008, 12, 31, 23, 59, 59, DateTimeKind.Local);
            dt2 = new DateTime(2003, 11, 13, 23, 59, 59, DateTimeKind.Local);

        }

        private void button13_Click(object sender, EventArgs e)
        {
            //干支
            for (int i = 0; i < 20; i++)
            {
                richTextBox1.Text += GanZhiYearString(i) + "\n";
            }

            //------------------------------------------------------------  # 60個

            //干支
            string chineseEra;
            string sky = "甲乙丙丁戊已庚辛壬癸";        //天干
            string earth = "子丑寅卯辰巳午未申酉戌亥";  //地支

            for (int i = 0; i < 60; i++)
            {
                chineseEra = sky.Substring(i % 10, 1) + earth.Substring(i % 12, 1);
                richTextBox1.Text += chineseEra + "  ";
            }
            richTextBox1.Text += "\n";

        }

        private const int GanZhiStartYear = 0; //干支計算起始年
        private static string ganStr = "甲乙丙丁戊己庚辛壬癸";
        private static string zhiStr = "子丑寅卯辰巳午未申酉戌亥";

        string GanZhiYearString(int year)
        {
            int i = (year - GanZhiStartYear) % 60; //計算干支
            string tempStr = ganStr[i % 10].ToString() + zhiStr[i % 12].ToString() + "年";
            return tempStr;
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //OLE自動化日期
            try
            {   //可能會產生錯誤的程式區段

                DateTime dt1 = new DateTime(2021, 5, 5, 12, 34, 56);

                double ole_date1 = dt1.ToOADate();

                richTextBox1.Text += "原日期 : " + dt1.ToString() + "\n";
                richTextBox1.Text += "OLE Automation date 日期 : " + ole_date1.ToString() + "\n";
            }
            catch (OverflowException ex)
            {
                //定義產生錯誤時的例外處理程式碼
                richTextBox1.Text += "錯誤訊息 : 類型 : " + ex.GetType() + ", 訊息 : " + ex.Message + "\n";
            }
            finally
            {
                //一定會被執行的程式區段
            }

            richTextBox1.Text += "\n";

            double ole_date2 = 43210.123456;
            DateTime dt2 = DateTime.FromOADate(ole_date2);
            richTextBox1.Text += "OLE自動化日期 : " + ole_date2.ToString() + "\n";
            richTextBox1.Text += "新日期 : " + dt2.ToString() + "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {
        }

        private void button16_Click(object sender, EventArgs e)
        {
            //星期幾

            string strWeek = "星期" + "日一二三四五六".Substring((int)DateTime.Now.DayOfWeek, 1);
            richTextBox1.Text += strWeek + "\n";

            //幾年幾月幾日 星期幾
            int year = 2006;
            int month = 3;
            int day = 11;
            string weekday = string.Empty;

            weekday = CaculateWeekDay(year, month, day);
            richTextBox1.Text += year.ToString() + "年" + month.ToString() + "月" + day.ToString() + "日\t是\t" + weekday + "\n";

            year = 1941;
            month = 12;
            day = 7;
            weekday = CaculateWeekDay(year, month, day);
            richTextBox1.Text += year.ToString() + "年" + month.ToString() + "月" + day.ToString() + "日\t是\t" + weekday + "\t珍珠港事變\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //尋找13號星期五
            int year_st = 2025;
            int year_sp = 2028;
            //int year = 0;
            //int month = 0;
            DateTime dt;

            // Loop over the selected years.
            for (year = year_st; year <= year_sp; year++)
            {
                // Loop over the months in the year.
                for (month = 1; month <= 12; month++)
                {
                    // See if this month's 13th is a Friday.
                    dt = new DateTime(year, month, 13);

                    // See if this is a Friday.
                    if (dt.DayOfWeek == DayOfWeek.Friday)
                    {
                        richTextBox1.Text += dt.ToShortDateString() + "\n";
                    }
                }
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //獲取當前星期幾的方法
            weekday = string.Empty;

            dt = DateTime.Now;

            //獲得中文星期名稱
            richTextBox1.Text += "英文星期名稱 : " + dt.DayOfWeek + "\n";

            // 獲得中文星期名稱
            switch (dt.DayOfWeek)
            {
                case DayOfWeek.Sunday:
                    weekday = "星期日";
                    break;
                case DayOfWeek.Monday:
                    weekday = "星期一";
                    break;
                case DayOfWeek.Tuesday:
                    weekday = "星期二";
                    break;
                case DayOfWeek.Wednesday:
                    weekday = "星期三";
                    break;
                case DayOfWeek.Thursday:
                    weekday = "星期四";
                    break;
                case DayOfWeek.Friday:
                    weekday = "星期五";
                    break;
                case DayOfWeek.Saturday:
                    weekday = "星期六";
                    break;
                default:
                    weekday = "星期一";
                    break;
            }

            richTextBox1.Text += "中文星期名稱 : " + weekday + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            dt = DateTime.Now;

            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(dt.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";

            //------------------------------------------------------------  # 60個

            string weekday1 = Day[Convert.ToInt32(dt.DayOfWeek.ToString("d"))].ToString();    //same
            string weekday2 = Day[Convert.ToInt16(dt.DayOfWeek)]; //same
            richTextBox1.Text += weekday1 + "\n";
            richTextBox1.Text += weekday2 + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            weekday = string.Empty;
            switch (DateTime.Today.DayOfWeek.ToString())
            {
                case "Monday":
                    weekday = "星期一";
                    break;
                case "Tuesday":
                    weekday = "星期二";
                    break;
                case "Wednesday":
                    weekday = "星期三";
                    break;
                case "Thursday":
                    weekday = "星期四";
                    break;
                case "Friday":
                    weekday = "星期五";
                    break;
                case "Saturday":
                    weekday = "星期六";
                    break;
                case "Sunday":
                    weekday = "星期日";
                    break;
                default:
                    weekday = "星期日";
                    break;
            }
            richTextBox1.Text += "今天是 : " + weekday + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            dt = DateTime.Now;

            string[] Day2 = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week2 = Day2[Convert.ToInt32(dt.DayOfWeek.ToString("d"))].ToString();

            richTextBox1.Text += week2 + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //星期幾
            richTextBox1.Text += CalculateWeekDay(2021, 10, 28);
            richTextBox1.Text += "\n";

            //根據年月日計算星期幾的函數
            weekday = CalculateWeekDay(2021, 10, 14);
            richTextBox1.Text += "日期 " + DateTime.Parse("2021/10/14").ToString() + "\t" + weekday + "\n";

            weekday = CalculateWeekDay(1941, 12, 7);
            richTextBox1.Text += "日期 " + DateTime.Parse("1941/12/7").ToString() + "\t" + weekday + "\n";

            weekday = CalculateWeekDay(2006, 3, 11);
            richTextBox1.Text += "日期 " + DateTime.Parse("2006/3/11").ToString() + "\t" + weekday + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個
        }

        private void button17_Click(object sender, EventArgs e)
        {
        }

        private void button18_Click(object sender, EventArgs e)
        {
            //列出全球時區

            //using System.Collections;
            richTextBox1.Text += "取得全球時區資訊\n";

            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                richTextBox1.Text += info + "\n";
            }

            //------------------------------------------------------------  # 60個

            //取得系統的時區資訊
            // Initialize the time zone lists.
            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                comboBox1.Items.Add(info);
                richTextBox1.Text += info + "\n";
            }

            // Select a default value
            comboBox1.SelectedItem = FindItemContaining(comboBox1.Items, "臺北");

            TimeZoneInfo zone1 = comboBox1.SelectedItem as TimeZoneInfo;
            string name1 = zone1.DisplayName;
            richTextBox1.Text += "name1 = " + name1 + "\n";
        }

        //------------------------------------------------------------  # 60個

        private void button20_Click(object sender, EventArgs e)
        {
            //特殊曆法

            //萬年曆 農曆 節日 節氣
            DateTime dt = DateTime.Now;
            TaiwanCalendar TC = new TaiwanCalendar();
            TaiwanLunisolarCalendar TA = new TaiwanLunisolarCalendar();
            richTextBox1.Text += string.Format("{0}", dt.Year) + "\n";
            richTextBox1.Text += ("西元年:" + dt.Year.ToString()) + "\n";
            richTextBox1.Text += ("民國年:" + TC.GetYear(dt)) + "\n";
            richTextBox1.Text += (string.Format("西元:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";
            richTextBox1.Text += (string.Format("民國:{0}/{1}/{2}", TC.GetYear(dt), TC.GetMonth(dt), TC.GetDayOfMonth(dt))) + "\n";
            richTextBox1.Text += (string.Format("農曆:{0}/{1}/{2}", TA.GetYear(dt), TA.GetMonth(dt), TA.GetDayOfMonth(dt))) + "\n";

            TaiwanLunisolarCalendar tlc = new TaiwanLunisolarCalendar();
            // 取得目前支援的農曆日曆到幾年幾月幾日( 2051-02-10 )
            richTextBox1.Text += "取得目前支援的農曆日曆 : " + tlc.MaxSupportedDateTime.ToShortDateString() + "\n";
            // 取得今天的農曆年月日
            richTextBox1.Text += "農曆 : " + tlc.GetYear(DateTime.Now).ToString() + " 年 " + tlc.GetMonth(DateTime.Now).ToString() + " 月 " + tlc.GetDayOfMonth(DateTime.Now).ToString() + " 日\n";

            //找特定日期的農曆日期
            dt = new DateTime(2006, 3, 11);
            TaiwanCalendar tc = new TaiwanCalendar();

            int year = tc.GetYear(dt);
            int month = tc.GetMonth(dt);
            int dayOfMonth = tc.GetDayOfMonth(dt);             //日
            int daysInMonth = tc.GetDaysInMonth(year, month);   //整個月的天數
            richTextBox1.Text += "民國" + year.ToString() + "年" + month.ToString() + "月" + dayOfMonth.ToString() + "日\n";

            //------------------------------------------------------------  # 60個

            //創建日曆對象ChineseLunisolarCalendar,將時間分成多個部分來表示，如分成年、月和日。 年按農曆計算，而日和月按陰陽曆計算。
            ChineseLunisolarCalendar chinseCaleander = new ChineseLunisolarCalendar();
            string TreeYear = "鼠牛虎兔龍蛇馬羊猴雞狗豬";//創建字符串對象
            int intYear = chinseCaleander.GetSexagenaryYear(DateTime.Now);//計算年信息,GetSexagenaryYear計算與指定日期對應的甲子（60 年）循環中的年。

            //得到生肖信息
            string Tree = TreeYear.Substring(chinseCaleander.GetTerrestrialBranch(intYear) - 1, 1);//GetTerrestrialBranch計算甲子（60 年）循環中指定年份的地支,
            //Substring(x,y)從此實例檢索子字符串。 子字符串從指定的字符位置開始且具有指定的長度
            richTextBox1.Text += "今年是十二生肖 " + Tree + " 年\n";

            //顯示星期信息
            richTextBox1.Text += "今天是 : " + DateTime.Now.ToString("dddd") + "\n";//dddd是星期日,ddd是日,dd是01

            //------------------------------------------------------------  # 60個

            //取得時辰
            dt = DateTime.Now;

            string ctime = getChineseTime(dt.Hour);
            richTextBox1.Text += "目前時辰 : " + ctime + "\n";

            //------------------------------------------------------------  # 60個

            dt = DateTime.Now;

            richTextBox1.Text += "民國記年\n";

            CultureInfo ci = new CultureInfo("zh-TW", true);
            ci.DateTimeFormat.Calendar = new TaiwanCalendar();

            richTextBox1.Text += "民國記年 : " + dt.ToString("yy/M/d", ci) + "\n";
            richTextBox1.Text += "民國記年 : " + dt.ToString("yyyy/MM/dd", ci) + "\n";

            ci = new CultureInfo("zh-TW");
            ci.DateTimeFormat.Calendar = ci.OptionalCalendars[2];

            richTextBox1.Text += "xxxx記年 : " + dt.ToString("yyyy/MM/dd", ci) + "\n";

            richTextBox1.Text += "xxxx" + dt.ToString() + "\n";
            richTextBox1.Text += "xxxx" + dt.ToString("yyyy/MM/dd", ci) + "\n";
            richTextBox1.Text += "xxxx" + dt.ToString("HH:mm:ss") + "\n";
            richTextBox1.Text += "xxxx" + dt.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += "CultureInfo.CurrentCulture.xxxx\n";

            richTextBox1.Text += "中文星期名 :\n";
            richTextBox1.Text += CultureInfo.CurrentCulture.DateTimeFormat.GetDayName(dt.DayOfWeek) + "\n";

            for (int weekday = 0; weekday < 7; weekday++)
            {
                richTextBox1.Text += "英/中文星期名 : ";
                richTextBox1.Text += ((DayOfWeek)weekday).ToString() + "\t";
                richTextBox1.Text += CultureInfo.CurrentCulture.DateTimeFormat.GetDayName((DayOfWeek)weekday) + "\t";
                richTextBox1.Text += CultureInfo.CurrentCulture.DateTimeFormat.DayNames[weekday] + "\n";
            }

            string[] month_names = CultureInfo.CurrentCulture.DateTimeFormat.MonthNames;  // 取得13個中文月名(多一個)

            foreach (string month_name in month_names)
            {
                if (month_name.Length > 0)  // 有一個長度為0的, 要排除
                {
                    richTextBox1.Text += month_name + " ";
                }
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            string[] day_names = CultureInfo.CurrentCulture.DateTimeFormat.DayNames;  // 取得7個中文星期名

            foreach (string day_name in day_names)
            {
                if (day_name.Length > 0)
                {
                    richTextBox1.Text += day_name + " ";
                }
            }
            richTextBox1.Text += "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "顯示中文格式的日期、星期幾\n";
            richTextBox1.Text += "//該語句顯示的為英文格式\n";
            richTextBox1.Text += dt.DayOfWeek.ToString() + "\n";

            richTextBox1.Text += "//顯示中文格式星期幾 簡中1\n";
            richTextBox1.Text += dt.ToString("ddd", new CultureInfo("zh-cn")) + "\n";      //3個d

            richTextBox1.Text += "//顯示中文格式星期幾 簡中2\n";
            richTextBox1.Text += dt.ToString("dddd", new CultureInfo("zh-cn")) + "\n";     //更新簡捷的顯示中文格式星期幾用4個dddd就可以搞定了，不需任何拼湊

            richTextBox1.Text += "//顯示中文格式星期幾 正中1\n";
            richTextBox1.Text += dt.ToString("ddd", new CultureInfo("zh-tw")) + "\n";      //3個d

            richTextBox1.Text += "//顯示中文格式星期幾 正中2\n";
            richTextBox1.Text += dt.ToString("dddd", new CultureInfo("zh-tw")) + "\n";     //4個d

            richTextBox1.Text += "//顯示日文格式星期幾\n";
            richTextBox1.Text += dt.ToString("ddd", new CultureInfo("ja")) + "\n";

            richTextBox1.Text += "//顯示美語格式星期幾\n";
            richTextBox1.Text += dt.ToString("ddd", new CultureInfo("en-us")) + "\n";
            richTextBox1.Text += dt.ToString("MMM", new CultureInfo("en-us")) + "\n";  // 月份英文簡寫 : Jul

            richTextBox1.Text += "//VS2005後顯示星期的新方法是\n";
            richTextBox1.Text += "星期" + dt.DayOfWeek.ToString(("d")) + "\n";

            // 看起來都一樣
            string dateString1 = DateTime.Today.ToString("yyyy-M-d dddd");
            string dateString2 = DateTime.Today.ToString("yyyy-M-d dddd", new CultureInfo("zh-CN"));
            richTextBox1.Text += "DateTime.Today dateString1 : " + dateString1 + "\n";
            richTextBox1.Text += "DateTime.Today dateString2 : " + dateString2 + "\n";

            dateString1 = dt.ToString("yyyy-M-d dddd");
            dateString2 = dt.ToString("yyyy-M-d dddd", new CultureInfo("zh-CN"));
            richTextBox1.Text += "DateTime.Now dateString1 : " + dateString1 + "\n";
            richTextBox1.Text += "DateTime.Now dateString2 : " + dateString2 + "\n";

            //------------------------------------------------------------  # 60個

            var japaneseCal = new JapaneseCalendar();
            ci = new CultureInfo("ja-JP");
            ci.DateTimeFormat.Calendar = japaneseCal;

            var date = new DateTime(1905, 2, 12);
            richTextBox1.Text += "Gregorian calendar date: " + date.ToString("d") + "\n";

            // Call the ToString(IFormatProvider) method.
            richTextBox1.Text += "Japanese calendar date: " + date.ToString("d", ci) + "\n";

            var date2 = new DateTime(2, 5, 10, japaneseCal);

            richTextBox1.Text += "Gregorian calendar date: " + date2.ToString("d") + "\n";
            richTextBox1.Text += "Japanese calendar date: " + date2.ToString("d", ci) + "\n";

            richTextBox1.Text += "Japanese calendar date: " + DateTime.Now.ToString("d", ci) + "\n";

            ci = new CultureInfo("ja-JP", true);
            ci.DateTimeFormat.Calendar = new JapaneseCalendar();
            DateTime dt_today = DateTime.Today;//當天時間

            // 西暦の出力方法
            richTextBox1.Text += dt_today + "\n";
            richTextBox1.Text += dt_today.ToString("yyyy/MM/dd") + "\n";

            // 和暦の出力方法
            richTextBox1.Text += dt_today.ToString("ggyy年MM月dd日(ddd)", ci) + "\n";
        }

        string getChineseTime(int hour)
        {
            //地支時間做成數組
            string[] CTime = "子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥".Split('|');
            return "【" + CTime[hour / 2] + "時】";
        }

        //------------------------------------------------------------  # 60個

        private void button21_Click(object sender, EventArgs e)
        {
        }

        //------------------------------------------------------------  # 60個

        private void button22_Click(object sender, EventArgs e)
        {
            //量測經歷時間 碼表 Stopwatch

            //量測時間1  用 Stopwatch
            Stopwatch sw = new Stopwatch();

            sw.Start();

            //XXXXXXXXXXX	//do something

            sw.Stop();

            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";  // 總秒數

            sw.Reset();	//碼表歸零

            sw.Start();
            //XXXXXXXXXXX	//do something
            sw.Stop();
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";  // 總秒數
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalMilliseconds.ToString() + " 毫秒\n";  // 總毫秒數

            //------------------------------------------------------------  # 60個

            //瞭解程式執行時間 

            sw = new Stopwatch();
            //long num = 0;
            sw.Reset();
            sw = Stopwatch.StartNew();
            //要測速的程式放這裡
            sw.Stop();
            TimeSpan el = sw.Elapsed;
            richTextBox1.Text += "花費 : " + el.ToString() + "\n";
            long ms = sw.ElapsedMilliseconds;
            richTextBox1.Text += "花費 : " + ms.ToString() + " 毫秒\n";

            //補充說明: 不一定每次測到的時間都相同喔!
            //建議值: 超過100毫秒就有點太慢囉…. (電腦爛會Lag更長)

            //------------------------------------------------------------  # 60個

            Stopwatch loadingWatch = new Stopwatch();
            loadingWatch.Start();

            //XXXXXXXXX

            loadingWatch.Stop();

            richTextBox1.Text += loadingWatch.ElapsedMilliseconds + "\n";

            //可以使用Reset()來重置計算時間.

            //------------------------------------------------------------  # 60個

            //量測時間2  用 TimeSpan
            DateTime start_time = DateTime.Now;  // 開始時間

            //XXXXXXXXXXX	//do something

            DateTime stop_time = DateTime.Now;  // 結束時間

            TimeSpan elapsed = stop_time - start_time;  // 取時間間隔

            richTextBox1.Text += "經過時間 : " + elapsed.TotalSeconds.ToString("0.00") + " 秒\n";  // 總秒數

            //------------------------------------------------------------  # 60個

            //量測時間
            int start = 0;
            start = Environment.TickCount;
            // Do stuff
            int duration = Environment.TickCount - start;
            richTextBox1.Text += "耗時 : " + (duration / 1000).ToString() + "." + (duration % 1000).ToString("D3") + " 秒\n";

            //------------------------------------------------------------  # 60個

            //計算程式執行的時間

            int URms = System.Environment.TickCount;

            //XXXXXXXXX

            richTextBox1.Text += "花費 : " + (Environment.TickCount - URms).ToString() + " ms 完成\n";

            //------------------------------------------------------------  # 60個

            DateTime LoginTime, LogoffTime;

            //取得停留時間
            TimeSpan ts = new TimeSpan();

            //取得目前登入的時間
            LoginTime = DateTime.Now;
            richTextBox1.Text += "登入時間 : " + LoginTime + "\n";

            // do something

            LogoffTime = DateTime.Now;
            richTextBox1.Text += "登出時間 : " + LogoffTime + "\n";

            //------------------------------------------------------------  # 60個

            /*
            DateTime結構的Subtract()方法計算時間間隔
            時間間隔(ts) = 登出時間 - 登入時間
            再以所得結果，換算時、分、秒
            */

            ts = LogoffTime.Subtract(LoginTime);  // dt減dt得到ts
            richTextBox1.Text += "您在此停留 : " + ts.Hours.ToString() + " 小時 " + ts.Minutes.ToString() + " 分鐘 " + ts.Seconds.ToString() + " 秒\n";

            //------------------------------------------------------------  # 60個

        }

        //------------------------------------------------------------  # 60個

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

        }

        private void button29_Click(object sender, EventArgs e)
        {
            //簡易測試, OK後再搬走


            //------------------------------------------------------------  # 60個


        }

        //------------------------------------------------------------  # 60個

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

            string mesg = string.Empty;

            dt = DateTime.Now;
            mesg += "臺灣本地時間\n";
            mesg += "時間 : " + dt.ToLongTimeString() + "\n";
            mesg += "日期 : " + dt.ToShortDateString() + "\n\n";

            DateTimeOffset local_offset = new DateTimeOffset(dt);
            DateTimeOffset utc_offset = local_offset.ToUniversalTime();
            mesg += "格林威治標準時間(GMT)\n";
            mesg += "時間 : " + utc_offset.DateTime.ToLongTimeString() + "\n";
            mesg += "日期 : " + utc_offset.DateTime.ToShortDateString() + "\n";

            lb_time.Text = mesg;
        }

        //------------------------------------------------------------  # 60個

        /*
        實現的根據年月日計算星期幾的函數
        基姆拉爾森計算公式
        W= (d 2*m 3*(m 1)/5 y y/4-y/100 y/400) mod 7
        在公式中d表示日期中的日數，m表示月份數，y表示年數。
        注意 : 在公式中有個與其他公式不同的地方 : 把一月和二月看成是上一年的十三月和十四月，
        例 : 如果是2004-1-10則換算成 : 2003-13-10來代入公式計算。
        */

        //根據年月日計算星期幾的函數
        //基姆拉爾森計算公式, 外文名是Kim larsen calculation formula。

        //在公式中d表示日期中的日數，m表示月份數，y表示年數。注意 : 在公式中有個與其他公式不同的地方 : 
        //把一月和二月看成是上一年的十三月和十四月，例 : 如果是2004-1-10則換算成 : 2003-13-10來代入公式計算。

        string CalculateWeekDay(int y, int m, int d)
        {
            if (m == 1)
            {
                m = 13;
            }
            if (m == 2)
            {
                m = 14;
            }
            int week = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400 + 1) % 7;

            string weekstr = "";
            switch (week)
            {
                case 0: weekstr = "星期日"; break;
                case 1: weekstr = "星期一"; break;
                case 2: weekstr = "星期二"; break;
                case 3: weekstr = "星期三"; break;
                case 4: weekstr = "星期四"; break;
                case 5: weekstr = "星期五"; break;
                case 6: weekstr = "星期六"; break;
            }
            return weekstr;
        }

        // Return the number of years, months, days, hours, minutes, seconds,
        // and milliseconds you need to add to from_date to get to_date.
        private void GetElapsedTime(DateTime from_date, DateTime to_date, out int years, out int months, out int days, out int hours, out int minutes, out int seconds, out int milliseconds)
        {
            // If from_date > to_date, switch them around.
            if (from_date > to_date)
            {
                GetElapsedTime(to_date, from_date, out years, out months, out days, out hours, out minutes, out seconds, out milliseconds);
                years = -years;
                months = -months;
                days = -days;
                hours = -hours;
                minutes = -minutes;
                seconds = -seconds;
                milliseconds = -milliseconds;
            }
            else
            {
                // Handle the years.
                years = to_date.Year - from_date.Year;

                // See if we went too far.
                DateTime test_date = from_date.AddMonths(12 * years);
                if (test_date > to_date)
                {
                    years--;
                    test_date = from_date.AddMonths(12 * years);
                }

                // Add months until we go too far.
                months = 0;
                while (test_date <= to_date)
                {
                    months++;
                    test_date = from_date.AddMonths(12 * years + months);
                }
                months--;

                // Subtract to see how many more days,
                // hours, minutes, etc. we need.
                from_date = from_date.AddMonths(12 * years + months);
                TimeSpan ts = to_date - from_date;
                days = ts.Days;
                hours = ts.Hours;
                minutes = ts.Minutes;
                seconds = ts.Seconds;
                milliseconds = ts.Milliseconds;
            }
        }

        //y－年，m－月，d－日期
        string CaculateWeekDay(int y, int m, int d)
        {
            if (m == 1)
            {
                m = 13;
            }
            if (m == 2)
            {
                m = 14;
            }
            //基姆拉爾森計算公式
            int week = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400 + 1) % 7;
            string weekstr = "";
            switch (week)
            {
                case 0: weekstr = "星期日"; break;
                case 1: weekstr = "星期一"; break;
                case 2: weekstr = "星期二"; break;
                case 3: weekstr = "星期三"; break;
                case 4: weekstr = "星期四"; break;
                case 5: weekstr = "星期五"; break;
                case 6: weekstr = "星期六"; break;
                case 7: weekstr = "星期日"; break;
            } return weekstr;
        }

        // Select an item containing the target string.
        private object FindItemContaining(IEnumerable items, string target)
        {
            foreach (object item in items)
            {
                if (item.ToString().Contains(target))
                {
                    return item;
                }
            }
            return null;
        }

        //本年第幾周
        private int WeekOfYear()
        {
            DateTime dt = DateTime.Now;
            int firstWeekend = Convert.ToInt32(DateTime.Parse(dt.Year + "-1-1").DayOfWeek);
            int weekDay = firstWeekend == 0 ? 1 : (7 - firstWeekend + 1);
            int currentDay = dt.DayOfYear;
            int current_week = Convert.ToInt32(Math.Ceiling((currentDay - weekDay) / 7.0)) + 1;
            return current_week;
        }

        //前幾周的周一和周日
        private void FEDayInLastWeek()
        {
            int N = 3;//前幾周引數
            DateTime dt = DateTime.Now;
            int daysInWeek = (int)dt.DayOfWeek == 0 ? 7 : (int)dt.DayOfWeek;//當前周第幾天,注釋:周日為0

            for (int i = N; i > 0; i--)
            {
                //起始日期
                DateTime firstDay = dt.AddDays(1 - (7 * i + daysInWeek));
                DateTime lastDay = dt.AddDays(7 - (7 * i + daysInWeek));
            }
        }

        //本周一和當前日
        private void FristDayToNowInThisWeek()
        {
            int daysInWeek = (int)DateTime.Now.DayOfWeek == 0 ? 7 : (int)DateTime.Now.DayOfWeek;//當前周第幾天,注釋:周日為0

            //起始日期
            DateTime firstDay = DateTime.Now.AddDays(1 - daysInWeek);
            DateTime lastDay = DateTime.Now;
        }

        //------------------------------------------------------------  # 60個

        private void timer_countdown_Tick(object sender, EventArgs e)
        {
            TimeSpan ts = dtTarget.Subtract(DateTime.Now);  // dt減dt得到ts

            string diffHour = Convert.ToString(ts.Hours);
            string diffMin = Convert.ToString(ts.Minutes);
            string diffSec = Convert.ToString(ts.Seconds);
            this.Text = "距離 " + dtTarget.ToString() + " 還有 " + diffHour + " 時 " + diffMin + " 分 " + diffSec + " 秒";
        }

        //------------------------------------------------------------  # 60個

        //月相 ST
        private double ip;
        private double ag;
        private int JulianDate(int d, int m, int y)
        {
            int mm, yy;
            int k1, k2, k3;
            int j;

            yy = y - (int)((12 - m) / 10);
            mm = m + 9;
            if (mm >= 12)
            {
                mm = mm - 12;
            }
            k1 = (int)(365.25 * (yy + 4712));
            k2 = (int)(30.6001 * mm + 0.5);
            k3 = (int)((int)((yy / 100) + 49) * 0.75) - 38;
            // 'j' for dates in Julian calendar:
            j = k1 + k2 + d + 59;
            if (j > 2299160)
            {
                // For Gregorian calendar:
                j = j - k3;  // 'j' is the Julian date at 12h UT (Universal Time)
            }
            return j;
        }

        private double MoonAge(int d, int m, int y)
        {
            int j = JulianDate(d, m, y);
            //Calculate the approximate phase of the moon
            ip = (j + 4.867) / 29.53059;
            ip = ip - Math.Floor(ip);
            //After several trials I've seen to add the following lines, 
            //which gave the result was not bad
            if (ip < 0.5)
            {
                ag = ip * 29.53059 + 29.53059 / 2;
            }
            else
            {
                ag = ip * 29.53059 - 29.53059 / 2;
            }
            // Moon's age in days
            ag = Math.Floor(ag) + 1;
            return ag;
        }

        public void ClearDraw()
        {
            if (pictureBox1.Image != null)
            {
                pictureBox1.Image = null;
            }
        }

        private void DrawMoon()
        {
            int Xpos, Ypos, Rpos;
            int Xpos1, Xpos2;
            double Phase;

            Phase = ip;

            // Width of 'bitmap1' Object = Width of 'pictureBox1' control
            int PageWidth = pictureBox1.Width;
            // Height of 'bitmap1' Object = Height of 'pictureBox1' control
            int PageHeight = pictureBox1.Height;
            // Initiate 'bitmap1' Object with size = size of control 'pictureBox1' control
            Bitmap bitmap1 = new Bitmap(PageWidth, PageHeight);
            // Create graphics object for alteration.
            Graphics g = Graphics.FromImage(bitmap1);

            Pen PenB = new Pen(Color.Black); // For darkness part of the moon
            Pen PenW = new Pen(Color.White); // For the lighted part of the moon

            for (Ypos = 0; Ypos <= 45; Ypos++)
            {
                Xpos = (int)(Math.Sqrt(45 * 45 - Ypos * Ypos));
                // Draw darkness part of the moon
                Point pB1 = new Point(90 - Xpos, Ypos + 90);
                Point pB2 = new Point(Xpos + 90, Ypos + 90);
                Point pB3 = new Point(90 - Xpos, 90 - Ypos);
                Point pB4 = new Point(Xpos + 90, 90 - Ypos);
                g.DrawLine(PenB, pB1, pB2);
                g.DrawLine(PenB, pB3, pB4);
                // Determine the edges of the lighted part of the moon
                Rpos = 2 * Xpos;
                if (Phase < 0.5)
                {
                    Xpos1 = -Xpos;
                    Xpos2 = (int)(Rpos - 2 * Phase * Rpos - Xpos);
                }
                else
                {
                    Xpos1 = Xpos;
                    Xpos2 = (int)(Xpos - 2 * Phase * Rpos + Rpos);
                }
                // Draw the lighted part of the moon
                Point pW1 = new Point(Xpos1 + 90, 90 - Ypos);
                Point pW2 = new Point(Xpos2 + 90, 90 - Ypos);
                Point pW3 = new Point(Xpos1 + 90, Ypos + 90);
                Point pW4 = new Point(Xpos2 + 90, Ypos + 90);
                g.DrawLine(PenW, pW1, pW2);
                g.DrawLine(PenW, pW3, pW4);
            }

            // Display the bitmap in the picture box.
            pictureBox1.Image = bitmap1;

            // Release graphics object
            PenB.Dispose();
            PenW.Dispose();
            g.Dispose();
            bitmap1 = null;
        }

        private void YourChoice(int year, int month, int day)
        {
            this.MoonAge(day, month, year);
        }

        private void ShowMoon(int year, int month, int day)
        {
            this.YourChoice(year, month, day);
            this.ClearDraw(); //clear pictureBox1 PictureBox
            this.DrawMoon(); //draw the moon
        }

        private void btn_moon_today_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            this.ShowMoon(dt.Year, dt.Month, dt.Day);
        }

        private void btn_moon_ok_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            bool conversionSuccessful = DateTime.TryParse(textBox4.Text, out dt);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "得到DateTime資料 : " + dt.ToString() + "\n";
                this.ShowMoon(dt.Year, dt.Month, dt.Day);
                //this.ShowMoon();
            }
            else
            {
                richTextBox1.Text += "DateTime.TryParse 失敗\n";
                richTextBox1.Text += "取得DateTime失敗 3\n";
            }
        }
    }
}

//6060
//richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
//------------------------------------------------------------  # 60個

//3030
//richTextBox1.Text += "------------------------------\n";  // 30個
//------------------------------  # 30個

/*  可搬出

*/

/*

//------------------------------------------------------------  # 60個

"-123年4月5日"
先自己解看看
若是年份是負的 先反相再交DateTime.Parse()來解
解出來的結果 再反相
                          
//------------------------------------------------------------  # 60個

String to DateTime
1. Parse : 將指定的日期時間字串，轉換成相對應的 DateTime 型別。若轉換失敗會產生 FormatException 。
2. TryParse : 將指定的日期時間字串，轉換成相對應的 DateTime 型別，回傳值表示轉換是否成功。
3. ParseExact : 將指定的日期時間字串，轉換成相對應的 DateTime 型別，字串表示的格式必須完全符合指定的格式，否則會擲回例外狀況。
4. TryParseExact : 將指定的日期時間字串，轉換成相對應的 DateTime 型別，字串表示的格式必須完全符合指定的格式，回傳值表示轉換是否成功。
  
//------------------------------------------------------------  # 60個

string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
string filename = "imsLink_log.long." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + 
string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
richTextBox1.Text += "PC時間 : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");
string filename = "imsLink_log." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + ".txt";

*/

/*
//計算時間間隔

//一戰
//1914年7月28日－1918年11月11日（4年3個月又2周） 
DateTime ww1_st = new DateTime(1914, 7, 28, 8, 12, 34);
DateTime ww1_sp = new DateTime(1918, 11, 11, 17, 8, 17);
TimeSpan ww1_time = ww1_sp - ww1_st;
richTextBox1.Text += "一戰經歷時間 : " + ww1_time.ToString("T") + "\n";
//換算成n年n月n日

//第一次世界大戰
//1914年7月28日－1918年11月11日（4年3個月又2周） 
//第二次世界大戰
//1939年9月1日—1945年9月2日（6年又1天）
//韓戰	 1950年 6月25日	~ 1953年7月27日 簽署停戰協定	4yr
//韓戰   1950年 6月25日 ~ 1953年7月27日（3年1個月又2天）
//日俄戰爭
//1904年2月8日－1905年9月5日
*/

