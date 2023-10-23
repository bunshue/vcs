using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace ForApp
{
    class Program
    {
        static void Main(string[] args)
        {
            WriteLine("1~20間奇數的和");
            int sum = 0;//設定總和的起始值為0
            WriteLine("所有的奇數:");
            for (int i = 1; i <= 20; i++)
            {
                if (i % 2 != 0)
                {//利用if敘述確定i為奇數
                    sum += i;
                    Write(i + " ");
                }
            }
            WriteLine();
            WriteLine("答案=" + sum);//輸出答案	
            Read();
        }
    }
}
