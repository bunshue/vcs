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

namespace vcs_test_all_01_DateTime
{
    public partial class Form1 : Form
    {
        int flag_timer_counter_down_enable = 0;
        int wait_seconds = 0;

        DateTime LoginTime;
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

            label5.Text = "------------";

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
            dy = h + 2;

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
            groupBox12.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            groupBox5.Location = new Point(x_st + dx * 2, y_st + dy * 7);

            groupBox6.Size = new Size(10 * 2 + 120 * 3 + 5 * 2, 20 + 35 * 2 + 5 * 3 + 10);
            groupBox8.Size = new Size(250, 160);
            groupBox5.Size = new Size(180, 160);
            groupBox9.Size = new Size(250, 360);
            groupBox12.Size = new Size(180, 180);

            groupBox6.Location = new Point(x_st + dx * 3, y_st + dy * 0);//特殊曆法
            groupBox8.Location = new Point(x_st + dx * 3, y_st + dy * 2);


            groupBox13.Location = new Point(x_st + dx * 3, y_st + dy * 5);//月相
            groupBox10.Location = new Point(x_st + dx * 3, y_st + dy * 10 - 45); //listView

            groupBox9.Location = new Point(x_st + dx * 5, y_st + dy * 0);

            textBox2.Size = new Size(160, 40);
            dateTimePicker1.Size = new Size(160, 40);
            textBox2.Location = new Point(x_st + dx * 0 - 5, y_st + dy * 0 + 10);
            bt1.Location = new Point(x_st + 170, y_st + dy * 0 + 10);
            dateTimePicker1.Location = new Point(x_st + dx * 0 - 5, y_st + dy * 0 + 80 + 10);
            bt2.Location = new Point(x_st + 170, y_st + dy * 0 + 90);

            int dd = 30;
            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 1);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 2);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 3);
            label5.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 4);
            lb_time0.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 5);
            lb_time1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 6);
            lb_time2.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 7);
            lb_time3.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 8);
            lb_time4.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 9);
            lb_time5.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20 + dd * 10);

            richTextBox1.Size = new Size(260, 400);
            richTextBox1.Location = new Point(x_st + dx * 5, y_st + dy * 6);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 120 + 5;
            dy = 35 + 5;

            bt_special_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_special_01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_special_02.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_special_03.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_special_04.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_special_05.Location = new Point(x_st + dx * 2, y_st + dy * 1);

            this.Size = new Size(1460, 860);
        }

        private void button0_Click(object sender, EventArgs e)
        {
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //時間差計算1
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
            richTextBox1.Text += "今天經過時間 " + interval.ToString() + "\n";
            richTextBox1.Text += "今天經過時間 " + interval.TotalSeconds.ToString() + " 秒\n";

            //------------------------------------------------------------

            //時間差計算1
            /*
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
            */

            //------------------------------------------------------------

            //時間差計算2

            //Timestamp 與 DateTime 互轉
            // 現在時間轉秒數
            //double timestamp = (DateTime.Now.AddHours(-8) - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
            double timestamp = (DateTime.Now.AddHours(-0) - new DateTime(2016, 5, 5, 23, 0, 0)).TotalSeconds;

            richTextBox1.Text += "從某時間距今秒數" + timestamp.ToString() + "\n";

            // 秒數轉 DateTime
            timestamp = 2400;
            DateTime dt = (new DateTime(2016, 5, 5, 23, 0, 0)).AddHours(0).AddSeconds(timestamp);

            richTextBox1.Text += "時間：" + dt.ToString() + "秒" + "\n";

            //時間差計算3

            //一戰
            //1914年7月28日－1918年11月11日
            //（4年3個月又2周） 
            DateTime ww1_st = new DateTime(1914, 7, 28, 8, 12, 34);
            DateTime ww1_sp = new DateTime(1918, 11, 11, 17, 8, 17);
            TimeSpan ww1_time = ww1_sp - ww1_st;
            richTextBox1.Text += "一戰經歷時間 = " + ww1_time.ToString("T") + "\n";

            //------------------------------------------------------------

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

            //------------------------------------------------------------

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
            //------------------------------------------------------------

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

            //------------------------------------------------------------

            //日期時間相加減
            DateTime war_st = Convert.ToDateTime("1937-7-7");
            DateTime war_sp = Convert.ToDateTime("1945-08-15");
            ts = war_sp.Subtract(war_st); //兩時間天數相減
            //dayCount = (int)tsDay.TotalDays;
            dayCount = ts.Days; //相距天數
            richTextBox1.Text += "相距天數： " + dayCount.ToString() + " 天\n";

            //------------------------------------------------------------

            dt = DateTime.Now;

            richTextBox1.Text += "登出時間： " + dt.ToString() + "\n";
            ts = dt.Subtract(LoginTime);
            richTextBox1.Text += "您在此停留了" + ts.Hours + "小時" + ts.Minutes + "分鐘" + ts.Seconds + "秒" + "\n";

            //------------------------------------------------------------

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

            //------------------------------------------------------------

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

            //------------------------------------------------------------

            //------------------------------------------------------------



            //------------------------------------------------------------



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

            //------------------------------------------------------------

            dt = new DateTime(2006, 3, 11, 9, 15, 23, 34);

            richTextBox1.Text += "Now : " + DateTime.Now + "\n";
            richTextBox1.Text += "Today : " + DateTime.Today + "\n";

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

            //------------------------------------------------------------

            dt = DateTime.Now;
            richTextBox1.Text += DateTime.Now.ToString("yyyy/MM/dd", DateTimeFormatInfo.InvariantInfo) + "\n";

            //------------------------------------------------------------

            //分出 時:分:秒 再組合
            dt = DateTime.Now;
            richTextBox1.Text += dt.Hour.ToString().PadLeft(2, '0') + ":"
                                    + dt.Minute.ToString().PadLeft(2, '0') + ":"
                                    + dt.Second.ToString().PadLeft(2, '0') + "\n";

            richTextBox1.Text += "現在時間 : " + dt.ToString("hh:mm:ss.fff") + "\n";

            //------------------------------------------------------------

            dt = DateTime.Now;

            richTextBox1.Text += "星期幾 : " + dt.DayOfWeek.ToString() + "\n";

            richTextBox1.Text += "當前時間 : " + dt.ToLongTimeString() + "\n";

            //DateTime轉字串需顯示毫秒
            //DateTime.ToString("yyyyMMddhhmmssfff")，fff 格式包含毫秒值中任何結尾的零。
            richTextBox1.Text += "顯示毫秒 : " + dt.ToString("yyyy_MMdd_hhmmss.fff") + "\n";

            richTextBox1.Text += "日期 : " + dt.ToString("yyyy-MM-dd") + "\n";

            //------------------------------------------------------------

            //僅顯示上下午幾點幾分幾秒
            richTextBox1.Text += "僅顯示上下午幾點幾分幾秒:\t" + DateTime.Now.ToString("T") + "\n";

            //------------------------------------------------------------

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

            //------------------------------------------------------------

            dt = DateTime.Now;

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

            DateTime ThisMonBeginDay = new DateTime(dt.Year, dt.Month, 1);
            DateTime ThisMonEndDay = ThisMonBeginDay.AddMonths(1).AddDays(-1);
            richTextBox1.Text += "本月月底日期:" + ThisMonEndDay.Day.ToString() + "\n";

            richTextBox1.Text += "本月月底日期:" + DateTime.DaysInMonth(DateTime.Now.Year, DateTime.Now.Month).ToString() + "\n";

            //------------------------------------------------------------

            //------------------------------------------------------------

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

            //------------------------------------------------------------



            //------------------------------------------------------------
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

            //------------------------------------------------------------

            dt1 = new DateTime(2016, 12, 9, 0, 0, 0);
            dt2 = new DateTime(2016, 12, 9, 11, 0, 0);
            int result = DateTime.Compare(dt1, dt2);
            string relationship;

            if (result < 0)
                relationship = "is earlier than";
            else if (result == 0)
                relationship = "is the same time as";
            else
                relationship = "is later than";

            richTextBox1.Text += dt1 + " " + relationship + " " + dt2 + "\n";

            //------------------------------------------------------------



            //------------------------------------------------------------






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

            //------------------------------------------------------------

            dt = new DateTime(2019, 1, 1);

            richTextBox1.Text += "2019/1/1 加一段時間後 : " + dt.AddDays(3125).AddSeconds(14653 * 2).ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            int yy = -280;
            int dd = -1250;
            richTextBox1.Text += "2019/1/1 減一段時間後 : " + dt.AddYears(yy).AddDays(dd).AddSeconds(14653 * 2).ToString() + "\n";

            //------------------------------------------------------------

            //------------------------------------------------------------

            //一段時間以後
            dt = DateTime.Now;

            //?日?時?分?秒 後
            DateTime dt_new = dt + new TimeSpan(365 * 10, 12, 34, 56);

            richTextBox1.Text += "現在時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "一段時間以後 : " + dt_new.ToString() + "\n";

            //------------------------------------------------------------

            //一段時間以後的寫法
            dt = DateTime.Now;
            DateTime EventDate = dt + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            richTextBox1.Text += "現在時間 + 1天13時42分59秒 = " + EventDate.ToString() + "\n";


            //------------------------------------------------------------

            dt = DateTime.Now;

            DateTime LastSalaryDay = new DateTime(DateTime.Now.Year, DateTime.Now.Month, 5);
            DateTime NextSalaryDay = new DateTime(DateTime.Now.AddMonths(1).Year, DateTime.Now.AddMonths(1).Month, 5);

            richTextBox1.Text += "上次發薪日：" + LastSalaryDay.ToString("yyyy/MM/dd") + "\n";
            TimeSpan ts1 = DateTime.Now - LastSalaryDay;

            richTextBox1.Text += "經過了 " + ts1.Days + " 天\n";

            richTextBox1.Text += "下次發薪日：" + NextSalaryDay.ToString("yyyy/MM/dd") + "\n";

            //用 大的日期 減 小的日期
            TimeSpan ts2 = DateTime.Now - NextSalaryDay;    //小的日期減大的日期

            richTextBox1.Text += "距離下次發薪日還有" + Math.Abs(ts2.Days) + " 天\n"; //距離幾天一定是正的 用Math.Abs取絕對值


            //------------------------------------------------------------

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

            int year = DateTime.Now.Year;

            int nextlinecount;//使用一個計數器沒過一天就加1，逢7換行
            for (int month = 1; month <= 12; month++)
            {
                nextlinecount = 0;//計數器每個月開始需要進行初始化
                Console.WriteLine("{0}年{1}月", year, month);
                Console.WriteLine("星期天\t 星期一\t 星期二\t 星期三\t 星期四\t 星期五\t 星期六\t");

                //獲取每個月第一天是星期幾然后輸出對應次數的空格
                for (int count = 1; count <= GetWeekByDay(year, month, 1); count++)
                {
                    Console.Write(" \t ");
                    nextlinecount++;//計數器增加，這里的空的是上個月的日子
                }

                for (int day = 1; day <= GetMonthDay(year, month); day++)
                {
                    if (nextlinecount % 7 == 0)//每次列印日期前先判斷是否為周六，逢7換行
                        Console.WriteLine();
                    Console.Write(day + "\t ");
                    nextlinecount++;
                }

                Console.WriteLine();
                Console.WriteLine();
                Console.WriteLine("=========================================================================");
                Console.WriteLine();
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
            Console.WriteLine("日\t一\t二\t三\t四\t五\t六\t");
            richTextBox1.Text += "日\t一\t二\t三\t四\t五\t六\n";
            for (i = 1; i <= (space + day); i++)
            {
                if (i <= space)
                {
                    Console.Write("\t");
                    richTextBox1.Text += "\t";
                }
                else
                {
                    Console.Write(i - space + "\t");
                    richTextBox1.Text += i - space + "\t";
                }
                if (i % 7 == 0)
                {
                    Console.WriteLine();
                    richTextBox1.Text += "\n";
                }
            }
            Console.WriteLine();
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

            DateTime ThisMonth_Frist = DateTime.Now.AddDays(1 - DateTime.Now.Day).Date;
            DateTime ThisMOnth_Last = DateTime.Now.AddDays(1 - DateTime.Now.Day).Date.AddMonths(1).AddSeconds(-1);
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

            int daysInWeek1 = (int)DateTime.Now.DayOfWeek;//注意：此處周,日時回傳0，
            int daysInWeek2 = (int)DateTime.Now.DayOfWeek == 0 ? 7 : (int)DateTime.Now.DayOfWeek;//當前周第幾天,注釋:周日為0
            richTextBox1.Text += "本周第幾天\t" + daysInWeek1.ToString() + "\n";
            richTextBox1.Text += "本周第幾天\t" + daysInWeek2.ToString() + "\n";

            //五、本月第幾周

            //int a = WeekOfMonth(DateTime.Now, false);//
            //richTextBox1.Text += "本月第幾周\t" + a + "\n";
        }

        private void button14_Click(object sender, EventArgs e)
        {
            //計算兩個時間差值的函數，傳回時間差的絕對值

            //韓戰	 1950年 6月25日	———————————————————1953年7月27日 簽署停戰協定	4yr
            string st1 = "1950/6/25";
            string st2 = "1953/7/27";
            DateTime dt1 = Convert.ToDateTime(st1);
            DateTime dt2 = Convert.ToDateTime(st2);

            string result = DateDiff(dt1, dt2);
            richTextBox1.Text += "result = " + result + "\n";

            //------------------------------------------------------------

            //時間比較

            /*            
            //時間比較
            use "DateTime.Compare" static method

            DateTime.Compare( dt1, dt2 ) > 0 : dt1 > dt2
            DateTime.Compare( dt1, dt2 ) == 0 : dt1 == dt2
            DateTime.Compare( dt1, dt2 ) < 0 : dt1 < dt2
       

            DateTime值類型代表了一個從公元0001年1月1日0點0分0秒到公元9999年12月31日23點59分59秒之間的具體日期時刻。
            因此，你可以用DateTime值類型來描述任何在想象范圍之內的時間。
            */
            dt1 = new DateTime(2006, 3, 11, 9, 15, 20);
            dt2 = DateTime.Now;
            string diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";

            //------------------------------------------------------------

            //計算兩個日期的時間間隔
            dt1 = new DateTime(1939, 9, 1);
            dt2 = new DateTime(1945, 9, 2);
            diff = DateDiff(dt1, dt2);
            richTextBox1.Text += "diff = " + diff + "\n";

            //------------------------------------------------------------

            //計算兩個日期的時間間隔
            dt1 = new DateTime(1974, 9, 24);
            dt2 = new DateTime(1999, 3, 8);
            diff = DateDiff(dt2, dt1);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";
        }

        /// 計算兩個日期的時間間隔
        private string DateDiff(DateTime dt1, DateTime dt2)
        {
            string dateDiff = null;
            TimeSpan ts1 = new TimeSpan(dt1.Ticks);
            TimeSpan ts2 = new TimeSpan(dt2.Ticks);
            TimeSpan ts = ts1.Subtract(ts2).Duration();
            dateDiff = ts.Days.ToString() + "天" + ts.Hours.ToString() + "小時" + ts.Minutes.ToString() + "分鐘" + ts.Seconds.ToString() + "秒";
            return dateDiff;
        }

        private void button15_Click(object sender, EventArgs e)
        {
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

            //------------------------------------------------------------

            richTextBox1.Text += "日期2 : " + string_datetime2 + "\n";

            if (DateTime.TryParse(string_datetime2, out dt))
            {
                richTextBox1.Text += "取得DateTime :" + dt.ToString() + "\n";
            }
            else
            {
            }

            //------------------------------------------------------------

            //Parse 大全
            string string_datetime3 = "20100504";
            dt = DateTime.ParseExact(string_datetime3, "yyyyMMdd", null, DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間：" + dt.ToString() + "\n";

            //------------------------------------------------------------

            string string_datetime4 = "3/11/2006 9:15:30 AM";
            dt = DateTime.Parse(string_datetime4);
            richTextBox1.Text += "生日: " + dt.ToString() + "\n";

            //------------------------------------------------------------

            DateTime dt1 = DateTime.ParseExact("2006/03/11", "yyyy/MM/dd", null);
            DateTime dt2 = DateTime.ParseExact("2018/02/01", "yyyy/MM/dd", null);

            //------------------------------------------------------------

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
            if (DateTime.TryParseExact(str2, "yyyyMMddHHmmss", ifp, DateTimeStyles.None, out dt2))
            {
                //MessageBox.Show(dt2.ToString());
                richTextBox1.Text += "解讀後1:\t" + dt2.ToString() + "\n";
            }
            else
            {
                richTextBox1.Text += "解讀後2:\t" + dtNow.ToString() + "\n";
                //MessageBox.Show(dtNow.ToString());
            }


            //------------------------------------------------------------



            //------------------------------------------------------------



            string date_time1 = "21 July 1969, 20:17:40";
            string date_time2 = "14 December 1972, 19:54:57";

            richTextBox1.Text += "時間1 : " + date_time1 + "\n";
            richTextBox1.Text += "時間2 : " + date_time2 + "\n";

            if (!DateTime.TryParse(date_time1, out dt1))
            {
                return;
            }
            richTextBox1.Text += "dt1 : " + dt1.ToString() + "\n";

            if (!DateTime.TryParse(date_time2, out dt2))
            {
                return;
            }
            richTextBox1.Text += "dt2 : " + dt2.ToString() + "\n";

            int years, months, days, hours, minutes, seconds, milliseconds;

            GetElapsedTime(dt1, dt2, out years, out months, out days, out hours, out minutes, out seconds, out milliseconds);

            // Display the result.
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
            DateTime MyEndDate = new DateTime(2023, 01, 01, 00, 00, 00);
            DateTime MyStartDate = DateTime.Now;
            TimeSpan MySpan = MyEndDate.Subtract(MyStartDate);
            string diffDay = Convert.ToString(MySpan.Days);
            string diffHour = Convert.ToString(MySpan.Hours);
            string diffMin = Convert.ToString(MySpan.Minutes);
            string diffSec = Convert.ToString(MySpan.Seconds);
            richTextBox1.Text += "距離2023新年還有 " + diffDay + " 天 " + diffHour + " 時 " + diffMin + " 分 " + diffSec + " 秒\n";

            //2023年距今還有多久
            DateTime EventDate = new DateTime(2023, 1, 1, 0, 0, 0);
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

            //** 日期時間輸出

            Console.WriteLine(String.Format("{0:dddd, MMM d yyyy}", DateTime.Now));
            Console.WriteLine(String.Format("{0:HH:mm:ss}", DateTime.Now));
            Console.WriteLine(String.Format("{0:D}", DateTime.Now));
            Console.WriteLine(String.Format("{0:hh:mm:ss tt}", DateTime.Now));
            Console.WriteLine(String.Format("{0:T}", DateTime.Now));
            Console.WriteLine(String.Format("{0:h:m:s}", DateTime.Now));
        }

        private void button18_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

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

            message += "////显示中文格式的日期\n";

            message += DateTime.Now.ToLongDateString() + "\n";          // 显示格式为"2008年1月1日"

            message += DateTime.Now.ToString("yyyy年MM月dd日") + "\n"; // 显示格式为"2008年01月01日"，注意：格式字符串中的字母大小写不能错

            richTextBox1.Text += message;
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

            //------------------------------------------------------------

            //尋找13號星期五
            int year_st = 2020;
            int year_sp = 2030;
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

            //------------------------------------------------------------

            //獲得中文星期名稱
            richTextBox1.Text += "今天是 : " + GetCnWeek() + "\n";

            //------------------------------------------------------------

            //獲取當前星期幾的三種方法

            //第一種：

            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";

            string weekday1 = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();    //same
            string weekday2 = Day[Convert.ToInt16(DateTime.Now.DayOfWeek)]; //same
            richTextBox1.Text += weekday1 + "\n";
            richTextBox1.Text += weekday2 + "\n";

            //第二種：

            richTextBox1.Text += CultureInfo.CurrentCulture.DateTimeFormat.GetDayName(DateTime.Now.DayOfWeek) + "\n";

            //第三種：

            //string dt;
            //string week = string.Empty;
            //dt = DateTime.Today.DayOfWeek.ToString();
            switch (DateTime.Today.DayOfWeek.ToString())
            {
                case "Monday":
                    week = "星期一";
                    break;
                case "Tuesday":
                    week = "星期二";
                    break;
                case "Wednesday":
                    week = "星期三";
                    break;
                case "Thursday":
                    week = "星期四";
                    break;
                case "Friday":
                    week = "星期五";
                    break;
                case "Saturday":
                    week = "星期六";
                    break;
                case "Sunday":
                    week = "星期日";
                    break;
                default:
                    week = "星期日";
                    break;
            }
            richTextBox1.Text += week + "\n";


            //星期幾
            string[] Day2 = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week2 = Day2[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();

            richTextBox1.Text += week2 + "\n";

            //------------------------------------------------------------

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

            //------------------------------------------------------------

            //------------------------------------------------------------



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

            //DateTime值類型代表了一個從公元0001年1月1日0點0分0秒到公元9999年12月31日23點59分59秒之間的具體日期時刻
            //vcs史上最早時間
            DateTime minTime = DateTime.MinValue;

            //vcs史上最晚時間
            DateTime maxTime = DateTime.MaxValue;

            richTextBox1.Text += "vcs史上最早時間 : " + minTime.ToString() + "\n";
            richTextBox1.Text += "vcs史上最晚時間 : " + maxTime.ToString() + "\n";

            //------------------------------------------------------------

            //列出全球時區
            
            //using System.Collections;
            richTextBox1.Text += "取得全球時區資訊\n";

            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                richTextBox1.Text += info + "\n";
            }

            //取得系統的時區資訊
            get_system_time_zone();

            //------------------------------------------------------------

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;

            CultureInfo cuinfo = new CultureInfo("zh-TW");
            cuinfo.DateTimeFormat.Calendar = cuinfo.OptionalCalendars[2];
            //TextBox1.Text = dt.ToString("yyyy/MM/dd", cuinfo);

            label1.Text = dt.ToString();
            label2.Text = dt.ToString("yyyy/MM/dd", cuinfo);
            label3.Text = dt.ToString("HH:mm:ss");
            label4.Text = dt.ToString("yyyy/MM/dd HH:mm:ss");

            //Local Time / GMT
            // Display the local time.
            dt = DateTime.Now;
            lb_time0.Text = "Local Time";
            lb_time1.Text = dt.ToLongTimeString() + "\n";
            lb_time2.Text = dt.ToShortDateString() + "\n";

            // Display the GMT time.
            DateTimeOffset local_offset = new DateTimeOffset(dt);
            DateTimeOffset utc_offset = local_offset.ToUniversalTime();

            lb_time3.Text = "GMT Time";
            lb_time4.Text = utc_offset.DateTime.ToLongTimeString() + "\n";
            lb_time5.Text = utc_offset.DateTime.ToShortDateString() + "\n";

            if (flag_timer_counter_down_enable == 1)
            {
                dt = DateTime.Now;
                TimeSpan interval = dt - dt_timer_st;

                //richTextBox1.Text += "與現在相距：" + ts2.ToString() + "\n";

                //TimeSpan interval = dt - dt.Date;
                //richTextBox1.Text += dt.ToString() + "\n";
                //richTextBox1.Text += dt.Date.ToString() + "\n";
                //richTextBox1.Text += "xxx " + interval.TotalSeconds.ToString();// +"\n";
                label5.Text = interval.TotalSeconds.ToString();

                if (interval.TotalSeconds > wait_seconds)
                {
                    this.TopMost = true;
                    label5.Text += "yyyy";
                }
            }
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

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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
            dateTimePicker2.MinDate = DateTime.Today;
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
            DateTime today = DateTime.Today;

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

            //------------------------------------------------------------

            ChineseCalendar cc = new ChineseCalendar(dt);

            richTextBox1.Text += "阳历：" + cc.DateString + "\n";
            richTextBox1.Text += "属相：" + cc.AnimalString + "\n";
            richTextBox1.Text += "农历：" + cc.ChineseDateString + "\n";
            richTextBox1.Text += "时辰：" + cc.ChineseHour + "\n";
            richTextBox1.Text += "节气：" + cc.ChineseTwentyFourDay + "\n";
            richTextBox1.Text += "节日：" + cc.DateHoliday + "\n";
            richTextBox1.Text += "前一个节气：" + cc.ChineseTwentyFourPrevDay + "\n";
            richTextBox1.Text += "后一个节气：" + cc.ChineseTwentyFourNextDay + "\n";
            richTextBox1.Text += "干支：" + cc.GanZhiDateString + "\n";
            richTextBox1.Text += "星期：" + cc.WeekDayStr + "\n";
            richTextBox1.Text += "星宿：" + cc.ChineseConstellation + "\n";
            richTextBox1.Text += "星座：" + cc.Constellation + "\n";

            //------------------------------------------------------------

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
            dtTarget = new DateTime(2022, 9, 30, 12, 0, 0);   //設定特定時間

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

        private void PrintAge()
        {
            string theAge = "Moon age";

            theAge = theAge + " " + ":" + " " + ag.ToString();

            if (ag == 1)
                theAge = theAge + " " + "day";
            else
                theAge = theAge + " " + "days";

            this.lb_moon_age.Text = theAge;
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
            this.PrintAge(); //print age of moon in days
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
            }

        }
    }

    #region ChineseCalendarException
    /// <summary>
    /// 中国日历异常处理
    /// </summary>
    public class ChineseCalendarException : System.Exception
    {
        public ChineseCalendarException(string msg)
            : base(msg)
        {
        }
    }
    #endregion
    /// <summary>
    /// 中国农历类 版本V1.0 支持 1900.1.31日起至 2049.12.31日止的数据
    /// </summary>
    /// <remarks>
    /// 本程序使用数据来源于网上的万年历查询，并综合了一些其它数据
    /// </remarks>
    public class ChineseCalendar
    {
        #region 内部结构
        private struct SolarHolidayStruct
        {
            public int Month;
            public int Day;
            public int Recess; //假期长度
            public string HolidayName;
            public SolarHolidayStruct(int month, int day, int recess, string name)
            {
                Month = month;
                Day = day;
                Recess = recess;
                HolidayName = name;
            }
        }
        private struct LunarHolidayStruct
        {
            public int Month;
            public int Day;
            public int Recess;
            public string HolidayName;
            public LunarHolidayStruct(int month, int day, int recess, string name)
            {
                Month = month;
                Day = day;
                Recess = recess;
                HolidayName = name;
            }
        }
        private struct WeekHolidayStruct
        {
            public int Month;
            public int WeekAtMonth;
            public int WeekDay;
            public string HolidayName;
            public WeekHolidayStruct(int month, int weekAtMonth, int weekDay, string name)
            {
                Month = month;
                WeekAtMonth = weekAtMonth;
                WeekDay = weekDay;
                HolidayName = name;
            }
        }
        #endregion
        #region 内部变量
        private DateTime _date;
        private DateTime _datetime;
        private int _cYear;
        private int _cMonth;
        private int _cDay;
        private bool _cIsLeapMonth; //当月是否闰月
        private bool _cIsLeapYear; //当年是否有闰月
        #endregion
        #region 基础数据
        #region 基本常量
        private const int MinYear = 1900;
        private const int MaxYear = 2050;
        private static DateTime MinDay = new DateTime(1900, 1, 30);
        private static DateTime MaxDay = new DateTime(2049, 12, 31);
        private const int GanZhiStartYear = 1864; //干支计算起始年
        private static DateTime GanZhiStartDay = new DateTime(1899, 12, 22);//起始日
        private const string HZNum = "零一二三四五六七八九";
        private const int AnimalStartYear = 1900; //1900年为鼠年
        private static DateTime ChineseConstellationReferDay = new DateTime(2007, 9, 13);//28星宿参考值,本日为角
        #endregion
        #region 阴历数据
        /// <summary>
        /// 来源于网上的农历数据
        /// </summary>
        /// <remarks>
        /// 数据结构如下，共使用17位数据
        /// 第17位：表示闰月天数，0表示29天   1表示30天
        /// 第16位-第5位（共12位）表示12个月，其中第16位表示第一月，如果该月为30天则为1，29天为0
        /// 第4位-第1位（共4位）表示闰月是哪个月，如果当年没有闰月，则置0
        ///</remarks>
        private static int[] LunarDateArray = new int[]{
                    0x04BD8,0x04AE0,0x0A570,0x054D5,0x0D260,0x0D950,0x16554,0x056A0,0x09AD0,0x055D2,
                    0x04AE0,0x0A5B6,0x0A4D0,0x0D250,0x1D255,0x0B540,0x0D6A0,0x0ADA2,0x095B0,0x14977,
                    0x04970,0x0A4B0,0x0B4B5,0x06A50,0x06D40,0x1AB54,0x02B60,0x09570,0x052F2,0x04970,
                    0x06566,0x0D4A0,0x0EA50,0x06E95,0x05AD0,0x02B60,0x186E3,0x092E0,0x1C8D7,0x0C950,
                    0x0D4A0,0x1D8A6,0x0B550,0x056A0,0x1A5B4,0x025D0,0x092D0,0x0D2B2,0x0A950,0x0B557,
                    0x06CA0,0x0B550,0x15355,0x04DA0,0x0A5B0,0x14573,0x052B0,0x0A9A8,0x0E950,0x06AA0,
                    0x0AEA6,0x0AB50,0x04B60,0x0AAE4,0x0A570,0x05260,0x0F263,0x0D950,0x05B57,0x056A0,
                    0x096D0,0x04DD5,0x04AD0,0x0A4D0,0x0D4D4,0x0D250,0x0D558,0x0B540,0x0B6A0,0x195A6,
                    0x095B0,0x049B0,0x0A974,0x0A4B0,0x0B27A,0x06A50,0x06D40,0x0AF46,0x0AB60,0x09570,
                    0x04AF5,0x04970,0x064B0,0x074A3,0x0EA50,0x06B58,0x055C0,0x0AB60,0x096D5,0x092E0,
                    0x0C960,0x0D954,0x0D4A0,0x0DA50,0x07552,0x056A0,0x0ABB7,0x025D0,0x092D0,0x0CAB5,
                    0x0A950,0x0B4A0,0x0BAA4,0x0AD50,0x055D9,0x04BA0,0x0A5B0,0x15176,0x052B0,0x0A930,
                    0x07954,0x06AA0,0x0AD50,0x05B52,0x04B60,0x0A6E6,0x0A4E0,0x0D260,0x0EA65,0x0D530,
                    0x05AA0,0x076A3,0x096D0,0x04BD7,0x04AD0,0x0A4D0,0x1D0B6,0x0D250,0x0D520,0x0DD45,
                    0x0B5A0,0x056D0,0x055B2,0x049B0,0x0A577,0x0A4B0,0x0AA50,0x1B255,0x06D20,0x0ADA0,
                    0x14B63        
                    };
        #endregion
        #region 星座名称
        private static string[] _constellationName = 
                    { 
                        "白羊座", "金牛座", "双子座", 
                        "巨蟹座", "狮子座", "处女座", 
                        "天秤座", "天蝎座", "射手座", 
                        "摩羯座", "水瓶座", "双鱼座"
                    };
        #endregion
        #region 二十四节气
        private static string[] _lunarHolidayName = 
                        { 
                        "小寒", "大寒", "立春", "雨水", 
                        "惊蛰", "春分", "清明", "谷雨", 
                        "立夏", "小满", "芒种", "夏至", 
                        "小暑", "大暑", "立秋", "处暑", 
                        "白露", "秋分", "寒露", "霜降", 
                        "立冬", "小雪", "大雪", "冬至"
                        };
        #endregion
        #region 二十八星宿
        private static string[] _chineseConstellationName =
                {
                      //四        五      六         日        一      二      三  
                    "角木蛟","亢金龙","女土蝠","房日兔","心月狐","尾火虎","箕水豹",
                    "斗木獬","牛金牛","氐土貉","虚日鼠","危月燕","室火猪","壁水獝",
                    "奎木狼","娄金狗","胃土彘","昴日鸡","毕月乌","觜火猴","参水猿",
                    "井木犴","鬼金羊","柳土獐","星日马","张月鹿","翼火蛇","轸水蚓" 
                };
        #endregion
        #region 节气数据
        private static string[] SolarTerm = new string[] { "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至" };
        private static int[] sTermInfo = new int[] { 0, 21208, 42467, 63836, 85337, 107014, 128867, 150921, 173149, 195551, 218072, 240693, 263343, 285989, 308563, 331033, 353350, 375494, 397447, 419210, 440795, 462224, 483532, 504758 };
        #endregion
        #region 农历相关数据
        private static string ganStr = "甲乙丙丁戊己庚辛壬癸";
        private static string zhiStr = "子丑寅卯辰巳午未申酉戌亥";
        private static string animalStr = "鼠牛虎兔龙蛇马羊猴鸡狗猪";
        private static string nStr1 = "日一二三四五六七八九";
        private static string nStr2 = "初十廿卅";
        private static string[] _monthString =
                    {
                        "出错","正月","二月","三月","四月","五月","六月","七月","八月","九月","十月","十一月","腊月"
                    };
        #endregion
        #region 按公历计算的节日
        private static SolarHolidayStruct[] sHolidayInfo = new SolarHolidayStruct[]{
                new SolarHolidayStruct(1, 1, 1, "元旦"),
                new SolarHolidayStruct(2, 2, 0, "世界湿地日"),
                new SolarHolidayStruct(2, 10, 0, "国际气象节"),
                new SolarHolidayStruct(2, 14, 0, "情人节"),
                new SolarHolidayStruct(3, 1, 0, "国际海豹日"),
                new SolarHolidayStruct(3, 5, 0, "学雷锋纪念日"),
                new SolarHolidayStruct(3, 8, 0, "妇女节"), 
                new SolarHolidayStruct(3, 12, 0, "植树节 孙中山逝世纪念日"), 
                new SolarHolidayStruct(3, 14, 0, "国际警察日"),
                new SolarHolidayStruct(3, 15, 0, "消费者权益日"),
                new SolarHolidayStruct(3, 17, 0, "中国国医节 国际航海日"),
                new SolarHolidayStruct(3, 21, 0, "世界森林日 消除种族歧视国际日 世界儿歌日"),
                new SolarHolidayStruct(3, 22, 0, "世界水日"),
                new SolarHolidayStruct(3, 24, 0, "世界防治结核病日"),
                new SolarHolidayStruct(4, 1, 0, "愚人节"),
                new SolarHolidayStruct(4, 7, 0, "世界卫生日"),
                new SolarHolidayStruct(4, 22, 0, "世界地球日"),
                new SolarHolidayStruct(5, 1, 1, "劳动节"), 
                new SolarHolidayStruct(5, 2, 1, "劳动节假日"),
                new SolarHolidayStruct(5, 3, 1, "劳动节假日"),
                new SolarHolidayStruct(5, 4, 0, "青年节"), 
                new SolarHolidayStruct(5, 8, 0, "世界红十字日"),
                new SolarHolidayStruct(5, 12, 0, "国际护士节"), 
                new SolarHolidayStruct(5, 31, 0, "世界无烟日"), 
                new SolarHolidayStruct(6, 1, 0, "国际儿童节"), 
                new SolarHolidayStruct(6, 5, 0, "世界环境保护日"),
                new SolarHolidayStruct(6, 26, 0, "国际禁毒日"),
                new SolarHolidayStruct(7, 1, 0, "建党节 香港回归纪念 世界建筑日"),
                new SolarHolidayStruct(7, 11, 0, "世界人口日"),
                new SolarHolidayStruct(8, 1, 0, "建军节"), 
                new SolarHolidayStruct(8, 8, 0, "中国男子节 父亲节"),
                new SolarHolidayStruct(8, 15, 0, "抗日战争胜利纪念"),
                new SolarHolidayStruct(9, 9, 0, "  逝世纪念"), 
                new SolarHolidayStruct(9, 10, 0, "教师节"), 
                new SolarHolidayStruct(9, 18, 0, "九·一八事变纪念日"),
                new SolarHolidayStruct(9, 20, 0, "国际爱牙日"),
                new SolarHolidayStruct(9, 27, 0, "世界旅游日"),
                new SolarHolidayStruct(9, 28, 0, "孔子诞辰"),
                new SolarHolidayStruct(10, 1, 1, "国庆节 国际音乐日"),
                new SolarHolidayStruct(10, 2, 1, "国庆节假日"),
                new SolarHolidayStruct(10, 3, 1, "国庆节假日"),
                new SolarHolidayStruct(10, 6, 0, "老人节"), 
                new SolarHolidayStruct(10, 24, 0, "联合国日"),
                new SolarHolidayStruct(11, 10, 0, "世界青年节"),
                new SolarHolidayStruct(11, 12, 0, "孙中山诞辰纪念"), 
                new SolarHolidayStruct(12, 1, 0, "世界艾滋病日"), 
                new SolarHolidayStruct(12, 3, 0, "世界残疾人日"), 
                new SolarHolidayStruct(12, 20, 0, "澳门回归纪念"), 
                new SolarHolidayStruct(12, 24, 0, "平安夜"), 
                new SolarHolidayStruct(12, 25, 0, "圣诞节"), 
                new SolarHolidayStruct(12, 26, 0, " 诞辰纪念")
               };
        #endregion
        #region 按农历计算的节日
        private static LunarHolidayStruct[] lHolidayInfo = new LunarHolidayStruct[]{
                new LunarHolidayStruct(1, 1, 1, "春节"), 
                new LunarHolidayStruct(1, 15, 0, "元宵节"), 
                new LunarHolidayStruct(5, 5, 0, "端午节"), 
                new LunarHolidayStruct(7, 7, 0, "七夕情人节"),
                new LunarHolidayStruct(7, 15, 0, "中元节 盂兰盆节"), 
                new LunarHolidayStruct(8, 15, 0, "中秋节"), 
                new LunarHolidayStruct(9, 9, 0, "重阳节"), 
                new LunarHolidayStruct(12, 8, 0, "腊八节"),
                new LunarHolidayStruct(12, 23, 0, "北方小年(扫房)"),
                new LunarHolidayStruct(12, 24, 0, "南方小年(掸尘)"),
                //new LunarHolidayStruct(12, 30, 0, "除夕")  //注意除夕需要其它方法进行计算
            };
        #endregion
        #region 按某月第几个星期几
        private static WeekHolidayStruct[] wHolidayInfo = new WeekHolidayStruct[]{
                new WeekHolidayStruct(5, 2, 1, "母亲节"), 
                new WeekHolidayStruct(5, 3, 1, "全国助残日"), 
                new WeekHolidayStruct(6, 3, 1, "父亲节"), 
                new WeekHolidayStruct(9, 3, 3, "国际和平日"), 
                new WeekHolidayStruct(9, 4, 1, "国际聋人节"), 
                new WeekHolidayStruct(10, 1, 2, "国际住房日"), 
                new WeekHolidayStruct(10, 1, 4, "国际减轻自然灾害日"),
                new WeekHolidayStruct(11, 4, 5, "感恩节")
            };
        #endregion
        #endregion
        #region 构造函数
        #region ChinaCalendar <公历日期初始化>
        /// <summary>
        /// 用一个标准的公历日期来初使化
        /// </summary>
        /// <param name="dt"></param>
        public ChineseCalendar(DateTime dt)
        {
            int i;
            int leap;
            int temp;
            int offset;
            CheckDateLimit(dt);
            _date = dt.Date;
            _datetime = dt;
            //农历日期计算部分
            leap = 0;
            temp = 0;
            TimeSpan ts = _date - ChineseCalendar.MinDay;//计算两天的基本差距
            offset = ts.Days;
            for (i = MinYear; i <= MaxYear; i++)
            {
                temp = GetChineseYearDays(i);  //求当年农历年天数
                if (offset - temp < 1)
                    break;
                else
                {
                    offset = offset - temp;
                }
            }
            _cYear = i;
            leap = GetChineseLeapMonth(_cYear);//计算该年闰哪个月
            //设定当年是否有闰月
            if (leap > 0)
            {
                _cIsLeapYear = true;
            }
            else
            {
                _cIsLeapYear = false;
            }
            _cIsLeapMonth = false;
            for (i = 1; i <= 12; i++)
            {
                //闰月
                if ((leap > 0) && (i == leap + 1) && (_cIsLeapMonth == false))
                {
                    _cIsLeapMonth = true;
                    i = i - 1;
                    temp = GetChineseLeapMonthDays(_cYear); //计算闰月天数
                }
                else
                {
                    _cIsLeapMonth = false;
                    temp = GetChineseMonthDays(_cYear, i);//计算非闰月天数
                }
                offset = offset - temp;
                if (offset <= 0) break;
            }
            offset = offset + temp;
            _cMonth = i;
            _cDay = offset;
        }
        #endregion
        #region ChinaCalendar <农历日期初始化>
        /// <summary>
        /// 用农历的日期来初使化
        /// </summary>
        /// <param name="cy">农历年</param>
        /// <param name="cm">农历月</param>
        /// <param name="cd">农历日</param>
        /// <param name="LeapFlag">闰月标志</param>
        public ChineseCalendar(int cy, int cm, int cd, bool leapMonthFlag)
        {
            int i, leap, Temp, offset;
            CheckChineseDateLimit(cy, cm, cd, leapMonthFlag);
            _cYear = cy;
            _cMonth = cm;
            _cDay = cd;
            offset = 0;
            for (i = MinYear; i < cy; i++)
            {
                Temp = GetChineseYearDays(i); //求当年农历年天数
                offset = offset + Temp;
            }
            leap = GetChineseLeapMonth(cy);// 计算该年应该闰哪个月
            if (leap != 0)
            {
                this._cIsLeapYear = true;
            }
            else
            {
                this._cIsLeapYear = false;
            }
            if (cm != leap)
            {
                _cIsLeapMonth = false;  //当前日期并非闰月
            }
            else
            {
                _cIsLeapMonth = leapMonthFlag;  //使用用户输入的是否闰月月份
            }

            if ((_cIsLeapYear == false) || //当年没有闰月
                 (cm < leap)) //计算月份小于闰月     
            {
                #region ...
                for (i = 1; i < cm; i++)
                {
                    Temp = GetChineseMonthDays(cy, i);//计算非闰月天数
                    offset = offset + Temp;
                }
                //检查日期是否大于最大天
                if (cd > GetChineseMonthDays(cy, cm))
                {
                    throw new ChineseCalendarException("不合法的农历日期");
                }
                offset = offset + cd; //加上当月的天数
                #endregion
            }
            else   //是闰年，且计算月份大于或等于闰月
            {
                #region ...
                for (i = 1; i < cm; i++)
                {
                    Temp = GetChineseMonthDays(cy, i); //计算非闰月天数
                    offset = offset + Temp;
                }
                if (cm > leap) //计算月大于闰月
                {
                    Temp = GetChineseLeapMonthDays(cy);   //计算闰月天数
                    offset = offset + Temp;               //加上闰月天数
                    if (cd > GetChineseMonthDays(cy, cm))
                    {
                        throw new ChineseCalendarException("不合法的农历日期");
                    }
                    offset = offset + cd;
                }
                else  //计算月等于闰月
                {
                    //如果需要计算的是闰月，则应首先加上与闰月对应的普通月的天数
                    if (this._cIsLeapMonth == true) //计算月为闰月
                    {
                        Temp = GetChineseMonthDays(cy, cm); //计算非闰月天数
                        offset = offset + Temp;
                    }
                    if (cd > GetChineseLeapMonthDays(cy))
                    {
                        throw new ChineseCalendarException("不合法的农历日期");
                    }
                    offset = offset + cd;
                }
                #endregion
            }

            _date = MinDay.AddDays(offset);
        }
        #endregion
        #endregion
        #region 私有函数
        #region GetChineseMonthDays
        //传回农历 y年m月的总天数
        private int GetChineseMonthDays(int year, int month)
        {
            if (BitTest32((LunarDateArray[year - MinYear] & 0x0000FFFF), (16 - month)))
            {
                return 30;
            }
            else
            {
                return 29;
            }
        }
        #endregion
        #region GetChineseLeapMonth
        //传回农历 y年闰哪个月 1-12 , 没闰传回 0
        private int GetChineseLeapMonth(int year)
        {
            return LunarDateArray[year - MinYear] & 0xF;
        }
        #endregion
        #region GetChineseLeapMonthDays
        //传回农历 y年闰月的天数
        private int GetChineseLeapMonthDays(int year)
        {
            if (GetChineseLeapMonth(year) != 0)
            {
                if ((LunarDateArray[year - MinYear] & 0x10000) != 0)
                {
                    return 30;
                }
                else
                {
                    return 29;
                }
            }
            else
            {
                return 0;
            }
        }
        #endregion
        #region GetChineseYearDays
        /// <summary>
        /// 取农历年一年的天数
        /// </summary>
        /// <param name="year"></param>
        /// <returns></returns>
        private int GetChineseYearDays(int year)
        {
            int i, f, sumDay, info;
            sumDay = 348; //29天 X 12个月
            i = 0x8000;
            info = LunarDateArray[year - MinYear] & 0x0FFFF;
            //计算12个月中有多少天为30天
            for (int m = 0; m < 12; m++)
            {
                f = info & i;
                if (f != 0)
                {
                    sumDay++;
                }
                i = i >> 1;
            }
            return sumDay + GetChineseLeapMonthDays(year);
        }
        #endregion
        #region GetChineseHour
        /// <summary>
        /// 获得当前时间的时辰
        /// </summary>
        /// <param name="time"></param>
        /// <returns></returns>
        /// 
        private string GetChineseHour(DateTime dt)
        {
            int _hour, _minute, offset, i;
            int indexGan;
            //string ganHour, zhiHour;
            string tmpGan;
            //计算时辰的地支
            _hour = dt.Hour;    //获得当前时间小时
            _minute = dt.Minute;  //获得当前时间分钟
            if (_minute != 0) _hour += 1;
            offset = _hour / 2;
            if (offset >= 12) offset = 0;
            //zhiHour = zhiStr[offset].ToString();
            //计算天干
            TimeSpan ts = this._date - GanZhiStartDay;
            i = ts.Days % 60;
            indexGan = ((i % 10 + 1) * 2 - 1) % 10 - 1; //ganStr[i % 10] 为日的天干,(n*2-1) %10得出地支对应,n从1开始
            tmpGan = ganStr.Substring(indexGan) + ganStr.Substring(0, indexGan + 2);//凑齐12位
            //ganHour = ganStr[((i % 10 + 1) * 2 - 1) % 10 - 1].ToString();
            return tmpGan[offset].ToString() + zhiStr[offset].ToString();
        }
        #endregion
        #region CheckDateLimit
        /// <summary>
        /// 检查公历日期是否符合要求
        /// </summary>
        /// <param name="dt"></param>
        private void CheckDateLimit(DateTime dt)
        {
            if ((dt < MinDay) || (dt > MaxDay))
            {
                throw new ChineseCalendarException("超出可转换的日期");
            }
        }
        #endregion
        #region CheckChineseDateLimit
        /// <summary>
        /// 检查农历日期是否合理
        /// </summary>
        /// <param name="year"></param>
        /// <param name="month"></param>
        /// <param name="day"></param>
        /// <param name="leapMonth"></param>
        private void CheckChineseDateLimit(int year, int month, int day, bool leapMonth)
        {
            if ((year < MinYear) || (year > MaxYear))
            {
                throw new ChineseCalendarException("非法农历日期");
            }
            if ((month < 1) || (month > 12))
            {
                throw new ChineseCalendarException("非法农历日期");
            }
            if ((day < 1) || (day > 30)) //中国的月最多30天
            {
                throw new ChineseCalendarException("非法农历日期");
            }
            int leap = GetChineseLeapMonth(year);// 计算该年应该闰哪个月
            if ((leapMonth == true) && (month != leap))
            {
                throw new ChineseCalendarException("非法农历日期");
            }

        }
        #endregion
        #region ConvertNumToChineseNum
        /// <summary>
        /// 将0-9转成汉字形式
        /// </summary>
        /// <param name="n"></param>
        /// <returns></returns>
        private string ConvertNumToChineseNum(char n)
        {
            if ((n < '0') || (n > '9')) return "";
            switch (n)
            {
                case '0':
                    return HZNum[0].ToString();
                case '1':
                    return HZNum[1].ToString();
                case '2':
                    return HZNum[2].ToString();
                case '3':
                    return HZNum[3].ToString();
                case '4':
                    return HZNum[4].ToString();
                case '5':
                    return HZNum[5].ToString();
                case '6':
                    return HZNum[6].ToString();
                case '7':
                    return HZNum[7].ToString();
                case '8':
                    return HZNum[8].ToString();
                case '9':
                    return HZNum[9].ToString();
                default:
                    return "";
            }
        }
        #endregion
        #region BitTest32
        /// <summary>
        /// 测试某位是否为真
        /// </summary>
        /// <param name="num"></param>
        /// <param name="bitpostion"></param>
        /// <returns></returns>
        private bool BitTest32(int num, int bitpostion)
        {
            if ((bitpostion > 31) || (bitpostion < 0))
                throw new Exception("Error Param: bitpostion[0-31]:" + bitpostion.ToString());
            int bit = 1 << bitpostion;
            if ((num & bit) == 0)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
        #endregion
        #region ConvertDayOfWeek
        /// <summary>
        /// 将星期几转成数字表示
        /// </summary>
        /// <param name="dayOfWeek"></param>
        /// <returns></returns>
        private int ConvertDayOfWeek(DayOfWeek dayOfWeek)
        {
            switch (dayOfWeek)
            {
                case DayOfWeek.Sunday:
                    return 1;
                case DayOfWeek.Monday:
                    return 2;
                case DayOfWeek.Tuesday:
                    return 3;
                case DayOfWeek.Wednesday:
                    return 4;
                case DayOfWeek.Thursday:
                    return 5;
                case DayOfWeek.Friday:
                    return 6;
                case DayOfWeek.Saturday:
                    return 7;
                default:
                    return 0;
            }
        }
        #endregion
        #region CompareWeekDayHoliday
        /// <summary>
        /// 比较当天是不是指定的第周几
        /// </summary>
        /// <param name="date"></param>
        /// <param name="month"></param>
        /// <param name="week"></param>
        /// <param name="day"></param>
        /// <returns></returns>
        private bool CompareWeekDayHoliday(DateTime date, int month, int week, int day)
        {
            bool ret = false;
            if (date.Month == month) //月份相同
            {
                if (ConvertDayOfWeek(date.DayOfWeek) == day) //星期几相同
                {
                    DateTime firstDay = new DateTime(date.Year, date.Month, 1);//生成当月第一天
                    int i = ConvertDayOfWeek(firstDay.DayOfWeek);
                    int firWeekDays = 7 - ConvertDayOfWeek(firstDay.DayOfWeek) + 1; //计算第一周剩余天数
                    if (i > day)
                    {
                        if ((week - 1) * 7 + day + firWeekDays == date.Day)
                        {
                            ret = true;
                        }
                    }
                    else
                    {
                        if (day + firWeekDays + (week - 2) * 7 == date.Day)
                        {
                            ret = true;
                        }
                    }
                }
            }
            return ret;
        }
        #endregion
        #endregion
        #region  属性
        #region 节日
        #region ChineseCalendarHoliday
        /// <summary>
        /// 计算中国农历节日
        /// </summary>
        public string ChineseCalendarHoliday
        {
            get
            {
                string tempStr = "";
                if (this._cIsLeapMonth == false) //闰月不计算节日
                {
                    foreach (LunarHolidayStruct lh in lHolidayInfo)
                    {
                        if ((lh.Month == this._cMonth) && (lh.Day == this._cDay))
                        {
                            tempStr = lh.HolidayName;
                            break;
                        }
                    }
                    //对除夕进行特别处理
                    if (this._cMonth == 12)
                    {
                        int i = GetChineseMonthDays(this._cYear, 12); //计算当年农历12月的总天数
                        if (this._cDay == i) //如果为最后一天
                        {
                            tempStr = "除夕";
                        }
                    }
                }
                return tempStr;
            }
        }
        #endregion
        #region WeekDayHoliday
        /// <summary>
        /// 按某月第几周第几日计算的节日
        /// </summary>
        public string WeekDayHoliday
        {
            get
            {
                string tempStr = "";
                foreach (WeekHolidayStruct wh in wHolidayInfo)
                {
                    if (CompareWeekDayHoliday(_date, wh.Month, wh.WeekAtMonth, wh.WeekDay))
                    {
                        tempStr = wh.HolidayName;
                        break;
                    }
                }
                return tempStr;
            }
        }
        #endregion
        #region DateHoliday
        /// <summary>
        /// 按公历日计算的节日
        /// </summary>
        public string DateHoliday
        {
            get
            {
                string tempStr = "";
                foreach (SolarHolidayStruct sh in sHolidayInfo)
                {
                    if ((sh.Month == _date.Month) && (sh.Day == _date.Day))
                    {
                        tempStr = sh.HolidayName;
                        break;
                    }
                }
                return tempStr;
            }
        }
        #endregion
        #endregion
        #region 公历日期
        #region Date
        /// <summary>
        /// 取对应的公历日期
        /// </summary>
        public DateTime Date
        {
            get { return _date; }
            set { _date = value; }
        }
        #endregion
        #region WeekDay
        /// <summary>
        /// 取星期几
        /// </summary>
        public DayOfWeek WeekDay
        {
            get { return _date.DayOfWeek; }
        }
        #endregion
        #region WeekDayStr
        /// <summary>
        /// 周几的字符
        /// </summary>
        public string WeekDayStr
        {
            get
            {
                switch (_date.DayOfWeek)
                {
                    case DayOfWeek.Sunday:
                        return "星期日";
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
                    default:
                        return "星期六";
                }
            }
        }
        #endregion
        #region DateString
        /// <summary>
        /// 公历日期中文表示法 如一九九七年七月一日
        /// </summary>
        public string DateString
        {
            get
            {
                return "公元" + this._date.ToLongDateString();
            }
        }
        #endregion
        #region IsLeapYear
        /// <summary>
        /// 当前是否公历闰年
        /// </summary>
        public bool IsLeapYear
        {
            get
            {
                return DateTime.IsLeapYear(this._date.Year);
            }
        }
        #endregion
        #region ChineseConstellation
        /// <summary>
        /// 28星宿计算
        /// </summary>
        public string ChineseConstellation
        {
            get
            {
                int offset = 0;
                int modStarDay = 0;
                TimeSpan ts = this._date - ChineseConstellationReferDay;
                offset = ts.Days;
                modStarDay = offset % 28;
                return (modStarDay >= 0 ? _chineseConstellationName[modStarDay] : _chineseConstellationName[27 + modStarDay]);
            }
        }
        #endregion
        #region ChineseHour
        /// <summary>
        /// 时辰
        /// </summary>
        public string ChineseHour
        {
            get
            {
                return GetChineseHour(_datetime);
            }
        }
        #endregion
        #endregion
        #region 农历日期
        #region IsChineseLeapMonth
        /// <summary>
        /// 是否闰月
        /// </summary>
        public bool IsChineseLeapMonth
        {
            get { return this._cIsLeapMonth; }
        }
        #endregion
        #region IsChineseLeapYear
        /// <summary>
        /// 当年是否有闰月
        /// </summary>
        public bool IsChineseLeapYear
        {
            get
            {
                return this._cIsLeapYear;
            }
        }
        #endregion
        #region ChineseDay
        /// <summary>
        /// 农历日
        /// </summary>
        public int ChineseDay
        {
            get { return this._cDay; }
        }
        #endregion
        #region ChineseDayString
        /// <summary>
        /// 农历日中文表示
        /// </summary>
        public string ChineseDayString
        {
            get
            {
                switch (this._cDay)
                {
                    case 0:
                        return "";
                    case 10:
                        return "初十";
                    case 20:
                        return "二十";
                    case 30:
                        return "三十";
                    default:
                        return nStr2[(int)(_cDay / 10)].ToString() + nStr1[_cDay % 10].ToString();
                }
            }
        }
        #endregion
        #region ChineseMonth
        /// <summary>
        /// 农历的月份
        /// </summary>
        public int ChineseMonth
        {
            get { return this._cMonth; }
        }
        #endregion
        #region ChineseMonthString
        /// <summary>
        /// 农历月份字符串
        /// </summary>
        public string ChineseMonthString
        {
            get
            {
                return _monthString[this._cMonth];
            }
        }
        #endregion
        #region ChineseYear
        /// <summary>
        /// 取农历年份
        /// </summary>
        public int ChineseYear
        {
            get { return this._cYear; }
        }
        #endregion
        #region ChineseYearString
        /// <summary>
        /// 取农历年字符串如，一九九七年
        /// </summary>
        public string ChineseYearString
        {
            get
            {
                string tempStr = "";
                string num = this._cYear.ToString();
                for (int i = 0; i < 4; i++)
                {
                    tempStr += ConvertNumToChineseNum(num[i]);
                }
                return tempStr + "年";
            }
        }
        #endregion
        #region ChineseDateString
        /// <summary>
        /// 取农历日期表示法：农历一九九七年正月初五
        /// </summary>
        public string ChineseDateString
        {
            get
            {
                if (this._cIsLeapMonth == true)
                {
                    return "农历" + ChineseYearString + "闰" + ChineseMonthString + ChineseDayString;
                }
                else
                {
                    return "农历" + ChineseYearString + ChineseMonthString + ChineseDayString;
                }
            }
        }
        #endregion
        #region ChineseTwentyFourDay
        /// <summary>
        /// 定气法计算二十四节气,二十四节气是按地球公转来计算的，并非是阴历计算的
        /// </summary>
        /// <remarks>
        /// 节气的定法有两种。古代历法采用的称为"恒气"，即按时间把一年等分为24份，
        /// 每一节气平均得15天有余，所以又称"平气"。现代农历采用的称为"定气"，即
        /// 按地球在轨道上的位置为标准，一周360°，两节气之间相隔15°。由于冬至时地
        /// 球位于近日点附近，运动速度较快，因而太阳在黄道上移动15°的时间不到15天。
        /// 夏至前后的情况正好相反，太阳在黄道上移动较慢，一个节气达16天之多。采用
        /// 定气时可以保证春、秋两分必然在昼夜平分的那两天。
        /// </remarks>
        public string ChineseTwentyFourDay
        {
            get
            {
                DateTime baseDateAndTime = new DateTime(1900, 1, 6, 2, 5, 0); //#1/6/1900 2:05:00 AM#
                DateTime newDate;
                double num;
                int y;
                string tempStr = "";
                y = this._date.Year;
                for (int i = 1; i <= 24; i++)
                {
                    num = 525948.76 * (y - 1900) + sTermInfo[i - 1];
                    newDate = baseDateAndTime.AddMinutes(num);//按分钟计算
                    if (newDate.DayOfYear == _date.DayOfYear)
                    {
                        tempStr = SolarTerm[i - 1];
                        break;
                    }
                }
                return tempStr;
            }
        }
        //当前日期前一个最近节气
        public string ChineseTwentyFourPrevDay
        {
            get
            {
                DateTime baseDateAndTime = new DateTime(1900, 1, 6, 2, 5, 0); //#1/6/1900 2:05:00 AM#
                DateTime newDate;
                double num;
                int y;
                string tempStr = "";
                y = this._date.Year;
                for (int i = 24; i >= 1; i--)
                {
                    num = 525948.76 * (y - 1900) + sTermInfo[i - 1];
                    newDate = baseDateAndTime.AddMinutes(num);//按分钟计算
                    if (newDate.DayOfYear < _date.DayOfYear)
                    {
                        tempStr = string.Format("{0}[{1}]", SolarTerm[i - 1], newDate.ToString("yyyy-MM-dd"));
                        break;
                    }
                }
                return tempStr;
            }
        }
        //当前日期后一个最近节气
        public string ChineseTwentyFourNextDay
        {
            get
            {
                DateTime baseDateAndTime = new DateTime(1900, 1, 6, 2, 5, 0); //#1/6/1900 2:05:00 AM#
                DateTime newDate;
                double num;
                int y;
                string tempStr = "";
                y = this._date.Year;
                for (int i = 1; i <= 24; i++)
                {
                    num = 525948.76 * (y - 1900) + sTermInfo[i - 1];
                    newDate = baseDateAndTime.AddMinutes(num);//按分钟计算
                    if (newDate.DayOfYear > _date.DayOfYear)
                    {
                        tempStr = string.Format("{0}[{1}]", SolarTerm[i - 1], newDate.ToString("yyyy-MM-dd"));
                        break;
                    }
                }
                return tempStr;
            }
        }
        #endregion
        #endregion
        #region 星座
        #region Constellation
        /// <summary>
        /// 计算指定日期的星座序号 
        /// </summary>
        /// <returns></returns>
        public string Constellation
        {
            get
            {
                int index = 0;
                int y, m, d;
                y = _date.Year;
                m = _date.Month;
                d = _date.Day;
                y = m * 100 + d;
                if (((y >= 321) && (y <= 419))) { index = 0; }
                else if ((y >= 420) && (y <= 520)) { index = 1; }
                else if ((y >= 521) && (y <= 620)) { index = 2; }
                else if ((y >= 621) && (y <= 722)) { index = 3; }
                else if ((y >= 723) && (y <= 822)) { index = 4; }
                else if ((y >= 823) && (y <= 922)) { index = 5; }
                else if ((y >= 923) && (y <= 1022)) { index = 6; }
                else if ((y >= 1023) && (y <= 1121)) { index = 7; }
                else if ((y >= 1122) && (y <= 1221)) { index = 8; }
                else if ((y >= 1222) || (y <= 119)) { index = 9; }
                else if ((y >= 120) && (y <= 218)) { index = 10; }
                else if ((y >= 219) && (y <= 320)) { index = 11; }
                else { index = 0; }
                return _constellationName[index];
            }
        }
        #endregion
        #endregion
        #region 属相
        #region Animal
        /// <summary>
        /// 计算属相的索引，注意虽然属相是以农历年来区别的，但是目前在实际使用中是按公历来计算的
        /// 鼠年为1,其它类推
        /// </summary>
        public int Animal
        {
            get
            {
                int offset = _date.Year - AnimalStartYear;
                return (offset % 12) + 1;
            }
        }
        #endregion
        #region AnimalString
        /// <summary>
        /// 取属相字符串
        /// </summary>
        public string AnimalString
        {
            get
            {
                int offset = _date.Year - AnimalStartYear; //阳历计算
                //int offset = this._cYear - AnimalStartYear;　农历计算
                return animalStr[offset % 12].ToString();
            }
        }
        #endregion
        #endregion
        #region 天干地支
        #region GanZhiYearString
        /// <summary>
        /// 取农历年的干支表示法如 乙丑年
        /// </summary>
        public string GanZhiYearString
        {
            get
            {
                string tempStr;
                int i = (this._cYear - GanZhiStartYear) % 60; //计算干支
                tempStr = ganStr[i % 10].ToString() + zhiStr[i % 12].ToString() + "年";
                return tempStr;
            }
        }
        #endregion
        #region GanZhiMonthString
        /// <summary>
        /// 取干支的月表示字符串，注意农历的闰月不记干支
        /// </summary>
        public string GanZhiMonthString
        {
            get
            {
                //每个月的地支总是固定的,而且总是从寅月开始
                int zhiIndex;
                string zhi;
                if (this._cMonth > 10)
                {
                    zhiIndex = this._cMonth - 10;
                }
                else
                {
                    zhiIndex = this._cMonth + 2;
                }
                zhi = zhiStr[zhiIndex - 1].ToString();
                //根据当年的干支年的干来计算月干的第一个
                int ganIndex = 1;
                string gan;
                int i = (this._cYear - GanZhiStartYear) % 60; //计算干支
                switch (i % 10)
                {
                    #region ...
                    case 0: //甲
                        ganIndex = 3;
                        break;
                    case 1: //乙
                        ganIndex = 5;
                        break;
                    case 2: //丙
                        ganIndex = 7;
                        break;
                    case 3: //丁
                        ganIndex = 9;
                        break;
                    case 4: //戊
                        ganIndex = 1;
                        break;
                    case 5: //己
                        ganIndex = 3;
                        break;
                    case 6: //庚
                        ganIndex = 5;
                        break;
                    case 7: //辛
                        ganIndex = 7;
                        break;
                    case 8: //壬
                        ganIndex = 9;
                        break;
                    case 9: //癸
                        ganIndex = 1;
                        break;
                    #endregion
                }
                gan = ganStr[(ganIndex + this._cMonth - 2) % 10].ToString();
                return gan + zhi + "月";
            }
        }
        #endregion
        #region GanZhiDayString
        /// <summary>
        /// 取干支日表示法
        /// </summary>
        public string GanZhiDayString
        {
            get
            {
                int i, offset;
                TimeSpan ts = this._date - GanZhiStartDay;
                offset = ts.Days;
                i = offset % 60;
                return ganStr[i % 10].ToString() + zhiStr[i % 12].ToString() + "日";
            }
        }
        #endregion
        #region GanZhiDateString
        /// <summary>
        /// 取当前日期的干支表示法如 甲子年乙丑月丙庚日
        /// </summary>
        public string GanZhiDateString
        {
            get
            {
                return GanZhiYearString + GanZhiMonthString + GanZhiDayString;
            }
        }
        #endregion
        #endregion
        #endregion
        #region 方法
        #region NextDay
        /// <summary>
        /// 取下一天
        /// </summary>
        /// <returns></returns>
        public ChineseCalendar NextDay()
        {
            DateTime nextDay = _date.AddDays(1);
            return new ChineseCalendar(nextDay);
        }
        #endregion
        #region PervDay
        /// <summary>
        /// 取前一天
        /// </summary>
        /// <returns></returns>
        public ChineseCalendar PervDay()
        {
            DateTime pervDay = _date.AddDays(-1);
            return new ChineseCalendar(pervDay);
        }
        #endregion
        #endregion
    }
}

//6060
//------------------------------------------------------------
//


/*

this.Date = DateTime.Today;

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


                year = DateTime.Now.Year;
                month = DateTime.Now.Month;
                day = DateTime.Now.Day;


*/

// DateTime.Parse()  抓出來



