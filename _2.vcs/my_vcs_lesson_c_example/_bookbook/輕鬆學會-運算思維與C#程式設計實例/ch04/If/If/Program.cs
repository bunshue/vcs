using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace If
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("輸入一個數值：");
            int number = int.Parse(ReadLine());

            if (number > 50)
                WriteLine("您所輸入的值大於50");
            if (number <= 50)
                WriteLine("您所輸入的值小於或等於50");
            Read();
        }
    }
}
