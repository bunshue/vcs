using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleNextFor1
{
    class Program
    {
        static void Main(string[] args)
        {
           for (int i = 1; i <= 5; i++)		  // 外層迴圈
           {
              for (int k = 1; k <= i; k++)    // 內層迴圈
                  Console.Write("  {0}", k);  // 游標停在同一列     
              Console.WriteLine();		      // 強迫換列
           }
           Console.Read();
        }
    }
}
