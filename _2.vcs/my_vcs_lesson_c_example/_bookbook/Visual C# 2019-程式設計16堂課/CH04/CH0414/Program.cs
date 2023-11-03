using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0414
{
    class Program
    {
        //do/while廻圈，按y繼續廻圈的執行
        static void Main(string[] args)
        {
            int count = 0, score, total = 0;
            float avg = 0.0F;
            string key = "";//空字串

            //後測試廻圈，先執行敘述，再做條件判斷
            do
            {
                count++;//統計科目
                Write("輸入分數：");
                score = Convert.ToInt32(ReadLine());
                total += score;//合計分數
                Write("繼續否？(Y/N)->");
                key = ReadLine();//讀取輸入字元
            } while (key == "Y" || key == "y");

            //計算平均，並將count轉為float型別
            avg = total / (float)count;
            WriteLine($"共{count}科，平均 = {avg}");

            ReadKey();//螢幕暫停
        }
    }
}
