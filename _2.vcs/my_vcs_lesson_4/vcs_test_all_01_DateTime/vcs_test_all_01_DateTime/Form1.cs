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

namespace vcs_test_all_01_DateTime
{
    public partial class Form1 : Form
    {
        DateTime LoginTime = DateTime.Now;
        DateTime dt_timer_st = DateTime.Now;
        DateTime start_time = DateTime.Now;  // 程式啟動時間
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
            richTextBox1.Text += "登入時間： " + LoginTime.ToString() + "\n";

            richTextBox1.Text += "現在時間 :\n";
            richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("yyyy" + '-' + "MM" + '-' + "dd" + " HH" + ':' + "mm" + ':' + "ss") + "\n";

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
            groupBox13.Location = new Point(x_st + dx * 3, y_st + dy * 0);//月相

            lb_time2.Location = new Point(x_st + dx * 3, y_st + dy * 3);

            groupBox9.Size = new Size(200, 160);
            groupBox9.Location = new Point(x_st + dx * 3, y_st + dy * 6);//Timer顯示時間

            richTextBox1.Size = new Size(400, 690);
            richTextBox1.Location = new Point(x_st + dx * 5 + 20, y_st + dy * 0);
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

            //建立DateTime
            DateTime dt = DateTime.Now;

            //DateTime dt = new DateTime(年, 月, 日);
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒);
            //DateTime dt = new DateTime(年, 月, 日, 時, 分, 秒, 毫秒);
            DateTime dt2 = new DateTime(2025, 12, 25);//指定時間, 年月日
            DateTime dt3 = new DateTime(2019, 1, 1, 0, 0, 0);//指定時間, 年月日時分秒毫秒
            DateTime dt4 = new DateTime(2037, 12, 30, 12, 34, 56, 15);//指定時間, 年月日時分秒毫秒

            richTextBox1.Text += "時間：" + dt.ToString() + "\n";
            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";

            richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + "\n";

            richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + "\n";
            richTextBox1.Text += "当前是否公历闰年 : " + DateTime.IsLeapYear(dt.Year) + "\n";


            richTextBox1.Text += DateTime.Now.ToString("yyyy/MM/dd HH:mm:ss") + "\n";
            richTextBox1.Text += DateTime.Now.ToString() + "\n";

        }

        void show_time_span(TimeSpan ts)
        {
            richTextBox1.Text += "時間間隔 : " + String.Format("{0} 日 {1} 時 {2} 分 {3} 秒 {4} 毫秒", ts.Days, ts.Hours, ts.Minutes, ts.Seconds, ts.Milliseconds) + "\n";
            richTextBox1.Text += "總日數 : " + ts.TotalDays + "\n";
            richTextBox1.Text += "總時數 : " + ts.TotalHours + "\n";
            richTextBox1.Text += "總分數 : " + ts.TotalMinutes + "\n";
            richTextBox1.Text += "總秒數 : " + ts.TotalSeconds + "\n";
            richTextBox1.Text += "總毫秒數 : " + ts.TotalMilliseconds + "\n";
            return;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //計算時間間隔 TimeSpan = 兩個dt相減
            /*
            C# 如何取得兩個 DateTime 日期之間的天數

            取得兩個日期之間的「天數」（不足一天者採「無條件刪去法」） 
                new TimeSpan(date1.Ticks - date2.Ticks).Days

            取得兩個日期之間的「天數」（回傳型別為 double 雙精確度）
                new TimeSpan(date1.Ticks - date2.Ticks).TotalDays

            取得兩個日期之間的「小時數」（回傳型別為 double 雙精確度）
                new TimeSpan(date1.Ticks - date2.Ticks).TotalHours

            取得兩個日期之間的「分鐘數」（回傳型別為 double 雙精確度） 
                new TimeSpan(date1.Ticks - date2.Ticks).TotalMinutes
            */

            //------------------------------------------------------------  # 60個

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
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Year, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 年\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Month, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 月\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Day, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 天\n";

            //計算耗時任務所需的秒數
            string diff_time = GetTimeSpan(dt1, dt2);
            richTextBox1.Text += "相隔 : " + diff_time.ToString() + "\n";

            //6060


            //計算時間間隔

            dt1 = new DateTime(2017, 1, 31);
            dt2 = new DateTime(2017, 2, 1, 2, 3, 4, 15);
            DateTime dt3 = DateTime.Now;
            TimeSpan ts1 = dt2 - dt1;
            TimeSpan ts2 = dt3 - dt1;
            richTextBox1.Text += "兩個時間相距：" + ts1.ToString() + "\n";
            richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";

            //6060

            //計算時間間隔, 使用 TimeSpan
            dt1 = new DateTime(2019, 1, 1, 0, 0, 0);
            dt2 = new DateTime(2037, 12, 30, 12, 34, 56, 15);
            dt3 = DateTime.Now;

            //TimeSpan 取 時間間隔，只能取到天數，不能算月數、年數
            //TimeSpan
            ts1 = dt2 - dt1;
            //TimeSpan
            ts2 = dt3 - dt1;

            richTextBox1.Text += "時間間隔 : " + ts1.ToString() + "\n";
            richTextBox1.Text += "時間間隔 : " + ts1.TotalSeconds.ToString() + " 秒\n";

            richTextBox1.Text += "與現在相距 : " + ts2.ToString() + "\n";
            richTextBox1.Text += "與現在相距 : " + ts2.TotalSeconds.ToString() + " 秒\n";

            ts = DateTime.Now - DateTime.Now.Date;
            //richTextBox1.Text += DateTime.Now.ToString() + "\n";
            //richTextBox1.Text += DateTime.Now.Date.ToString() + "\n";
            richTextBox1.Text += "今天經過時間 : " + ts.ToString() + "\n";
            richTextBox1.Text += "今天經過時間 : " + ts.TotalSeconds.ToString() + " 秒\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算時間間隔
            //Timestamp 與 DateTime 互轉
            // 現在時間轉秒數
            //double timestamp = (DateTime.Now.AddHours(-8) - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
            double timestamp = (DateTime.Now.AddHours(-0) - new DateTime(2016, 5, 5, 23, 0, 0)).TotalSeconds;

            richTextBox1.Text += "從某時間距今秒數 : " + timestamp.ToString() + "\n";

            // 秒數轉 DateTime
            timestamp = 2400;
            DateTime dt = (new DateTime(2016, 5, 5, 23, 0, 0)).AddHours(0).AddSeconds(timestamp);

            richTextBox1.Text += "時間 : " + dt.ToString() + "\n";

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
            //韓戰
            //1950年6月25日－1953年7月27日（3年1個月又2天）
            //韓戰
            //1950年6月25日－1953年7月27日（3年1個月又2天）
            //日俄戰爭
            //1904年2月8日－1905年9月5日

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算時間間隔

            string string_datetime3 = "2006/03/11";
            int year = 0;
            int month = 0;
            int day = 0;
            dt = DateTime.ParseExact(string_datetime3, "yyyy/MM/dd", null, DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "年 : " + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月 : " + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日 : " + dt.Day.ToString() + "\n";
            year = dt.Year;
            month = dt.Month;
            day = dt.Day;

            richTextBox1.Text += year.ToString() + "  " + month.ToString() + "   " + day.ToString() + "\n\n";

            calculate_date_diff(year, month, day);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算差異天數
            string startDate = "2007/07/01";
            string endDate = "2007/07/07";
            DateTime dtStart = DateTime.ParseExact(startDate, "yyyy/MM/dd", null);
            DateTime dtEnd = DateTime.ParseExact(endDate, "yyyy/MM/dd", null);

            richTextBox1.Text += "dt1 = " + dtStart.ToString() + "\n";
            richTextBox1.Text += "dt2 = " + dtEnd.ToString() + "\n";

            // 計算差異天數
            TimeSpan tsDay = dtEnd - dtStart;
            int dayCount = (int)tsDay.TotalDays;
            richTextBox1.Text += "相差" + dayCount.ToString() + "天" + "\n";

            //計算差異天數
            startDate = "628年7月21日";
            endDate = "683年12月27日";

            dtStart = DateTime.Parse(startDate);
            dtEnd = DateTime.Parse(endDate);

            richTextBox1.Text += "dt1 = " + dtStart.ToString() + "\n";
            richTextBox1.Text += "dt2 = " + dtEnd.ToString() + "\n";

            // 計算差異天數
            tsDay = dtEnd - dtStart;
            dayCount = (int)tsDay.TotalDays;
            richTextBox1.Text += "相差" + dayCount.ToString() + "天" + "\n";
            richTextBox1.Text += "天1 : " + tsDay.Days.ToString() + "\n";        //same
            richTextBox1.Text += "天1 : " + tsDay.TotalDays.ToString() + "\n";   //same

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //日期時間相加減
            DateTime war_st = Convert.ToDateTime("1937-7-7");
            DateTime war_sp = Convert.ToDateTime("1945-08-15");
            ts = war_sp.Subtract(war_st); //兩時間天數相減
            //dayCount = (int)tsDay.TotalDays;
            dayCount = ts.Days; //相距天數
            richTextBox1.Text += "相距天數： " + dayCount.ToString() + " 天\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;

            richTextBox1.Text += "登出時間： " + dt.ToString() + "\n";
            ts = dt.Subtract(LoginTime);
            richTextBox1.Text += "您在此停留了" + ts.Hours + "小時" + ts.Minutes + "分鐘" + ts.Seconds + "秒" + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string str = string.Empty;

            dt = DateTime.Now;
            ts = DateTime.Now - start_time;

            richTextBox1.Text += "程式啟動時間: " + start_time.ToString() + " 秒\n";
            richTextBox1.Text += "按鍵經歷時間: " + ts.ToString() + " 秒\n";
            str = ts.ToString();
            richTextBox1.Text += "相距時間: " + str + "\n";
            str = str.Substring(0, str.IndexOf("."));
            richTextBox1.Text += "相距時間(去掉尾數): " + str + "\n";

            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + "\n";

            richTextBox1.Text += "aaaaaaaaaaaaaaaaa\n";
            return;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算日期差距
            //要計算兩個日期間的差距必須要透過 TimeSpan 來達成

            //TimeSpan ts1 = dt2 - dt1;
            dt1 = Convert.ToDateTime("2006/3/11");
            //DateTime dt1 = new DateTime(2006, 3, 11);

            dt2 = DateTime.Now;

            ts = dt2 - dt1;

            show_time_span(ts);

            richTextBox1.Text += "經歷時間: " + ts.ToString() + "\n";
            richTextBox1.Text += "兩時間相隔 :\n";
            richTextBox1.Text += ts.Days.ToString() + "天" + ts.Hours.ToString() + "小時" + ts.Minutes.ToString() + "分鐘" + ts.Seconds.ToString() + "秒" + "\n";

            richTextBox1.Text += "日 : " + ts.TotalDays.ToString() + "\n";
            richTextBox1.Text += "時 : " + ts.TotalHours.ToString() + "\n";
            richTextBox1.Text += "分 : " + ts.TotalMinutes.ToString() + "\n";
            richTextBox1.Text += "秒 : " + ts.TotalSeconds.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //倒數計時, 2026年距今還有多久
            DateTime dt_target = new DateTime(2026, 1, 1, 0, 0, 0);
            dt = DateTime.Now;
            ts = dt_target.Subtract(dt);
            ts = dt_target - dt;//same

            if (ts.TotalSeconds < 0)
            {
                richTextBox1.Text += "時間 " + dt_target + " 已過\n";
            }
            else
            {
                richTextBox1.Text += "時間 " + dt_target + " 距今:\t";
                richTextBox1.Text += ts.Days + " 天\t";
                richTextBox1.Text += ts.Hours + " 時\t";
                richTextBox1.Text += ts.Minutes + " 分\t";
                richTextBox1.Text += ts.Seconds + " 秒\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算時間間隔
            //計算兩個時間差值的函數，傳回時間差的絕對值

            //韓戰	 1950年 6月25日	~ 1953年7月27日 簽署停戰協定	4yr
            string st1 = "1950/6/25";
            string st2 = "1953/7/27";
            dt1 = Convert.ToDateTime(st1);
            dt2 = Convert.ToDateTime(st2);
            string diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算兩個日期的時間間隔
            dt1 = new DateTime(1939, 9, 1);
            dt2 = new DateTime(1945, 9, 2);
            diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算兩個日期的時間間隔
            dt1 = new DateTime(2006, 3, 11, 9, 15, 20);
            dt2 = DateTime.Now;
            diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "計算時間往回推 1天 2小時 3分 4秒\n";

            uint elapssed_time_msec = 1000 * (60 * 60 * 24 * 1 + 60 * 60 * 2 + 60 * 3 + 4);  // msec

            // 換算成 DateTime
            TimeSpan uptime = TimeSpan.FromMilliseconds(elapssed_time_msec);
            Console.WriteLine("已開機時間: {0} 天 {1} 小時 {2} 分鐘", uptime.Days, uptime.Hours, uptime.Minutes);

            DateTime before_time = DateTime.Now - TimeSpan.FromMilliseconds(elapssed_time_msec);

            richTextBox1.Text += "計算時間往回推 : " + before_time + "\n";

            richTextBox1.Text += "計算時間往回推 1天 2小時 3分 4秒\n";

            uint elapssed_time = 60 * 60 * 24 * 1 + 60 * 60 * 2 + 60 * 3 + 4;  // sec

            before_time = DateTime.Now - TimeSpan.FromSeconds(elapssed_time);

            richTextBox1.Text += "計算時間往回推 : " + before_time + "\n";

            //6060

            DateTime date1 = new DateTime(2008, 12, 31, 23, 59, 59, DateTimeKind.Local);
            DateTime date2 = new DateTime(2003, 2, 13, 23, 59, 59, DateTimeKind.Local);
            //TimeSpan
            ts = new TimeSpan(date1.Ticks - date2.Ticks);

            //------------------------------------------------------------  # 60個


        }

        //計算時間間隔
        private string DateDiff(DateTime dt1, DateTime dt2)
        {
            string dateDiff = string.Empty;
            TimeSpan ts1 = new TimeSpan(dt1.Ticks);
            TimeSpan ts2 = new TimeSpan(dt2.Ticks);
            TimeSpan ts = ts1.Subtract(ts2).Duration();
            dateDiff = ts.Days.ToString() + "天" + ts.Hours.ToString() + "小時" + ts.Minutes.ToString() + "分鐘" + ts.Seconds.ToString() + "秒";
            return dateDiff;
        }

        //計算耗時任務所需的秒數
        public string GetTimeSpan(DateTime dt1, DateTime dt2)
        {
            TimeSpan ts1 = new TimeSpan(dt1.Ticks);
            TimeSpan ts2 = new TimeSpan(dt2.Ticks);
            TimeSpan ts = ts2.Subtract(ts1).Duration();//秒
            string dateDiff = ts.Days.ToString() + "天" + ts.Hours.ToString() + "小時" + ts.Minutes.ToString() + "分鐘" + ts.Seconds.ToString() + "秒";
            richTextBox1.Text += dateDiff + "\n";
            return dateDiff;
        }

        public void calculate_date_diff(int year, int month, int day)
        {
            DateTime dt = DateTime.Now;
            int year_now = dt.Year;
            int month_now = dt.Month;
            int day_now = dt.Day;
            int year_diff = year_now - year;
            int month_diff = month_now - month;
            int day_diff = day_now - day;

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

        //6060

        long ticks_old = 0;
        private void button2_Click(object sender, EventArgs e)
        {
            long seconds = DateTime.Now.Ticks / TimeSpan.TicksPerSecond;

            richTextBox1.Text += "現在時間用Ticks表示 : " + DateTime.Now.Ticks.ToString() + "\n";
            //一秒 1千萬 個 Ticks
            richTextBox1.Text += "每秒有幾個Ticks : " + TimeSpan.TicksPerSecond.ToString() + "\n";
            richTextBox1.Text += "現在時間用秒表示 : " + seconds.ToString() + "\n";

            richTextBox1.Text += DateTime.Now.ToString() + "\n";
            richTextBox1.Text += "diff = " + (DateTime.Now.Ticks - ticks_old).ToString() + "\n";

            ticks_old = DateTime.Now.Ticks;

            richTextBox1.Text += "TicksPerSecond : " + TimeSpan.TicksPerSecond + "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //時間資料範例
            //DateTime dt = DateTime.Now;
            //DateTime dt = new DateTime(2006, 3, 11);	//年月日
            DateTime dt = new DateTime(2006, 3, 11, 9, 15, 10, 20);	//年月日時分秒毫秒
            //dt = DateTime.Parse(string_datetime1);

            richTextBox1.Text += "全部日期 : " + dt.ToString() + "\n";
            richTextBox1.Text += "D\t完整日期 : " + dt.ToString("D") + "\n";
            richTextBox1.Text += "d\t簡短日期 : " + dt.ToString("d") + "\n";
            richTextBox1.Text += "F\t完整日期及時間 : " + dt.ToString("F") + "\n";
            richTextBox1.Text += "G\t一般日期 : " + dt.ToString("G") + "\n";
            richTextBox1.Text += "Y\t年月格式 : " + dt.ToString("Y") + "\n";
            richTextBox1.Text += "M\t月日格式 : " + dt.ToString("M") + "\n";
            richTextBox1.Text += "T\t完整時間 : " + dt.ToString("T") + "\n";
            richTextBox1.Text += "t\t簡短時間 : " + dt.ToString("t") + "\n";
            richTextBox1.Text += "完整日期時間 : " + dt.ToString("F") + "\n";
            richTextBox1.Text += "簡短日期時間 : " + dt.ToString("f") + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            richTextBox1.Text += "ToLongDateString : " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "ToLongTimeString : " + dt.ToLongTimeString() + "\n";
            richTextBox1.Text += "ToShortDateString : " + dt.ToShortDateString() + "\n";
            richTextBox1.Text += "ToShortTimeString : " + dt.ToShortTimeString() + "\n";
            richTextBox1.Text += "ToString : " + dt.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = new DateTime(2006, 3, 11, 9, 15, 23, 34);//指定時間
            dt = DateTime.Now;

            richTextBox1.Text += "Now : " + DateTime.Now + "\n";
            richTextBox1.Text += "Today : " + DateTime.Today + "\n";//當天時間

            richTextBox1.Text += "Date : " + dt.Date + "\n";
            richTextBox1.Text += "Year : " + dt.Year + "\n";
            richTextBox1.Text += "Month : " + dt.Month + "\n";
            richTextBox1.Text += "Day : " + dt.Day + "\n";
            richTextBox1.Text += "Hour : " + dt.Hour + "\n";
            richTextBox1.Text += "Minute : " + dt.Minute + "\n";
            richTextBox1.Text += "Second : " + dt.Second + "\n";
            richTextBox1.Text += "Millisecond : " + dt.Millisecond + "\n";

            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            richTextBox1.Text += "天：" + dt.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "星：" + dt.DayOfWeek.ToString() + "\n";  // 星期幾
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
            richTextBox1.Text += "毫秒：" + dt.Millisecond.ToString() + "\n";
            richTextBox1.Text += "Ticks：" + dt.Ticks.ToString() + "\n";
            richTextBox1.Text += "TimeOfDay：" + dt.TimeOfDay.ToString() + "\n";
            richTextBox1.Text += "日期 1:\t" + dt.Date.ToString() + "\n";//2005-11-5 0:00:00
            richTextBox1.Text += "日期 1:\t" + dt.ToString() + "\n";//2005-11-5 13:47:04

            //日期函數
            dt = DateTime.Now;
            richTextBox1.Text += "當前時間 :\n";
            richTextBox1.Text += dt.ToFileTime().ToString() + "\n";//127756416859912816
            richTextBox1.Text += dt.ToFileTimeUtc().ToString() + "\n";//127756704859912816
            richTextBox1.Text += dt.ToLocalTime().ToString() + "\n";//2005-11-5 21:21:25
            richTextBox1.Text += dt.ToLongDateString().ToString() + "\n";//2005年11月5日
            richTextBox1.Text += dt.ToLongTimeString().ToString() + "\n";//13:21:25
            richTextBox1.Text += dt.ToOADate().ToString() + "\n";//38661.5565508218
            richTextBox1.Text += dt.ToShortDateString().ToString() + "\n";//2005-11-5
            richTextBox1.Text += dt.ToShortTimeString().ToString() + "\n";//13:21
            richTextBox1.Text += dt.ToUniversalTime().ToString() + "\n";//2005-11-5 5:21:25

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;
            richTextBox1.Text += dt.ToString("yyyy/MM/dd", DateTimeFormatInfo.InvariantInfo) + "\n";
            richTextBox1.Text += dt.ToString("yyyy年MM月dd日") + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //分出 時:分:秒 再組合
            dt = DateTime.Now;
            richTextBox1.Text += dt.Hour.ToString().PadLeft(2, '0') + ":"
                                    + dt.Minute.ToString().PadLeft(2, '0') + ":"
                                    + dt.Second.ToString().PadLeft(2, '0') + "\n";

            richTextBox1.Text += "現在時間 : " + dt.ToString("hh:mm:ss.fff") + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //DateTime轉字串需顯示毫秒
            //DateTime.ToString("yyyyMMddhhmmssfff")，fff 格式包含毫秒值中任何結尾的零。
            richTextBox1.Text += "顯示毫秒 : " + dt.ToString("yyyy_MMdd_hhmmss.fff") + "\n";
            richTextBox1.Text += "日期 : " + dt.ToString("yyyy-MM-dd") + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;
            //僅顯示上下午幾點幾分幾秒
            richTextBox1.Text += "僅顯示上下午幾點幾分幾秒:\t" + dt.ToString("T") + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //打印時間訊息用法

            dt = DateTime.Now;
            //2007年4月24日
            richTextBox1.Text += dt.ToString("D") + "\n";
            //2007-4-24
            richTextBox1.Text += dt.ToString("d") + "\n";
            //2007年4月24日 16:30:15
            richTextBox1.Text += dt.ToString("F") + "\n";
            //2007年4月24日 16:30
            richTextBox1.Text += dt.ToString("f") + "\n";

            //2007-4-24 16:30:15
            richTextBox1.Text += dt.ToString("G") + "\n";
            //2007-4-24 16:30
            richTextBox1.Text += dt.ToString("g") + "\n";
            //16:30:15
            richTextBox1.Text += dt.ToString("T") + "\n";
            //16:30
            richTextBox1.Text += dt.ToString("t") + "\n";
            //2007年4月24日 8:30:15
            richTextBox1.Text += dt.ToString("U") + "\n";
            //2007-04-24 16:30:15Z
            richTextBox1.Text += dt.ToString("u") + "\n";
            //4月24日
            richTextBox1.Text += dt.ToString("m") + "\n";
            richTextBox1.Text += dt.ToString("M") + "\n";
            //Tue, 24 Apr 2007 16:30:15 GMT
            richTextBox1.Text += dt.ToString("r") + "\n";
            richTextBox1.Text += dt.ToString("R") + "\n";
            //2007年4月 
            richTextBox1.Text += dt.ToString("y") + "\n";
            richTextBox1.Text += dt.ToString("Y") + "\n";
            //2007-04-24T15:52:19.1562500+08:00
            richTextBox1.Text += dt.ToString("o") + "\n";
            richTextBox1.Text += dt.ToString("O") + "\n";
            //2007-04-24T16:30:15
            richTextBox1.Text += dt.ToString("s") + "\n";
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

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;

            //string.Format 格式化日期

            //DateTime的屬性
            dt = DateTime.Now;
            richTextBox1.Text += "全部格式1a：" + dt.ToString() + "\n";
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



            richTextBox1.Text += "日期 1:\t" + dt.CompareTo(dt).ToString() + "\n";//0
            //richTextBox1.Text +="日期 1:\t"+ dt.Add(?).ToString()+"\n";//問號為一個時間段

            richTextBox1.Text += "日期 1:\t" + dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            richTextBox1.Text += "日期 1:\t" + dt.Equals(dt).ToString() + "\n";//True
            richTextBox1.Text += "日期 1:\t" + dt.GetHashCode().ToString() + "\n";//1474088234
            richTextBox1.Text += "日期 1:\t" + dt.GetType().ToString() + "\n";//DateTime
            richTextBox1.Text += "日期 1:\t" + dt.GetTypeCode().ToString() + "\n";//DateTime

            /*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(s)[0].ToString() + "\n";//2005-11-05T14:06:25
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(t)[0].ToString() + "\n";//14:06
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(y)[0].ToString() + "\n";//2005年11月
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[0].ToString() + "\n";//2005年11月5*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[1].ToString() + "\n";//2005 11 05
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[2].ToString() + "\n";//星期六 2005 11 05
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(D)[3].ToString() + "\n";//星期六 2005年11月5*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(M)[0].ToString() + "\n";//11月5*
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(f)[0].ToString() + "\n";//2005年11月5* 14:06
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(g)[0].ToString() + "\n";//2005-11-5 14:06
            richTextBox1.Text += "日期 1:\t" + dt.GetDateTimeFormats(r)[0].ToString() + "\n";//Sat, 05 Nov 2005 14:06:25 GMT
            */

            /*
            或者dt.ToString("yyyy年MM月dd*");//2005年11月5*
            dt.ToString("yyyy-MM-dd");//2005-11-5*
            以此類推……
            */

            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:d｝", dt) + "\n";//2005-11-5
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:D｝", dt) + "\n";//2005年11月5*
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:f｝", dt) + "\n";//2005年11月5* 14:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:F｝", dt) + "\n";//2005年11月5* 14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:g｝", dt) + "\n";//2005-11-5 14:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:G｝", dt) + "\n";//2005-11-5 14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:M｝", dt) + "\n";//11月5*
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:R｝", dt) + "\n";//Sat, 05 Nov 2005 14:23:23 GMT
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:s｝", dt) + "\n";//2005-11-05T14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:t｝", dt) + "\n";//14:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:T｝", dt) + "\n";//14:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:u｝", dt) + "\n";//2005-11-05 14:23:23Z
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:U｝", dt) + "\n";//2005年11月5* 6:23:23
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:Y｝", dt) + "\n";//2005年11月
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0｝", dt) + "\n";//2005-11-5 14:23:23?
            richTextBox1.Text += "日期 1:\t" + string.Format("｛0:yyyyMMddHHmmssffff｝", dt) + "\n";
            //yyyymm等可以設置,比如Label16.Text = string.Format("｛0:yyyyMMdd｝",dt)+"\n";
            //綁定也適用:例:<%# string.Format("｛0:yyyy.MM.dd｝",eval_r("sj"))%>

            //-------- same
            richTextBox1.Text += dt.CompareTo(dt).ToString() + "\n";//0

            //richTextBox1.Text += dt.Add(?).ToString() + "\n";//问号为一个时间段

            richTextBox1.Text += dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            richTextBox1.Text += dt.Equals(dt).ToString() + "\n";//True
            richTextBox1.Text += dt.GetHashCode().ToString() + "\n";//1474088234
            richTextBox1.Text += dt.GetType().ToString() + "\n";//DateTime
            richTextBox1.Text += dt.GetTypeCode().ToString() + "\n";//DateTime

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

            richTextBox1.Text += string.Format("{0:d}", dt) + "\n";//2005-11-5
            richTextBox1.Text += string.Format("{0:D}", dt) + "\n";//2005年11月5日
            richTextBox1.Text += string.Format("{0:f}", dt) + "\n";//2005年11月5日 14:23
            richTextBox1.Text += string.Format("{0:F}", dt) + "\n";//2005年11月5日 14:23:23
            richTextBox1.Text += string.Format("{0:g}", dt) + "\n";//2005-11-5 14:23
            richTextBox1.Text += string.Format("{0:G}", dt) + "\n";//2005-11-5 14:23:23
            richTextBox1.Text += string.Format("{0:M}", dt) + "\n";//11月5日
            richTextBox1.Text += string.Format("{0:R}", dt) + "\n";//Sat, 05 Nov 2005 14:23:23 GMT
            richTextBox1.Text += string.Format("{0:s}", dt) + "\n";//2005-11-05T14:23:23
            richTextBox1.Text += string.Format("{0:t}", dt) + "\n";//14:23
            richTextBox1.Text += string.Format("{0:T}", dt) + "\n";//14:23:23
            richTextBox1.Text += string.Format("{0:u}", dt) + "\n";//2005-11-05 14:23:23Z
            richTextBox1.Text += string.Format("{0:U}", dt) + "\n";//2005年11月5日 6:23:23
            richTextBox1.Text += string.Format("{0:Y}", dt) + "\n";//2005年11月
            richTextBox1.Text += string.Format("{0}", dt) + "\n";//2005-11-5 14:23:23
            richTextBox1.Text += string.Format("{0:yyyyMMddHHmmssffff}", dt) + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //日期時間輸出
            dt = DateTime.Now;
            richTextBox1.Text += String.Format("{0:dddd, MMM d yyyy}", dt) + "\n";
            richTextBox1.Text += String.Format("{0:HH:mm:ss}", dt) + "\n";
            richTextBox1.Text += String.Format("{0:D}", dt) + "\n";
            richTextBox1.Text += String.Format("{0:hh:mm:ss tt}", dt) + "\n";
            richTextBox1.Text += String.Format("{0:T}", dt) + "\n";
            richTextBox1.Text += String.Format("{0:h:m:s}", dt) + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

        private void button4_Click(object sender, EventArgs e)
        {
            // DateTime.Compare() 比較時間早晚

            //string st1 = "2010/05/30 12:13:50";
            //string st2 = "2018/09/20 14:14:30";
            string st1 = "2010/05/30";
            string st2 = "2018/09/20";
            DateTime dt1 = Convert.ToDateTime(st1);
            DateTime dt2 = Convert.ToDateTime(st2);

            if (DateTime.Compare(dt1, dt2) > 0)
            {
                richTextBox1.Text += st1 + " 晚於 " + st2 + "\n";
            }
            else
            {
                richTextBox1.Text += st1 + " 早於 " + st2 + "\n";
            }

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            // DateTime.Compare() 比較時間早晚
            dt1 = new DateTime(2016, 12, 9, 0, 0, 0);
            dt2 = new DateTime(2016, 12, 9, 11, 0, 0);
            int result = DateTime.Compare(dt1, dt2);

            string relationship = string.Empty;
            if (result < 0)
                relationship = "is earlier than";
            else if (result == 0)
                relationship = "is the same time as";
            else
                relationship = "is later than";

            richTextBox1.Text += dt1 + " " + relationship + " " + dt2 + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            /*
            //時間比較
            DateTime.Compare( dt1, dt2 ) > 0 : dt1 > dt2
            DateTime.Compare( dt1, dt2 ) == 0 : dt1 == dt2
            DateTime.Compare( dt1, dt2 ) < 0 : dt1 < dt2       
            */
        }

        private void button5_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
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
        }

        private void button6_Click(object sender, EventArgs e)
        {
            // 時間加減

            DateTime dt = DateTime.Now;
            richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + "\n";

            DateTime ThisMonBeginDay = new DateTime(dt.Year, dt.Month, 1);
            DateTime ThisMonEndDay = ThisMonBeginDay.AddMonths(1).AddDays(-1);
            richTextBox1.Text += "本月月底日期:" + ThisMonEndDay.Day.ToString() + "\n";
            richTextBox1.Text += "本月月底日期:" + DateTime.DaysInMonth(dt.Year, dt.Month).ToString() + "\n";



            richTextBox1.Text += "日期 1:\t" + dt.AddYears(1).ToString() + "\n";//2006-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddDays(1.1).ToString() + "\n";//2005-11-6 16:11:04
            richTextBox1.Text += "日期 1:\t" + dt.AddHours(1.1).ToString() + "\n";//2005-11-5 14:53:04
            richTextBox1.Text += "日期 1:\t" + dt.AddMilliseconds(1.1).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddMonths(1).ToString() + "\n";//2005-12-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddSeconds(1.1).ToString() + "\n";//2005-11-5 13:47:05
            richTextBox1.Text += "日期 1:\t" + dt.AddMinutes(1.1).ToString() + "\n";//2005-11-5 13:48:10
            richTextBox1.Text += "日期 1:\t" + dt.AddTicks(1000).ToString() + "\n";//2005-11-5 13:47:04


            richTextBox1.Text += dt.AddYears(1).ToString() + "\n";//2006-11-5 13:47:04
            richTextBox1.Text += dt.AddDays(1.1).ToString() + "\n";//2005-11-6 16:11:04
            richTextBox1.Text += dt.AddHours(1.1).ToString() + "\n";//2005-11-5 14:53:04
            richTextBox1.Text += dt.AddMilliseconds(1.1).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += dt.AddMonths(1).ToString() + "\n";//2005-12-5 13:47:04
            richTextBox1.Text += dt.AddSeconds(1.1).ToString() + "\n";//2005-11-5 13:47:05
            richTextBox1.Text += dt.AddMinutes(1.1).ToString() + "\n";//2005-11-5 13:48:10
            richTextBox1.Text += dt.AddTicks(1000).ToString() + "\n";//2005-11-5 13:47:04



            //現在日期加天數寫法(本例為加5天):
            DateTime Add5Day = dt.AddDays(5);
            richTextBox1.Text += "現在日期加5天： " + Add5Day.ToLongDateString() + "\n";

            //現在時間加小時寫法(本例為加12個小時):
            DateTime Add12Hours = dt.AddHours(12);
            richTextBox1.Text += "現在時間加12小時： " + Add12Hours.ToLongTimeString() + "\n";

            //現在時間減分鐘寫法(本例為減30分鐘):
            DateTime Minus30Minutes = dt.AddMinutes(-30);
            richTextBox1.Text += "現在時間減30分鐘： " + Minus30Minutes.ToLongTimeString() + "\n";

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

            richTextBox1.Text += "上次發薪日：" + LastSalaryDay.ToString("yyyy/MM/dd") + "\n";
            TimeSpan ts1 = dt - LastSalaryDay;

            richTextBox1.Text += "經過了 " + ts1.Days + " 天\n";

            richTextBox1.Text += "下次發薪日：" + NextSalaryDay.ToString("yyyy/MM/dd") + "\n";

            //用 大的日期 減 小的日期
            TimeSpan ts2 = dt - NextSalaryDay;    //小的日期減大的日期

            richTextBox1.Text += "距離下次發薪日還有" + Math.Abs(ts2.Days) + " 天\n"; //距離幾天一定是正的 用Math.Abs取絕對值
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //從零點到現在的秒數

            int total_time = inputToSeconds("23:59:59");
            richTextBox1.Text += "total_time = " + total_time.ToString() + "\n";

            int nn = 86399;
            string current_time = secondsToTime(nn);
            richTextBox1.Text += "current_time = " + current_time + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //時間相關
            //中時間相關知識點小結
            //一、月份英文簡寫

            DateTime dt = DateTime.Now;

            string MM = dt.AddMonths(-1).ToString("MMM", new CultureInfo("en-us"));  // 月英文縮寫：Jul
            richTextBox1.Text += "月份英文簡寫\t" + MM + "\n";

            //二、當月第一天和最后一天

            DateTime ThisMonth_Frist = dt.AddDays(1 - dt.Day).Date;
            DateTime ThisMOnth_Last = dt.AddDays(1 - dt.Day).Date.AddMonths(1).AddSeconds(-1);
            richTextBox1.Text += "當月第一天\t" + ThisMonth_Frist + "\n";
            richTextBox1.Text += "當月最后一天\t" + ThisMOnth_Last + "\n";

            //三、上月第一天和最后一天

            DateTime Today = DateTime.Today;//當天時間
            DateTime ThisMonth = new DateTime(Today.Year, Today.Month, 1);//當前月第一天時間
            DateTime LastMonth_First = ThisMonth.AddMonths(-1);//上月第一天時間
            DateTime LastMonth_Last = ThisMonth.AddDays(-1);//上月最后一天時間
            richTextBox1.Text += "上月第一天\t" + LastMonth_First + "\n";
            richTextBox1.Text += "上月最后一天\t" + LastMonth_Last + "\n";

            //四、本周第幾天

            int daysInWeek1 = (int)dt.DayOfWeek;//注意：此處周,日時回傳0，
            int daysInWeek2 = (int)dt.DayOfWeek == 0 ? 7 : (int)dt.DayOfWeek;//當前周第幾天,注釋:周日為0
            richTextBox1.Text += "本周第幾天\t" + daysInWeek1.ToString() + "\n";
            richTextBox1.Text += "本周第幾天\t" + daysInWeek2.ToString() + "\n";

            //五、本月第幾周

            //int a = WeekOfMonth(dt, false);//
            //richTextBox1.Text += "本月第幾周\t" + a + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "印出今年年曆\n";

            DateTime dt = DateTime.Now;

            int year = dt.Year;

            int nextlinecount;//使用一個計數器沒過一天就加1，逢7換行
            for (int month = 1; month <= 12; month++)
            {
                nextlinecount = 0;//計數器每個月開始需要進行初始化
                richTextBox1.Text += year.ToString() + "年" + month.ToString() + "月\n";
                richTextBox1.Text += "星期天\t 星期一\t 星期二\t 星期三\t 星期四\t 星期五\t 星期六\n";

                //獲取每個月第一天是星期幾然后輸出對應次數的空格
                for (int count = 1; count <= GetWeekByDay(year, month, 1); count++)
                {
                    richTextBox1.Text += " \t ";
                    nextlinecount++;//計數器增加，這里的空的是上個月的日子
                }

                for (int day = 1; day <= GetMonthDay(year, month); day++)
                {
                    if (nextlinecount % 7 == 0)//每次列印日期前先判斷是否為周六，逢7換行
                    {
                        richTextBox1.Text += "\n";
                    }
                    richTextBox1.Text += day + "\t ";
                    nextlinecount++;
                }
                richTextBox1.Text += "\n\n=========================================================================\n\n";
            }
        }

        /// 輸入年月日，得到這天是星期幾
        private static int GetWeekByDay(int year, int month, int day)
        {
            DateTime dt = new DateTime(year, month, day);
            return (int)dt.DayOfWeek;
        }

        /// 獲取某個月的天數，輸入(int)年份，月份，回傳天數(int)
        private static int GetMonthDay(int year, int month)
        {
            int thismonthdays = DateTime.DaysInMonth(year, month);
            return thismonthdays;
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //實現小小的日曆
            show_calendar();
        }

        //實現小小的日曆 ST
        void show_calendar()
        {
            DateTime dt = DateTime.Now;

            int year = dt.Year;
            int month = dt.Month;
            int day = 0;
            int sum = 0;
            int i;
            for (i = 1900; i < year; i++)
            {
                if (i % 4 == 0 && i % 100 != 0 || i % 400 == 0)
                {
                    sum += 366;
                }
                else
                {
                    sum += 365;
                }
            }

            switch (month)
            {
                case 12:
                    day = 31;
                    break;
                case 11:
                    day = 30;
                    break;
                case 10:
                    day = 31;
                    break;
                case 9:
                    day = 30;
                    break;
                case 8:
                    day = 31;
                    break;
                case 7:
                    day = 31;
                    break;
                case 6:
                    day = 30;
                    break;
                case 5:
                    day = 31;
                    break;
                case 4:
                    day = 30;
                    break;
                case 3:
                    day = 31;
                    break;
                case 2:
                    if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0)
                        day = 29;
                    else
                        day = 28;
                    break;
                case 1:
                    day = 31;
                    break;
            }

            int leap;
            /*先計算某月以前月份的總天數*/
            switch (month)
            {
                case 1: sum += 0; break;
                case 2: sum += 31; break;
                case 3: sum += 59; break;
                case 4: sum += 90; break;
                case 5: sum += 120; break;
                case 6: sum += 151; break;
                case 7: sum += 181; break;
                case 8: sum += 212; break;
                case 9: sum += 243; break;
                case 10: sum += 273; break;
                case 11: sum += 304; break;
                case 12: sum += 334; break;
            }
            //判斷是不是閏年
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
            {
                leap = 1;
            }
            else
            {
                leap = 0;
            }

            //如果是閏年且月份大於2,總天數應該加一天
            if (leap == 1 && month > 2)
            {
                sum++;
            }

            int space = (sum + 1) % 7;
            richTextBox1.Text += "日\t一\t二\t三\t四\t五\t六\n";
            for (i = 1; i <= (space + day); i++)
            {
                if (i <= space)
                {
                    richTextBox1.Text += "\t";
                }
                else
                {
                    richTextBox1.Text += i - space + "\t";
                }
                if (i % 7 == 0)
                {
                    richTextBox1.Text += "\n";
                }
            }
            richTextBox1.Text += "\n";
        }
        //實現小小的日曆 SP

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
            richTextBox1.Text += "時間：" + dt.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            string string_datetime4 = "3/11/2006 9:15:30 AM";
            dt = DateTime.Parse(string_datetime4);
            richTextBox1.Text += "生日: " + dt.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            DateTime dt1 = DateTime.ParseExact("2006/03/11", "yyyy/MM/dd", null);
            DateTime dt2 = DateTime.ParseExact("2018/02/01", "yyyy/MM/dd", null);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //DateTime Parse
            string str1 = "20091014223600";
            IFormatProvider ifp = new CultureInfo("zh-TW", true);
            dt1 = DateTime.ParseExact(str1, "yyyyMMddHHmmss", ifp);

            richTextBox1.Text += "原字串:\t" + str1 + "\n";
            richTextBox1.Text += "解讀後:\t" + dt1.ToString() + "\n";
            //MessageBox.Show(dt1.ToString());

            string str2 = "20091014223600";
            dt = DateTime.Now;
            richTextBox1.Text += "原字串:\t" + str2 + "\n";
            //IFormatProvider ifp = new CultureInfo("zh-TW", true);
            if (DateTime.TryParseExact(str2, "yyyyMMddHHmmss", ifp, DateTimeStyles.None, out dt2) == true)
            {
                //MessageBox.Show(dt2.ToString());
                richTextBox1.Text += "解讀後1:\t" + dt2.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "解讀後2:\t" + dt.ToString() + "\n";
                //MessageBox.Show(dt.ToString());
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

            //6060

            //新進

            //時間格式轉換
            //parse convert todatetime


            //計算時間間隔
            dt1 = Convert.ToDateTime("2010-10-15 15:50:39");
            dt2 = Convert.ToDateTime("2010-10-25 15:50:39");
            TimeSpan ts = dt1 - dt2;
            double days2 = ts.TotalDays;
            richTextBox1.Text += "差距 " + Convert.ToInt32(days2).ToString() + "天\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


            //dt1 = Convert.ToDateTime(st1);
            //dt2 = Convert.ToDateTime(st2);




        }

        private void button13_Click(object sender, EventArgs e)
        {
            //干支
            for (int i = 0; i < 20; i++)
            {
                richTextBox1.Text += GanZhiYearString(i) + "\n";
            }

            //6060

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

        private const int GanZhiStartYear = 0; //干支计算起始年
        private static string ganStr = "甲乙丙丁戊己庚辛壬癸";
        private static string zhiStr = "子丑寅卯辰巳午未申酉戌亥";

        string GanZhiYearString(int year)
        {
            int i = (year - GanZhiStartYear) % 60; //计算干支
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
            DateTime dt = DateTime.Now;

            //後一天
            DateTime nextDay = dt.AddDays(1);
            richTextBox1.Text += "後一天 : " + nextDay + "\n";

            //前一天
            DateTime pervDay = dt.AddDays(-1);
            richTextBox1.Text += "前一天 : " + pervDay + "\n";

            /*
            DateTime baseDateAndTime = new DateTime(1900, 1, 6, 2, 5, 0); //#1/6/1900 2:05:00 AM#
            DateTime newDate;
            num = 525948.76 * (y - 1900) + sTermInfo[i - 1];
            newDate = baseDateAndTime.AddMinutes(num);//按分钟计算
            */

            dt = DateTime.Now;
            string message = "";
            message += string.Format("{0}", dt.Year) + "\n";
            message += ("西元年:" + dt.Year.ToString()) + "\n";
            message += (string.Format("西元:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";

            dt = DateTime.Now;
            richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + Environment.NewLine;
            richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + Environment.NewLine;

            //現在日期加天數寫法(本例為加5天):
            DateTime Add5Day = dt.AddDays(5);
            richTextBox1.Text += "現在日期加5天： " + Add5Day.ToLongDateString() + Environment.NewLine;

            //現在時間加小時寫法(本例為加12個小時):
            DateTime Add12Hours = dt.AddHours(12);
            richTextBox1.Text += "現在時間加12小時： " + Add12Hours.ToLongTimeString() + Environment.NewLine;

            //現在時間減分鐘寫法(本例為減30分鐘):
            DateTime Minus30Minutes = dt.AddMinutes(-30);
            richTextBox1.Text += "現在時間減30分鐘： " + Minus30Minutes.ToLongTimeString() + Environment.NewLine;

            //------------------------------------------------------------  # 60個

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
            richTextBox1.Text += dt.DayOfWeek + "\n";

            /// 獲得中文星期名稱
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

            richTextBox1.Text += "今天是 : " + weekday + "\n";

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
            //系統時間相關
            //vcs時間之最早最晚

            //vcs史上最早時間
            DateTime minTime = DateTime.MinValue;

            //vcs史上最晚時間
            DateTime maxTime = DateTime.MaxValue;

            richTextBox1.Text += "vcs史上最早時間 : " + minTime.ToString() + "\n";
            richTextBox1.Text += "vcs史上最晚時間 : " + maxTime.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //列出全球時區

            //using System.Collections;
            richTextBox1.Text += "取得全球時區資訊\n";

            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                richTextBox1.Text += info + "\n";
            }

            //取得系統的時區資訊
            get_system_time_zone();

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個
        }

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

            //取得時辰
            dt = DateTime.Now;

            string ctime = getChineseTime(dt.Hour);
            richTextBox1.Text += "目前時辰 : " + ctime + "\n";

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "民國記年\n";

            CultureInfo ci = new CultureInfo("zh-TW", true);
            ci.DateTimeFormat.Calendar = new TaiwanCalendar();
            //改用datetime
            //richTextBox1.Text += dateTimePicker1.Value.ToString("yy/M/d", ci) + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += CultureInfo.CurrentCulture.DateTimeFormat.GetDayName(dt.DayOfWeek) + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            string[] month_names = CultureInfo.CurrentCulture.DateTimeFormat.MonthNames;
            foreach (string name in month_names)
            {
                if (name.Length > 0)
                {
                    richTextBox1.Text += name + " ";
                }
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            string[] day_names = CultureInfo.CurrentCulture.DateTimeFormat.DayNames;
            foreach (string name in day_names)
            {
                if (name.Length > 0)
                {
                    richTextBox1.Text += name + " ";
                }
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            for (int i = 0; i < 7; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + CultureInfo.CurrentCulture.DateTimeFormat.DayNames[i] + "\n";
            }

            //------------------------------------------------------------  # 60個

            richTextBox1.Text += "CultureInfo相關, 月名星期名\n";

            ci = new CultureInfo("zh-TW");
            ci.DateTimeFormat.Calendar = ci.OptionalCalendars[2];
            //TextBox1.Text = dt.ToString("yyyy/MM/dd", ci);

            dt = DateTime.Now;

            string mesg = string.Empty;
            mesg += dt.ToString() + "\n";
            mesg += dt.ToString("yyyy/MM/dd", ci) + "\n";
            mesg += dt.ToString("HH:mm:ss") + "\n";
            mesg += dt.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            richTextBox1.Text += mesg + "\n";

            //------------------------------------------------------------  # 60個

            string message = "";
            message += "显示中文格式的日期、星期几\n";
            message += "//该语句显示的为英文格式\n";
            message += DateTime.Now.DayOfWeek.ToString() + "\n";

            message += "//顯示中文格式星期幾 簡中1\n";
            message += DateTime.Now.ToString("ddd", new CultureInfo("zh-cn")) + "\n";      //3個d

            message += "//顯示中文格式星期幾 簡中2\n";
            message += DateTime.Now.ToString("dddd", new CultureInfo("zh-cn")) + "\n";     //更新简捷的显示中文格式星期几用4个dddd就可以搞定了，不需任何拼凑

            message += "//顯示中文格式星期幾 正中1\n";
            message += DateTime.Now.ToString("ddd", new CultureInfo("zh-tw")) + "\n";      //3個d

            message += "//顯示中文格式星期幾 正中2\n";
            message += DateTime.Now.ToString("dddd", new CultureInfo("zh-tw")) + "\n";     //4個d

            message += "//顯示日文格式星期幾\n";
            message += DateTime.Now.ToString("ddd", new CultureInfo("ja")) + "\n";

            message += "//顯示美語格式星期幾\n";
            message += DateTime.Now.ToString("ddd", new CultureInfo("en-us")) + "\n";

            message += "//VS2005后显示星期的新方法是\n";
            message += "星期" + DateTime.Now.DayOfWeek.ToString(("d")) + "\n";

            richTextBox1.Text += message + "\n";

            string dateString = DateTime.Today.ToString("yyyy-M-d dddd", new CultureInfo("zh-CN"));

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
            //生肖/星座

            //創建日曆對象ChineseLunisolarCalendar,將時間分成多個部分來表示，如分成年、月和日。 年按農曆計算，而日和月按陰陽曆計算。
            ChineseLunisolarCalendar chinseCaleander = new ChineseLunisolarCalendar();
            string TreeYear = "鼠牛虎兔龍蛇馬羊猴雞狗豬";//創建字符串對象
            int intYear = chinseCaleander.GetSexagenaryYear(DateTime.Now);//計算年信息,GetSexagenaryYear計算與指定日期對應的甲子（60 年）循環中的年。

            //得到生肖信息
            string Tree = TreeYear.Substring(chinseCaleander.GetTerrestrialBranch(intYear) - 1, 1);//GetTerrestrialBranch計算甲子（60 年）循環中指定年份的地支,
            //Substring(x,y)從此實例檢索子字符串。 子字符串從指定的字符位置開始且具有指定的長度
            richTextBox1.Text += "今年是十二生肖 " + Tree + " 年\n";

            //顯示星期信息
            richTextBox1.Text += "今天是： " + DateTime.Now.ToString("dddd") + "\n";//dddd是星期日,ddd是日,dd是01

            //由日期找出星座
            int month = 3;
            int day = 11;
            string astro_name = getAstro(month, day);
            richTextBox1.Text += astro_name + "\n";
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
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";

            sw.Reset();	//碼表歸零

            sw.Start();
            //XXXXXXXXXXX	//do something
            sw.Stop();
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString("0.00") + " 秒\n";
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalSeconds.ToString() + " 秒\n";
            richTextBox1.Text += "經過時間 : " + sw.Elapsed.TotalMilliseconds.ToString() + " 毫秒\n";
            richTextBox1.Text += "經過時間: "
            + sw.Elapsed.Hours.ToString().PadLeft(2, '0') + ":"
            + sw.Elapsed.Minutes.ToString().PadLeft(2, '0') + ":"
            + sw.Elapsed.Seconds.ToString().PadLeft(2, '0');

            //瞭解程式執行時間 

            sw = new Stopwatch();
            //long num = 0;
            sw.Reset();
            sw = Stopwatch.StartNew();
            //要測速的程式放這裡
            sw.Stop();
            TimeSpan el = sw.Elapsed;
            Console.WriteLine("花費 {0} ", el);
            long ms = sw.ElapsedMilliseconds;
            Console.WriteLine("花費 {0} 毫秒", ms);

            //補充說明: 不一定每次測到的時間都相同喔!
            //建議值: 超過100毫秒就有點太慢囉…. (電腦爛會Lag更長)

            Stopwatch loadingWatch = new Stopwatch();
            loadingWatch.Start();

            //XXXXXXXXX

            loadingWatch.Stop();

            Console.WriteLine(loadingWatch.ElapsedMilliseconds);

            //可以使用Reset()來重置計算時間.

            //------------------------------------------------------------  # 60個


            //量測時間2  用 TimeSpan
            DateTime start_time = DateTime.Now;
            //XXXXXXXXXXX	//do something
            DateTime stop_time = DateTime.Now;
            TimeSpan elapsed = stop_time - start_time;

            richTextBox1.Text += "經過時間 : " + elapsed.TotalSeconds.ToString("0.00") + " 秒\n";

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

            Console.WriteLine("花費 {0} ms 完成!!!", Environment.TickCount - URms);

            //------------------------------------------------------------  # 60個

            DateTime LoginTime, LogoffTime;

            //StayTime取得停留時間
            TimeSpan StayTime = new TimeSpan();

            //取得目前登入的時間
            LoginTime = DateTime.Now;
            Console.WriteLine("登入時間：{LoginTime}");

            // do something

            LogoffTime = DateTime.Now;
            Console.WriteLine("登出時間：{LogoffTime}");
            /*
            DateTime結構的Subtract()方法計算時間間隔
            時間間隔(StayTime) = 登出時間 - 登入時間
            再以所得結果，換算時、分、秒
            */

            StayTime = LogoffTime.Subtract(LoginTime);
            Console.WriteLine("您在此停留{StayTime.Hours,2}" + " 小時，{StayTime.Minutes} 分鐘 " + "{StayTime.Seconds} 秒");

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


            //6060


        }

        //------------------------------------------------------------  # 60個

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

            string mesg = string.Empty;

            // Local Time / GMT
            dt = DateTime.Now;
            mesg += "Local Time\n";
            mesg += dt.ToLongTimeString() + "\n";
            mesg += dt.ToShortDateString() + "\n";

            // Display the GMT time.
            DateTimeOffset local_offset = new DateTimeOffset(dt);
            DateTimeOffset utc_offset = local_offset.ToUniversalTime();

            mesg += "GMT Time\n";
            mesg += utc_offset.DateTime.ToLongTimeString() + "\n";
            mesg += utc_offset.DateTime.ToShortDateString() + "\n";

            lb_time.Text = mesg;

            //------------------------------------------------------------  # 60個

            DateTime get_time1 = Convert.ToDateTime(DateTime.Now.ToString());
            DateTime sta_ontime1 = Convert.ToDateTime(Convert.ToDateTime("2028-07-14 20:00:00"));

            lb_time2.Text = "距離2028年洛杉磯奧運會開幕還有\n";

            lb_time2.Text += DateAndTime.DateDiff("yyyy", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 年\n";
            lb_time2.Text += DateAndTime.DateDiff("m", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 月\n";
            lb_time2.Text += DateAndTime.DateDiff("d", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 日\n";
            lb_time2.Text += DateAndTime.DateDiff("h", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 時\n";
            lb_time2.Text += DateAndTime.DateDiff("n", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 分\n";
            lb_time2.Text += DateAndTime.DateDiff("s", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString() + " 秒\n";
        }

        void get_system_time_zone()
        {
            // Initialize the time zone lists.
            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                comboBox1.Items.Add(info);
                richTextBox1.Text += info + "\n";
            }

            // Select a default value
            comboBox1.SelectedItem = FindItemContaining(comboBox1.Items, "台北");

            TimeZoneInfo zone1 = comboBox1.SelectedItem as TimeZoneInfo;
            string name1 = zone1.DisplayName;
            richTextBox1.Text += "name1 = " + name1 + "\n";
        }

        /*
        實現的根據年月日計算星期幾的函數
        基姆拉爾森計算公式
        W= (d 2*m 3*(m 1)/5 y y/4-y/100 y/400) mod 7
        在公式中d表示日期中的日數，m表示月份數，y表示年數。注意：在公式中有個與其他公式不同的地方：把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10則換算成：2003-13-10來代入公式計算。
        */

        //根據年月日計算星期幾的函數
        //基姆拉爾森計算公式, 外文名是Kim larsen calculation formula。

        //在公式中d表示日期中的日數，m表示月份數，y表示年數。注意：在公式中有個與其他公式不同的地方：
        //把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10則換算成：2003-13-10來代入公式計算。

        string CalculateWeekDay(int y, int m, int d)
        {
            if (m == 1) m = 13;
            if (m == 2) m = 14;
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

        public int inputToSeconds(string timerInput)
        {
            string[] timeArray = new string[3];
            int minutes = 0;
            int hours = 0;
            int seconds = 0;
            int occurence = 0;
            int length = 0;
            int totalTime = 0;

            occurence = timerInput.LastIndexOf(":");
            length = timerInput.Length;

            //Check for invalid input
            if (occurence == -1 || length != 8)
            {
                richTextBox1.Text += "Invalid Time Format.\n";
            }
            else
            {
                timeArray = timerInput.Split(':');

                seconds = Convert.ToInt32(timeArray[2]);
                minutes = Convert.ToInt32(timeArray[1]);
                hours = Convert.ToInt32(timeArray[0]);

                totalTime += seconds;
                totalTime += minutes * 60;
                totalTime += (hours * 60) * 60;
            }
            return totalTime;
        }

        //secondsToTime方法是把秒转换一个时间格式的字串返回。

        public static string secondsToTime(int seconds)
        {
            int minutes = 0;
            int hours = 0;
            while (seconds >= 60)
            {
                minutes += 1;
                seconds -= 60;
            }
            while (minutes >= 60)
            {
                hours += 1;
                minutes -= 60;
            }
            string strHours = hours.ToString();
            string strMinutes = minutes.ToString();
            string strSeconds = seconds.ToString();

            if (strHours.Length < 2)
            {
                strHours = "0" + strHours;
            }
            if (strMinutes.Length < 2)
            {
                strMinutes = "0" + strMinutes;
            }
            if (strSeconds.Length < 2)
            {
                strSeconds = "0" + strSeconds;
            }
            return strHours + ":" + strMinutes + ":" + strSeconds;
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

        //由日期找出星座
        private static String getAstro(int month, int day)
        {
            String[] starArr = { "魔羯座", "水瓶座", "雙魚座", "牡羊座", "金牛座", "雙子座", "巨蟹座", "獅子座", "處女座", "天秤座", "天蠍座", "射手座" };
            int[] DayArr = { 22, 20, 19, 21, 21, 21, 22, 23, 23, 23, 23, 22 };  // 兩個星座分割日
            int index = month;
            // 所查詢日期在分割日之前，索引-1，否則不變
            if (day < DayArr[month - 1])
            {
                index = index - 1;
            }
            index = index % 12;
            // 返回索引指向的星座string
            return starArr[index];
        }

        private void timer_countdown_Tick(object sender, EventArgs e)
        {
            TimeSpan ts = dtTarget.Subtract(DateTime.Now);

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
                richTextBox1.Text += "得到DateTime資料： " + dt.ToString() + "\n";
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
1. Parse ：將指定的日期時間字串，轉換成相對應的 DateTime 型別。若轉換失敗會產生 FormatException 。
2. TryParse ：將指定的日期時間字串，轉換成相對應的 DateTime 型別，回傳值表示轉換是否成功。
3. ParseExact ：將指定的日期時間字串，轉換成相對應的 DateTime 型別，字串表示的格式必須完全符合指定的格式，否則會擲回例外狀況。
4. TryParseExact ：將指定的日期時間字串，轉換成相對應的 DateTime 型別，字串表示的格式必須完全符合指定的格式，回傳值表示轉換是否成功。
  
//------------------------------------------------------------  # 60個

string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
string filename = "imsLink_log.long." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + 
string drawDate = DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss");
lb_time1.Text = "PC時間 : " + DateTime.Now.ToString("yyyy" + '/' + "MM" + '/' + "dd ") + weekday + DateTime.Now.ToString(" HH" + ':' + "mm" + ':' + "ss");
string filename = "imsLink_log." + DateTime.Now.ToString("yyyy.MMdd.HHmm.ss") + ".txt";

//------------------------------------------------------------  # 60個

計算時間間隔
dtpicker_first dtpicker_second 為DateTimePicker
            MessageBox.Show("間隔 "+
                DateAndTime.DateDiff(	//使用DateDiff方法獲取日期間隔
                DateInterval.Day, dtpicker_first.Value, dtpicker_second.Value,
                FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString()+" 天", "間隔時間");

DateTime.Parse   DateTime.TryParse	在處理西元1~99年會處理成20XX年

//------------------------------------------------------------  # 60個

*/

