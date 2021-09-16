using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace xCh4_1_4_1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            textBox1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            textBox1.Multiline = true;
            textBox1.ReadOnly = true;
            textBox1.Size = new System.Drawing.Size(800, 20);

            label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            label1.Size = new System.Drawing.Size(800, 20);
            label1.Text = "";

            // 設定表單物件
            ClientSize = new System.Drawing.Size(1080, 566);
            Controls.AddRange(new System.Windows.Forms.Control[] { textBox1, monthCalendar1 });
            Text = "MonthCalendar範例";

            // 變更顏色
            monthCalendar1.BackColor = System.Drawing.SystemColors.Info;
            monthCalendar1.ForeColor = System.Drawing.Color.FromArgb(
                                     ((System.Byte)(192)), ((System.Byte)(0)), ((System.Byte)(192)));
            monthCalendar1.TitleBackColor = System.Drawing.Color.Purple;
            monthCalendar1.TitleForeColor = System.Drawing.Color.Yellow;
            monthCalendar1.TrailingForeColor = System.Drawing.Color.FromArgb(
                                     ((System.Byte)(192)), ((System.Byte)(192)), ((System.Byte)(0)));

            // 設定 AnnuallyBoldedDates
            monthCalendar1.AnnuallyBoldedDates =
                new System.DateTime[] { new System.DateTime(2013, 4, 20, 0, 0, 0, 0),
                                    new System.DateTime(2013, 4, 28, 0, 0, 0, 0),
                                    new System.DateTime(2013, 5, 5, 0, 0, 0, 0),
                                    new System.DateTime(2013, 7, 4, 0, 0, 0, 0),
                                    new System.DateTime(2013, 12, 15, 0, 0, 0, 0),
                                    new System.DateTime(2013, 12, 18, 0, 0, 0, 0)};

            // 設定BoldedDates
            monthCalendar1.BoldedDates = new System.DateTime[] 
                                                    { new System.DateTime(2013, 9, 26, 0, 0, 0, 0) };

            // 設定MonthlyBoldedDates
            monthCalendar1.MonthlyBoldedDates =
               new System.DateTime[] {new System.DateTime(2013, 1, 15, 0, 0, 0, 0),
                                  new System.DateTime(2013, 1, 30, 0, 0, 0, 0)};

            // 設定3列及4欄，共12個月的外觀
            monthCalendar1.CalendarDimensions = new System.Drawing.Size(4, 3);

            // 設定每週的第一天是星期一
            monthCalendar1.FirstDayOfWeek = System.Windows.Forms.Day.Monday;

            // 被容許的上限日期12/31/2014
            monthCalendar1.MaxDate = new System.DateTime(2014, 12, 31, 0, 0, 0, 0);

            // 被容許的下限日期 1/1/2012
            monthCalendar1.MinDate = new System.DateTime(2012, 1, 1, 0, 0, 0, 0);

            // 允許最多能夠同時選取21日
            monthCalendar1.MaxSelectionCount = 21;

            // 速率是一個月
            monthCalendar1.ScrollChange = 1;

            // TodayDate 屬性代表的日期是不要顯示在控制項下方
            monthCalendar1.ShowToday = false;

            // 今天日期不以圓形或方格識別
            monthCalendar1.ShowTodayCircle = false;

            // 將週數 (1-52) 顯示在每列日期的左方
            monthCalendar1.ShowWeekNumbers = true;
        }

        private void monthCalendar1_DateSelected(object sender, DateRangeEventArgs e)
        {
            textBox1.Text = "選取後的日期： 開始是： " +
                e.Start.ToShortDateString() + "，結束是： " + e.End.ToShortDateString();
        }

        private void monthCalendar1_DateChanged(object sender, DateRangeEventArgs e)
        {
            label1.Text = "改變後的日期： 開始是： " +
                e.Start.ToShortDateString() + " ，結束是： " + e.End.ToShortDateString();
        }
    }
}
