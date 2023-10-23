using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace CallReffrene_ref
{
    class Program
    {
        public static void Call_Reference(ref int j, ref int k)
        {
            j = k = 200;  //指定多重傳回值
        }

        static void Main(string[] args)
        {
            int a, b;
            a = 400;
            b = 700;
            Call_Reference(ref b, ref a);
            WriteLine("呼叫方法後: a={0} b={1}", a, b);
            ReadLine();
        }
    }
}
