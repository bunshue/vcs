using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Params
{
    class Program
    {
        public static void EchoParamters(params string[] args)
        {
            for (int i = 0; i < args.Length; i++)    //參數個數  
            {
                Write("參數{0}:" + args[i] + " ", i);
            }
            WriteLine();
            WriteLine("============================================");
            WriteLine();
        }

        static void Main(string[] args)
        {
            string[] four = { "忠孝", "仁愛", "信義", "和平" };

            EchoParamters();         //傳入零個參數
            EchoParamters(four);     //傳入參數陣列
            EchoParamters("我更注重", "禮義廉恥", "聖美善真"); //傳入三個參數
            Read();
        }
    }
}
