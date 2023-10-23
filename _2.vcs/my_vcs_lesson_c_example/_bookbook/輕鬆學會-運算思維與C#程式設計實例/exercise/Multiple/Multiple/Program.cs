using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Multiple
{
    class Program
    {
        static void Main(string[] args)
        {

            Write("請輸入一個數字= ");
            int number = int.Parse(ReadLine());
            if (number % 7 == 0)  //如果輸入的數值可以被7整除
                WriteLine(number + "是7的倍數");
            else
                WriteLine(number + "不是7的倍數");
            Read();
        }
    }
}