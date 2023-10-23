using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Overload
{
    class Program
    {
        static void add() //多載的add方法，但不接收參數
        {
           WriteLine("輸入錯誤");
        }

        static void add(int x, int y) //多載的add方法，接收二個整數參數
        {
           WriteLine("加法運算結果=" + (x + y));
        }

        static void add(string x, string y) //多載的add方法，接收二個字串參數
        {
           WriteLine("相加結果=" + (x + y));
        }

        static void Main(string[] args)
        {
            int num1 = 6;
            int num2 = 8;
            string str1 = "Visual C# ";
            string str2 = "輕鬆易學";
            int choice;

           WriteLine("加法多載的示範: ");
           Write("請選擇多載加方式 (1)數值加法 (2)字串加法:");
            choice = int.Parse(Console.ReadLine()); //取得所輸入的值
            switch (choice)
            {
                case 1: //執行數字加法
                    add(num1, num2);
                    break;
                case 2: //執行字串連結
                    add(str1, str2);
                    break;
                default://顯示輸入錯誤
                    add();
                    break;
            }
           Read();
        }
    }
}
