using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0308
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 10, b = 30, c = 20;
            int result1 = 0, result2 = 0;
            result1 = a + b;
            result2 = a - c;
            //將兩個運算元做比較
            WriteLine($"{a} == {b}, {a == b}");
            WriteLine(
               $"{result1} >= {result2}, {result1 >= result2}");
            WriteLine($"{a} != {result2}, {a != result2}");

            char wd1 = 'H', wd2 = 'h';
            WriteLine($"{wd1} <= {wd2}, {wd1 <= wd2}");

            ReadKey(); //螢幕暫停
        }
    }
}
