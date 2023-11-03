using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0410
{
    class Program
    {
        //for迴圈以偶數做累加
        static void Main(string[] args)
        {
            Write("輸入數值做累加：");
            //呼叫Convert類別ToUInt()方法轉為uint型別
            uint number = Convert.ToUInt16(ReadLine());
            int k, total = 0;

            WriteLine("數值  結果");
            WriteLine("----------");

            //for廻圈：計數器k、條件式k < number、控制運算 k++
            for (k = 1; k < number; k++)
            {
                //偶數-只有餘數為零才做加總
                if (k % 2 == 0)
                {
                    total += k;//累加數值
                               //觀看數值加總的變化
                    WriteLine($"{k,3}  {total,4:N0}");
                }
            }
            //只輸出加總結果
            //WriteLine($"1~{number}數值累加 {total:N0}");

            ReadKey();//螢幕暫停
        }
    }
}
