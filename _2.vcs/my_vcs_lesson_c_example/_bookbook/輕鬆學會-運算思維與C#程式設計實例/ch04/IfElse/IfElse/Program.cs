using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace IfElse
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("請輸入總分：");
            int number = int.Parse(ReadLine());

            if (number > 600)
               WriteLine("您的多益成績水準以上!!");
            else
               WriteLine("您的多益成績還可以努力再考高一點!!");
           Read();
        }
    }
}