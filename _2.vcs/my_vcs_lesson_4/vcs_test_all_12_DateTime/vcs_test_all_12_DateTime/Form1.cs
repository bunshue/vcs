using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Globalization; //for CultureInfo   //for 民國記年

namespace vcs_test_all_12_DateTime
{
    public partial class Form1 : Form
    {
        int flag_timer_counter_down_enable = 0;
        int wait_seconds = 0;
        System.DateTime dt_timer_st = System.DateTime.Now;
        DateTime start_time = DateTime.Now;
        public Form1()
        {
            InitializeComponent();
            LoginTime = DateTime.Now; //取得目前登入的時間
            richTextBox1.Text += "登入時間： " + LoginTime.ToString() + "\n";
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //DateTime dt = new DateTime(年, 月, 日);
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒);
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒, 毫秒);
            DateTime dt1 = new DateTime(2019, 1, 1, 0, 0, 0);
            DateTime dt2 = new DateTime(2037, 12, 30, 12, 34, 56, 15);
            DateTime dt3 = DateTime.Now;

            //TimeSpan 取時間差，只能取到天數，不能算月數、年數
            TimeSpan ts1 = dt2 - dt1;
            TimeSpan ts2 = dt3 - dt1;

            richTextBox1.Text += "兩個時間相距：" + ts1.ToString() + "\n";
            richTextBox1.Text += "兩個時間相距：" + ts1.TotalSeconds.ToString() + " 秒\n";

            richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";
            richTextBox1.Text += "與現在相距：" + ts2.TotalSeconds.ToString() + " 秒\n";
            TimeSpan interval = DateTime.Now - DateTime.Now.Date;
            //richTextBox1.Text += DateTime.Now.ToString() + "\n";
            //richTextBox1.Text += DateTime.Now.Date.ToString() + "\n";
            richTextBox1.Text += "今天經過時間 "+ interval.ToString() + "\n";
            richTextBox1.Text += "今天經過時間 " + interval.TotalSeconds.ToString() + " 秒\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Timestamp 與 DateTime 互轉
            // 現在時間轉秒數
            //double timestamp = (DateTime.Now.AddHours(-8) - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
            double timestamp = (DateTime.Now.AddHours(-0) - new DateTime(2016, 5, 5, 23, 0, 0)).TotalSeconds;

            richTextBox1.Text += "從某時間距今秒數" + timestamp.ToString() + "\n";

            // 秒數轉 DateTime
            timestamp = 2400;
            DateTime dt = (new DateTime(2016, 5, 5, 23, 0, 0)).AddHours(0).AddSeconds(timestamp);

            richTextBox1.Text += "時間：" + dt.ToString() + "秒" + "\n";

        }

        private void button4_Click(object sender, EventArgs e)
        {
            //C# 計算差異天數
            string startDate = "2007/07/01";
            string endDate = "2007/07/07";
            DateTime dtStart = DateTime.ParseExact(startDate, "yyyy/MM/dd", null);
            DateTime dtEnd = DateTime.ParseExact(endDate, "yyyy/MM/dd", null);
            // 計算差異天數
            TimeSpan tsDay = dtEnd - dtStart;
            int dayCount = (int)tsDay.TotalDays;
            richTextBox1.Text += "相差" + dayCount.ToString() + "天" + "\n";

        }

        private void button5_Click(object sender, EventArgs e)
        {
            string data = "";
            data += "DateTime.Now.ToString(\"yyyyMMdd\")                       20080923" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"yyyy/MM/dd\")                     2008/09/23" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"yyyy/M/d\")                          2008/9/23" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"yyyy/MM/dd HH:mm:ss\")    2008/09/23 13:03:03" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"T\")                                      下午 01:04:43" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"t\")                                       下午 01:05" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"tt\")                                      下午" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"yyyy/MM/dd tt hh:mm:ss\")  2008/09/23 下午 01:07:27" + Environment.NewLine;
            data += "DateTime.Now.ToString(\"yyyyMMddhhmmss\")          20080923010921" + Environment.NewLine;
            data += "HH為24小時制，hh為12小時制" + Environment.NewLine;
            richTextBox1.Text += data;
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string sDate = "20100504";
            DateTime NewDate = DateTime.ParseExact(sDate, "yyyyMMdd", null, System.Globalization.DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間：" + NewDate.ToString() + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("yyyy" + '-' + "MM" + '-' + "dd" + " HH" + ':' + "mm" + ':' + "ss") + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //DateTime dt = new DateTime(年, 月, 日);
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒);
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒, 毫秒);
            DateTime dt1 = new DateTime(2017, 1, 31);
            DateTime dt2 = new DateTime(2017, 2, 1, 2, 3, 4, 15);
            DateTime dt3 = DateTime.Now;
            TimeSpan ts1 = dt2 - dt1;
            TimeSpan ts2 = dt3 - dt1;
            richTextBox1.Text += "兩個時間相距：" + ts1.ToString() + "\n";
            richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";

        }

        private void button10_Click(object sender, EventArgs e)
        {
            string sDate = "2006/03/11";
            int year = 0;
            int month = 0;
            int day = 0;
            DateTime NewDate = DateTime.ParseExact(sDate, "yyyy/MM/dd", null, System.Globalization.DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間：" + NewDate.ToString() + "\n";
            richTextBox1.Text += "年：" + NewDate.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + NewDate.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + NewDate.Day.ToString() + "\n";
            year = NewDate.Year;
            month = NewDate.Month;
            day = NewDate.Day;

            richTextBox1.Text += year.ToString() + "  " + month.ToString() + "   " + day.ToString() + "\n\n";
            calculate_date_diff(year, month, day);


        }

        public void calculate_date_diff(int year, int month, int day)
        {
            int year_now = 0;
            int month_now = 0;
            int day_now = 0;
            int year_diff = 0;
            int month_diff = 0;
            int day_diff = 0;
            DateTime now_date = DateTime.Now;
            year_now = now_date.Year;
            month_now = now_date.Month;
            day_now = now_date.Day;
            year_diff = year_now - year;
            month_diff = month_now - month;
            day_diff = day_now - day;

            if (day_diff < 0)
            {
                day_diff += 30;
                month_diff -= 1;
            }
            if (month_diff < 0)
            {
                month_diff += 12;
                year_diff -= 1;
            }

            //richTextBox1.Text += "diff year = " + year_diff.ToString() + "\n";
            //richTextBox1.Text += "diff month = " + month_diff.ToString() + "\n";
            //richTextBox1.Text += "diff day = " + day_diff.ToString() + "\n";
            richTextBox1.Text += "距今：" + year_diff.ToString() + " 年 " + month_diff.ToString() + "月 " + day_diff.ToString() + "日\n";



        }

        private void button8_Click(object sender, EventArgs e)
        {
            System.DateTime dt = System.DateTime.Now;
            richTextBox1.Text += "全部格式1a：" + DateTime.Now.ToString() + "\n";

            richTextBox1.Text += "全部格式1b：" + dt.ToString() + "\n";
            richTextBox1.Text += "全部格式2：" + dt.ToShortTimeString() + "\n";
            richTextBox1.Text += "全部格式3：" + dt.ToShortDateString() + "\n";
            //richTextBox1.Text += "全部格式4：" + dt.ToBinary() + "\n";
            //richTextBox1.Text += "全部格式5：" + dt.ToFileTime() + "\n";
            //richTextBox1.Text += "全部格式6：" + dt.ToFileTimeUtc() + "\n";
            richTextBox1.Text += "全部格式7：" + dt.ToLocalTime() + "\n";
            richTextBox1.Text += "全部格式8：" + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "全部格式9：" + dt.ToLongTimeString() + "\n";
            richTextBox1.Text += "全部格式10：" + dt.ToOADate() + "\n";
            richTextBox1.Text += "全部格式11：" + dt.ToShortDateString() + "\n";
            richTextBox1.Text += "全部格式12：" + dt.ToShortTimeString() + "\n";


            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "天：" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "星：" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
            richTextBox1.Text += "毫秒：" + dt.Millisecond.ToString() + "\n";
            richTextBox1.Text += "Ticks：" + dt.Ticks.ToString() + "\n";
            richTextBox1.Text += "TimeOfDay：" + dt.TimeOfDay.ToString() + "\n";




            System.DateTime ThisMonBeginDay = new System.DateTime(dt.Year, dt.Month, 1);
            System.DateTime ThisMonEndDay = ThisMonBeginDay.AddMonths(1).AddDays(-1);
            richTextBox1.Text += "本月月底日期:" + ThisMonEndDay.Day.ToString() + "\n";

            richTextBox1.Text += "本月月底日期:" + DateTime.DaysInMonth(DateTime.Now.Year, DateTime.Now.Month).ToString() + "\n";

        }

        private void button15_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

            richTextBox1.Text += "D\t完整日期\t" + dt.ToString("D") + "\n";
            richTextBox1.Text += "d\t簡短日期\t" + dt.ToString("d") + "\n";
            richTextBox1.Text += "F\t完整日期及時間\t" + dt.ToString("F") + "\n";
            richTextBox1.Text += "G\t一般日期\t" + dt.ToString("G") + "\n";
            richTextBox1.Text += "M\t月日格式\t" + dt.ToString("M") + "\n";
            richTextBox1.Text += "T\t完整時間\t" + dt.ToString("T") + "\n";
            richTextBox1.Text += "t\t簡短時間\t" + dt.ToString("t") + "\n";
            richTextBox1.Text += "Y\t年月格式\t" + dt.ToString("Y") + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Parse(textBox1.Text);
            richTextBox1.Text += "D\t完整日期\t" + dt.ToString("D") + "\n";
            richTextBox1.Text += "d\t簡短日期\t" + dt.ToString("d") + "\n";
            richTextBox1.Text += "F\t完整日期及時間\t" + dt.ToString("F") + "\n";
            richTextBox1.Text += "G\t一般日期\t" + dt.ToString("G") + "\n";
            richTextBox1.Text += "M\t月日格式\t" + dt.ToString("M") + "\n";
            richTextBox1.Text += "T\t完整時間\t" + dt.ToString("T") + "\n";
            richTextBox1.Text += "t\t簡短時間\t" + dt.ToString("t") + "\n";
            richTextBox1.Text += "Y\t年月格式\t" + dt.ToString("Y") + "\n";

        }

        private void button13_Click(object sender, EventArgs e)
        {
            DateTime departure = new DateTime(2006, 3, 11, 9, 15, 20);
            DateTime arrival = new DateTime(2017, 3, 15, 22, 47, 0);
            TimeSpan travelTime = arrival - departure;
            richTextBox1.Text += "time = " + travelTime.ToString("T") + "\n";

        }

        private void button12_Click(object sender, EventArgs e)
        {
            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";

        }

        private void button11_Click(object sender, EventArgs e)
        {
            System.Globalization.TaiwanCalendar TC = new System.Globalization.TaiwanCalendar();
            System.Globalization.TaiwanLunisolarCalendar TA = new System.Globalization.TaiwanLunisolarCalendar();

            DateTime dt = DateTime.Now;
            string message = "";
            message += string.Format("{0}", dt.Year) + "\n";
            message += ("西元年:" + dt.Year.ToString()) + "\n";
            message += ("民國年:" + TC.GetYear(dt)) + "\n";
            message += (string.Format("西元:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";
            message += (string.Format("民國:{0}/{1}/{2}", TC.GetYear(dt), TC.GetMonth(dt), TC.GetDayOfMonth(dt))) + "\n";
            message += (string.Format("農曆:{0}/{1}/{2}", TA.GetYear(dt), TA.GetMonth(dt), TA.GetDayOfMonth(dt))) + "\n";

            richTextBox1.Text += message;
        }

        private void button20_Click(object sender, EventArgs e)
        {
            //C#計算日期差距
            //C#中要計算兩個日期間的差距必須要透過 TimeSpan 來達成
            DateTime dt1 = Convert.ToDateTime("2006/3/11");
            TimeSpan ts = DateTime.Now - dt1;
            string message = "";
            message += "距今 " + ts.Days + " 天";
            message += Environment.NewLine;
            richTextBox1.Text += message;
        }

        private void button19_Click(object sender, EventArgs e)
        {
            string message = "";
            DateTime dt = DateTime.Now;


            message += dt.ToString() + "\n";//2005-11-5 13:21:25
            message += dt.ToFileTime().ToString() + "\n";//127756416859912816
            message += dt.ToFileTimeUtc().ToString() + "\n";//127756704859912816
            message += dt.ToLocalTime().ToString() + "\n";//2005-11-5 21:21:25
            message += dt.ToLongDateString().ToString() + "\n";//2005年11月5日
            message += dt.ToLongTimeString().ToString() + "\n";//13:21:25
            message += dt.ToOADate().ToString() + "\n";//38661.5565508218
            message += dt.ToShortDateString().ToString() + "\n";//2005-11-5
            message += dt.ToShortTimeString().ToString() + "\n";//13:21
            message += dt.ToUniversalTime().ToString() + "\n";//2005-11-5 5:21:25
            message += dt.Year.ToString() + "\n";//2005
            message += dt.Date.ToString() + "\n";//2005-11-5 0:00:00
            message += dt.DayOfWeek.ToString() + "\n";//Saturday
            message += dt.DayOfYear.ToString() + "\n";//309
            message += dt.Hour.ToString() + "\n";//13
            message += dt.Millisecond.ToString() + "\n";//441
            message += dt.Minute.ToString() + "\n";//30
            message += dt.Month.ToString() + "\n";//11
            message += dt.Second.ToString() + "\n";//28
            message += dt.Ticks.ToString() + "\n";//632667942284412864
            message += dt.TimeOfDay.ToString() + "\n";//13:30:28.4412864
            message += dt.ToString() + "\n";//2005-11-5 13:47:04
            message += dt.AddYears(1).ToString() + "\n";//2006-11-5 13:47:04
            message += dt.AddDays(1.1).ToString() + "\n";//2005-11-6 16:11:04
            message += dt.AddHours(1.1).ToString() + "\n";//2005-11-5 14:53:04
            message += dt.AddMilliseconds(1.1).ToString() + "\n";//2005-11-5 13:47:04
            message += dt.AddMonths(1).ToString() + "\n";//2005-12-5 13:47:04
            message += dt.AddSeconds(1.1).ToString() + "\n";//2005-11-5 13:47:05
            message += dt.AddMinutes(1.1).ToString() + "\n";//2005-11-5 13:48:10
            message += dt.AddTicks(1000).ToString() + "\n";//2005-11-5 13:47:04
            message += dt.CompareTo(dt).ToString() + "\n";//0


            //message += dt.Add(?).ToString() + "\n";//问号为一个时间段

            message += dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            message += dt.Equals(dt).ToString() + "\n";//True
            message += dt.GetHashCode().ToString() + "\n";//1474088234
            message += dt.GetType().ToString() + "\n";//System.DateTime
            message += dt.GetTypeCode().ToString() + "\n";//DateTime

            message += dt.GetDateTimeFormats('s')[0].ToString() + "\n";//2005-11-05T14:06:25
            message += dt.GetDateTimeFormats('t')[0].ToString() + "\n";//14:06
            message += dt.GetDateTimeFormats('y')[0].ToString() + "\n";//2005年11月
            message += dt.GetDateTimeFormats('D')[0].ToString() + "\n";//2005年11月5日
            message += dt.GetDateTimeFormats('D')[1].ToString() + "\n";//2005 11 05
            //message += dt.GetDateTimeFormats('D')[2].ToString() + "\n";//星期六 2005 11 05
            //message += dt.GetDateTimeFormats('D')[3].ToString() + "\n";//星期六 2005年11月5日
            message += dt.GetDateTimeFormats('M')[0].ToString() + "\n";//11月5日
            message += dt.GetDateTimeFormats('f')[0].ToString() + "\n";//2005年11月5日 14:06
            message += dt.GetDateTimeFormats('g')[0].ToString() + "\n";//2005-11-5 14:06
            message += dt.GetDateTimeFormats('r')[0].ToString() + "\n";//Sat, 05 Nov 2005 14:06:25 GMT

            message += string.Format("{0:d}", dt) + "\n";//2005-11-5
            message += string.Format("{0:D}", dt) + "\n";//2005年11月5日
            message += string.Format("{0:f}", dt) + "\n";//2005年11月5日 14:23
            message += string.Format("{0:F}", dt) + "\n";//2005年11月5日 14:23:23
            message += string.Format("{0:g}", dt) + "\n";//2005-11-5 14:23
            message += string.Format("{0:G}", dt) + "\n";//2005-11-5 14:23:23
            message += string.Format("{0:M}", dt) + "\n";//11月5日
            message += string.Format("{0:R}", dt) + "\n";//Sat, 05 Nov 2005 14:23:23 GMT
            message += string.Format("{0:s}", dt) + "\n";//2005-11-05T14:23:23
            message += string.Format("{0:t}", dt) + "\n";//14:23
            message += string.Format("{0:T}", dt) + "\n";//14:23:23
            message += string.Format("{0:u}", dt) + "\n";//2005-11-05 14:23:23Z
            message += string.Format("{0:U}", dt) + "\n";//2005年11月5日 6:23:23
            message += string.Format("{0:Y}", dt) + "\n";//2005年11月
            message += string.Format("{0}", dt) + "\n";//2005-11-5 14:23:23
            message += string.Format("{0:yyyyMMddHHmmssffff}", dt) + "\n";

            message += Environment.NewLine;
            richTextBox1.Text += message;

        }

        private void button18_Click(object sender, EventArgs e)
        {
            string message = "";
            message += "C# 怎么显示中文格式的日期、星期几\n";
            message += "//该语句显示的为英文格式\n";
            message += DateTime.Now.DayOfWeek.ToString() + "\n";


            message += "//顯示中文格式星期幾 簡中1\n";
            message += DateTime.Now.ToString("ddd", new System.Globalization.CultureInfo("zh-cn")) + "\n";      //3個d

            message += "//顯示中文格式星期幾 簡中2\n";
            message += DateTime.Now.ToString("dddd", new System.Globalization.CultureInfo("zh-cn")) + "\n";     //更新简捷的显示中文格式星期几用4个dddd就可以搞定了，不需任何拼凑

            message += "//顯示中文格式星期幾 正中1\n";
            message += DateTime.Now.ToString("ddd", new System.Globalization.CultureInfo("zh-tw")) + "\n";      //3個d

            message += "//顯示中文格式星期幾 正中2\n";
            message += DateTime.Now.ToString("dddd", new System.Globalization.CultureInfo("zh-tw")) + "\n";     //4個d

            message += "//顯示日文格式星期幾\n";
            message += DateTime.Now.ToString("ddd", new System.Globalization.CultureInfo("ja")) + "\n";

            message += "//顯示美語格式星期幾\n";
            message += DateTime.Now.ToString("ddd", new System.Globalization.CultureInfo("en-us")) + "\n";

            message += "//VS2005后显示星期的新方法是\n";
            message += "星期" + DateTime.Now.DayOfWeek.ToString(("d")) + "\n";

            message += "////显示中文格式的日期\n";

            message += DateTime.Now.ToLongDateString() + "\n";          // 显示格式为"2008年1月1日"

            message += DateTime.Now.ToString("yyyy年MM月dd日") + "\n"; // 显示格式为"2008年01月01日"，注意：格式字符串中的字母大小写不能错

            richTextBox1.Text += message;

        }

        private void button22_Click(object sender, EventArgs e)
        {
            DateTime timeBirth;
            string birthstr = "3/11/2006 9:15:30 AM";
            timeBirth = DateTime.Parse(birthstr);

            richTextBox1.Text += "生日: " + timeBirth.ToString() + "\n";

            TimeSpan span;
            span = DateTime.Now - timeBirth;

            richTextBox1.Text += "經歷時間: " + span.ToString() + "\n";

        }

        private void button21_Click(object sender, EventArgs e)
        {
            System.DateTime dt = System.DateTime.Now;
            richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
            richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

            //現在日期加天數寫法(本例為加5天):
            System.DateTime Add5Day = dt.AddDays(5);
            richTextBox1.Text += "現在日期加5天： " + Add5Day.ToLongDateString() + Environment.NewLine;

            //現在時間加小時寫法(本例為加12個小時):
            System.DateTime Add12Hours = dt.AddHours(12);
            richTextBox1.Text += "現在時間加12小時： " + Add12Hours.ToLongTimeString() + Environment.NewLine;

            //現在時間減分鐘寫法(本例為減30分鐘):
            System.DateTime Minus30Minutes = dt.AddMinutes(-30);
            richTextBox1.Text += "現在時間減30分鐘： " + Minus30Minutes.ToLongTimeString() + Environment.NewLine;
        }

        private void button24_Click(object sender, EventArgs e)
        {
            string str = string.Empty;
            TimeSpan span;
            span = DateTime.Now - start_time;

            richTextBox1.Text += "程式啟動時間: " + start_time.ToString() + " 秒\n";
            richTextBox1.Text += "按鍵經歷時間: " + span.ToString() + " 秒\n";
            str = span.ToString();
            richTextBox1.Text += "相距時間: " + str + "\n";
            str = str.Substring(0, str.IndexOf("."));
            richTextBox1.Text += "相距時間(去掉尾數): " + str + "\n";

        }

        private void button17_Click(object sender, EventArgs e)
        {
            DateTime LastSalaryDay = new DateTime(DateTime.Now.Year, DateTime.Now.Month, 5);
            DateTime NextSalaryDay = new DateTime(DateTime.Now.AddMonths(1).Year, DateTime.Now.AddMonths(1).Month, 5);

            MessageBox.Show("上次發薪日：" + LastSalaryDay.ToString("yyyy/MM/dd"));
            TimeSpan ts1 = DateTime.Now - LastSalaryDay;

            MessageBox.Show("經過了 " + ts1.Days + " 天");

            MessageBox.Show("下次發薪日：" + NextSalaryDay.ToString("yyyy/MM/dd"));

            //用大的日期 減小的日期
            TimeSpan ts2 = DateTime.Now - NextSalaryDay;    //小的日期減大的日期

            MessageBox.Show("距離下次發薪日還有" + Math.Abs(ts2.Days) + " 天");//距離幾天一定是正的 用Math.Abs取絕對值

        }

        private void button16_Click(object sender, EventArgs e)
        {
            //計算兩個時間差
            DateTime sDate = Convert.ToDateTime("2010-10-15 15:50:39");
            DateTime eDate = Convert.ToDateTime("2010-10-25 15:50:39");
            TimeSpan ts = sDate - eDate;
            double days = ts.TotalDays;
            richTextBox1.Text = "差距 " + Convert.ToInt32(days).ToString() + "天";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Interval = 1000;
            timer1.Enabled = true;

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            System.Globalization.CultureInfo cuinfo = new System.Globalization.CultureInfo("zh-TW");
            cuinfo.DateTimeFormat.Calendar = cuinfo.OptionalCalendars[2];
            //TextBox1.Text = DateTime.Now.ToString("yyyy/MM/dd", cuinfo);

            label1.Text = DateTime.Now.ToString();
            label2.Text = DateTime.Now.ToString("yyyy/MM/dd", cuinfo);
            label3.Text = DateTime.Now.ToString("HH:mm:ss");
            label4.Text = DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss");


            if (flag_timer_counter_down_enable == 1)
            {
                //DateTime dt3 = DateTime.Now;
                //TimeSpan ts2 = dt3 - dt_timer_st;
                TimeSpan interval = DateTime.Now - dt_timer_st;

                //richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";


                //TimeSpan interval = DateTime.Now - DateTime.Now.Date;
                //richTextBox1.Text += DateTime.Now.ToString() + "\n";
                //richTextBox1.Text += DateTime.Now.Date.ToString() + "\n";
                //richTextBox1.Text += "xxx " + interval.TotalSeconds.ToString();// +"\n";
                label5.Text = interval.TotalSeconds.ToString();

                if (interval.TotalSeconds > wait_seconds)
                {
                    this.TopMost = true;
                    label5.Text += "yyyy";
                }


            }


        }

        private void button23_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += DateTime.Now.ToString("yyyy/MM/dd", System.Globalization.DateTimeFormatInfo.InvariantInfo) + "\n";
        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "The selected value is " + dateTimePicker1.Value + "\n";
            richTextBox1.Text += "The selected value is " + dateTimePicker1.Text + "\n";
            richTextBox1.Text += "The day of the week is " + dateTimePicker1.Value.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "The day of the year is " + dateTimePicker1.Value.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "Millisecond is: " + dateTimePicker1.Value.Millisecond.ToString() + "\n";

        }

        private void button30_Click(object sender, EventArgs e)
        {
            //dateTimePicker1.Value = new DateTime(2006, 3, 11);                //特定日期
            //dateTimePicker1.Value = Convert.ToDateTime("2006/3/11 9:15:30");  //特定日期與時間
            //this.dateTimePicker1.Value = DateTime.Today;                      //今天日期
            this.dateTimePicker1.Value = DateTime.Now;                          //現在時刻

        }

        private void button28_Click(object sender, EventArgs e)
        {
            DateTime dateTime1 = new DateTime(2006, 3, 11, 9, 15, 23, 34);
            richTextBox1.Text += "Now : " + DateTime.Now + "\n";
            richTextBox1.Text += "Today : " + DateTime.Today + "\n";

            richTextBox1.Text += "Date : " + dateTime1.Date + "\n";
            richTextBox1.Text += "Year : " + dateTime1.Year + "\n";
            richTextBox1.Text += "Month : " + dateTime1.Month + "\n";
            richTextBox1.Text += "Day : " + dateTime1.Day + "\n";
            richTextBox1.Text += "Hour : " + dateTime1.Hour + "\n";
            richTextBox1.Text += "Minute : " + dateTime1.Minute + "\n";
            richTextBox1.Text += "Second : " + dateTime1.Second + "\n";
            richTextBox1.Text += "Millisecond : " + dateTime1.Millisecond + "\n";

        }

        private void button27_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "電腦開機時間 : " + (Environment.TickCount / 1000).ToString() + " 秒\n";
        }

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + " 秒\n";
        }

        private void button25_Click(object sender, EventArgs e)
        {
            System.Globalization.CultureInfo culture = new System.Globalization.CultureInfo("ja-JP", true);
            culture.DateTimeFormat.Calendar = new System.Globalization.JapaneseCalendar();
            DateTime today = DateTime.Today;

            // 西暦の出力方法
            richTextBox1.Text += today + "\n";
            richTextBox1.Text += today.ToString("yyyy/MM/dd") + "\n";

            // 和暦の出力方法
            richTextBox1.Text += today.ToString("ggyy年MM月dd日(ddd)", culture) + "\n";
        }

        public struct Age
        {
            public int Years;
            public int Months;
            public int Days;
        }
        public static Age CalculateAge(DateTime birthDate, DateTime endDate)
        {
            if (birthDate.Date > endDate.Date)
            {
                throw new ArgumentException("birthDate cannot be higher then endDate", "birthDate");
            }

            int years = endDate.Year - birthDate.Year;
            int months = 0;
            int days = 0;

            // Check if the last year, was a full year.
            if (endDate < birthDate.AddYears(years) && years != 0)
            {
                years--;
            }

            // Calculate the number of months.
            birthDate = birthDate.AddYears(years);

            if (birthDate.Year == endDate.Year)
            {
                months = endDate.Month - birthDate.Month;
            }
            else
            {
                months = (12 - birthDate.Month) + endDate.Month;
            }

            // Check if last month was a complete month.
            if (endDate < birthDate.AddMonths(months) && months != 0)
            {
                months--;
            }

            // Calculate the number of days.
            birthDate = birthDate.AddMonths(months);

            days = (endDate - birthDate).Days;
            Age result;
            result.Years = years;
            result.Months = months;
            result.Days = days;
            return result;
        }

        private void button29_Click(object sender, EventArgs e)
        {
            try
            {   //可能會產生錯誤的程式區段
                DateTime dt = DateTime.Parse(textBox1.Text);
                richTextBox1.Text += dt.ToString() + "\n";
                Age myAge = CalculateAge(dt, DateTime.Now);
                richTextBox1.Text += "年 : " + myAge.Years.ToString() + "\n";
                richTextBox1.Text += "月 : " + myAge.Months.ToString() + "\n";
                richTextBox1.Text += "日 : " + myAge.Days.ToString() + "\n";

            }
            catch (Exception ex)
            {   //定義產生錯誤時的例外處理程式碼
                MessageBox.Show(ex.Message);
            }
            finally
            {
                //一定會被執行的程式區段
                richTextBox1.Text += "DateTime.Parse完成\n";
            }

        }

        private void button38_Click(object sender, EventArgs e)
        {
            //民國記年
            CultureInfo cui = new CultureInfo("zh-TW", true);
            cui.DateTimeFormat.Calendar = new TaiwanCalendar();
            richTextBox1.Text += dateTimePicker1.Value.ToString("yy/M/d", cui) + "\n";
        }

        private void button37_Click(object sender, EventArgs e)
        {
            DateTime MyEndDate = new DateTime(2020, 01, 01, 00, 00, 00);
            DateTime MyStartDate = DateTime.Now;
            TimeSpan MySpan = MyEndDate.Subtract(MyStartDate);
            string diffDay = Convert.ToString(MySpan.Days);
            string diffHour = Convert.ToString(MySpan.Hours);
            string diffMin = Convert.ToString(MySpan.Minutes);
            string diffSec = Convert.ToString(MySpan.Seconds);
            String MyInfo = "距離2020新年還有 " + diffDay + " 天 " + diffHour + " 時 " + diffMin + " 分 " + diffSec + " 秒 ";
            MessageBox.Show(MyInfo, "信息提示", MessageBoxButtons.OK, MessageBoxIcon.Information);

        }

        private void button36_Click(object sender, EventArgs e)
        {
            DateTime myBirthday = DateTime.ParseExact("2006/03/11", "yyyy/MM/dd", null);
            DateTime flakNow = DateTime.ParseExact("2018/02/01", "yyyy/MM/dd", null);
            Age myAge = CalculateAge(myBirthday, flakNow);
            richTextBox1.Text += "年 : " + myAge.Years.ToString() + "\n";
            richTextBox1.Text += "月 : " + myAge.Months.ToString() + "\n";
            richTextBox1.Text += "日 : " + myAge.Days.ToString() + "\n";

        }

        private void button35_Click(object sender, EventArgs e)
        {
            //日期時間相加減
            DateTime start = Convert.ToDateTime("1937-7-7");
            DateTime end = Convert.ToDateTime("1945-08-15");
            TimeSpan ts = end.Subtract(start); //兩時間天數相減
            double dayCount = ts.Days; //相距天數
            richTextBox1.Text += "相距天數： " + dayCount.ToString() + " 天\n";

        }

        DateTime LoginTime;
        DateTime LogoffTime;
        TimeSpan StayTime = new TimeSpan();
        private void button32_Click(object sender, EventArgs e)
        {
            LogoffTime = DateTime.Now;
            richTextBox1.Text += "登出時間： " + LogoffTime.ToString() + "\n";
            StayTime = LogoffTime.Subtract(LoginTime);
            richTextBox1.Text += "您在此停留了" + StayTime.Hours + "小時" + StayTime.Minutes + "分鐘" + StayTime.Seconds + "秒" + "\n";

        }

        private void button34_Click(object sender, EventArgs e)
        {
            this.TopMost = false;
            if (flag_timer_counter_down_enable == 1)
            {
                flag_timer_counter_down_enable = 0;
                button34.Text = "倒數";
            }
            else
            {
                flag_timer_counter_down_enable = 1;
                button34.Text = "停止";

                dt_timer_st = System.DateTime.Now;
                wait_seconds = int.Parse(textBox2.Text) * 60;
                richTextBox1.Text += "等待時間： " + wait_seconds.ToString() + Environment.NewLine;
            }


        }

        private void button43_Click(object sender, EventArgs e)
        {
            //比較兩個時間

            DateTime date1 = new DateTime(2016, 12, 9, 0, 0, 0);
            DateTime date2 = new DateTime(2016, 12, 9, 11, 0, 0);
            int result = DateTime.Compare(date1, date2);
            string relationship;

            if (result < 0)
                relationship = "is earlier than";
            else if (result == 0)
                relationship = "is the same time as";
            else
                relationship = "is later than";

            //Console.WriteLine("{0} {1} {2}", date1, relationship, date2);
            richTextBox1.Text += date1 + " " + relationship + " " + date2 + "\n";

        }

        private void button42_Click(object sender, EventArgs e)
        {
            //string st1 = "2010/05/30 12:13:50";
            //string st2 = "2018/09/20 14:14:30";
            string st1 = "2010/05/30";
            string st2 = "2018/09/20";
            DateTime dt1 = Convert.ToDateTime(st1);
            DateTime dt2 = Convert.ToDateTime(st2);

            if (DateTime.Compare(dt1, dt2) > 0)
            {
                richTextBox1.Text = st1 + " 晚於 " + st2 + "\n";
            }
            else
            {
                richTextBox1.Text = st1 + " 早於 " + st2 + "\n";
            }

        }

        private void button41_Click(object sender, EventArgs e)
        {
            //計算兩個時間差值的函數，傳回時間差的絕對值
            //計算兩個時間差值的函數，傳回時間差的絕對值

            //韓戰	 1950年 6月25日	———————————————————1953年7月27日 簽署停戰協定	4yr
            string st1 = "1950/6/25";
            string st2 = "1953/7/27";
            DateTime dt1 = Convert.ToDateTime(st1);
            DateTime dt2 = Convert.ToDateTime(st2);

            string result = DateDiff(dt1, dt2);
            richTextBox1.Text += "result = " + result + "\n";

        }

        private string DateDiff(DateTime DateTime1, DateTime DateTime2)
        {
            string dateDiff = null;
            try
            {
                TimeSpan ts1 = new TimeSpan(DateTime1.Ticks);
                TimeSpan ts2 = new TimeSpan(DateTime2.Ticks);
                TimeSpan ts = ts1.Subtract(ts2).Duration();
                dateDiff = ts.Days.ToString() + "天"
                + ts.Hours.ToString() + "小時"
                + ts.Minutes.ToString() + "分鐘"
                + ts.Seconds.ToString() + "秒";
            }
            catch
            {

            }
            return dateDiff;
        }

        private void button46_Click(object sender, EventArgs e)
        {
            DateTime d = new DateTime(2019, 1, 1);

            richTextBox1.Text += "2019/1/1 加一段時間後 : " + d.AddDays(3125).AddSeconds(14653 * 2).ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            int yy = -280;
            int dd = -1250;
            richTextBox1.Text += "2019/1/1 減一段時間後 : " + d.AddYears(yy).AddDays(dd).AddSeconds(14653 * 2).ToString() + "\n";

        }

   
    }
}


