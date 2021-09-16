using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleDoWhile
{
    class Program
    {
        static void Main(string[] args)
        {
            
          string yes = "";       // yes字串變數用來存放使用者輸入的資料            
          int score, sum, count; // score存放輸入的成績，sum累計成績總和, count紀錄人數
          sum=0; count=0;
          Console.Write("\n === 程式語言設計成績試算 ===\n");  
          do
          {
             count += 1;       // count加1
             Console.Write("\n{0}. 請輸入第 {1} 位同學成績 : ",count, count);          
             score = int.Parse(Console.ReadLine());
             sum += score;
             Console.Write("\n == 是否繼續 ? (Y/N) : ");
             yes = Console.ReadLine();           // 將使用者由鍵盤輸入的資料放入yes變數               
            } while (yes == "y" || yes == "Y");  // 若yes變數等於"y"或"Y"則進入迴圈

            Console.WriteLine ("\n == 共輸入 {0} 位同學成績, 班上平均成績 : {1}",count, sum/count);
            Console.Read();
         }
    }
}
