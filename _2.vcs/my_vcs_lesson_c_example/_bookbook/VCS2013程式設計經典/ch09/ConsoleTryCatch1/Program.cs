using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTryCatch1
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b, c;
            Console.Write("a = ");
            // 使用int.Parse() 方法將鍵盤所輸入的值轉成整數
            a = int.Parse(Console.ReadLine());
            Console.Write("b = ");
            b = int.Parse(Console.ReadLine());
            c = a / b;
            Console.WriteLine("a / b  = {0}", c);
            Console.ReadLine();
        }
    }
}
