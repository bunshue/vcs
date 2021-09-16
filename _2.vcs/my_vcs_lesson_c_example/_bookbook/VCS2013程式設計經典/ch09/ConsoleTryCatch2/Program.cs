using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTryCatch2
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b, c = 0;
            Console.Write("a = ");
            a = int.Parse(Console.ReadLine()); 
            Console.Write("b = ");
            b = int.Parse(Console.ReadLine());
            try
            {
                c = a / b;
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
            Console.WriteLine("a / b = {0}", c);
            Console.Read();

        }
    }
}
