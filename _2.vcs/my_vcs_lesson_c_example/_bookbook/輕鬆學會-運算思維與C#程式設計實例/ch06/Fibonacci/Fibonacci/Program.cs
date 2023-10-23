using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Fibonacci
{
    class Program
    {
        public static int fib(int n)
        {
            if (n == 0) return 0;
            if (n == 1)
                return 1;
            else
                return fib(n - 1) + fib(n - 2);//遞迴引用本身2次
        }

        static void Main(string[] args)
        {
            int i, n;

            Write("請輸入費伯那序列值= ");
            n = int.Parse(ReadLine());
            for (i = 0; i <= n; i++)
                WriteLine("fib({0}) = {1}", i, fib(i));
            Read();
        }
    }
}
