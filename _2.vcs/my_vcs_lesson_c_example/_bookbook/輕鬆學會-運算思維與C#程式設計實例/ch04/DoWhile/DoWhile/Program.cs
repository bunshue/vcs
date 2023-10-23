using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace DoWhile
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = 144, m = 72;
            int temp = 0;//作為交換n與m的功能
           WriteLine("n=" + n + ",m=" + m);

            //do while迴圈開始		
            do
            {
                temp = m % n;
                m = n;
                n = temp;
            } while (n != 0);//檢查條件運算式

           WriteLine("兩數的最大公因數=" + m);
           Read();
        }
    }
}
