using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Fac
{
    class Program
    {
        static void Main(string[] args)
        {
            int product = 1, number, i = 1;

           Write("請輸入一個數值= ");
            number = int.Parse(Console.ReadLine());
            while (i <= number)
            {
                product = product * i;
                i++;
            }
           WriteLine(number + "!=" + product);
           Read();
        }
    }
}
