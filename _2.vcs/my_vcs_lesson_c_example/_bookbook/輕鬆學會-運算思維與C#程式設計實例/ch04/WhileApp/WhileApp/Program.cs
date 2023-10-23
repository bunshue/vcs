using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace WhileApp
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 1, sum = 0;//宣告n的起始值和累加值sum
                               //while迴圈開始
            while (n <= 10)
            {
                Write("n=" + n);
                sum += n;//計算n的累加值
                WriteLine("\t累加值=" + sum);
                n++;
            }
            WriteLine("迴圈結束");
            Read();
        }
    }
}
