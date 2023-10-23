using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Precedence
{
    class Program
    {
        static void Main(string[] args)
        {
            bool value;
            value = (58 + 25) - 23 * 3 >= 108 + 25 / 5;
            //將運算的結果顯示出來
            WriteLine("(58 + 25) - 23 * 3 >= 108 + 25 / 5=" + value);
            Read(); //暫停
        }
    }
}
