using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {

            /*--------------------------------------------------*
             *   第 1 章: 兩個整數相加的主控台應用程式          *
             *--------------------------------------------------*/
            
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
            

            /*
                        Console.WriteLine("Hello, 這是我的第一個C#程式!");
                        Console.Read();
            */

            /*--------------------------------------------------*
             *   第 3 章: 變數與算術運算式                      *
             *--------------------------------------------------*/
            /*
            
                        //short a = 456; //OK
                        //short s = 40000; // error            
             
                        int k = 40000;
                        long l = k;

                        Console.WriteLine("l = " + l);

                        //short s = k; //error

                        //int i = 1.23f; //error
                        //int i = 1.23;  //error

                        short s = (short) k;
            
                        Console.WriteLine("s = " + s); //-25536

                        int a = 17, b = 5;
                        float f;
                        f = a / b;
                        Console.WriteLine("f = " + f);
                        f = (float)a / (float)b;
                        Console.WriteLine("f = " + f);
            
                        Console.WriteLine("My \"C#\" Program ");
             */

    }
}
           
}
