using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleNum
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 5;
            switch (i)
            {
                case 1:
                case 3:
                case 5:
                case 7:
                case 9:
                    Console.WriteLine("{0} 為 奇數 ", i);
                    break;
                case 2:
                case 4:
                case 6:
                case 8:
                    Console.WriteLine("{0} 為 偶數 ", i);
                    break;
                default:
                    Console.WriteLine("Other ");
                    break;
            }
            Console.Read();

        }
    }
}
