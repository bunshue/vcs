using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleEnum1
{
    class Program
    {
        // 定義WeekDays列舉內容7個成員
        // 用來表示一星期的星期日到星期六的列舉常數值
        enum WeekDays : int
        {
            Monday = 1,      	// 星期一
            Tuesday = 2,         // 星期二
            Wednesday = 3,       // 星期三
            Thursday = 4,        // 星期四
            Friday = 5,          // 星期五
            Saturday = 6,        // 星期六
            Sunday = 7           // 星期日
        };

        static void Main(string[] args)
        {
            // 取出WeekDays.Wednesday列舉常數值之後再轉成整數
            Console.WriteLine("星期三列舉常數值：{0}", (int)WeekDays.Wednesday);
            Console.WriteLine("星期五列舉常數值：{0}", (int)WeekDays.Friday);
            Console.Read();
        }
    }
}
