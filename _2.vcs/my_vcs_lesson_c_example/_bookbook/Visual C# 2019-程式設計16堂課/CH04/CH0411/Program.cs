using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0411
{
    class Program
    {
        /* for廻圈配合continue、break敘述
         * 取得按鍵來決定廻圈是否繼續
         */
        static void Main(string[] args)
        {
            uint score = 0, count = 0, total = 0;
            string endkey = "";//空字串

            //for廻圈中再設計數器count
            for (; ; )
            {
                Write("請輸入分數：");
                score = Convert.ToUInt32(ReadLine());

                //計數器count, 控制運算式遞增1
                count++;
                total += score;//儲存累加的分數

                Write("繼續否？按y繼續，按n離開-->");
                endkey = ReadLine();

                //條件式，按Y或y繼續，按N或n則中斷廻圈
                if (endkey == "Y" || endkey == "y")
                    continue;//回到for廻續，繼續執行
                else if (endkey == "N" || endkey == "n")
                    break;//中斷廻圈的執行
            }

            WriteLine($"共{count}科，總分 {total}");

            ReadKey();//螢幕暫停
        }
    }
}
