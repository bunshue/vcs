using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Tower
{
    class Program
    {
        static void hanoi(int n, int p1, int p2, int p3)
        {
            if (n == 1)
                WriteLine("盤子從 " + p1 + " 移到 " + p3 );
            else
            {
                hanoi(n - 1, p1, p3, p2);
                WriteLine("盤子從 " + p1 + " 移到 " + p3);
                hanoi(n - 1, p2, p1, p3);
            }
        }

        static void Main(string[] args)
        {
            int j;
            Write("請輸入盤子數量：");
            j = int.Parse(ReadLine());
                hanoi(j, 1, 2, 3);
            Read();
        }     
    }
}
