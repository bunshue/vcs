using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0902
{
    class Program
    {
        static void Main(string[] args)
        {
            for (int index = 5; index >= 0; index--)
            {
                int dob = 10;
                Console.Write($"{dob / index} ");
            }
            Console.ReadKey();
        }
    }
}
