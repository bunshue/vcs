using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTryCatch4
{
    class Program
    {
        static void Main(string[] args)
        {
            int i = 1, n = 0, f = 0;
            while (true)
            {
                try
                {
                    Console.Write("n = ");
                    n = int.Parse(Console.ReadLine());
                    f = 1;
                    for (i = 1; i <= n; i++)
                    {
                        f = f * i;
                    }
                    break;
                }
                catch (InvalidCastException ex)
                {
                    Console.WriteLine("資料型態錯誤");
                }
                catch (OverflowException ex)
                {
                    Console.WriteLine("溢位錯誤");
                }
                catch (Exception ex)
                {
                    Console.WriteLine("其他錯誤");
                }
            }
            Console.WriteLine("{0} != {1}", n, f);
            Console.ReadLine();
        }
    }
}
