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
            //顯示冬奧會時間
            textBox2.Text = "2024/7/26  00:00:00" + "　　星期五";
            label10.Text = dt_target.ToString();


            timer1.Enabled = true;//開啟計時器
        }


        //變量用于存儲年、月、日、時、分、秒
        public long LogYear, logMonth, logDay, logHour, logMinte, logSencon;
        private void timer1_Tick(object sender, EventArgs e)
        {
            //得到當前系統時間
            DateTime dt = DateTime.Now;

            //計算相隔年數
            txtYear.Text = DateAndTime.DateDiff("yyyy", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label11.Text = DateAndTime.DateDiff("yyyy", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //計算相隔月數
            txtMonth.Text = DateAndTime.DateDiff("m", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label12.Text = DateAndTime.DateDiff("m", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //計算相隔天數
            textday.Text = DateAndTime.DateDiff("d", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label13.Text = DateAndTime.DateDiff("d", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //計算相隔小時數
            txtHour.Text = DateAndTime.DateDiff("h", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label14.Text = DateAndTime.DateDiff("h", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //計算相隔分鐘數
            txtmintue.Text = DateAndTime.DateDiff("n", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label15.Text = DateAndTime.DateDiff("h", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            //計算相隔秒數
            txtsecon.Text = DateAndTime.DateDiff("s", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();
            label16.Text = DateAndTime.DateDiff("s", dt, dt_target, FirstDayOfWeek.Sunday, FirstWeekOfYear.FirstFourDays).ToString();

            textBox1.Text = DateTime.Now.ToString();


            //label11.Text = "距離時間 : ";
        }


    }
}