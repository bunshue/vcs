using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//static關鍵字滙入靜態類別Console
using static System.Console;

/* 第一個主控台應用程式
   WriteLine()方法在螢幕上顯示訊息
   ReadLine()方法讀取訊息
   呼叫DateTiem類別的Today來顯示今天日期
 */

namespace CH0201
{
    class Program
    {
        static void Main(string[] args)
        {
            //取得系統目前的日期
            DateTime today = DateTime.Today;

            Write("請輸入你的名字：");

            //變數name取得輸入的名稱
            string name = ReadLine();

            WriteLine("Hi! {0} ", name);
            //字串插補
            //WriteLine($"Hi! {name}");

            //顯示今天的日期
            WriteLine($"今天是{today:D}");

            //讓畫面暫時停留，等待使用者按任意鍵
            ReadKey();
        }
    }
}
