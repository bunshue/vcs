using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0304
{
    class Program
    {
        static void Main(string[] args)
        {
            //變數以float, double,decimal為型別
            float a; double b; decimal c;
            a = 3.22222222222222222222222F;
            b = 3.22222222222222222222222;
            c = 3.22222222222222222222222M;
            WriteLine($"單精度  = {a}");
            WriteLine($"倍精度  = {b}");
            WriteLine($"精確小數 = {c}");

            //暫停螢幕
            ReadKey();
        }
    }
}
