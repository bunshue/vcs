using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0301
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告兩個變數並設初值，然後把它們相加
            int num1 = 75;
            int num2 = 92;
            Console.WriteLine(
               $"{num1} + {num2} = {num1 + num2}");

            //讓螢幕暫停
            Console.ReadKey();
        }
    }
}
