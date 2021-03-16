using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Console_3
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, 這是我的第一個C#程式!");


            int k = 40000;
            long l = k;

            Console.WriteLine("l = " + l);

            //short s = k; //error

            //int i = 1.23f; //error
            //int i = 1.23;  //error

            short s = (short)k;

            Console.WriteLine("s = " + s); //-25536

            int a = 17, b = 5;
            float f;
            f = a / b;
            Console.WriteLine("f = " + f);
            f = (float)a / (float)b;
            Console.WriteLine("f = " + f);

            Console.WriteLine("My \"C#\" Program ");

            Console.WriteLine("");

            Console.WriteLine("<<<兩位數相加>>>");

            string input1, input2;
            int num1, num2;

            Console.Write("數字一:");
            input1 = Console.ReadLine();
            num1 = Convert.ToInt16(input1);

            Console.Write("數字二:");
            input2 = Console.ReadLine();
            num2 = Convert.ToInt16(input2);

            int result = num1 + num2;

            //Console.WriteLine(num1 + " + " + num2 + " = " + result);

            Console.WriteLine("{0} + {1} = {2}", num1, num2, result);



            Console.Read();

        }
    }
}
