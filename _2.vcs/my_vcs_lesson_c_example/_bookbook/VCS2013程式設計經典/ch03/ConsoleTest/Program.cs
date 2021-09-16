using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleTest
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("\n 題目 : \n"); 
            Console.WriteLine(" 試問 Visual Studio 可開發下列哪種應用程式\n");
            Console.WriteLine(" 1.視窗程式  2.Web 程式   3.裝置應用程式   4.以上皆是\n");
            Console.Write(" 請作答 ： ");
            // 宣告Ans字串變數用來存放使用者由鍵盤輸入的答案
            string Ans = Console.ReadLine();
            // 判斷Ans是否為1, 2, 3其中之一
            if (Ans == "1" || Ans == "2" || Ans == "3")
                Console.WriteLine("\n === 答錯了, 正確答案是 4 .");
            else if (Ans == "4")	// 判斷Ans是否等於4
                Console.WriteLine("\n === 答對了, 真不愧是 .NET 達人 ....");
            else               	// 當Ans不等於1 ,2 ,3, 4時執行下列敘述
                Console.WriteLine("\n === 無此選項....");
            Console.Read();
         }
    }
}
