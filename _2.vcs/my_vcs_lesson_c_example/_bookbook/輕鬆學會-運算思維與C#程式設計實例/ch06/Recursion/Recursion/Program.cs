using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Recursion
{
    class Program
    {
        public static int factorial(int i)
        {
            int sum;
            if (i == 0)//遞迴終止的條件 
                return (1);
            else
                sum = i * factorial(i - 1); //遞迴呼叫自身方法
            return sum;
        }

        static void Main(string[] args)
        {
            int i, n;

            Write("請輸入階層數= ");
            n = int.Parse(ReadLine());
            WriteLine(" {0}!值為={1}", n, factorial(n));
            Read();
        }
    }
}
