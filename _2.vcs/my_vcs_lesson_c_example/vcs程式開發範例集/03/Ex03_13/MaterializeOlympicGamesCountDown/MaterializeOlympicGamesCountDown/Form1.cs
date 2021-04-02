using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using Microsoft.VisualBasic;
namespace MaterializeOlympicGamesCountDown
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        //變量用於存儲年、月、日、時、分、秒
        public long LogYear, logMonth, logDay, logHour, logMinte, logSencon;
        private void timer1_Tick(object sender, EventArgs e)
        {
            DateTime get_time1 = Convert.ToDateTime(DateTime.Now.ToString());
            DateTime sta_ontime1 = Convert.ToDateTime(Convert.ToDateTime("2008-08-08 20:00:00"));
           txtYear.Text = DateAndTime.DateDiff("yyyy", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
           txtMonth.Text = DateAndTime.DateDiff("m", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
           textday.Text = DateAndTime.DateDiff("d", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
           txtHour.Text = DateAndTime.DateDiff("h", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
           txtmintue.Text = DateAndTime.DateDiff("n", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
           txtsecon.Text = DateAndTime.DateDiff("s", get_time1, sta_ontime1, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
           textBox1.Text = DateTime.Now.ToString();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            textBox2.Text = "2008-08-08  20:00:00" + "　　星期五";
            timer1.Enabled = true;
        }
    }
}