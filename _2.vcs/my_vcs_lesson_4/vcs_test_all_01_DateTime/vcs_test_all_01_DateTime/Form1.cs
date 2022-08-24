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
        DateTime dt_timer_st = DateTime.Now;
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
            dx = 170 + 10;
            dy = 50 + 2;

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
            button15.Location = new Point(x_st + dx * 0, y_st + dy * 15);
            button16.Location = new Point(x_st + dx * 0, y_st + dy * 16);
            button17.Location = new Point(x_st + dx * 0, y_st + dy * 17);
            button18.Location = new Point(x_st + dx * 0, y_st + dy * 18);
            button19.Location = new Point(x_st + dx * 0, y_st + dy * 19);

            button20.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            button21.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            button22.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            button23.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            button24.Location = new Point(x_st + dx * 1, y_st + dy * 4);
            button25.Location = new Point(x_st + dx * 1, y_st + dy * 5);
            button26.Location = new Point(x_st + dx * 1, y_st + dy * 6);
            button27.Location = new Point(x_st + dx * 1, y_st + dy * 7);
            button28.Location = new Point(x_st + dx * 1, y_st + dy * 8);
            button29.Location = new Point(x_st + dx * 1, y_st + dy * 9);
            button30.Location = new Point(x_st + dx * 1, y_st + dy * 10);
            button31.Location = new Point(x_st + dx * 1, y_st + dy * 11);
            button32.Location = new Point(x_st + dx * 1, y_st + dy * 12);
            button33.Location = new Point(x_st + dx * 1, y_st + dy * 13);
            button34.Location = new Point(x_st + dx * 1, y_st + dy * 14);
            button35.Location = new Point(x_st + dx * 1, y_st + dy * 15);
            button36.Location = new Point(x_st + dx * 1, y_st + dy * 16);
            button37.Location = new Point(x_st + dx * 1, y_st + dy * 17);
            button38.Location = new Point(x_st + dx * 1, y_st + dy * 18);
            button39.Location = new Point(x_st + dx * 1, y_st + dy * 19);

            button40.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            button41.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            button42.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            button43.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            button44.Location = new Point(x_st + dx * 2, y_st + dy * 4);
            button45.Location = new Point(x_st + dx * 2, y_st + dy * 5);
            button46.Location = new Point(x_st + dx * 2, y_st + dy * 6);
            button47.Location = new Point(x_st + dx * 2, y_st + dy * 7);
            button48.Location = new Point(x_st + dx * 2, y_st + dy * 8);
            button49.Location = new Point(x_st + dx * 2, y_st + dy * 9);
            button50.Location = new Point(x_st + dx * 2, y_st + dy * 10);
            button51.Location = new Point(x_st + dx * 2, y_st + dy * 11);
            comboBox1.Location = new Point(x_st + dx * 2, y_st + dy * 12);
            //button52.Location = new Point(x_st + dx * 2, y_st + dy * 12);
            button53.Location = new Point(x_st + dx * 2, y_st + dy * 13);
            button54.Location = new Point(x_st + dx * 2, y_st + dy * 14);
            button55.Location = new Point(x_st + dx * 2, y_st + dy * 15);
            button56.Location = new Point(x_st + dx * 2, y_st + dy * 16);
            button57.Location = new Point(x_st + dx * 2, y_st + dy * 17);
            button58.Location = new Point(x_st + dx * 2, y_st + dy * 18);
            button59.Location = new Point(x_st + dx * 2, y_st + dy * 19);

            button60.Location = new Point(x_st + dx * 3, y_st + dy * 0);
            button61.Location = new Point(x_st + dx * 3, y_st + dy * 1);
            button62.Location = new Point(x_st + dx * 3, y_st + dy * 2);
            button63.Location = new Point(x_st + dx * 3, y_st + dy * 3);
            button64.Location = new Point(x_st + dx * 3, y_st + dy * 4);
            button65.Location = new Point(x_st + dx * 3, y_st + dy * 5);
            button66.Location = new Point(x_st + dx * 3, y_st + dy * 6);
            button67.Location = new Point(x_st + dx * 3, y_st + dy * 7);
            button68.Location = new Point(x_st + dx * 3, y_st + dy * 8);
            button69.Location = new Point(x_st + dx * 3, y_st + dy * 9);
            button70.Location = new Point(x_st + dx * 3, y_st + dy * 10);
            button71.Location = new Point(x_st + dx * 3, y_st + dy * 11);
            button72.Location = new Point(x_st + dx * 3, y_st + dy * 12);
            button73.Location = new Point(x_st + dx * 3, y_st + dy * 13);
            button74.Location = new Point(x_st + dx * 3, y_st + dy * 14);
            button75.Location = new Point(x_st + dx * 3, y_st + dy * 15);
            button76.Location = new Point(x_st + dx * 3, y_st + dy * 16);
            button77.Location = new Point(x_st + dx * 3, y_st + dy * 17);
            button78.Location = new Point(x_st + dx * 3, y_st + dy * 18);
            button79.Location = new Point(x_st + dx * 3, y_st + dy * 19);

            groupBox5.Location = new Point(x_st + dx * 4, y_st + dy * 6+30);
            groupBox6.Location = new Point(x_st + dx * 4, y_st + dy * 0);
            groupBox8.Location = new Point(x_st + dx * 4, y_st + dy * 8 + 30);
            groupBox7.Location = new Point(x_st + dx * 4, y_st + dy * 12 - 20);
            groupBox9.Location = new Point(x_st + dx * 4 + 145, y_st + dy * 12 - 20);
            groupBox10.Location = new Point(x_st + dx * 4, y_st + dy * 16 + 45);
            groupBox13.Location = new Point(x_st + dx * 4, y_st + dy * 3 + 30);

            groupBox1.Location = new Point(x_st + dx * 6+35, y_st + dy * 0);
            groupBox2.Location = new Point(x_st + dx * 6 + 35, y_st + dy * 5);
            groupBox4.Location = new Point(x_st + dx * 6 + 35, y_st + dy * 10);
            groupBox3.Location = new Point(x_st + dx * 6 + 35, y_st + dy * 12);
            groupBox11.Location = new Point(x_st + dx * 6 + 35, y_st + dy * 14);
            groupBox12.Location = new Point(x_st + dx * 6 + 110, y_st + dy * 17);

            textBox2.Location = new Point(x_st + dx * 0, y_st + dy * 0+10);
            bt1.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            textBox1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 40+10);
            bt0.Location = new Point(x_st + dx * 1, y_st + dy * 0 + 40);
            dateTimePicker1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 80+10);
            bt2.Location = new Point(x_st + dx * 1, y_st + dy * 0 + 80);

            label1.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 20);
            label2.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 60);
            label3.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 100);
            label4.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 140);
            label5.Location = new Point(x_st + dx * 0, y_st + dy * 0 + 180);

            richTextBox1.Size = new Size(520, 1040);
            richTextBox1.Location = new Point(x_st + dx * 8 - 60, y_st + dy * 0);
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            x_st = 10;
            y_st = 20;
            dx = 120 + 5;
            dy = 35 + 5;

            bt_special_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_special_01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_special_02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_special_03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_special_04.Location = new Point(x_st + dx * 1, y_st + dy * 0);
            bt_special_05.Location = new Point(x_st + dx * 1, y_st + dy * 1);
            bt_special_06.Location = new Point(x_st + dx * 1, y_st + dy * 2);
            bt_special_07.Location = new Point(x_st + dx * 1, y_st + dy * 3);
            bt_special_08.Location = new Point(x_st + dx * 2, y_st + dy * 0);
            bt_special_09.Location = new Point(x_st + dx * 2, y_st + dy * 1);
            bt_special_10.Location = new Point(x_st + dx * 2, y_st + dy * 2);
            bt_special_11.Location = new Point(x_st + dx * 2, y_st + dy * 3);
            groupBox6.Size = new Size(10 * 2 + 120 * 3+5*2, 20 + 35 * 4 + 5 * 3+10);
            groupBox13.Size = new Size(10 * 2 + 120 * 3 + 5 * 2, 20 + 35 * 4 + 5 * 3 + 10-30);




            dx = 120 + 5;
            dy = 40 + 5;
            bt_weekday_00.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            bt_weekday_01.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            bt_weekday_02.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            bt_weekday_03.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            bt_weekday_04.Location = new Point(x_st + dx * 0, y_st + dy * 4);

            //最大化螢幕
            this.FormBorderStyle = FormBorderStyle.None;
            this.WindowState = FormWindowState.Maximized;
            bt_exit_setup();
        }

        private void bt_exit_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        void bt_exit_setup()
        {
            int width = 5;
            int w = 50; //設定按鈕大小 W
            int h = 50; //設定按鈕大小 H

            Button bt_exit = new Button();  // 實例化按鈕
            bt_exit.Size = new Size(w, h);
            bt_exit.Text = "";
            Bitmap bmp = new Bitmap(w, h);
            Graphics g = Graphics.FromImage(bmp);
            Pen p = new Pen(Color.Red, width);
            g.Clear(Color.Pink);
            g.DrawRectangle(p, width + 1, width + 1, w - 1 - (width + 1) * 2, h - 1 - (width + 1) * 2);
            g.DrawLine(p, 0, 0, w - 1, h - 1);
            g.DrawLine(p, w - 1, 0, 0, h - 1);
            bt_exit.Image = bmp;

            bt_exit.Location = new Point(this.ClientSize.Width - bt_exit.Width, 0);
            bt_exit.Click += bt_exit_Click;     // 加入按鈕事件

            this.Controls.Add(bt_exit); // 將按鈕加入表單
            bt_exit.BringToFront();     //移到最上層
        }

        private void button0_Click(object sender, EventArgs e)
        {
            //時間資料範例
            //DateTime dt = new DateTime(2006, 3, 11);	//年月日
            DateTime dt = new DateTime(2006, 3, 11, 9, 15, 10, 20);	//年月日時分秒毫秒

            richTextBox1.Text += "完整日期： " + dt.ToString() + "\n";       //日期時間模式 2009/8/24 下午 08:09:42
            richTextBox1.Text += "完整日期： " + dt.ToString("D") + "\n";    //完整日期模式  2009年8月24日
            richTextBox1.Text += "簡短日期： " + dt.ToString("d") + "\n";    //簡短日期模式  2009/8/24
            richTextBox1.Text += "一般日期： " + dt.ToString("G") + "\n";
            richTextBox1.Text += "年月格式： " + dt.ToString("Y") + "\n";    //年月模式  2009年8月
            richTextBox1.Text += "月日格式： " + dt.ToString("M") + "\n";    //月日模式  8月24日
            richTextBox1.Text += "完整時間： " + dt.ToString("T") + "\n";    //完整時間模式   下午 08:09:42
            richTextBox1.Text += "簡短時間： " + dt.ToString("t") + "\n";    //簡短時間模式   下午 08:09
            richTextBox1.Text += "完整時間： " + dt.ToString("F") + "\n";    //完整日期時間模式  2009年8月24日 下午 08:09:42
            richTextBox1.Text += "簡短時間： " + dt.ToString("f") + "\n";    //簡短日期時間模式  2009年8月24日 下午 08:09

            //時間資料範例
            richTextBox1.Text += "完整日期： " + DateTime.Now.ToString("D") + "\n";
            richTextBox1.Text += "簡短日期： " + DateTime.Now.ToString("d") + "\n";
            richTextBox1.Text += "完整日期及時間： " + DateTime.Now.ToString("F") + "\n";
            richTextBox1.Text += "一般日期： " + DateTime.Now.ToString("G") + "\n";
            richTextBox1.Text += "月日格式： " + DateTime.Now.ToString("M") + "\n";
            richTextBox1.Text += "完整時間： " + DateTime.Now.ToString("T") + "\n";
            richTextBox1.Text += "簡短時間： " + DateTime.Now.ToString("t") + "\n";
            richTextBox1.Text += "年月格式： " + DateTime.Now.ToString("Y") + "\n";
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

            //時間差計算1

            //Timestamp 與 DateTime 互轉
            // 現在時間轉秒數
            //double timestamp = (DateTime.Now.AddHours(-8) - new DateTime(1970, 1, 1, 0, 0, 0)).TotalSeconds;
            double timestamp = (DateTime.Now.AddHours(-0) - new DateTime(2016, 5, 5, 23, 0, 0)).TotalSeconds;

            richTextBox1.Text += "從某時間距今秒數" + timestamp.ToString() + "\n";

            // 秒數轉 DateTime
            timestamp = 2400;
            DateTime dt = (new DateTime(2016, 5, 5, 23, 0, 0)).AddHours(0).AddSeconds(timestamp);

            richTextBox1.Text += "時間：" + dt.ToString() + "秒" + "\n";

            //時間差計算
            //一戰
            //1914年7月28日－1918年11月11日
            //（4年3個月又2周） 
            DateTime ww1_st = new DateTime(1914, 7, 28, 8, 12, 34);
            DateTime ww1_sp = new DateTime(1918, 11, 11, 17, 8, 17);
            TimeSpan ww1_time = ww1_sp - ww1_st;
            richTextBox1.Text += "一戰經歷時間 = " + ww1_time.ToString("T") + "\n";
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
            DateTime dt = DateTime.ParseExact(sDate, "yyyyMMdd", null, DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間：" + dt.ToString() + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd HH:mm:ss") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("yyyy" + '-' + "MM" + '-' + "dd" + " HH" + ':' + "mm" + ':' + "ss") + "\n";
        }

        private void button8_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
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

            DateTime ThisMonBeginDay = new DateTime(dt.Year, dt.Month, 1);
            DateTime ThisMonEndDay = ThisMonBeginDay.AddMonths(1).AddDays(-1);
            richTextBox1.Text += "本月月底日期:" + ThisMonEndDay.Day.ToString() + "\n";

            richTextBox1.Text += "本月月底日期:" + DateTime.DaysInMonth(DateTime.Now.Year, DateTime.Now.Month).ToString() + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //時間差計算5

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


            //時間差計算5

            string sDate = "2006/03/11";
            int year = 0;
            int month = 0;
            int day = 0;
            DateTime dt = DateTime.ParseExact(sDate, "yyyy/MM/dd", null, DateTimeStyles.AllowWhiteSpaces);
            richTextBox1.Text += "時間：" + dt.ToString() + "\n";
            richTextBox1.Text += "年：" + dt.Year.ToString() + "\n";
            richTextBox1.Text += "月：" + dt.Month.ToString() + "\n";
            richTextBox1.Text += "日：" + dt.Day.ToString() + "\n";
            year = dt.Year;
            month = dt.Month;
            day = dt.Day;

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

        private void button11_Click(object sender, EventArgs e)
        {
            TaiwanCalendar TC = new TaiwanCalendar();
            TaiwanLunisolarCalendar TA = new TaiwanLunisolarCalendar();

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

        private void button12_Click(object sender, EventArgs e)
        {
            DateTime dt;
            richTextBox1.Text += "日期 : " + textBox1.Text + "\n";
            try    // Parse the date and display it in ordinal format.
            {
                dt = DateTime.Parse(textBox1.Text);
                richTextBox1.Text += "日期轉序數 : " + dt.ToOrdinal() + "\n";
            }
            catch
            {
            }

            richTextBox1.Text += "日期 : " + dateTimePicker1.Text + "\n";
            try    // Parse the date and display it in ordinal format.
            {
                dt = DateTime.Parse(dateTimePicker1.Text);
                richTextBox1.Text += "日期轉序數 : " + dt.ToOrdinal() + "\n";
            }
            catch
            {
            }
        }

        private void button13_Click(object sender, EventArgs e)
        {
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

            dt = DateTime.Now;

            richTextBox1.Text += "D\t完整日期\t" + dt.ToString("D") + "\n";
            richTextBox1.Text += "d\t簡短日期\t" + dt.ToString("d") + "\n";
            richTextBox1.Text += "F\t完整日期及時間\t" + dt.ToString("F") + "\n";
            richTextBox1.Text += "G\t一般日期\t" + dt.ToString("G") + "\n";
            richTextBox1.Text += "M\t月日格式\t" + dt.ToString("M") + "\n";
            richTextBox1.Text += "T\t完整時間\t" + dt.ToString("T") + "\n";
            richTextBox1.Text += "t\t簡短時間\t" + dt.ToString("t") + "\n";
            richTextBox1.Text += "Y\t年月格式\t" + dt.ToString("Y") + "\n";
        }

        private void button15_Click(object sender, EventArgs e)
        {

        }

        private void button16_Click(object sender, EventArgs e)
        {
            //時間差計算2

            DateTime d1 = new DateTime(2006, 3, 11, 9, 15, 15);
            DateTime d2 = DateTime.Now;
            TimeSpan ts = new TimeSpan(d2.Ticks - d1.Ticks);

            richTextBox1.Text += "兩時間相距 : " + ts.TotalMilliseconds.ToString() + "\n";
            richTextBox1.Text += "兩時間相距 : " + ts.TotalHours.ToString() + "\n";

            //計算兩個時間差
            DateTime dt_st = Convert.ToDateTime("2010-10-15 15:50:39");
            DateTime dt_sp = Convert.ToDateTime("2010-10-25 15:50:39");
            TimeSpan time_diff = dt_st - dt_sp;
            double days = time_diff.TotalDays;
            richTextBox1.Text = "差距 " + Convert.ToInt32(days).ToString() + "天\n";

            //計算兩個日期的時間間隔
            dt_st = new DateTime(1974, 9, 24);
            dt_sp = new DateTime(1999, 3, 8);
            string diff = DateDiff3(dt_sp, dt_st);
            richTextBox1.Text += "時間間隔 : " + diff + "\n";

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
        }

        /// <summary>
        /// 計算兩個日期的時間間隔
        /// </summary>
        /// <param name="dt1">第一個日期和時間</param>
        /// <param name="dt2">第二個日期和時間</param>
        /// <returns></returns>
        private string DateDiff3(DateTime dt1, DateTime dt2)
        {
            string dateDiff = null;
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

        private void button17_Click(object sender, EventArgs e)
        {
            DateTime LastSalaryDay = new DateTime(DateTime.Now.Year, DateTime.Now.Month, 5);
            DateTime NextSalaryDay = new DateTime(DateTime.Now.AddMonths(1).Year, DateTime.Now.AddMonths(1).Month, 5);

            richTextBox1.Text += "上次發薪日：" + LastSalaryDay.ToString("yyyy/MM/dd") + "\n";
            TimeSpan ts1 = DateTime.Now - LastSalaryDay;

            richTextBox1.Text += "經過了 " + ts1.Days + " 天\n";

            richTextBox1.Text += "下次發薪日：" + NextSalaryDay.ToString("yyyy/MM/dd") + "\n";

            //用大的日期 減小的日期
            TimeSpan ts2 = DateTime.Now - NextSalaryDay;    //小的日期減大的日期

            richTextBox1.Text += "距離下次發薪日還有" + Math.Abs(ts2.Days) + " 天\n"; //距離幾天一定是正的 用Math.Abs取絕對值
        }

        private void button18_Click(object sender, EventArgs e)
        {
            string message = "";
            message += "C# 怎么显示中文格式的日期、星期几\n";
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

        private void button21_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
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

        private void button23_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += DateTime.Now.ToString("yyyy/MM/dd", DateTimeFormatInfo.InvariantInfo) + "\n";
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

            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + "\n";
        }

        //C#實現小小的日歷 ST
        void show_calendar()
        {
            int year = DateTime.Now.Year;
            int month = DateTime.Now.Month;
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

        private void button25_Click(object sender, EventArgs e)
        {
            //C#實現小小的日曆
            show_calendar();
        }
        //C#實現小小的日歷 SP

        private void timer1_Tick(object sender, EventArgs e)
        {
            CultureInfo cuinfo = new CultureInfo("zh-TW");
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

        private void button26_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "程式開啟時間: " + (DateTime.Now - start_time).ToString() + " 秒\n";
        }

        private void button27_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "電腦開機時間 : " + (Environment.TickCount / 1000).ToString() + " 秒\n";  //???
        }

        private void button28_Click(object sender, EventArgs e)
        {
            DateTime dt = new DateTime(2006, 3, 11, 9, 15, 23, 34);
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
        }

        private void button29_Click(object sender, EventArgs e)
        {
        }

        private void button30_Click(object sender, EventArgs e)
        {
        }

        private void button31_Click(object sender, EventArgs e)
        {
            //僅顯示上下午幾點幾分幾秒
            richTextBox1.Text += "僅顯示上下午幾點幾分幾秒:\t" + DateTime.Now.ToString("T") + "\n";
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

        private void button33_Click(object sender, EventArgs e)
        {
        }

        private void button34_Click(object sender, EventArgs e)
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

        private void button35_Click(object sender, EventArgs e)
        {
            //日期時間相加減
            DateTime war_st = Convert.ToDateTime("1937-7-7");
            DateTime war_sp = Convert.ToDateTime("1945-08-15");
            TimeSpan ts = war_sp.Subtract(war_st); //兩時間天數相減
            double dayCount = ts.Days; //相距天數
            richTextBox1.Text += "相距天數： " + dayCount.ToString() + " 天\n";
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

        private void button36_Click(object sender, EventArgs e)
        {
            DateTime myBirthday = DateTime.ParseExact("2006/03/11", "yyyy/MM/dd", null);
            DateTime flakNow = DateTime.ParseExact("2018/02/01", "yyyy/MM/dd", null);
            Age myAge = CalculateAge(myBirthday, flakNow);
            richTextBox1.Text += "年 : " + myAge.Years.ToString() + "\n";
            richTextBox1.Text += "月 : " + myAge.Months.ToString() + "\n";
            richTextBox1.Text += "日 : " + myAge.Days.ToString() + "\n";
        }

        private void button37_Click(object sender, EventArgs e)
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

        private void button38_Click(object sender, EventArgs e)
        {
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

        private void button40_Click(object sender, EventArgs e)
        {
            //從零點到現在的秒數

            int total_time = inputToSeconds("23:59:59");
            richTextBox1.Text += "total_time = " + total_time.ToString() + "\n";


            int nn = 86399;
            string current_time = secondsToTime(nn);
            richTextBox1.Text += "current_time = " + current_time + "\n";
        }

        private void button41_Click(object sender, EventArgs e)
        {
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

        private void button43_Click(object sender, EventArgs e)
        {
            //比較兩個時間

            DateTime dt1 = new DateTime(2016, 12, 9, 0, 0, 0);
            DateTime dt2 = new DateTime(2016, 12, 9, 11, 0, 0);
            int result = DateTime.Compare(dt1, dt2);
            string relationship;

            if (result < 0)
                relationship = "is earlier than";
            else if (result == 0)
                relationship = "is the same time as";
            else
                relationship = "is later than";

            richTextBox1.Text += dt1 + " " + relationship + " " + dt2 + "\n";
        }

        private void button44_Click(object sender, EventArgs e)
        {
        }

        private void button45_Click(object sender, EventArgs e)
        {
            //列出全球時區
            // Load the timezone information.
            foreach (TimeZoneInfo info in TimeZoneInfo.GetSystemTimeZones())
            {
                richTextBox1.Text += info + "\n";
            }
        }

        private void button46_Click(object sender, EventArgs e)
        {
            DateTime dt = new DateTime(2019, 1, 1);

            richTextBox1.Text += "2019/1/1 加一段時間後 : " + dt.AddDays(3125).AddSeconds(14653 * 2).ToString("yyyy/MM/dd HH:mm:ss") + "\n";

            int yy = -280;
            int dd = -1250;
            richTextBox1.Text += "2019/1/1 減一段時間後 : " + dt.AddYears(yy).AddDays(dd).AddSeconds(14653 * 2).ToString() + "\n";
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

        private void button47_Click(object sender, EventArgs e)
        {
            //分出 時:分:秒 再組合
            DateTime dt = DateTime.Now;
            richTextBox1.Text += dt.Hour.ToString().PadLeft(2, '0') + ":"
                                    + dt.Minute.ToString().PadLeft(2, '0') + ":"
                                    + dt.Second.ToString().PadLeft(2, '0') + "\n";

            richTextBox1.Text += "現在時間 : " + DateTime.Now.ToString("hh:mm:ss.fff") + "\n";
        }

        private void button48_Click(object sender, EventArgs e)
        {
            //依時間建立檔案
            DateTime dt = DateTime.Now;
            string filename = String.Format("{0}-{1}-{2}_{3}-{4}-{5}",
                                            dt.Year, dt.Month, dt.Day,
                                            dt.Hour, dt.Minute,
                                            dt.Second);

            richTextBox1.Text += "依時間建立檔案 :" + filename + "\n";

            string m_fileName = DateTime.Now.ToFileTime().ToString() + ".jpg";
            richTextBox1.Text += "依時間建立檔案 :" + m_fileName + "\n";


            richTextBox1.Text += DateTime.Now.Ticks.ToString() + "\n";
            richTextBox1.Text += Environment.NewLine + "Conversion finished @ " + DateTime.Now.ToString();
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
            DateTime dt1;
            DateTime dt2;

            if (!DateTime.TryParse(textBox8.Text, out dt1))
            {
                return;
            }
            textBox3.Text = dt1.ToString();

            if (!DateTime.TryParse(textBox10.Text, out dt2))
            {
                return;
            }
            textBox9.Text = dt1.ToString();

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
            textBox7.Text = txt;
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
                richTextBox1.Text += "錯誤訊息 : " + ex.Message + "\n";
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

                dt_timer_st = DateTime.Now;
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

        private void button51_Click(object sender, EventArgs e)
        {
            //取得系統的時區資訊
            get_system_time_zone();
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

        private void button53_Click(object sender, EventArgs e)
        {
            string result;
            //根據年月日計算星期幾的函數
            result = CalculateWeekDay(2021, 10, 14);
            richTextBox1.Text += "日期 " + DateTime.Parse("2021/10/14").ToString() + "\t" + result + "\n";

            result = CalculateWeekDay(1941, 12, 7);
            richTextBox1.Text += "日期 " + DateTime.Parse("1941/12/7").ToString() + "\t" + result + "\n";

            result = CalculateWeekDay(2006, 3, 11);
            richTextBox1.Text += "日期 " + DateTime.Parse("2006/3/11").ToString() + "\t" + result + "\n";
        }

        //根據年月日計算星期幾的函數
        //基姆拉爾森計算公式, 外文名是Kim larsen calculation formula。

        //在公式中d表示日期中的日數，m表示月份數，y表示年數。注意：在公式中有個與其他公式不同的地方：
        //把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10則換算成：2003-13-10來代入公式計算。

        //y－年，m－月，d－日期
        string CalculateWeekDay(int y, int m, int d)
        {
            if (m == 1) m = 13;
            if (m == 2) m = 14;
            //int week = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400) % 7;

            int week = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400 + 1) % 7; //C++計算公式

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
            }
            return weekstr;
        }

        private void button54_Click(object sender, EventArgs e)
        {
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
            DateTime dt1 = new DateTime(2006, 3, 11, 9, 15, 20);
            DateTime dt2 = DateTime.Now;
            string diff = DateDiff2(dt1, dt2);
            richTextBox1.Text += "diff = " + diff + "\n";

            dt1 = new DateTime(1939, 9, 1);
            dt2 = new DateTime(1945, 9, 2);
            diff = DateDiff2(dt1, dt2);
            richTextBox1.Text += "diff = " + diff + "\n";
        }

        /// <summary>
        /// 計算兩個日期的時間間隔
        /// </summary>
        /// <param name="DateTime1">第一個日期和時間</param>
        /// <param name="DateTime2">第二個日期和時間</param>
        /// <returns></returns>
        private string DateDiff2(DateTime DateTime1, DateTime DateTime2)
        {
            string dateDiff = null;

            TimeSpan ts1 = new TimeSpan(DateTime1.Ticks);
            TimeSpan ts2 = new TimeSpan(DateTime2.Ticks);
            TimeSpan ts = ts1.Subtract(ts2).Duration();
            dateDiff = ts.Days.ToString() + "天"
                + ts.Hours.ToString() + "小時"
                + ts.Minutes.ToString() + "分鐘"
                + ts.Seconds.ToString() + "秒";

            return dateDiff;
        }

        private void button55_Click(object sender, EventArgs e)
        {
            //string.Format 格式化日期

            //c# 日期函數

            DateTime dt = DateTime.Now;

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
        }

        private void button56_Click(object sender, EventArgs e)
        {
            //打印時間訊息用法

            //2007年4月24日
            richTextBox1.Text += DateTime.Now.ToString("D") + "\n";
            //2007-4-24
            richTextBox1.Text += DateTime.Now.ToString("d") + "\n";

            //2007年4月24日 16:30:15
            richTextBox1.Text += DateTime.Now.ToString("F") + "\n";
            //2007年4月24日 16:30
            richTextBox1.Text += DateTime.Now.ToString("f") + "\n";

            //2007-4-24 16:30:15
            richTextBox1.Text += DateTime.Now.ToString("G") + "\n";
            //2007-4-24 16:30
            richTextBox1.Text += DateTime.Now.ToString("g") + "\n";

            //16:30:15
            richTextBox1.Text += DateTime.Now.ToString("T") + "\n";
            //16:30
            richTextBox1.Text += DateTime.Now.ToString("t") + "\n";

            //2007年4月24日 8:30:15
            richTextBox1.Text += DateTime.Now.ToString("U") + "\n";
            //2007-04-24 16:30:15Z
            richTextBox1.Text += DateTime.Now.ToString("u") + "\n";

            //4月24日
            richTextBox1.Text += DateTime.Now.ToString("m") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("M") + "\n";
            //Tue, 24 Apr 2007 16:30:15 GMT
            richTextBox1.Text += DateTime.Now.ToString("r") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("R") + "\n";
            //2007年4月 
            richTextBox1.Text += DateTime.Now.ToString("y") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("Y") + "\n";
            //2007-04-24T15:52:19.1562500+08:00
            richTextBox1.Text += DateTime.Now.ToString("o") + "\n";
            richTextBox1.Text += DateTime.Now.ToString("O") + "\n";
            //2007-04-24T16:30:15
            richTextBox1.Text += DateTime.Now.ToString("s") + "\n";
            //2007-04-24 15:52:19
            richTextBox1.Text += DateTime.Now.ToString("yyyy-MM-dd HH：mm：ss：ffff") + "\n";
            //2007年04月24 15時56分48秒
            richTextBox1.Text += DateTime.Now.ToString("yyyy年MM月dd HH時mm分ss秒") + "\n";

            //星期二, 四月 24 2007
            richTextBox1.Text += DateTime.Now.ToString("dddd, MMMM dd yyyy") + "\n";
            //二, 四月 24 '07
            richTextBox1.Text += DateTime.Now.ToString("ddd, MMM d \"'\"yy") + "\n";
            //星期二, 四月 24
            richTextBox1.Text += DateTime.Now.ToString("dddd, MMMM dd") + "\n";
            //4-07
            richTextBox1.Text += DateTime.Now.ToString("M/yy") + "\n";
            //24-04-07
            richTextBox1.Text += DateTime.Now.ToString("dd-MM-yy") + "\n";
        }

        private void button57_Click(object sender, EventArgs e)
        {
            //C#中時間相關知識點小結
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

        private void button58_Click(object sender, EventArgs e)
        {

        }

        private void button59_Click(object sender, EventArgs e)
        {

        }

        private void button60_Click(object sender, EventArgs e)
        {
            //vcs時間之最早最晚

            //DateTime值類型代表了一個從公元0001年1月1日0點0分0秒到公元9999年12月31日23點59分59秒之間的具體日期時刻
            //vcs史上最早時間
            DateTime minTime = DateTime.MinValue;

            //vcs史上最晚時間
            DateTime maxTime = DateTime.MaxValue;

            richTextBox1.Text += "vcs史上最早時間 : " + minTime.ToString() + "\n";
            richTextBox1.Text += "vcs史上最晚時間 : " + maxTime.ToString() + "\n";
        }

        private void button61_Click(object sender, EventArgs e)
        {

            richTextBox1.Text += "星期幾 : " + DateTime.Now.DayOfWeek.ToString() + "\n";

            richTextBox1.Text += "當前時間 : " + DateTime.Now.ToLongTimeString() + "\n";

            //DateTime轉字串需顯示毫秒
            //DateTime.ToString("yyyyMMddhhmmssfff")，fff 格式包含毫秒值中任何結尾的零。
            richTextBox1.Text += "顯示毫秒 : " + DateTime.Now.ToString("yyyy_MMdd_hhmmss.fff") + "\n";

            richTextBox1.Text += "日期 : " + DateTime.Now.ToString("yyyy-MM-dd") + "\n";
        }

        private void button62_Click(object sender, EventArgs e)
        {
            //日曆1
            Calendar calendar = new Calendar();
            calendar.Printdate(DateTime.Now.Year);
            Console.ReadLine();
        }

        private void button63_Click(object sender, EventArgs e)
        {
            //日曆2
            //萬年曆農曆節日節氣

            DateTime dt = DateTime.Now;
            ChineseCalendar cc = new ChineseCalendar(dt);
            Console.WriteLine("阳历：" + cc.DateString);
            Console.WriteLine("属相：" + cc.AnimalString);
            Console.WriteLine("农历：" + cc.ChineseDateString);
            Console.WriteLine("时辰：" + cc.ChineseHour);
            Console.WriteLine("节气：" + cc.ChineseTwentyFourDay);
            Console.WriteLine("节日：" + cc.DateHoliday);
            Console.WriteLine("前一个节气：" + cc.ChineseTwentyFourPrevDay);
            Console.WriteLine("后一个节气：" + cc.ChineseTwentyFourNextDay);
            Console.WriteLine("干支：" + cc.GanZhiDateString);
            Console.WriteLine("星期：" + cc.WeekDayStr);
            Console.WriteLine("星宿：" + cc.ChineseConstellation);
            Console.WriteLine("星座：" + cc.Constellation);

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
        }

        private void button64_Click(object sender, EventArgs e)
        {

        }

        private void button65_Click(object sender, EventArgs e)
        {

        }

        private void button66_Click(object sender, EventArgs e)
        {

        }

        private void button67_Click(object sender, EventArgs e)
        {

        }

        private void button68_Click(object sender, EventArgs e)
        {

        }

        private void button69_Click(object sender, EventArgs e)
        {

        }

        private void button70_Click(object sender, EventArgs e)
        {

        }

        private void button71_Click(object sender, EventArgs e)
        {

        }

        private void button72_Click(object sender, EventArgs e)
        {

        }

        private void button73_Click(object sender, EventArgs e)
        {

        }

        private void button74_Click(object sender, EventArgs e)
        {

        }

        private void button75_Click(object sender, EventArgs e)
        {

        }

        private void button76_Click(object sender, EventArgs e)
        {

        }

        private void button77_Click(object sender, EventArgs e)
        {

        }

        private void button78_Click(object sender, EventArgs e)
        {

        }

        private void button79_Click(object sender, EventArgs e)
        {

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
            //農曆計算
            DateTime _d = DateTime.Now;
            LunarDate1 ld = new LunarDate1(_d);
            string result = "";
            result += "干支年：" + ld.LunarYear + "\n";
            result += "生肖：" + ld.Animal + "\n";
            result += "月：" + ld.LunarMonth + "\n";
            result += "日：" + ld.LunarDay + "\n";
            result += "节气：" + ld.SolarTerm + "\n";
            result += "数字农历年：" + ld.Year + "月" + ld.Month + "日" + ld.Day + "\n";

            richTextBox1.Text += result + "\n";

            //DateTime _d = DateTime.Now;
            LunarDateClass ldc = new LunarDateClass(_d);

            result = "";
            result += "干支年：" + ldc.LunarYear + "\n";
            result += "生肖：" + ldc.Animal + "\n";
            result += "月：" + ldc.LunarMonth + "\n";
            result += "日：" + ldc.LunarDay + "\n";
            result += "节气：" + ldc.SolarTerm + "\n";
            //ldc.LunarDate 返回 LunarDate对象。。
            result += "数字农历年：" + ldc.LunarDate.Year + "月" + ldc.LunarDate.Month + "日" + ldc.LunarDate.Day + "\n";

            richTextBox1.Text += result + "\n";
        }

        private void bt_special_04_Click(object sender, EventArgs e)
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

        //農曆 ST
        private void bt_special_05_Click(object sender, EventArgs e)
        {
            DateTime dt = DateTime.Now;
            string lunar_date;
            lunar_date = GetLunarCalendar(dt);
            richTextBox1.Text += lunar_date + "\n";
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
                {
                    k = 11;
                }
                else
                {
                    k = 12;
                }
                n = k;
                while (n >= 0)
                {
                    //獲取LunarData[m]的第n個二進位的值
                    nBit = LunarData[m];
                    for (i = 1; i < n + 1; i++)
                    {
                        nBit = nBit / 2;
                    }
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
                {
                    break;
                }
                m = m + 1;
            }
            year = 1921 + m;
            month = k - n + 1;
            day = nTheDate;
            //return year + "-" + month + "-" + day;

            if (k == 12)
            {
                if (month == LunarData[m] / 65536 + 1)
                {
                    month = 1 - month;
                }
                else if (month > LunarData[m] / 65536 + 1)
                {
                    month = month - 1;
                }
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
            {
                calendar += "閏" + MonthName[-1 * month].ToString() + "月";
            }
            else
            {
                calendar += MonthName[month].ToString() + "月";
            }

            //農曆日
            calendar += DayName[day].ToString() + "日";

            return calendar;
        }
        //農曆 SP

        private void bt_special_06_Click(object sender, EventArgs e)
        {

        }

        private void bt_special_07_Click(object sender, EventArgs e)
        {

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

        private void bt_special_08_Click(object sender, EventArgs e)
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

        private void bt_special_09_Click(object sender, EventArgs e)
        {
            //陽歷轉換成農曆的類

            LunarDate2 date = new LunarDate2(1901, 9, 7);

            richTextBox1.Text += "農曆 = " + date.ToString() + "\n";

            richTextBox1.Text += "天干地支 : " + date.chineseEar + "\n";
            richTextBox1.Text += "生肖 : " + date.Aminals + "\n";

            richTextBox1.Text += "農曆年 = " + date.LunarYear + "\n";
            richTextBox1.Text += "農曆月 = " + date.LunarMonth + "\n";
            richTextBox1.Text += "農曆日 = " + date.LunarDay + "\n";
        }

        private void bt_special_10_Click(object sender, EventArgs e)
        {

        }

        private void bt_special_11_Click(object sender, EventArgs e)
        {

        }

        private void bt_weekday_00_Click(object sender, EventArgs e)
        {
            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string week = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();
            richTextBox1.Text += week + "\n";

        }

        private void bt_weekday_01_Click(object sender, EventArgs e)
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

        private void bt_weekday_02_Click(object sender, EventArgs e)
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

        private void bt_weekday_03_Click(object sender, EventArgs e)
        {
            //獲得中文星期名稱
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


        private void bt_weekday_04_Click(object sender, EventArgs e)
        {
            //星期幾
            richTextBox1.Text += CaculateWeekDay2(2021, 10, 28);
            richTextBox1.Text += "\n";

            //C#獲取當前星期幾的三種方法

            //第一種：

            string[] Day = new string[] { "星期日", "星期一", "星期二", "星期三", "星期四", "星期五", "星期六" };
            string weekday1 = Day[Convert.ToInt32(DateTime.Now.DayOfWeek.ToString("d"))].ToString();    //same
            string weekday2 = Day[Convert.ToInt16(DateTime.Now.DayOfWeek)]; //same
            richTextBox1.Text += weekday1 + "\n";
            richTextBox1.Text += weekday2 + "\n";

            //第二種：

            richTextBox1.Text += CultureInfo.CurrentCulture.DateTimeFormat.GetDayName(DateTime.Now.DayOfWeek) + "\n";

            //第三種：

            string dt;
            string week = string.Empty;
            dt = DateTime.Today.DayOfWeek.ToString();
            switch (dt)
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
        }

        /*
        C#實現的根據年月日計算星期幾的函數

        基姆拉爾森計算公式

        W= (d 2*m 3*(m 1)/5 y y/4-y/100 y/400) mod 7

        在公式中d表示日期中的日數，m表示月份數，y表示年數。注意：在公式中有個與其他公式不同的地方：把一月和二月看成是上一年的十三月和十四月，例：如果是2004-1-10則換算成：2003-13-10來代入公式計算。
        */

        //y－年，m－月，d－日期
        string CaculateWeekDay2(int y, int m, int d)
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
            }
            return weekstr;
        }

        private void bt_diff_time_Click(object sender, EventArgs e)
        {
            //相距天數


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
            TimeSpan diffTime = dtTarget.Subtract(DateTime.Now);

            string diffHour = Convert.ToString(diffTime.Hours);
            string diffMin = Convert.ToString(diffTime.Minutes);
            string diffSec = Convert.ToString(diffTime.Seconds);
            tb_countdown.Text = "距離 " + dtTarget.ToString() + " 還有 " + diffHour + " 時 " + diffMin + " 分 " + diffSec + " 秒";


        }

        private void textBox7_TextChanged(object sender, EventArgs e)
        {

        }


    }

    #region LunarDate

    public class LunarDateClass
    {
        private const ushort START_YEAR = 1901;
        private const ushort END_YEAR = 2050;
        private DateTime m_Date = DateTime.MinValue;
        private LunarDate1 m_LunarDate = null;
        private string m_LunarYear = "", m_LunarMonth = "", m_LunarDay = "";
        private string m_Animal = "", m_Constellation = "", m_SolarTerm = "";

        /// <summary>始化农历类。</summary>
        public LunarDateClass()
        {
            this.Date = DateTime.Today;
        }


        /// <summary>以公历日期初始化农历类。</summary>
        /// <param name="dt">初始化公历日期。要查询的日期。</param>
        public LunarDateClass(DateTime dt)
        {
            this.Date = dt.Date;
        }

        /// <summary>初始化公历日期。要查询的日期。</summary>
        public DateTime Date
        {
            get { return m_Date; }
            set
            {
                this.m_Animal = "";
                this.m_Constellation = "";
                this.m_LunarDate = null;
                this.m_LunarDay = "";
                this.m_LunarMonth = "";
                this.m_LunarYear = "";
                this.m_SolarTerm = "";
                m_Date = value;
            }
        }

        #region LunarDateClassData

        /// <summary>星座名称。</summary>
        private string[] ConstellationName =
   {
    "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座",
    "天秤座", "天蝎座", "射手座", "摩羯座", "水瓶座", "双鱼座"
   };

        /// <summary>节气名称。</summary>
        private string[] LunarHolDayName =
   {
    "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
    "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑",
    "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"
   };

        /// <summary>
        /// 数组gLunarDay存入阴历1901年到2050年每年中的月天数信息，
        /// 阴历每月只能是29或30天，一年用12（或13）个二进制位表示，
        /// 对应位为1表30天，否则为29天.
        /// 测试数据只有1901.1.1 --2050.12.31
        /// </summary>
        private int[] gLunarMonthDay = {
 0x4ae0, 0xa570, 0x5268, 0xd260, 0xd950, 0x6aa8, 0x56a0, 0x9ad0, 0x4ae8, 0x4ae0, //1910
 0xa4d8, 0xa4d0, 0xd250, 0xd548, 0xb550, 0x56a0, 0x96d0, 0x95b0, 0x49b8, 0x49b0, //1920
 0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada8, 0x2b60, 0x9570, 0x4978, 0x4970, 0x64b0, //1930
 0xd4a0, 0xea50, 0x6d48, 0x5ad0, 0x2b60, 0x9370, 0x92e0, 0xc968, 0xc950, 0xd4a0, //1940
 0xda50, 0xb550, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950, 0xb4a8, 0x6ca0, //1950
 0xb550, 0x55a8, 0x4da0, 0xa5b0, 0x52b8, 0x52b0, 0xa950, 0xe950, 0x6aa0, 0xad50, //1960
 0xab50, 0x4b60, 0xa570, 0xa570, 0x5260, 0xe930, 0xd950, 0x5aa8, 0x56a0, 0x96d0, //1970
 0x4ae8, 0x4ad0, 0xa4d0, 0xd268, 0xd250, 0xd528, 0xb540, 0xb6a0, 0x96d0, 0x95b0, //1980
 0x49b0, 0xa4b8, 0xa4b0, 0xb258, 0x6a50, 0x6d40, 0xada0, 0xab60, 0x9370, 0x4978, //1990
 0x4970, 0x64b0, 0x6a50, 0xea50, 0x6b28, 0x5ac0, 0xab60, 0x9368, 0x92e0, 0xc960, //2000
 0xd4a8, 0xd4a0, 0xda50, 0x5aa8, 0x56a0, 0xaad8, 0x25d0, 0x92d0, 0xc958, 0xa950, //2010
 0xb4a0, 0xb550, 0xb550, 0x55a8, 0x4ba0, 0xa5b0, 0x52b8, 0x52b0, 0xa930, 0x74a8, //2020
 0x6aa0, 0xad50, 0x4da8, 0x4b60, 0x9570, 0xa4e0, 0xd260, 0xe930, 0xd530, 0x5aa0, //2030
 0x6b50, 0x96d0, 0x4ae8, 0x4ad0, 0xa4d0, 0xd258, 0xd250, 0xd520, 0xdaa0, 0xb5a0, //2040
 0x56d0, 0x4ad8, 0x49b0, 0xa4b8, 0xa4b0, 0xaa50, 0xb528, 0x6d20, 0xada0, 0x55b0 //2050
            };

        /// <summary>数组gLanarMonth存放阴历1901年到2050年闰月的月份，如没有则为0，每字节存两年</summary>
        private byte[] gLunarMonth = {
 0x00, 0x50, 0x04, 0x00, 0x20, //1910
 0x60, 0x05, 0x00, 0x20, 0x70, //1920
 0x05, 0x00, 0x40, 0x02, 0x06, //1930
 0x00, 0x50, 0x03, 0x07, 0x00, //1940
 0x60, 0x04, 0x00, 0x20, 0x70, //1950
 0x05, 0x00, 0x30, 0x80, 0x06, //1960
 0x00, 0x40, 0x03, 0x07, 0x00, //1970
 0x50, 0x04, 0x08, 0x00, 0x60, //1980
 0x04, 0x0a, 0x00, 0x60, 0x05, //1990
 0x00, 0x30, 0x80, 0x05, 0x00, //2000
 0x40, 0x02, 0x07, 0x00, 0x50, //2010
 0x04, 0x09, 0x00, 0x60, 0x04, //2020
 0x00, 0x20, 0x60, 0x05, 0x00, //2030
 0x30, 0xb0, 0x06, 0x00, 0x50, //2040
 0x02, 0x07, 0x00, 0x50, 0x03 //2050
          };


        //数组gLanarHoliDay存放每年的二十四节气对应的阳历日期

        //每年的二十四节气对应的阳历日期几乎固定，平均分布于十二个月中
        // 1月 2月 3月 4月 5月 6月
        //小寒 大寒 立春 雨水 惊蛰 春分 清明 谷雨 立夏 小满 芒种 夏至
        // 7月 8月 9月 10月 11月 12月
        //小暑 大暑 立秋 处暑 白露 秋分 寒露 霜降 立冬 小雪 大雪 冬至
        //*********************************************************************************
        // 节气无任何确定规律,所以只好存表,要节省空间,所以....
        //**********************************************************************************}
        //数据格式说明:
        //如1901年的节气为
        // 1月 2月 3月 4月 5月 6月 7月 8月 9月 10月 11月 12月
        // 6, 21, 4, 19, 6, 21, 5, 21, 6,22, 6,22, 8, 23, 8, 24, 8, 24, 8, 24, 8, 23, 8, 22
        // 9, 6, 11,4, 9, 6, 10,6, 9,7, 9,7, 7, 8, 7, 9, 7, 9, 7, 9, 7, 8, 7, 15
        //上面第一行数据为每月节气对应日期,15减去每月第一个节气,每月第二个节气减去15得第二行
        // 这样每月两个节气对应数据都小于16,每月用一个字节存放,高位存放第一个节气数据,低位存放
        //第二个节气的数据,可得下表
        private byte[] gLunarHolDay = {
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1901
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1902
  0x96, 0xA5, 0x87, 0x96, 0x87, 0x87, 0x79, 0x69, 0x69, 0x69, 0x78, 0x78, //1903
  0x86, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x78, 0x87, //1904
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1905
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1906
  0x96, 0xA5, 0x87, 0x96, 0x87, 0x87, 0x79, 0x69, 0x69, 0x69, 0x78, 0x78, //1907
  0x86, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1908
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1909
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1910
  0x96, 0xA5, 0x87, 0x96, 0x87, 0x87, 0x79, 0x69, 0x69, 0x69, 0x78, 0x78, //1911
  0x86, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1912
  0x95, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1913
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1914
  0x96, 0xA5, 0x97, 0x96, 0x97, 0x87, 0x79, 0x79, 0x69, 0x69, 0x78, 0x78, //1915
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1916
  0x95, 0xB4, 0x96, 0xA6, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x87, //1917
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x77, //1918
  0x96, 0xA5, 0x97, 0x96, 0x97, 0x87, 0x79, 0x79, 0x69, 0x69, 0x78, 0x78, //1919
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1920
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x87, //1921
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x77, //1922
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x69, 0x69, 0x78, 0x78, //1923
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1924
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x87, //1925
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1926
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1927
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1928
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1929
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1930
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x87, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1931
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1932
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1933
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1934
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1935
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1936
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1937
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1938
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1939
  0x96, 0xA5, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1940
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1941
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1942
  0x96, 0xA4, 0x96, 0x96, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1943
  0x96, 0xA5, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1944
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1945
  0x95, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1946
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1947
  0x96, 0xA5, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1948
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x79, 0x78, 0x79, 0x77, 0x87, //1949
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1950
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x79, 0x79, 0x79, 0x69, 0x78, 0x78, //1951
  0x96, 0xA5, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1952
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1953
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x68, 0x78, 0x87, //1954
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1955
  0x96, 0xA5, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1956
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1957
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1958
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1959
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1960
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1961
  0x96, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1962
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1963
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1964
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1965
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1966
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1967
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1968
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1969
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1970
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x79, 0x69, 0x78, 0x77, //1971
  0x96, 0xA4, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1972
  0xA5, 0xB5, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1973
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1974
  0x96, 0xB4, 0x96, 0xA6, 0x97, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1975
  0x96, 0xA4, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x89, 0x88, 0x78, 0x87, 0x87, //1976
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1977
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x78, 0x87, //1978
  0x96, 0xB4, 0x96, 0xA6, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1979
  0x96, 0xA4, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1980
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x77, 0x87, //1981
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1982
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x78, 0x79, 0x78, 0x69, 0x78, 0x77, //1983
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //1984
  0xA5, 0xB4, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //1985
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1986
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x79, 0x78, 0x69, 0x78, 0x87, //1987
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //1988
  0xA5, 0xB4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1989
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //1990
  0x95, 0xB4, 0x96, 0xA5, 0x86, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1991
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //1992
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1993
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1994
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x76, 0x78, 0x69, 0x78, 0x87, //1995
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //1996
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //1997
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //1998
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //1999
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2000
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2001
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //2002
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //2003
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2004
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2005
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2006
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x69, 0x78, 0x87, //2007
  0x96, 0xB4, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2008
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2009
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2010
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x78, 0x87, //2011
  0x96, 0xB4, 0xA5, 0xB5, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2012
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //2013
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2014
  0x95, 0xB4, 0x96, 0xA5, 0x96, 0x97, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //2015
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2016
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //2017
  0xA5, 0xB4, 0xA6, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2018
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //2019
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x86, //2020
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2021
  0xA5, 0xB4, 0xA5, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2022
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x79, 0x77, 0x87, //2023
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2024
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2025
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2026
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //2027
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2028
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2029
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2030
  0xA5, 0xB4, 0x96, 0xA5, 0x96, 0x96, 0x88, 0x78, 0x78, 0x78, 0x87, 0x87, //2031
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2032
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x86, //2033
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x78, 0x88, 0x78, 0x87, 0x87, //2034
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2035
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2036
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x86, //2037
  0xA5, 0xB3, 0xA5, 0xA5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2038
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2039
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x96, //2040
  0xA5, 0xC3, 0xA5, 0xB5, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2041
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x88, 0x88, 0x88, 0x78, 0x87, 0x87, //2042
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2043
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x88, 0x87, 0x96, //2044
  0xA5, 0xC3, 0xA5, 0xB4, 0xA5, 0xA6, 0x87, 0x88, 0x87, 0x78, 0x87, 0x86, //2045
  0xA5, 0xB3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x88, 0x78, 0x87, 0x87, //2046
  0xA5, 0xB4, 0x96, 0xA5, 0xA6, 0x96, 0x88, 0x88, 0x78, 0x78, 0x87, 0x87, //2047
  0x95, 0xB4, 0xA5, 0xB4, 0xA5, 0xA5, 0x97, 0x87, 0x87, 0x88, 0x86, 0x96, //2048
  0xA4, 0xC3, 0xA5, 0xA5, 0xA5, 0xA6, 0x97, 0x87, 0x87, 0x78, 0x87, 0x86, //2049
  0xA5, 0xC3, 0xA5, 0xB5, 0xA6, 0xA6, 0x87, 0x88, 0x78, 0x78, 0x87, 0x87 //2050
           };

        #endregion

        #region Core

        /// <summary>
        /// 取得指定阴历年的阴历闰月月份。
        /// </summary>
        /// <param name="iLunarYear">年份。</param>
        /// <returns>返回指定年的闰月月份。</returns>
        private int GetLeapMonth(ushort iLunarYear)
        {
            byte Flag;
            if (iLunarYear < START_YEAR || iLunarYear > END_YEAR)
            {
                return 0;
            }

            Flag = gLunarMonth[(iLunarYear - START_YEAR) / 2];
            if ((iLunarYear - START_YEAR) % 2 == 0)
            {
                return Flag >> 4;
            }
            else
            {
                return Flag & 0x0F;
            }
        }


        /// <summary>
        /// 计算指定阴历年月的总天数。
        /// </summary>
        /// <param name="iLunarYear">年份。</param>
        /// <param name="iLunarMonth">月份。</param>
        /// <returns>
        /// 返回阴历阴历年月的天数，如果该月为闰月，高字为第二个该月的天数，否则高字为0。
        /// </returns>
        /// <remarks>
        /// 指定年月范围在1901年1月---2050年12月之间。
        /// </remarks>
        private uint GetLunarMonthDays(ushort iLunarYear, ushort iLunarMonth)
        {
            int Height, Low;
            int iBit;
            if (iLunarYear < START_YEAR || iLunarYear > END_YEAR)
            {
                return 30;
            }
            Height = 0;
            Low = 29;
            iBit = 16 - iLunarMonth;
            if (iLunarMonth > GetLeapMonth(iLunarYear) && GetLeapMonth(iLunarYear) > 0)
            {
                iBit--;
            }

            if ((gLunarMonthDay[iLunarYear - START_YEAR] & (1 << iBit)) > 0)
            {
                Low++;
            }

            if (iLunarMonth == GetLeapMonth(iLunarYear))
            {
                if ((gLunarMonthDay[iLunarYear - START_YEAR] & (1 << (iBit - 1))) > 0)
                {
                    Height = 30;
                }
                else
                {
                    Height = 29;
                }
            }
            return (uint)(Low) | (uint)(Height) << 16; //合成为uint
        }


        /// <summary>
        /// 计算指定阴历年总天数。
        /// </summary>
        /// <param name="iLunarYear">指定阴历年，范围1901-2050。</param>
        /// <returns>返指定阴历年的总天数。</returns>
        private int GetLunarYearDays(ushort iLunarYear)
        {
            int Days;
            uint tmp;
            if (iLunarYear < START_YEAR || iLunarYear > END_YEAR)
            {
                return 0;
            }

            Days = 0;
            for (ushort i = 1; i <= 12; i++)
            {
                tmp = GetLunarMonthDays(iLunarYear, i);
                Days = Days + ((ushort)(tmp >> 16) & 0xFFFF); //取高位
                Days = Days + (ushort)(tmp); //取低位
            }
            return Days;
        }


        /// <summary>
        /// 计算从1901年1月1日过iSpanDays天后的阴历日期
        /// </summary>
        /// <param name="iYear">返回的年份。</param>
        /// <param name="iMonth">返回的月份。</param>
        /// <param name="iDay">返回的日子。</param>
        /// <param name="iSpanDays">天数。</param>
        private void CalcLunarDate(out ushort iYear, out ushort iMonth, out ushort iDay, uint iSpanDays)
        {
            uint tmp;
            //阳历1901年2月19日为阴历1901年正月初一
            //阳历1901年1月1日到2月19日共有49天
            if (iSpanDays < 49)
            {
                iYear = START_YEAR - 1;
                if (iSpanDays < 19)
                {
                    iMonth = 11;
                    iDay = (ushort)(11 + iSpanDays);
                }
                else
                {
                    iMonth = 12;
                    iDay = (ushort)(iSpanDays - 18);
                }
                return;
            }

            //下面从阴历1901年正月初一算起
            iSpanDays = iSpanDays - 49;
            iYear = START_YEAR;
            iMonth = 1;
            iDay = 1;
            //计算年
            tmp = (uint)GetLunarYearDays(iYear);
            while (iSpanDays >= tmp)
            {
                iSpanDays = iSpanDays - tmp;
                iYear++;
                tmp = (uint)GetLunarYearDays(iYear);
            }
            //计算月
            tmp = GetLunarMonthDays(iYear, iMonth); //取低位
            while (iSpanDays >= tmp)
            {
                iSpanDays = iSpanDays - tmp;
                if (iMonth == GetLeapMonth(iYear))
                {
                    tmp = (GetLunarMonthDays(iYear, iMonth) >> 16) & 0xFFFF; //取高位
                    if (iSpanDays < tmp)
                    {
                        break;
                    }
                    iSpanDays = iSpanDays - tmp;
                }
                iMonth++;
                tmp = GetLunarMonthDays(iYear, iMonth); //取低位
            }
            //计算日
            iDay = (ushort)(iDay + iSpanDays);
        }

        #endregion

        #region 星座

        /// <summary>
        /// 计算指定当前日期的星座序号。
        /// </summary>
        /// <returns>星座序号。</returns>
        private int GetConstellationIndex()
        {
            int Y, M, D;
            Y = m_Date.Year;
            M = m_Date.Month;
            D = m_Date.Day;
            Y = M * 100 + D;
            if (Y >= 321 && Y <= 419)
            {
                return 0;
            }
            else if (Y >= 420 && Y <= 520)
            {
                return 1;
            }
            else if (Y >= 521 && Y <= 620)
            {
                return 2;
            }
            else if (Y >= 621 && Y <= 722)
            {
                return 3;
            }
            else if (Y >= 723 && Y <= 822)
            {
                return 4;
            }
            else if (Y >= 823 && Y <= 922)
            {
                return 5;
            }
            else if (Y >= 923 && Y <= 1022)
            {
                return 6;
            }
            else if (Y >= 1023 && Y <= 1121)
            {
                return 7;
            }
            else if (Y >= 1122 && Y <= 1221)
            {
                return 8;
            }
            else if (Y >= 1222 || Y <= 119)
            {
                return 9;
            }
            else if (Y >= 120 && Y <= 218)
            {
                return 10;
            }
            else if (Y >= 219 && Y <= 320)
            {
                return 11;
            }
            else
            {
                return -1;
            }
        }


        /// <summary>
        /// 格式化星座序号为星座名称。
        /// </summary>
        /// <param name="ConstellationIndex">星座序号。</param>
        /// <returns>星座名称。</returns>
        private string FormatConstellation(int ConstellationIndex)
        {
            if (ConstellationIndex >= 0 && ConstellationIndex <= 11)
            {
                return ConstellationName[ConstellationIndex];
            }
            else
            {
                return "";
            }
        }

        #endregion

        #region 节气

        /// <summary>
        /// 计算公历当天对应的节气序号。
        /// </summary>
        /// <returns>返回值0-23为节气序号，-1表示不是节气。</returns>
        private int GetSolarTermIndex()
        {
            byte Flag;
            int Day, iYear, iMonth, iDay;
            iYear = m_Date.Year;
            if (iYear < START_YEAR || iYear > END_YEAR)
            {
                return -1;
            }

            iMonth = m_Date.Month;
            iDay = m_Date.Day;
            Flag = gLunarHolDay[(iYear - START_YEAR) * 12 + iMonth - 1];
            if (iDay < 15)
            {
                Day = 15 - ((Flag >> 4) & 0x0f);
            }
            else
            {
                Day = (Flag & 0x0f) + 15;
            }

            if (iDay == Day)
            {
                if (iDay > 15)
                {
                    return (iMonth - 1) * 2 + 1;
                }
                else
                {
                    return (iMonth - 1) * 2;
                }
            }
            else
            {
                return -1;
            }
        }


        /// <summary>
        /// 格式化节气序号为节气名称。
        /// </summary>
        /// <param name="SolarTermIndex">节气序号。</param>
        /// <returns>节气名称。</returns>
        private string FormatSolarTerm(int SolarTermIndex)
        {
            //string[] stroe = {"小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至"};
            if (SolarTermIndex <= this.LunarHolDayName.Length && SolarTermIndex >= 0)
                return this.LunarHolDayName[SolarTermIndex];
            return "";
        }

        #endregion

        #region 年月日

        /// <summary>
        /// 格式化阴历月份。
        /// </summary>
        /// <param name="iYear">年份。</param>
        /// <returns>干支记年。</returns>
        private string FormatLunarYear(int iYear)
        {
            string strG = "甲乙丙丁戊己庚辛壬癸";
            string strZ = "子丑寅卯辰巳午未申酉戌亥";
            return strG.Substring((iYear - 4) % 10, 1) + strZ.Substring((iYear - 4) % 12, 1);
        }


        /// <summary>
        /// 格式化阴历年份。
        /// </summary>
        /// <param name="iYear">年份。</param>
        /// <returns>生肖。</returns>
        private string FormatAnimalYear(int iYear)
        {
            string strSX = "鼠牛虎免龙蛇马羊猴鸡狗猪";
            return strSX.Substring((iYear - 4) % 12, 1);
        }


        /// <summary>
        /// 格式化阴历月份。
        /// </summary>
        /// <param name="iMonth">月份。</param>
        /// <returns>中文月份。</returns>
        private string FormatLunarMonth(int iMonth)
        {
            string szText = "正二三四五六七八九十";
            if (iMonth <= 10) return szText.Substring(iMonth - 1, 1) + "月";
            if (iMonth == 11) return "十一月";
            if (iMonth == 12) return "十二月";
            return "";
        }


        /// <summary>
        /// 格式化阴历日子。
        /// </summary>
        /// <param name="iDay">日子。</param>
        /// <returns>中文日子。</returns>
        private string FormatLunarDay(int iDay)
        {
            string szText1 = "初十廿三";
            string szText2 = "一二三四五六七八九十";
            string strDay = "";
            if (iDay != 20 && iDay != 30)
            {
                try
                {
                    strDay = szText1.Substring((iDay - 1) / 10, 1);
                    strDay = strDay + szText2.Substring((iDay - 1) % 10, 1);
                }
                catch (Exception)
                {

                }
            }
            else
            {
                strDay = szText1.Substring((iDay / 10), 1);
                strDay = strDay + "十";
            }
            return strDay;
        }

        #endregion

        #region OutPut

        /// <summary>阴历日期,以LunarDate(年日月)形式表示。</summary>
        public LunarDate1 LunarDate
        {
            get
            {
                if (this.m_LunarDate == null)
                {
                    ushort iYear, iMonth, iDay;
                    TimeSpan ts = m_Date - (new DateTime(START_YEAR, 1, 1));
                    this.CalcLunarDate(out iYear, out iMonth, out iDay, (uint)(ts.Days));
                    this.m_LunarDate = new LunarDate1(iYear, iMonth, iDay);
                }
                return this.m_LunarDate;
            }
        }


        /// <summary>阴历干支记年。</summary>
        public string LunarYear
        {
            get
            {
                if (m_LunarYear == "")
                    this.m_LunarYear = this.FormatLunarYear(this.LunarDate.Year);
                return this.m_LunarYear;
            }
        }


        /// <summary>阴历生肖。</summary>
        public string Animal
        {
            get
            {
                if (m_Animal == "")
                    this.m_Animal = this.FormatAnimalYear(this.LunarDate.Year);
                return this.m_Animal;
            }
        }


        /// <summary>格式化后的阴历月份。</summary>
        public string LunarMonth
        {
            get
            {
                if (this.m_LunarMonth == "")
                    this.m_LunarMonth = this.FormatLunarMonth(ushort.Parse(this.LunarDate.Month.ToString()));
                return this.m_LunarMonth;
            }
        }

        /// <summary>格式化后的阴历日子。</summary>
        public string LunarDay
        {
            get
            {
                if (this.m_LunarDay == "")
                    this.m_LunarDay = this.FormatLunarDay(ushort.Parse(this.LunarDate.Day.ToString()));
                if (this.m_LunarDay == "初一")
                {
                    this.m_LunarDay = this.LunarMonth;
                }
                return this.m_LunarDay;
            }
        }


        /// <summary>格式化后的阴历节气。</summary>
        public string SolarTerm
        {
            get
            {
                if (this.m_SolarTerm == "")
                    this.m_SolarTerm = this.FormatSolarTerm(this.GetSolarTermIndex());
                return this.m_SolarTerm;
            }
        }


        /// <summary>格式化后的星座。</summary>
        public string Constellation
        {
            get
            {
                if (this.m_Constellation == "")
                    this.m_Constellation = this.FormatConstellation(this.GetConstellationIndex());
                return this.m_Constellation;
            }
        }

        #endregion
    }

    public class LunarDate1
    {
        private int _y, _m, _d;
        private string lunardate = "";
        private string lunarmonth = "", lunarday = "", lunaryear = "";
        private string solarterm = "", animal = "";


        public LunarDate1(DateTime dt)
        {
            LunarDateClass ldc = new LunarDateClass(dt);
            this.lunarday = ldc.LunarDay;
            this.lunarmonth = ldc.LunarMonth;
            this.lunaryear = ldc.LunarYear;
            this.solarterm = ldc.SolarTerm;
            this.animal = ldc.Animal;
            this.lunardate = this.lunaryear + "(" + this.animal + ")年" + this.lunarmonth + this.lunarday + (this.solarterm == "" ? "" : " " + this.solarterm);
            this._y = ldc.LunarDate.Year;
            this._m = ldc.LunarDate.Month;
            this._d = ldc.LunarDate.Day;
        }
        public LunarDate1(int y, int m, int d)
        {
            this._y = y;
            this._m = m;
            this._d = d;
        }

        public int Year
        {
            get { return this._y; }
        }


        public int Month
        {
            get { return this._m; }
        }


        public int Day
        {
            get { return this._d; }
        }


        public string LunarDay
        {
            get
            {
                return this.lunarday;
            }
        }


        public string LunarMonth
        {
            get
            {
                return this.lunarmonth;
            }
        }


        public string LunarYear
        {
            get
            {
                return this.lunaryear;
            }
        }


        public string SolarTerm
        {
            get
            {
                return this.solarterm;
            }
        }


        public string Animal
        {
            get
            {
                return this.animal;
            }
        }


        public new string ToString()
        {
            return this.lunardate;
        }

    }


    #endregion



    public class LunarDate2
    {
        public const int MAX_YEAR = 2011;
        public const int MIN_YEAR = 1900;

        static readonly string[] lookupTable = new string[] 
    { 
        "0100101101101080131", "0100101011100000219", "1010010101110000208",
        "0101001001101050129", "1101001001100000216", "1101100101010000204",
        "0110101010101040125", "0101011010100000213", "1001101011010000202", 
        "0100101011101020122", "0100101011100000210", "1010010011011060130",
        "1010010011010000218", "1101001001010000206", "1101010101001050126",
        "1011010101010000214", "0101011010100000204", "1001011011010020123", 
        "1001010110110000211", "0100100110111070201", "0100100110110000220", 
        "1010010010110000208", "1011001001011050128", "0110101001010000216", 
        "0110110101000000205", "1010110110101040124", "0010101101100000213", 
        "1001010101110000202", "0100100101111020123", "0100100101110000210", 
        "0110010010110060130", "1101010010100000217", "1110101001010000206", 
        "0110110101001050126", "0101101011010000214", "0010101101100000204", 
        "1001001101110030124", "1001001011100000211", "1100100101101070131", 
        "1100100101010000219", "1101010010100000208", "1101101001010060127",
        "1011010101010000215", "0101011010100000205", "1010101011011040125", 
        "0010010111010000213", "1001001011010000202", "1100100101011020122", 
        "1010100101010000210", "1011010010101070129", "0110110010100000217", 
        "1011010101010000206", "0101010110101050127", "0100110110100000214", 
        "1010010110110000203", "0101001010111030124", "0101001010110000212", 
        "1010100101010080131", "1110100101010000218", "0110101010100000208", 
        "1010110101010060128", "1010101101010000215", "0100101101100000205",
        "1010010101110040125", "1010010101110000213", "0101001001100000202",
        "1110100100110030121", "1101100101010000209", "0101101010101070130",
        "0101011010100000217", "1001011011010000206", "0100101011101050127",
        "0100101011010000215", "1010010011010000203", "1101001001101040123",
        "1101001001010000211", "1101010100101080131", "1011010101000000218",
        "1011011010100000207", "1001011011010060128", "1001010110110000216", 
        "0100100110110000205", "1010010010111040125", "1010010010110000213", 
        "1011001001011100202", "0110101001010000220", "0110110101000000209", 
        "1010110110101060129", "1010101101100000217", "1001001101110000206",
        "0100100101111050127", "0100100101110000215", "0110010010110000204", 
        "0110101001010030123", "1110101001010000210", "0110101100101080131",
        "0101101011000000219", "1010101101100000207", "1001001101101050128", 
        "1001001011100000216", "1100100101100000205", "1101010010101040124",
        "1101010010100000212", "1101101001010000201", "0101101010101020122",
        "0101011010100000209", "1010101011011070129", "0010010111010000218",
        "1001001011010000207", "1100100101011050126", "1010100101010000214",
        "1011010010100000214" 
    };

        /**/
        /// <summary>十二生肖</summary>
        static readonly string animalsTable = "鼠牛虎兔龍蛇馬羊猴雞狗豬";
        static readonly string monthsTable = "正二三四五六七八九十寒臘";
        static readonly string daysTable = "初一初二初三初四初五初六初七初八初九初十十一十二十三十四十五十六十七十八十九二十廿一廿二廿三廿四廿五廿六廿七廿八廿九三十";

        /**/
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

        public LunarDate2(int year, int month, int day)
        {
            if ((year < MIN_YEAR) || (year > MAX_YEAR))
                throw new ArgumentOutOfRangeException("year too large or too small");

            // 計算農歷年
            int lunarYear;
            int lunarMonth;
            int lunarDay;

            lunarYear = year;
            // 農歷新年月份
            lunarMonth = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(15, 2)));
            // 農歷新年日子
            lunarDay = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(17, 2))); ;
            if ((month < lunarMonth) || ((month == lunarMonth) && (day < lunarDay)))
            {
                lunarYear--;
                // 農歷新年月份
                lunarMonth = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(15, 2)));
                // 農歷新年日子
                lunarDay = Convert.ToInt32((lookupTable[lunarYear - MIN_YEAR].Substring(17, 2))); ;
            }

            // 計算農歷月
            DateTime date = new DateTime(year, month, day);
            DateTime lunarDate2 = new DateTime(lunarYear, lunarMonth, lunarDay);
            TimeSpan span = date - lunarDate2;
            int dayCount = span.Days;
            lunarMonth = 1;
            lunarDay = 1;
            bool leapMonth = false; //閏月
            for (int i = 0; i < dayCount; i++)
            {
                lunarDay++;
                if (lunarDay == 30 + Convert.ToInt32(lookupTable[lunarYear - MIN_YEAR].Substring(lunarMonth - 1, 1)) ||
                (leapMonth == true && (lunarDay == 30 + Convert.ToInt32(lookupTable[lunarYear - MIN_YEAR].Substring(12, 1)))))
                {
                    if (
                        (leapMonth == false) &&
                        (lunarMonth == Convert.ToInt32(lookupTable[lunarYear - MIN_YEAR].Substring(13, 2)))
                        )
                    {
                        leapMonth = true;
                    }
                    else
                    {
                        leapMonth = false;
                        lunarMonth++;
                    }
                    lunarDay = 1;
                }
                else
                {
                }
            }

            // 計算農歷日
            lunarDayText = daysTable.Substring((lunarDay - 1) * 2, 2);
            // 計算農歷月
            lunarMonthText = monthsTable.Substring(lunarMonth - 1, 1) + "月";
            if (leapMonth == true) lunarMonthText = "閏" + lunarMonthText;
            // 農歷年
            lunarYearText = Convert.ToString(lunarYear, 10) + "年";
            // 計算天干地支
            chineseEarText = chineseEra[(lunarYear - 4) % 60];
            // 計算生肖
            aminalsText = animalsTable.Substring((lunarYear - 4) % 12, 1);
        }

        //農歷日
        private string lunarDayText;
        public string LunarDay { get { return this.lunarDayText; } }

        //農歷月
        private string lunarMonthText;
        public string LunarMonth { get { return this.lunarMonthText; } }

        //農歷年
        private string lunarYearText;
        public string LunarYear { get { return this.lunarYearText; } }

        //天干地支
        private string chineseEarText;
        public string chineseEar { get { return this.chineseEarText; } }

        //生肖
        private string aminalsText;
        public string Aminals { get { return this.aminalsText; } }

        public override string ToString()
        {
            return aminalsText + "," + chineseEarText + "," + lunarYearText + lunarMonthText + lunarDayText;
        }
    }

    class Calendar
    {
        /// <summary>
        /// 輸入年月日，得到這天是星期幾
        /// </summary>
        /// <param name="year">年</param>
        /// <param name="month">月</param>
        /// <param name="day">日</param>
        /// <returns>星期幾</returns>
        private static int GetWeekByDay(int year, int month, int day)
        {
            DateTime dt = new DateTime(year, month, day);
            return (int)dt.DayOfWeek;
        }

        /// <summary>
        /// 獲取某個月的天數，輸入(int)年份，月份，回傳天數(int)
        /// </summary>
        /// <param name="year">年</param>
        /// <param name="month">月</param>
        /// <returns>天數</returns>
        private static int GetMonthDay(int year, int month)
        {
            int thismonthdays = DateTime.DaysInMonth(year, month);
            return thismonthdays;
        }
        /// <summary>
        /// 列印年歷
        /// </summary>
        /// <param name="year"></param>
        public void Printdate(int year)
        {
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
            string ganHour, zhiHour;
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

