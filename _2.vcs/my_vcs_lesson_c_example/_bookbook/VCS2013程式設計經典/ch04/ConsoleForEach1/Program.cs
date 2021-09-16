using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleForEach1
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, num;       // i for迴圈計數變數 , num 來存放總人數 
            double sum = 0;  // 存放總人數身高的加總

            Console.Write("請輸入總人數 : ");
            num = int.Parse(Console.ReadLine()); // 輸入值轉整數再指定給 num 變數
            Console.WriteLine();

            double[] tall = new double[num];  // 建立tall倍精確陣列存放每位的身高

            for (i = 0; i <= tall.GetUpperBound(0); i++)
            {
                Console.Write("請輸入第 {0} 位身高(公分) : ", i + 1);
                tall[i] = double.Parse(Console.ReadLine()); //輸入身高逐一存入陣列  
            }

            foreach (double height in tall)  // 計算總人數身高的加總
                sum += height;   // 將所有陣列元素依序加總指定給sum           

            Console.WriteLine("\n=== " + i.ToString("#") + " 位平均身高:" +
                (sum / num).ToString("00.00"));// 顯示平均身高
            Console.Read();
        }
    }
}
