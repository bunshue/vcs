using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace CallReference_out
{
    class Program
    {
        public static void Call_Reference(out int j, out int k)
        {
            j = k = 200;  //指定多重傳回值
        }

        static void Main(string[] args)
        {
            int a, b;
            Call_Reference(out b, out a);
           WriteLine("呼叫方法後: a={0} b={1}", a, b);
           ReadLine();
        }
    }
}