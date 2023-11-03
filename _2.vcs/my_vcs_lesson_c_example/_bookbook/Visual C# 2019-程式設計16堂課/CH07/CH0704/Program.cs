using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0704
{
    class Program
    {
        static void Main(string[] args)
        {
            Person pern = new Person()
            { Name = "王小風", Height = 176 };
            Console.WriteLine("By Value -> ");
            //Passing By Value - 輸出王小風
            pern.showInfo(pern);
            Console.WriteLine($"{pern.Name}, " +
               $"您的身高 {pern.Height}cm");
            Console.WriteLine("By Reference -> ");
            //Passing By Reference - 輸出江大海
            pern.display(ref pern);
            Console.WriteLine($"{pern.Name}, " +
               $"您的身高 {pern.Height}cm");
            Console.ReadKey();
        }
    }
}
