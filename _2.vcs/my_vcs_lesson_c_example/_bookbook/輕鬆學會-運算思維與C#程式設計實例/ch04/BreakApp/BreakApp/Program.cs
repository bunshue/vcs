using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace BreakApp
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, j;
            WriteLine("跳出單層迴圈");
            for (i = 1; i < 10; i++)
            {
                for (j = 1; j <= i; j++)
                {
                    if (j == 5) break; //跳出單層迴圈
                    Write(j);
                }
                WriteLine();
            }

            WriteLine();
            Read();
        }
    }
}
