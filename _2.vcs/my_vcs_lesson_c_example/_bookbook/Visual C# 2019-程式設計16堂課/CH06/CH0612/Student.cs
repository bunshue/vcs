using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0612
{
    class Student
    {
        //唯讀靜態欄位，物件共有 -- 取得系統時間
        static readonly DateTime start;

        //靜態屬性 -- 記錄生成的物件
        public static int Count { get; private set; }

        //自動實做成員屬性：Name, Age
        public string Name { get; set; }
        public int Age { get; set; }

        //靜態建構函式，只會執行一次
        static Student()
        {
            //取得系統目前的日期和時間, ToLongTimeString()只顯示時間
            start = DateTime.Now;
            WriteLine($"靜態建構函式執行時間：" +
               $"{start.ToLongTimeString()}");
        }

        //含有2個參數的建構函式
        public Student(string title, int num)
        {
            //TimeSpan為時間間隔，以毫秒為間隔單位
            TimeSpan period = DateTime.Now - start;
            Name = title; Age = num;
            Count++;   //建立物件時就累計
            Write($"新生 {Count} {Name,9} {Age} 歲，");
            WriteLine($"{period.TotalSeconds} 秒");
        }
        ~Student() { }//解構函式
    }
}
