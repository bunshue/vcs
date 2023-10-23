using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace TypeChange
{
    class Program
    {
        static void Main(string[] args)
        {
            const double pi = 3.14159D;//常數
            Write("請輸入半徑(單位為公尺)：");
            //讀取半徑，再以Parse轉為int
            int radius = int.Parse(ReadLine());
            WriteLine("圓面積是{0}平方公尺", pi * radius * radius);
            Read();
        }
    }
}
