using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0901
{
    class Program
    {
        static void Main(string[] args)
        {
            byte[] number = { 21, 31, 41 };
            //k <= 3 錯誤，執行時會進入偵錯模式
            for (int k = 0; k <= 2; k++)
                Console.Write($"{number[k],3}");
            Console.ReadKey();
        }
    }
}
