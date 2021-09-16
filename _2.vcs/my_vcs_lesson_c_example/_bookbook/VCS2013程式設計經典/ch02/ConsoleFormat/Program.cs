using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleFormat
{
    class Program
    {
        static void Main(string[] args)
        {
                        int num1, num2;
            double num3, num4;
            num3 = 1234.567;
            num4 = -1234.567;
            Console.WriteLine
 				("num3=1234.567      num4=-1234.567 的 C/c3 格式分別為:");
            Console.WriteLine
 				("num3={0:C}   num4={1:c3} ", num3, num4);
            Console.WriteLine();

            num1 = 123456;
            num2 = -123456;
            Console.WriteLine();
            Console.WriteLine
 				("num1=123456      num2=-123456 的 D9/d3/D 格式分別為 :");
            Console.WriteLine
 				("num1={0:D9}  num2={1:d3}  num2={2:D}", num1, num2, num2);

            Console.WriteLine();
            Console.WriteLine
 				("num3=1234.567       num4=-1234.567 的 E/e2 格式分別為 :");
            Console.WriteLine("num3={0:E}    num4={1:e2}", num3, num4);
            Console.WriteLine();

            num3 = 1234.567;
            num4 = -1234.567;
            Console.WriteLine
 				("num3=1234.567  num4=-1234.567 的 F1/f 格式分別為:");
            Console.WriteLine
 				("num3={0:F1}   num4={1:f} ", num3, num4);
            Console.WriteLine();

            num3 = 1234.567;
            num4 = -1234.567;
            Console.WriteLine
 				("num3=1234.567  num4=-1234.567 的 G3 和 g 格式分別為 :");
            Console.WriteLine("num3={0:G3}   num4={1:g} ", num3, num4);
            Console.WriteLine();

            num3 = 1234.567;
            num4 = -1234.567;
            Console.WriteLine
 				("num3=1234.567  num4=-1234.567 的 G/g4 格式分別為:");
            Console.WriteLine
 				("num3={0:G}   num4={1:g4} ", num3, num4);
            Console.WriteLine();

            num3 = 1234.567;
            num4 = -1234.567;
            Console.WriteLine
 				("num3=1234.567   num4=-1234.567 的 N3 和 n 格式分別為 :");
            Console.WriteLine("num3={0:N3}   num4={1:n} ", num3, num4);
            Console.WriteLine();

            num1 = 123;
            num2 = -123;
            Console.WriteLine("num1=123     num2=-123 的 X 格式分別為:");
            Console.WriteLine("num1={0:X}      num2={1:x} ", num1, num2);
            Console.Read();

        }
    }
}
