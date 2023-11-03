using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0612
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine($"未實體化，學生{Student.Count}個\n");

            Student st1 = new Student("Michelle", 25);
            Student st2 = new Student("Janet", 19);
            Student st3 = new Student("Vasily", 22);

            ReadKey();
        }
    }
}
