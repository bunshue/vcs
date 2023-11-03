using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0309
{
    class Program
    {
        static void Main(string[] args)
        {
            int a = 12, b = 24, c = 30, d = 40;
            bool isResult = (a < b) && (c < d);
            WriteLine($"AND運算 {isResult}");
            isResult = (a > b) || (b < c);
            WriteLine($"OR運算 {isResult}");
            //將變數isResult經過OR的運算，再做反相
            WriteLine($"!運算子，反相結果 {!isResult}");

            ReadKey();//螢幕暫停
        }
    }
}
