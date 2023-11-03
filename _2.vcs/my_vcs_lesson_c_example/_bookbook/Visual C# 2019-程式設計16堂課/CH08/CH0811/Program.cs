using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0811
{
    class Program
    {
        static void Main(string[] args)
        {
            string sign = new string('-', 33);
            WriteLine($"{"科目",-10}{"選必修",-4}" +
               $" {"學分"} {"費用",5}");
            WriteLine(sign);
            Student st1 = new Student(1, "計算機概論", 4, true);
            st1.Display();
            Student st2 = new Student(2, "英文      ", 2, false);
            st2.Display();
            Student st3 = new Student(1, "多媒體    ", 3, true);
            st3.Display();
            Console.ReadKey();
        }
    }
}
