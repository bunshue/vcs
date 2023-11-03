using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0807
{
    class Program
    {
        static void Main(string[] args)
        {
            Person p1 = new Person("Tomas");
            int pay1 = p1.Display(3);
            Worker manag = new Worker("經理");
            int pay2 = manag.Display(3);
            WriteLine($"***{p1.Name}***");
            WriteLine($"薪水 {pay1:N0}, " +
               $"{manag.Name}津貼 {pay2:N0}");
            int total = pay1 + pay2;
            Write($"實領金額 {total:c0}");
            ReadKey();
        }
    }
}
