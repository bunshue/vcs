using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0404
{
    class Program
    {
        static void Main(string[] args)
        {
            Write("輸入數值1~12，顯示當月天數：");
            //呼叫Parse()方法轉換ushort型別
            ushort month = UInt16.Parse(ReadLine());

            //第一層if/else敘述，確認數值是否在1~12
            if ((month >= 1) && (month <= 12))
            {
                /* 第二層if/else敘述，配合||(OR)運算子，
                   數值若是 1, 3, 5, 7, 8, 10, 12 回傳31天 */
                if ((month == 1) || (month == 3) || (month == 5)
                         || (month == 7) || (month == 8)
                         || (month == 10) || (month == 12))
                {
                    WriteLine($"{month}月 31天");
                }
                else
                {
                    /* 第三層使用「? :」運算子，若是2，回傳28或29天
                       其餘回傳30天 */
                    WriteLine(month == 2 ?
                       $"{month}月 28天或29天" :
                       $"{month}月 30天");
                }//第二層if/else敘述結束
            }
            else
            {
                WriteLine("輸入數值不對");
            }//第一層if/else敘述結束

            ReadKey();
        }
    }
}
