using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace PrivateFun
{
    class Data
    {
        private Data() { }     //私有建構函式

        static void dump(string s)    //將字串輸出的私有靜態函式
        {
            Console.WriteLine("字串輸出結果: " + s);
        }

        static string read()          //從鍵盤讀取字串的私有靜態函式
        {
            Console.Write("請輸入一個字串: ");
            return Console.ReadLine();
        }

        public static void print() //公用的靜態函式
        {
            dump(read());
        }
    }

    class One
    {
        public One()
        {
            Console.WriteLine("==========================");
            Console.WriteLine("這是由 One 類別輸出：");
            Data.print(); //呼叫共用函式 
        }
    }

    class Two
    {
        public Two()
        {
            Console.WriteLine("==========================");
            Console.WriteLine("這是由 Two 類別輸出：");
            Data.print(); //呼叫共用函式
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            new One();
            new Two();
            Console.Read();
        }
    }
}
