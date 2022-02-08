using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_Calendar
{
    public partial class Form1 : Form
    {
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

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Calendar calendar = new Calendar();
            calendar.Printdate(DateTime.Now.Year);
            Console.ReadLine();
        }
    }
}

