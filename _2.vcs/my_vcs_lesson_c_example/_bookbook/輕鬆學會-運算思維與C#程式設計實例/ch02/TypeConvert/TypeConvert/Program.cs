using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace TypeConvert
{
    class Program
    {
        static void Main(string[] args)
        {
            string day;
            DateTime datetime_format;
            Write("請您輸入日期及時間字串：");
            day = ReadLine();//輸入日期
                                     //利用ToDateTime(字串)轉為日期格式
            datetime_format = Convert.ToDateTime(day);
            WriteLine("經轉換的日期格式是{0}", datetime_format);
            Read();//讓畫面暫停
        }
    }
}
