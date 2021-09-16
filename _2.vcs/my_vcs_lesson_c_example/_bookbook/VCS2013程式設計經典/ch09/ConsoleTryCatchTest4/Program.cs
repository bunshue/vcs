using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTryCatchTest4
{
    class Program
    {
        static void Main(string[] args)
        {
          int[] score = new int[] { 100, 86, 98 };
          try
          {
              Console.WriteLine("第 4 位學生的成績 {0} ", score[3]);
          }
          catch (IndexOutOfRangeException ex)
          {
             //Console.WriteLine (ex.ToString() + "\n" + ex.HelpLink + "\n" + ex.StackTrace );
              Console.WriteLine(ex.ToString());
              Console.WriteLine();
              Console.WriteLine(ex.HelpLink + "\n" + ex.StackTrace);
          }
          Console.Read();
        }
    }
}
