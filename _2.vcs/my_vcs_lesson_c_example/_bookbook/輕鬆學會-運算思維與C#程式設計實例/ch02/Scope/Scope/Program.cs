using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Scope
{
    class Program
    {
        static void Main(string[] args)
        {
            float a;
            double b;
            decimal c;
            a = 3.14159265358979323846264f;
            b = 3.14159265358979323846264;
            c = 3.14159265358979323846264m;

            WriteLine("使用單精度   a={0}", a);
            WriteLine("使用倍精度   a={0}", b);
            WriteLine("貨弊 a={0}", c);
            Read();
        }
    }
}
