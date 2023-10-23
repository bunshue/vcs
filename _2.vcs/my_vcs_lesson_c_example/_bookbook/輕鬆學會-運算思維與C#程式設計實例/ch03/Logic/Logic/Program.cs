using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Logic
{
    class Program
    {
        static void Main(string[] args)
        {
            bool bin;
            int num;

            bin = (91 > 23) && (5 > 32);
           WriteLine(" (91 > 23) && (5 > 32) -> " + bin.ToString());

            num = 101 & 110;
           WriteLine("101 & 110 -> " + num.ToString());
           Read(); //暫停
        }
    }
}
