﻿using System;
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

            /*
            Console.WriteLine("<<<兩位數相加>>>");

            string input1, input2;
            int num1, num2;

            Console.Write("數字一 : ");
            input1 = Console.ReadLine();
            num1 = Convert.ToInt16(input1);

            Console.Write("數字二 : ");
            input2 = Console.ReadLine();
            num2 = Convert.ToInt16(input2);

            int result = num1 + num2;

            //Console.WriteLine(num1 + " + " + num2 + " = " + result);

            Console.WriteLine("{0} + {1} = {2}", num1, num2, result);

            string age, name;

            Console.WriteLine("請輸入您的姓名 : ");
            name = Console.ReadLine();
            Console.WriteLine("請輸入您的年齡 : ");
            age = Console.ReadLine();
            Console.Write(name + " 您好, 您今年是 " + age + " 歲");

            int radius;
            const float pi = 3.14159F;

            Console.WriteLine("請輸入半徑");
            radius = int.Parse(Console.ReadLine());
            Console.WriteLine("所求圓周為" + radius * 2 * pi);
            */

            Console.WriteLine("測試多型（Polymorphism）");
            hi();

            hi("lion-mouse");


            Console.Read(); //Hold住畫面
        }

        public static void hi()
        {

            Console.WriteLine("hi,C Sharp");
        }

        public static void hi(string name)
        {
            Console.WriteLine("hi,{0}", name);
        }
    }
}

