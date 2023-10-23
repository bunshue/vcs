using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace MultiTable
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, j;
           WriteLine("==============================================================");
            for (i = 1; i <= 9; i++)
            {
                for (j = 1; j <= 9; j++)
                   Write("{0:D}*{1:D}={2,2:D} ", j, i, i * j);
               WriteLine();
            }
           WriteLine("==============================================================");
           Read(); //暫停
        }
    }
}
