using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleBreakContinue
{
    class Program
    {
        static void Main(string[] args)
        {
            int sum, upper, n ; // sum 為連加的總和, upper為上限值, n為連加的終值 
            sum = 0; n = 0;

            Console.Write("\n 請輸入上限值 ： ");
            upper = int.Parse(Console.ReadLine()); // 輸入上限值轉成整數再指定給input變數

            do
            {
                n += 1;            // 連加增值為1
                if (sum <= upper)  // 判斷 sum總和是否小於等於輸入的上限值                    
                {
                    sum += n;
                    continue;	// 跳到do…while 處判斷n是否大於0
                }
                else
                {
                    sum -= n - 1;
                    break;	    // 離開迴圈
                }
            } while (n > 0); 	// 若n>0則進入迴圈

            Console.WriteLine("\n 終值 : {0}  ,  上限值 : {1} ", n-2, upper);
            Console.WriteLine("\n 結果 : 1 + 2... + {0} 總和為 {1} ", n-2, sum);

            Console.Read();

        }
    }
}
