using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Globalization; //for CultureInfo   //for 民國記年 農曆

namespace vcs_test_all_01_DateTime
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
            label5.Text = "";
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            timer1.Interval = 1000;
            timer1.Enabled = true;

            // Start with a sample date.
            txtDate.Text = "11 March 2006, 9:15";

            calculate_time_difference();

            load_listview_data();

            show_item_location();

        }

        void show_item_location()
        {
            /*
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 1700;
            y_st = 12;
            dx = 190;
            dy = 50;
            */

            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 170;
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
            button10.Location = new Point(x_st + dx * 0, y_st + dy * 10);
            button11.Location = new Point(x_st + dx * 0, y_st + dy * 11);
            button12.Location = new Point(x_st + dx * 0, y_st + dy * 12);
            button13.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            button14.Location = new Point(x_st + dx * 0, y_st + dy * 14);

            button15.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button16.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button17.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button18.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button19.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button20.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button24.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button27.Location = new Point(x_st + dx * 1, y_st + dy * 12);
            button28.Location = new Point(x_st + dx * 1, y_st + dy * 13);
            button29.Location = new Point(x_st + dx * 1, y_st + dy * 14);

            button30.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button31.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button32.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button33.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button34.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button35.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button36.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button37.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button38.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button39.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button40.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button41.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            button42.Location = new Point(x_st + dx * 2, y_st + dy * 12);
            button43.Location = new Point(x_st + dx * 2, y_st + dy * 13);
            button44.Location = new Point(x_st + dx * 2, y_st + dy * 14);

            button45.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button46.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button47.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button48.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button49.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button50.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button51.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            /*
            button52.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button53.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button54.Location = new Point(x_st + dx * 3, y_st + dy * 9);
            button55.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            button56.Location = new Point(x_st + dx * 3, y_st + dy * 11);
            button57.Location = new Point(x_st + dx * 3, y_st + dy * 12);
            button58.Location = new Point(x_st + dx * 3, y_st + dy * 13);
            button59.Location = new Point(x_st + dx * 3, y_st + dy * 14);
            */

            //button
            x_st = 10;
            y_st = 10;
            dx = 170;
            dy = 55;

            textBox2.Location = new Point(x_st + dx * 4, y_st + dy * 9);
            bt1.Location = new Point(x_st + dx * 5, y_st + dy * 9);
            textBox1.Location = new Point(x_st + dx * 4, y_st + dy * 10);
            bt0.Location = new Point(x_st + dx * 5, y_st + dy * 10);
            dateTimePicker1.Location = new Point(x_st + dx * 4, y_st + dy * 11);
            bt2.Location = new Point(x_st + dx * 5, y_st + dy * 11);
            bt4.Location = new Point(x_st + dx * 5, y_st + dy * 12);

            label1.Location = new Point(x_st + dx * 4, y_st + dy * 15);
            label2.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 15);
            label5.Location = new Point(x_st + dx * 6 + 200, y_st + dy * 15);

            label3.Location = new Point(x_st + dx * 4, y_st + dy * 16);
            label4.Location = new Point(x_st + dx * 5 + 100, y_st + dy * 16);

            //richTextBox1.Location = new Point(x_st + dx * 0, y_st + dy * 13);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            //最大化螢幕
            //this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
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

            //C# 計算差異天數
            startDate = "628年7月21日";
            endDate = "683年12月27日";

            dtStart = DateTime.Parse(startDate);
            dtEnd = DateTime.Parse(endDate);
            // 計算差異天數
            tsDay = dtEnd - dtStart;
            dayCount = (int)tsDay.TotalDays;
            richTextBox1.Text += "相差" + dayCount.ToString() + "天" + "\n";
            richTextBox1.Text += "天1 : " + tsDay.Days.ToString() + "\n";        //same
            richTextBox1.Text += "天1 : " + tsDay.TotalDays.ToString() + "\n";   //same
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


            richTextBox1.Text += "\n";
            richTextBox1.Text += dateTimePicker1.Value.Year.ToString();
            richTextBox1.Text += "/" + dateTimePicker1.Value.Month.ToString();
            richTextBox1.Text += "/" + dateTimePicker1.Value.Day.ToString();

            richTextBox1.Text += " " + DateTime.Now.Hour;
            richTextBox1.Text += ":" + DateTime.Now.Minute;
            richTextBox1.Text += ":" + DateTime.Now.Second;
            richTextBox1.Text += "\n";


        }

        private void button30_Click(object sender, EventArgs e)
        {
            //尋找13號星期五
            int year_st = 2020;
            int year_sp = 2030;

            // Loop over the selected years.
            for (int year = year_st; year <= year_sp; year++)
            {
                // Loop over the months in the year.
                for (int month = 1; month <= 12; month++)
                {
                    // See if this month's 13th is a Friday.
                    DateTime dt = new DateTime(year, month, 13);

                    // See if this is a Friday.
                    if (dt.DayOfWeek == DayOfWeek.Friday)
                    {
                        richTextBox1.Text += dt.ToShortDateString() + "\n";
                    }
                }
            }
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
            //2022年距今還有多久
            DateTime EventDate = new DateTime(2022, 1, 1, 0, 0, 0);
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


        private void button31_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            string lunar_date;
            lunar_date = GetLunarCalendar(dt);
            richTextBox1.Text += lunar_date + "\n";

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

        private void button40_Click(object sender, EventArgs e)
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

        private void button45_Click(object sender, EventArgs e)
        {
        }

        private void button33_Click(object sender, EventArgs e)
        {
            System.Globalization.ChineseLunisolarCalendar chinseCaleander =//創建日歷對象ChineseLunisolarCalendar,將時間分成多個部分來表示，如分成年、月和日。 年按農歷計算，而日和月按陰陽歷計算。
new System.Globalization.ChineseLunisolarCalendar();
            string TreeYear = "鼠牛虎兔龍蛇馬羊猴雞狗豬";//創建字符串對象
            int intYear = chinseCaleander.GetSexagenaryYear(DateTime.Now);//計算年信息,GetSexagenaryYear計算與指定日期對應的甲子（60 年）循環中的年。
            string Tree = TreeYear.Substring(chinseCaleander.//得到生肖信息
                GetTerrestrialBranch(intYear) - 1, 1);//GetTerrestrialBranch計算甲子（60 年）循環中指定年份的地支,
            //Substring(x,y)從此實例檢索子字符串。 子字符串從指定的字符位置開始且具有指定的長度
            richTextBox1.Text += "今年是十二生肖 " + Tree + " 年\n";


            richTextBox1.Text += "今天是： "//顯示星期信息
                + DateTime.Now.ToString("dddd") + "\n";//dddd是星期日,ddd是日,dd是01

        }

        private void button47_Click(object sender, EventArgs e)
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




        }

        //y－年，m－月，d－日期
        string CaculateWeekDay(int y, int m, int d)
        {
            if (m == 1) m = 13;
            if (m == 2) m = 14;
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

        private void button48_Click(object sender, EventArgs e)
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
        }

        private void button39_Click(object sender, EventArgs e)
        {
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

        // If the text is a date, display
        // the elapsed time between then and now.
        private void txtDate_TextChanged(object sender, EventArgs e)
        {
            DateTime date;
            if (DateTime.TryParse(txtDate.Text, out date))
            {
                txtParsed.Text = date.ToString();

                TimeSpan elapsed = DateTime.Now - date;
                txtDays.Text = elapsed.TotalDays.ToString();
                txtHours.Text = elapsed.TotalHours.ToString();
                txtMinutes.Text = elapsed.TotalMinutes.ToString();
                txtSeconds.Text = elapsed.TotalSeconds.ToString();
            }
            else
            {
                txtParsed.Clear();
                txtDays.Clear();
                txtHours.Clear();
                txtMinutes.Clear();
                txtSeconds.Clear();
            }
        }

        void calculate_time_difference()
        {
            DateTime date1, date2;
            if (!DateTime.TryParse(textBox8.Text, out date1))
                return;
            textBox3.Text = date1.ToString();

            if (!DateTime.TryParse(textBox10.Text, out date2))
                return;
            textBox9.Text = date1.ToString();

            int years, months, days, hours, minutes, seconds, milliseconds;

            GetElapsedTime(date1, date2, out years, out months,
                out days, out hours, out minutes, out seconds, out milliseconds);

            // Display the result.
            string txt = "";
            if (years != 0) txt += ", " + years.ToString() + " years";
            if (months != 0) txt += ", " + months.ToString() + " months";
            if (days != 0) txt += ", " + days.ToString() + " days";
            if (hours != 0) txt += ", " + hours.ToString() + " hours";
            if (minutes != 0) txt += ", " + minutes.ToString() + " minutes";
            if (seconds != 0) txt += ", " + seconds.ToString() + " seconds";
            if (milliseconds != 0) txt += ", " + milliseconds.ToString() + " milliseconds";
            if (txt.Length > 0) txt = txt.Substring(2);
            if (txt.Length == 0) txt = "Same";
            textBox7.Text = txt;
        }

        // Return the number of years, months, days, hours, minutes, seconds,
        // and milliseconds you need to add to from_date to get to_date.
        private void GetElapsedTime(DateTime from_date, DateTime to_date,
            out int years, out int months, out int days, out int hours,
            out int minutes, out int seconds, out int milliseconds)
        {
            // If from_date > to_date, switch them around.
            if (from_date > to_date)
            {
                GetElapsedTime(to_date, from_date,
                    out years, out months, out days, out hours,
                    out minutes, out seconds, out milliseconds);
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

        // Update the clocks.
        private void timer2_Tick(object sender, EventArgs e)
        {
            // Display the local time.
            DateTime now = DateTime.Now;
            lblLocalTime.Text = now.ToLongTimeString();
            lblLocalDate.Text = now.ToShortDateString();

            // Display the GMT time.
            DateTimeOffset local_offset = new DateTimeOffset(now);
            DateTimeOffset utc_offset = local_offset.ToUniversalTime();
            lblGmtTime.Text = utc_offset.DateTime.ToLongTimeString();
            lblGmtDate.Text = utc_offset.DateTime.ToShortDateString();
        }

        void load_listview_data()
        {
            DateTime now = DateTime.Now;
            listView1.Items.Add(new ListViewItem(new String[] { "ToLongDateString", "D", now.ToLongDateString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToLongTimeString", "T", now.ToLongTimeString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToShortDateString", "d", now.ToShortDateString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToShortTimeString", "t", now.ToShortTimeString() }));
            listView1.Items.Add(new ListViewItem(new String[] { "ToString", "G", now.ToString() }));
        }

        private void button51_Click(object sender, EventArgs e)
        {
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void bt0_Click(object sender, EventArgs e)
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

                dt_timer_st = System.DateTime.Now;
                wait_seconds = int.Parse(textBox2.Text) * 60;
                richTextBox1.Text += "等待時間： " + wait_seconds.ToString() + Environment.NewLine;
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

        private void bt4_Click(object sender, EventArgs e)
        {
            DateTime value;
            richTextBox1.Text += "日期 : " + textBox1.Text + "\n";
            try    // Parse the date and display it in ordinal format.
            {
                value = DateTime.Parse(textBox1.Text);
                richTextBox1.Text += "日期轉序數 : " + value.ToOrdinal() + "\n";
            }
            catch
            {
            }

            richTextBox1.Text += "日期 : " + dateTimePicker1.Text + "\n";
            try    // Parse the date and display it in ordinal format.
            {
                value = DateTime.Parse(dateTimePicker1.Text);
                richTextBox1.Text += "日期轉序數 : " + value.ToOrdinal() + "\n";
            }
            catch
            {
            }
        }

        private void button49_Click(object sender, EventArgs e)
        {
            //一段時間以後
            DateTime dt = DateTime.Now;

            //?日?時?分?秒 後
            DateTime dt_new = dt + new TimeSpan(365 * 10, 12, 34, 56);


            richTextBox1.Text += "現在時間 : " + dt.ToString() + "\n";
            richTextBox1.Text += "一段時間以後 : " + dt_new.ToString() + "\n";
        }

        private void button50_Click(object sender, EventArgs e)
        {
            //一段時間以後的寫法
            DateTime EventDate = DateTime.Now + new TimeSpan(1, 13, 42, 59);    //現在時間 + 1天13時42分59秒
            richTextBox1.Text += "現在時間 + 1天13時42分59秒 = " + EventDate.ToString() + "\n";

        }
    }
}


