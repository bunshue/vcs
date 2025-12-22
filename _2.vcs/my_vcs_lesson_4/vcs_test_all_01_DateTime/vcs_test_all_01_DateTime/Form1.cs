using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Globalization; //for CultureInfo   //for 民國記年 農曆   //for DateTimeStyles
using System.Collections;   //for IEnumerable
using Microsoft.VisualBasic;    //for DateAndTime, 需要 參考/加入參考/.NET/Microsoft.VisualBasic

/*
DateTime值類型代表了一個從公元0001年1月1日0點0分0秒到公元9999年12月31日23點59分59秒之間的具體日期時刻。
因此，你可以用DateTime值類型來描述任何在想象范圍之內的時間。
*/

namespace vcs_test_all_01_DateTime
{
    public partial class Form1 : Form
    {
        int flag_timer_counter_down_enable = 0;
        int wait_seconds = 0;

        DateTime LoginTime = DateTime.Now;
        DateTime dt_timer_st = DateTime.Now;
        DateTime start_time = DateTime.Now;

        string string_datetime1 = "3/11/2006 9:15:30 AM";

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoginTime = DateTime.Now; //取得目前登入的時間
            richTextBox1.Text += "登入時間： " + LoginTime.ToString() + "\n";

            richTextBox1.Text += "現在時間 :\n";
            richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("yyyy" + '-' + "MM" + '-' + "dd" + " HH" + ':' + "mm" + ':' + "ss") + "\n";

            lb_time_interval.Text = "------------";

            timer1.Interval = 1000;
            timer1.Enabled = true;

            load_listview_data();

            show_item_location();

            this.ShowMoon();

            this.monthCalendar1.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.monthCalendar1.RightToLeft = System.Windows.Forms.RightToLeft.No;
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            int w = 220;
            int h = 60;

            //button
            x_st = 10;
            y_st = 10;
            dx = w + 10;
            dy = h + 10;

            button0.Size = new Size(w, h);
            button1.Size = new Size(w, h);
            button2.Size = new Size(w, h);
            button3.Size = new Size(w, h);
            button4.Size = new Size(w, h);
            button5.Size = new Size(w, h);
            button6.Size = new Size(w, h);
            button7.Size = new Size(w, h);
            button8.Size = new Size(w, h);
            button9.Size = new Size(w, h);
            button10.Size = new Size(w, h);
            button11.Size = new Size(w, h);
            button12.Size = new Size(w, h);
            button13.Size = new Size(w, h);
            button14.Size = new Size(w, h);
            button15.Size = new Size(w, h);
            button16.Size = new Size(w, h);
            button17.Size = new Size(w, h);
            button18.Size = new Size(w, h);
            button19.Size = new Size(w, h);
            button20.Size = new Size(w, h);
            button21.Size = new Size(w, h);
            button22.Size = new Size(w, h);
            comboBox1.Size = new Size(w, h);

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
            comboBox1.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            groupBox5.Location = new Point(x_st + dx * 0, y_st + dy * 10);//DateTimePicker
            groupBox12.Location = new Point(x_st + dx * 1, y_st + dy * 10);//設定倒數計時
            groupBox8.Location = new Point(x_st + dx * 2, y_st + dy * 10);//DateTimePicker
            groupBox13.Location = new Point(x_st + dx * 2, y_st + dy * 4 - 30);//月相
            groupBox10.Location = new Point(x_st + dx * 2, y_st + dy * 8 - 70); //listView

            groupBox6.Size = new Size(270, 150);
            groupBox8.Size = new Size(250, 130);
            groupBox5.Size = new Size(180, 150);
            groupBox9.Size = new Size(220, 280);
            groupBox12.Size = new Size(180, 150);

            groupBox6.Location = new Point(x_st + dx * 3, y_st + dy * 0);//特殊曆法

            groupBox9.Location = new Point(x_st + dx * 4 + 60, y_st + dy * 0);//Timer顯示時間

            textBox2.Size = new Size(160, 40);
            dateTimePicker1.Size = new Size(160, 40);
            textBox2.Location = new Point(x_st + dx * 0 - 5, y_st + dy * 0 + 10);
            bt1.Location = new Point(x_st + 170, y_st + dy * 0 + 10);
            dateTimePicker1.Location = new Point(x_st + dx * 0 - 5, y_st + dy * 0 + 60);
            bt2.Location = new Point(x_st + 170, y_st + dy * 0 + 60);

            lb_time.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20);
            lb_time_interval.Location = new Point(x_st + dx * 0, y_st + dy * 3 + 30);

            richTextBox1.Size = new Size(480, 530);
            richTextBox1.Location = new Point(x_st + dx * 4 + 10, y_st + dy * 4 + 30);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 120 + 5;
            dy = 35 + 5;

            bt_special_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_special_01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_special_02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_special_03.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_special_04.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_special_05.Location = new Point(x_st + dx * 1, y_st + dy * 2);

            this.Size = new Size(1460, 910);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //建立DateTime
            DateTime dt = DateTime.Now;//現在時間
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
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //時間差計算, 使用 TimeSpan
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
            richTextBox1.Text += "今天經過時間 " + interval.ToString() + "\n";
            richTextBox1.Text += "今天經過時間 " + interval.TotalSeconds.ToString() + " 秒\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //時間差計算1
            /*
            DateTime dt1 = new DateTime(2017, 1, 31);
            DateTime dt2 = new DateTime(2017, 2, 1, 2, 3, 4, 15);
            DateTime dt3 = DateTime.Now;
            TimeSpan ts1 = dt2 - dt1;
            TimeSpan ts2 = dt3 - dt1;
            richTextBox1.Text += "兩個時間相距：" + ts1.ToString() + "\n";
            richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";
            */

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //時間差計算2
            //Timestamp 與 DateTime 互轉
            // 現在時間轉秒數
            //double timestamp = (DateTime.Now.AddHours(-8) - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
            double timestamp = (DateTime.Now.AddHours(-0) - new DateTime(2016, 5, 5, 23, 0, 0)).TotalSeconds;

            richTextBox1.Text += "從某時間距今秒數" + timestamp.ToString() + "\n";

            // 秒數轉 DateTime
            timestamp = 2400;
            DateTime dt = (new DateTime(2016, 5, 5, 23, 0, 0)).AddHours(0).AddSeconds(timestamp);

            richTextBox1.Text += "時間：" + dt.ToString() + "\n";

            //時間差計算3

            //一戰
            //1914年7月28日－1918年11月11日（4年3個月又2周） 
            DateTime ww1_st = new DateTime(1914, 7, 28, 8, 12, 34);
            DateTime ww1_sp = new DateTime(1918, 11, 11, 17, 8, 17);
            TimeSpan ww1_time = ww1_sp - ww1_st;
            richTextBox1.Text += "一戰經歷時間 = " + ww1_time.ToString("T") + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //時間差計算5

            string string_datetime3 = "2006/03/11";
            int year = 0;
            int month = 0;
            int day = 0;
            dt = DateTime.ParseExact(string_datetime3, "yyyy/MM/dd", null, DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間：" + dt.ToString() + "\n";
            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            year = dt.Year;
            month = dt.Month;
            day = dt.Day;

            richTextBox1.Text += year.ToString() + "  " + month.ToString() + "   " + day.ToString() + "\n\n";

            calculate_date_diff(year, month, day);

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //時間差計算2

            DateTime d1 = new DateTime(2006, 3, 11, 9, 15, 15);
            DateTime d2 = DateTime.Now;
            TimeSpan ts = new TimeSpan(d2.Ticks - d1.Ticks);

            richTextBox1.Text += "兩時間相距 : " + ts.TotalMilliseconds.ToString() + "\n";
            richTextBox1.Text += "兩時間相距 : " + ts.TotalHours.ToString() + "\n";

            //計算兩個時間差
            dt1 = Convert.ToDateTime("2010-10-15 15:50:39");
            dt2 = Convert.ToDateTime("2010-10-25 15:50:39");
            TimeSpan time_diff = dt1 - dt2;
            double days = time_diff.TotalDays;
            richTextBox1.Text += "差距 " + Convert.ToInt32(days).ToString() + "天\n";

            /*
            //兩時間相隔
            DateTime dt1 = new DateTime(2006, 3, 11, 9, 15, 30);
            //DateTime dt1 = new DateTime(2021, 5, 21, 9, 15, 30);
            DateTime dt2 = DateTime.Now;
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Year, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 年\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Month, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 月\n";
            richTextBox1.Text += "相隔" + DateAndTime.DateDiff(DateInterval.Day, dt1, dt2, FirstDayOfWeek.Sunday, FirstWeekOfYear.Jan1).ToString() + " 天\n";

            //計算耗時任務所需的秒數
            string diff_time = GetTimeSpan(dt1, dt2);
            richTextBox1.Text += "相隔 : " + diff_time.ToString() + "\n";
            */

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
            TimeSpan span;
            span = DateTime.Now - start_time;

            richTextBox1.Text += "程式啟動時間: " + start_time.ToString() + " 秒\n";
            richTextBox1.Text += "按鍵經歷時間: " + span.ToString() + " 秒\n";
            str = span.ToString();
            richTextBox1.Text += "相距時間: " + str + "\n";
            str = str.Substring(0, str.IndexOf("."));
            richTextBox1.Text += "相距時間(去掉尾數): " + str + "\n";

            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            //計算日期差距
            //要計算兩個日期間的差距必須要透過 TimeSpan 來達成

            //TimeSpan ts1 = dt2 - dt1;
            dt1 = Convert.ToDateTime("2006/3/11");
            //DateTime dt1 = new DateTime(2006, 3, 11);

            dt2 = DateTime.Now;

            ts = dt2 - dt1;
            richTextBox1.Text += "經歷時間: " + ts.ToString() + "\n";
            richTextBox1.Text += "兩時間相隔 :\n";
            richTextBox1.Text += ts.Days.ToString() + "天" + ts.Hours.ToString() + "小時" + ts.Minutes.ToString() + "分鐘" + ts.Seconds.ToString() + "秒" + "\n";

            richTextBox1.Text += "日 : " + ts.TotalDays.ToString() + "\n";
            richTextBox1.Text += "時 : " + ts.TotalHours.ToString() + "\n";
            richTextBox1.Text += "分 : " + ts.TotalMinutes.ToString() + "\n";
            richTextBox1.Text += "秒 : " + ts.TotalSeconds.ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個


        }

        public void calculate_date_diff(int year, int month, int day)
        {
            int year_now = 0;
            int month_now = 0;
            int day_now = 0;
            int year_diff = 0;
            int month_diff = 0;
            int day_diff = 0;
            DateTime dt = DateTime.Now;
            year_now = dt.Year;
            month_now = dt.Month;
            day_now = dt.Day;
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

        private void button2_Click(object sender, EventArgs e)
        {
            long seconds = DateTime.Now.Ticks / TimeSpan.TicksPerSecond;

            richTextBox1.Text += "現在時間用Ticks表示 : " + DateTime.Now.Ticks.ToString() + "\n";
            richTextBox1.Text += "每秒有幾個Ticks : " + TimeSpan.TicksPerSecond.ToString() + "\n";
            richTextBox1.Text += "現在時間用秒表示 : " + seconds.ToString() + "\n";
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

            dt = new DateTime(2006, 3, 11, 9, 15, 23, 34);//指定時間
            dt = DateTime.Now;//現在時間

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
            richTextBox1.Text += "星：" + dt.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "時：" + dt.Hour.ToString() + "\n";
            richTextBox1.Text += "分：" + dt.Minute.ToString() + "\n";
            richTextBox1.Text += "秒：" + dt.Second.ToString() + "\n";
            richTextBox1.Text += "毫秒：" + dt.Millisecond.ToString() + "\n";
            richTextBox1.Text += "Ticks：" + dt.Ticks.ToString() + "\n";
            richTextBox1.Text += "TimeOfDay：" + dt.TimeOfDay.ToString() + "\n";

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

            dt = DateTime.Now;

            richTextBox1.Text += "星期幾 : " + dt.DayOfWeek.ToString() + "\n";

            richTextBox1.Text += "當前時間 : " + dt.ToLongTimeString() + "\n";

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

            DateTime ThisMonBeginDay = new DateTime(dt.Year, dt.Month, 1);
            DateTime ThisMonEndDay = ThisMonBeginDay.AddMonths(1).AddDays(-1);
            richTextBox1.Text += "本月月底日期:" + ThisMonEndDay.Day.ToString() + "\n";

            richTextBox1.Text += "本月月底日期:" + DateTime.DaysInMonth(dt.Year, dt.Month).ToString() + "\n";

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            dt = DateTime.Now;

            //string.Format 格式化日期

            //日期函數

            richTextBox1.Text += "日期 1:\t" + dt.ToString() + "\n";//2005-11-5 13:21:25
            richTextBox1.Text += "日期 1:\t" + dt.ToFileTime().ToString() + "\n";//127756416859912816
            richTextBox1.Text += "日期 1:\t" + dt.ToFileTimeUtc().ToString() + "\n";//127756704859912816
            richTextBox1.Text += "日期 1:\t" + dt.ToLocalTime().ToString() + "\n";//2005-11-5 21:21:25
            richTextBox1.Text += "日期 1:\t" + dt.ToLongDateString().ToString() + "\n";//2005年11月5*
            richTextBox1.Text += "日期 1:\t" + dt.ToLongTimeString().ToString() + "\n";//13:21:25
            richTextBox1.Text += "日期 1:\t" + dt.ToOADate().ToString() + "\n";//38661.5565508218
            richTextBox1.Text += "日期 1:\t" + dt.ToShortDateString().ToString() + "\n";//2005-11-5
            richTextBox1.Text += "日期 1:\t" + dt.ToShortTimeString().ToString() + "\n";//13:21
            richTextBox1.Text += "日期 1:\t" + dt.ToUniversalTime().ToString() + "\n";//2005-11-5 5:21:25

            //?2005-11-5 13:30:28.4412864
            richTextBox1.Text += "日期 1:\t" + dt.Year.ToString() + "\n";//2005
            richTextBox1.Text += "日期 1:\t" + dt.Date.ToString() + "\n";//2005-11-5 0:00:00
            richTextBox1.Text += "日期 1:\t" + dt.DayOfWeek.ToString() + "\n";//Saturday
            richTextBox1.Text += "日期 1:\t" + dt.DayOfYear.ToString() + "\n";//309
            richTextBox1.Text += "日期 1:\t" + dt.Hour.ToString() + "\n";//13
            richTextBox1.Text += "日期 1:\t" + dt.Millisecond.ToString() + "\n";//441
            richTextBox1.Text += "日期 1:\t" + dt.Minute.ToString() + "\n";//30
            richTextBox1.Text += "日期 1:\t" + dt.Month.ToString() + "\n";//11
            richTextBox1.Text += "日期 1:\t" + dt.Second.ToString() + "\n";//28
            richTextBox1.Text += "日期 1:\t" + dt.Ticks.ToString() + "\n";//632667942284412864
            richTextBox1.Text += "日期 1:\t" + dt.TimeOfDay.ToString() + "\n";//13:30:28.4412864
            richTextBox1.Text += "日期 1:\t" + dt.ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddYears(1).ToString() + "\n";//2006-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddDays(1.1).ToString() + "\n";//2005-11-6 16:11:04
            richTextBox1.Text += "日期 1:\t" + dt.AddHours(1.1).ToString() + "\n";//2005-11-5 14:53:04
            richTextBox1.Text += "日期 1:\t" + dt.AddMilliseconds(1.1).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddMonths(1).ToString() + "\n";//2005-12-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.AddSeconds(1.1).ToString() + "\n";//2005-11-5 13:47:05
            richTextBox1.Text += "日期 1:\t" + dt.AddMinutes(1.1).ToString() + "\n";//2005-11-5 13:48:10
            richTextBox1.Text += "日期 1:\t" + dt.AddTicks(1000).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += "日期 1:\t" + dt.CompareTo(dt).ToString() + "\n";//0
            //richTextBox1.Text +="日期 1:\t"+ dt.Add(?).ToString()+"\n";//問號為一個時間段

            richTextBox1.Text += "日期 1:\t" + dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            richTextBox1.Text += "日期 1:\t" + dt.Equals(dt).ToString() + "\n";//True
            richTextBox1.Text += "日期 1:\t" + dt.GetHashCode().ToString() + "\n";//1474088234
            richTextBox1.Text += "日期 1:\t" + dt.GetType().ToString() + "\n";//System.DateTime
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

            richTextBox1.Text += dt.ToString() + "\n";//2005-11-5 13:21:25
            richTextBox1.Text += dt.ToFileTime().ToString() + "\n";//127756416859912816
            richTextBox1.Text += dt.ToFileTimeUtc().ToString() + "\n";//127756704859912816
            richTextBox1.Text += dt.ToLocalTime().ToString() + "\n";//2005-11-5 21:21:25
            richTextBox1.Text += dt.ToLongDateString().ToString() + "\n";//2005年11月5日
            richTextBox1.Text += dt.ToLongTimeString().ToString() + "\n";//13:21:25
            richTextBox1.Text += dt.ToOADate().ToString() + "\n";//38661.5565508218
            richTextBox1.Text += dt.ToShortDateString().ToString() + "\n";//2005-11-5
            richTextBox1.Text += dt.ToShortTimeString().ToString() + "\n";//13:21
            richTextBox1.Text += dt.ToUniversalTime().ToString() + "\n";//2005-11-5 5:21:25
            richTextBox1.Text += dt.Year.ToString() + "\n";//2005
            richTextBox1.Text += dt.Date.ToString() + "\n";//2005-11-5 0:00:00
            richTextBox1.Text += dt.DayOfWeek.ToString() + "\n";//Saturday
            richTextBox1.Text += dt.DayOfYear.ToString() + "\n";//309
            richTextBox1.Text += dt.Hour.ToString() + "\n";//13
            richTextBox1.Text += dt.Millisecond.ToString() + "\n";//441
            richTextBox1.Text += dt.Minute.ToString() + "\n";//30
            richTextBox1.Text += dt.Month.ToString() + "\n";//11
            richTextBox1.Text += dt.Second.ToString() + "\n";//28
            richTextBox1.Text += dt.Ticks.ToString() + "\n";//632667942284412864
            richTextBox1.Text += dt.TimeOfDay.ToString() + "\n";//13:30:28.4412864
            richTextBox1.Text += dt.ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += dt.AddYears(1).ToString() + "\n";//2006-11-5 13:47:04
            richTextBox1.Text += dt.AddDays(1.1).ToString() + "\n";//2005-11-6 16:11:04
            richTextBox1.Text += dt.AddHours(1.1).ToString() + "\n";//2005-11-5 14:53:04
            richTextBox1.Text += dt.AddMilliseconds(1.1).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += dt.AddMonths(1).ToString() + "\n";//2005-12-5 13:47:04
            richTextBox1.Text += dt.AddSeconds(1.1).ToString() + "\n";//2005-11-5 13:47:05
            richTextBox1.Text += dt.AddMinutes(1.1).ToString() + "\n";//2005-11-5 13:48:10
            richTextBox1.Text += dt.AddTicks(1000).ToString() + "\n";//2005-11-5 13:47:04
            richTextBox1.Text += dt.CompareTo(dt).ToString() + "\n";//0

            //richTextBox1.Text += dt.Add(?).ToString() + "\n";//问号为一个时间段

            richTextBox1.Text += dt.Equals("2005-11-6 16:11:04").ToString() + "\n";//False
            richTextBox1.Text += dt.Equals(dt).ToString() + "\n";//True
            richTextBox1.Text += dt.GetHashCode().ToString() + "\n";//1474088234
            richTextBox1.Text += dt.GetType().ToString() + "\n";//System.DateTime
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
            //DateTime.Compare, 比較兩個時間

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
            DateTime dt = DateTime.Now;
            richTextBox1.Text += "現在日期： " + dt.ToLongDateString() + "\n";
            richTextBox1.Text += "現在時間： " + dt.ToLongTimeString() + "\n";

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
            DateTime EventDate = dt + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            richTextBox1.Text += "現在時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "現在時間 + 1天13時42分59秒 = " + EventDate.ToString() + "\n";

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

        //實現小小的日歷 ST
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
            /*判斷是不是閏年*/
            if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0))
                leap = 1;
            else
                leap = 0;
            /*如果是閏年且月份大於2,總天數應該加一天*/
            if (leap == 1 && month > 2)
                sum++;

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
        //實現小小的日歷 SP

        private void button11_Click(object sender, EventArgs e)
        {
            //依時間建立檔案
            DateTime dt = DateTime.Now;

            string filename = String.Format("{0}-{1}-{2}_{3}-{4}-{5}",
                                            dt.Year, dt.Month, dt.Day,
                                            dt.Hour, dt.Minute,
                                            dt.Second);

            richTextBox1.Text += "依時間建立檔案 :" + filename + "\n";

            string m_fileName = dt.ToFileTime().ToString() + ".jpg";
            richTextBox1.Text += "依時間建立檔案 :" + m_fileName + "\n";

            richTextBox1.Text += "Conversion finished @ " + dt.ToString() + "\n";
        }

        private void button12_Click(object sender, EventArgs e)
        {
        }

        private void button13_Click(object sender, EventArgs e)
        {
            //中時間相關知識點小結
            //一、月份英文簡寫

            DateTime dt = DateTime.Now;

            string MM = dt.AddMonths(-1).ToString("MMM", new CultureInfo("en-us"));//月英文縮寫：Jul
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

        private void button14_Click(object sender, EventArgs e)
        {
            //計算兩個時間差值的函數，傳回時間差的絕對值

            //韓戰	 1950年 6月25日	~ 1953年7月27日 簽署停戰協定	4yr
            string st1 = "1950/6/25";
            string st2 = "1953/7/27";
            DateTime dt1 = Convert.ToDateTime(st1);
            DateTime dt2 = Convert.ToDateTime(st2);
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
        }

        /// 計算兩個日期的時間間隔
        private string DateDiff(DateTime dt1, DateTime dt2)
        {
            string dateDiff = string.Empty;
            TimeSpan ts1 = new TimeSpan(dt1.Ticks);
            TimeSpan ts2 = new TimeSpan(dt2.Ticks);
            TimeSpan ts = ts1.Subtract(ts2).Duration();
            dateDiff = ts.Days.ToString() + "天" + ts.Hours.ToString() + "小時" + ts.Minutes.ToString() + "分鐘" + ts.Seconds.ToString() + "秒";
            return dateDiff;
        }

        private void button15_Click(object sender, EventArgs e)
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
            //DateTime dt2;
            DateTime dtNow = DateTime.Now;
            richTextBox1.Text += "原字串:\t" + str2 + "\n";
            //IFormatProvider ifp = new CultureInfo("zh-TW", true);
            if (DateTime.TryParseExact(str2, "yyyyMMddHHmmss", ifp, DateTimeStyles.None, out dt2) == true)
            {
                //MessageBox.Show(dt2.ToString());
                richTextBox1.Text += "解讀後1:\t" + dt2.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "解讀後2:\t" + dtNow.ToString() + "\n";
                //MessageBox.Show(dtNow.ToString());
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
            richTextBox1.Text += "時間差 : " + txt + "\n";
        }

        private void button16_Click(object sender, EventArgs e)
        {
            DateTime MyEndDate = new DateTime(2027, 01, 01, 00, 00, 00);
            DateTime MyStartDate = DateTime.Now;
            TimeSpan MySpan = MyEndDate.Subtract(MyStartDate);
            string diffDay = Convert.ToString(MySpan.Days);
            string diffHour = Convert.ToString(MySpan.Hours);
            string diffMin = Convert.ToString(MySpan.Minutes);
            string diffSec = Convert.ToString(MySpan.Seconds);
            richTextBox1.Text += "距離2027新年還有 " + diffDay + " 天 " + diffHour + " 時 " + diffMin + " 分 " + diffSec + " 秒\n";

            //2027年距今還有多久
            DateTime EventDate = new DateTime(2027, 1, 1, 0, 0, 0);
            TimeSpan remaining = EventDate - DateTime.Now;

            if (remaining.TotalSeconds < 0)
            {
                richTextBox1.Text += "時間 " + EventDate + " 早就過了\n";
            }
            else
            {
                richTextBox1.Text += "時間 " + EventDate + " 距今:\n";
                richTextBox1.Text += remaining.Days + "  天\n";
                richTextBox1.Text += remaining.Hours + "  時\n";
                richTextBox1.Text += remaining.Minutes + "  分\n";
                richTextBox1.Text += remaining.Seconds + "  秒\n";
            }
        }

        private void button17_Click(object sender, EventArgs e)
        {
            //ttttttttttttttttttttttt
            int i = 0;
            for (i = 0; i < 20; i++)
            {
                richTextBox1.Text += GanZhiYearString(i) + "\n";

            }
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

        private void button18_Click(object sender, EventArgs e)
        {
        }

        private void button19_Click(object sender, EventArgs e)
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

        private void button20_Click(object sender, EventArgs e)
        {
            //幾年幾月幾日星期幾
            int year;
            int month;
            int day;
            string result;

            year = 2006;
            month = 3;
            day = 11;
            result = CaculateWeekDay(year, month, day);
            richTextBox1.Text += year.ToString() + "年" + month.ToString() + "月" + day.ToString() + "日\t是\t" + result + "\n";

            year = 1941;
            month = 12;
            day = 7;
            result = CaculateWeekDay(year, month, day);
            richTextBox1.Text += year.ToString() + "年" + month.ToString() + "月" + day.ToString() + "日\t是\t" + result + "\t珍珠港事變\n";

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
            string weekday = string.Empty;

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

            return;

            richTextBox1.Text += "------------------------------\n";  // 30個

            dt = DateTime.Now;

            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(dt.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";

            string weekday1 = Day[Convert.ToInt32(dt.DayOfWeek.ToString("d"))].ToString();    //same
            string weekday2 = Day[Convert.ToInt16(dt.DayOfWeek)]; //same
            richTextBox1.Text += weekday1 + "\n";
            richTextBox1.Text += weekday2 + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            richTextBox1.Text += CultureInfo.CurrentCulture.DateTimeFormat.GetDayName(dt.DayOfWeek) + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個

            //string dt;
            weekday = string.Empty;
            //dt = DateTime.Today.DayOfWeek.ToString();
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
            result = CalculateWeekDay(2021, 10, 14);
            richTextBox1.Text += "日期 " + DateTime.Parse("2021/10/14").ToString() + "\t" + result + "\n";

            result = CalculateWeekDay(1941, 12, 7);
            richTextBox1.Text += "日期 " + DateTime.Parse("1941/12/7").ToString() + "\t" + result + "\n";

            result = CalculateWeekDay(2006, 3, 11);
            richTextBox1.Text += "日期 " + DateTime.Parse("2006/3/11").ToString() + "\t" + result + "\n";

            richTextBox1.Text += "------------------------------\n";  // 30個


            richTextBox1.Text += "------------------------------\n";  // 30個

        }

        private void button21_Click(object sender, EventArgs e)
        {
            //CultureInfo 相關

            string[] month_names = CultureInfo.CurrentCulture.DateTimeFormat.MonthNames;
            foreach (string name in month_names)
            {
                if (name.Length > 0)
                {
                    richTextBox1.Text += name + "\n";
                }
            }

            string[] day_names = CultureInfo.CurrentCulture.DateTimeFormat.DayNames;
            foreach (string name in day_names)
            {
                if (name.Length > 0)
                {
                    richTextBox1.Text += name + "\n";
                }
            }

            for (int i = 0; i < 7; i++)
            {
                richTextBox1.Text += "i = " + i.ToString() + "\t" + CultureInfo.CurrentCulture.DateTimeFormat.DayNames[i] + "\n";
            }
        }

        private void button22_Click(object sender, EventArgs e)
        {
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

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

            CultureInfo cuinfo = new CultureInfo("zh-TW");
            cuinfo.DateTimeFormat.Calendar = cuinfo.OptionalCalendars[2];
            //TextBox1.Text = dt.ToString("yyyy/MM/dd", cuinfo);

            string mesg = string.Empty;

            mesg += dt.ToString() + "\n";
            mesg += dt.ToString("yyyy/MM/dd", cuinfo) + "\n";
            mesg += dt.ToString("HH:mm:ss") + "\n";
            mesg += dt.ToString("yyyy/MM/dd HH:mm:ss") + "\n";

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

            if (flag_timer_counter_down_enable == 1)
            {
                dt = DateTime.Now;
                TimeSpan interval = dt - dt_timer_st;

                //richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";

                //TimeSpan interval = dt - dt.Date;
                //richTextBox1.Text += dt.ToString() + "\n";
                //richTextBox1.Text += dt.Date.ToString() + "\n";
                //richTextBox1.Text += "xxx " + interval.TotalSeconds.ToString();// +"\n";
                lb_time_interval.Text = interval.TotalSeconds.ToString();

                if (interval.TotalSeconds > wait_seconds)
                {
                    this.TopMost = true;
                    lb_time_interval.Text += "yyyy";
                    richTextBox1.Text += "Q ";
                }
            }


            lb_time.Text = mesg;



        }

        private void dateTimePicker1_ValueChanged(object sender, EventArgs e)
        {
            richTextBox1.Text += "The selected value is " + dateTimePicker1.Value + "\n";
            richTextBox1.Text += "The selected value is " + dateTimePicker1.Text + "\n";
            richTextBox1.Text += "The day of the week is " + dateTimePicker1.Value.DayOfWeek.ToString() + "\n";
            richTextBox1.Text += "The day of the year is " + dateTimePicker1.Value.DayOfYear.ToString() + "\n";
            richTextBox1.Text += "Millisecond is: " + dateTimePicker1.Value.Millisecond.ToString() + "\n";

            richTextBox1.Text += "\n";
            richTextBox1.Text += dateTimePicker1.Value.Year.ToString();
            richTextBox1.Text += "/" + dateTimePicker1.Value.Month.ToString();
            richTextBox1.Text += "/" + dateTimePicker1.Value.Day.ToString();

            DateTime dt = DateTime.Now;
            richTextBox1.Text += " " + dt.Hour;
            richTextBox1.Text += ":" + dt.Minute;
            richTextBox1.Text += ":" + dt.Second;
            richTextBox1.Text += "\n";
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
                TimeSpan remainder = to_date - from_date;
                days = remainder.Days;
                hours = remainder.Hours;
                minutes = remainder.Minutes;
                seconds = remainder.Seconds;
                milliseconds = remainder.Milliseconds;
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
                strHours = "0" + strHours;
            if (strMinutes.Length < 2)
                strMinutes = "0" + strMinutes;
            if (strSeconds.Length < 2)
                strSeconds = "0" + strSeconds;
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

        void load_listview_data()
        {
            DateTime dt = DateTime.Now;
            listView1.Items.Add(new ListViewItem(new String[] { "ToLongDateString", "D", dt.ToLongDateString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToLongTimeString", "T", dt.ToLongTimeString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToShortDateString", "d", dt.ToShortDateString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToShortTimeString", "t", dt.ToShortTimeString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToString", "G", dt.ToString() }));
        }

        private void bt1_Click(object sender, EventArgs e)
        {
            this.TopMost = false;
            if (flag_timer_counter_down_enable == 1)
            {
                flag_timer_counter_down_enable = 0;
                bt1.Text = "倒數";
            }
            else
            {
                flag_timer_counter_down_enable = 1;
                bt1.Text = "停止";

                dt_timer_st = DateTime.Now;
                wait_seconds = int.Parse(textBox2.Text) * 60;
                richTextBox1.Text += "等待時間： " + wait_seconds.ToString() + "\n";
            }
        }

        private void bt2_Click(object sender, EventArgs e)
        {
            //dateTimePicker1.Value = new DateTime(2006, 3, 11);                //特定日期
            //dateTimePicker1.Value = Convert.ToDateTime("2006/3/11 9:15:30");  //特定日期與時間
            //this.dateTimePicker1.Value = DateTime.Today;                      //今天日期
            this.dateTimePicker1.Value = DateTime.Now;                          //現在時刻
        }

        private void bt3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "c = " + listView1.Items.Count.ToString() + "\n";
            for (int i = 0; i < listView1.Items.Count; i++)
            {
                for (int j = 0; j < listView1.Items[i].SubItems.Count; j++)
                {
                    //richTextBox1.Text += "c2 = " + listView1.Items[i].SubItems.Count.ToString() + "\n";
                    richTextBox1.Text += "i = " + i.ToString() + listView1.Items[i] + "\tj = " + j.ToString() + listView1.Items[i].SubItems[j] + "\n";
                }
            }
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

        private void bt_dtp_set_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "設定DateTimePicker的顯示範圍\n";
            richTextBox1.Text += "顯示現在到未來12天\n";
            dateTimePicker2.MinDate = DateTime.Today;//當天時間
            dateTimePicker2.MaxDate = DateTime.Today.AddDays(12);
        }

        private void bt_dtp_get_Click(object sender, EventArgs e)
        {
            string date1 = dateTimePicker2.Value.Month.ToString() + "/" + dateTimePicker2.Value.Day.ToString();
            richTextBox1.Text += "你選取的日期是 : " + date1.ToString() + "\n";

            string date2 = DateTime.Today.AddDays(12).Month.ToString() + "/" + DateTime.Today.AddDays(12).Day.ToString();
            richTextBox1.Text += "12天後的日期是 : " + date2.ToString() + "\n";
        }

        //本年第幾周
        private int WeekOfYear()
        {
            var dt = DateTime.Now;
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
            DateTime Today = DateTime.Now;
            int daysInWeek = (int)Today.DayOfWeek == 0 ? 7 : (int)Today.DayOfWeek;//當前周第幾天,注釋:周日為0

            for (int i = N; i > 0; i--)
            {
                //起始日期
                DateTime firstDay = Today.AddDays(1 - (7 * i + daysInWeek));
                DateTime lastDay = Today.AddDays(7 - (7 * i + daysInWeek));
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

        private void bt_special_00_Click(object sender, EventArgs e)
        {
            //民國記年
            CultureInfo cui = new CultureInfo("zh-TW", true);
            cui.DateTimeFormat.Calendar = new TaiwanCalendar();
            richTextBox1.Text += dateTimePicker1.Value.ToString("yy/M/d", cui) + "\n";

            DateTime dd = new DateTime(2006, 3, 11);
            TaiwanCalendar tc = new TaiwanCalendar();

            int year = tc.GetYear(dd);
            int month = tc.GetMonth(dd);
            int dayOfMonth = tc.GetDayOfMonth(dd);             //日
            int daysInMonth = tc.GetDaysInMonth(year, month);   //整個月的天數
            richTextBox1.Text += "民國" + year.ToString() + "年" + month.ToString() + "月" + dayOfMonth.ToString() + "日\n";
        }

        private void bt_special_01_Click(object sender, EventArgs e)
        {
            var japaneseCal = new JapaneseCalendar();
            var jaJp = new CultureInfo("ja-JP");
            jaJp.DateTimeFormat.Calendar = japaneseCal;

            var date = new DateTime(1905, 2, 12);
            richTextBox1.Text += "Gregorian calendar date: " + date.ToString("d") + "\n";

            // Call the ToString(IFormatProvider) method.
            richTextBox1.Text += "Japanese calendar date: " + date.ToString("d", jaJp) + "\n";

            var date2 = new DateTime(2, 5, 10, japaneseCal);

            richTextBox1.Text += "Gregorian calendar date: " + date2.ToString("d") + "\n";
            richTextBox1.Text += "Japanese calendar date: " + date2.ToString("d", jaJp) + "\n";

            richTextBox1.Text += "Japanese calendar date: " + DateTime.Now.ToString("d", jaJp) + "\n";

            CultureInfo culture = new CultureInfo("ja-JP", true);
            culture.DateTimeFormat.Calendar = new JapaneseCalendar();
            DateTime today = DateTime.Today;//當天時間

            // 西暦の出力方法
            richTextBox1.Text += today + "\n";
            richTextBox1.Text += today.ToString("yyyy/MM/dd") + "\n";

            // 和暦の出力方法
            richTextBox1.Text += today.ToString("ggyy年MM月dd日(ddd)", culture) + "\n";
        }

        private void bt_special_02_Click(object sender, EventArgs e)
        {
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

        private void bt_special_03_Click(object sender, EventArgs e)
        {
            //取得時辰
            DateTime dt = DateTime.Now;

            string ctime = getChineseTime(dt.Hour);
            richTextBox1.Text += "目前時辰 : " + ctime + "\n";
        }

        string getChineseTime(int hour)
        {
            //地支時間做成數組
            string[] CTime = "子|丑|寅|卯|辰|巳|午|未|申|酉|戌|亥".Split('|');
            return "【" + CTime[hour / 2] + "時】";
        }

        private void bt_special_04_Click(object sender, EventArgs e)
        {
            //生肖/星座

            //創建日歷對象ChineseLunisolarCalendar,將時間分成多個部分來表示，如分成年、月和日。 年按農歷計算，而日和月按陰陽歷計算。
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
            string result = getAstro(month, day);
            richTextBox1.Text += result + "\n";
        }

        private void bt_special_05_Click(object sender, EventArgs e)
        {
            //萬年曆農曆節日節氣

            DateTime dt = DateTime.Now;

            richTextBox1.Text += "------------------------------------------------------------\n";  // 60個

            TaiwanCalendar TC = new TaiwanCalendar();
            TaiwanLunisolarCalendar TA = new TaiwanLunisolarCalendar();

            richTextBox1.Text += string.Format("{0}", dt.Year) + "\n";
            richTextBox1.Text += ("西元年:" + dt.Year.ToString()) + "\n";
            richTextBox1.Text += ("民國年:" + TC.GetYear(dt)) + "\n";
            richTextBox1.Text += (string.Format("西元:{0}/{1}/{2}", dt.Year, dt.Month, dt.Day)) + "\n";
            richTextBox1.Text += (string.Format("民國:{0}/{1}/{2}", TC.GetYear(dt), TC.GetMonth(dt), TC.GetDayOfMonth(dt))) + "\n";
            richTextBox1.Text += (string.Format("農曆:{0}/{1}/{2}", TA.GetYear(dt), TA.GetMonth(dt), TA.GetDayOfMonth(dt))) + "\n";
        }

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

        DateTime dtTarget;
        private void bt_countdown_Click(object sender, EventArgs e)
        {
            //設定倒數計時

            //dtTarget = DateTime.Now.AddHours(2);  //設定兩小時後
            dtTarget = new DateTime(2026, 9, 30, 12, 0, 0);   //設定特定時間

            timer_countdown.Start();
        }

        private void timer_countdown_Tick(object sender, EventArgs e)
        {
            TimeSpan ts = dtTarget.Subtract(DateTime.Now);

            string diffHour = Convert.ToString(ts.Hours);
            string diffMin = Convert.ToString(ts.Minutes);
            string diffSec = Convert.ToString(ts.Seconds);
            tb_countdown.Text = "距離 " + dtTarget.ToString() + " 還有 " + diffHour + " 時 " + diffMin + " 分 " + diffSec + " 秒";
        }

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
                ag = ip * 29.53059 + 29.53059 / 2;
            else
                ag = ip * 29.53059 - 29.53059 / 2;
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

        private void YourChoice()
        {
            //user select date from MonthCalendar control
            int Aday, Amonth, Ayear;
            Aday = this.monthCalendar1.SelectionStart.Day;
            Amonth = this.monthCalendar1.SelectionStart.Month;
            Ayear = this.monthCalendar1.SelectionStart.Year;
            this.MoonAge(Aday, Amonth, Ayear);
        }

        private void ShowMoon()
        {
            //draw moon and print age in selected days
            this.YourChoice(); //select date
            this.ClearDraw(); //clear pictureBox1 PictureBox
            this.DrawMoon(); //draw the moon
        }

        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            this.ShowMoon();
        }

        private void btn_moon_today_Click(object sender, EventArgs e)
        {
            //set the date of today
            this.monthCalendar1.SetDate(this.monthCalendar1.TodayDate.Date);
        }

        private void btn_moon_ok_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            bool conversionSuccessful = DateTime.TryParse(textBox4.Text, out dt);    //out為必須
            if (conversionSuccessful == true)
            {
                richTextBox1.Text += "得到DateTime資料： " + dt.ToString() + "\n";
                this.monthCalendar1.SetDate(dt);
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

//1515
//---------------  # 15個


/*  可搬出

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



*/

/*
        /// <summary>天干地支</summary>
        static readonly string[] chineseEra;
        static LunarDate2()
        {
            string sky = "甲乙丙丁戊已庚辛壬癸";        //天干
            string earth = "子丑寅卯辰巳午未申酉戌亥";  //地支
            chineseEra = new string[60];
            for (int i = 0; i < 60; i++)
                chineseEra[i] = sky.Substring(i % 10, 1) + earth.Substring(i % 12, 1);
        }
        
        private string FormatLunarYear(int iYear)
        {
            string strG = "甲乙丙丁戊己庚辛壬癸";
            string strZ = "子丑寅卯辰巳午未申酉戌亥";
            return strG.Substring((iYear - 4) % 10, 1) + strZ.Substring((iYear - 4) % 12, 1);
        }

        private string FormatAnimalYear(int iYear)
        {
            string strSX = "鼠牛虎免龙蛇马羊猴鸡狗猪";
            return strSX.Substring((iYear - 4) % 12, 1);
        }
*/

// DateTime.Parse()  抓出來


/*



*/

