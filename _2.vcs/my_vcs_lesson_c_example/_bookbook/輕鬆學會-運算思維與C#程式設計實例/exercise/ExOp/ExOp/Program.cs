using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace ExOp
{
    class Program
    {
        static void Main(string[] args)
        {
            bool binResult;
            int numResult;

            binResult = (99 < 102) && (8 > 15);
            WriteLine("(99 <102 ) && (8 > 15)的運算結果為：" + binResult.ToString());
            numResult = 15 & 31;
            WriteLine("15 & 31的運算結果為： " + numResult.ToString());
            Read(); //暫停
        }
    }
}
