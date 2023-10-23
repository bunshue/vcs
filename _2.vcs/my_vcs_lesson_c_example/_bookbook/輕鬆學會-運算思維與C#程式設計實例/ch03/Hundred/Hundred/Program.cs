using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Hundred
{
    class Program
    {
        static void Main(string[] args)
        {
            int num;

            Write("請輸入三位數以上整數: ");
            num = int.Parse(ReadLine());

            num = (num / 100) % 10;
            WriteLine("百位數的數字為"+num );
            Read();
        }
    }
}
