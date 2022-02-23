using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

using Microsoft.VisualBasic;    //for DateAndTime

namespace TimeNow
{
    public partial class Frm_Main : Form
    {
        //目標時間
        DateTime dt_target = Convert.ToDateTime(Convert.ToDateTime("2024-7-26 00:00:00"));

        public Frm_Main()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //显示冬奥会时间
            textBox2.Text = "2024/7/26  00:00:00" + "　　星期五";
            label10.Text = dt_target.ToString();


            timer1.Enabled = true;//开启计时器
        }


        //变量用于存储年、月、日、时、分、秒
        public long LogYear, logMonth, logDay, logHour, logMinte, logSencon;
        private void timer1_Tick(object sender, EventArgs e)
        {
            //得到当前系统时间
            DateTime dt = DateTime.Now;


            //计算相隔年数
            txtYear.Text = DateAndTime.DateDiff("yyyy", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label11.Text = DateAndTime.DateDiff("yyyy", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //计算相隔月数
            txtMonth.Text = DateAndTime.DateDiff("m", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label12.Text = DateAndTime.DateDiff("m", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();


            //计算相隔天数
            textday.Text = DateAndTime.DateDiff("d", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label13.Text = DateAndTime.DateDiff("d", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //计算相隔小时数
            txtHour.Text = DateAndTime.DateDiff("h", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label14.Text = DateAndTime.DateDiff("h", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //计算相隔分钟数
            txtmintue.Text = DateAndTime.DateDiff("n", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label15.Text = DateAndTime.DateDiff("h", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //计算相隔秒数
            txtsecon.Text = DateAndTime.DateDiff("s", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label16.Text = DateAndTime.DateDiff("s", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            textBox1.Text = DateTime.Now.ToString();


            //label11.Text = "距離時間 : ";
        }


    }
}