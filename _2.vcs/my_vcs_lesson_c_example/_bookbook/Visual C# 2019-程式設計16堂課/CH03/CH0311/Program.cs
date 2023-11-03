using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0311
{
    class Program
    {
        static void Main(string[] args)
        {
            int price = 450;
            bool result1, result2, onsale;
            onsale = false;
            result1 = (5 + 11) * 10 / 2 >= 50 / 2 * 3;
            result2 = (price <= 450) || (onsale == true);
            //將運算的結果顯示出來
            WriteLine($"(5 + 11) * 10 / 2 >= 50 / 2 * 3" +
               $", 結果 {result1}");
            WriteLine($"(price <= 450) Or (onsale == true)" +
               $", 結果 {result2}");
            ReadKey(); //暫停
        }
    }
}
