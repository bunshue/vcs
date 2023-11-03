using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;   //滙入靜態類別

namespace CH0508
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] yr = { 101, 102, 103, 104 };//年
                                              //建立3*4二維陣列
            int[,] gdp = { {250872, 259564, 288579, 283280 },
               { 3208572, 3541387, 401368, 4244227},
               { 7804898, 8071281, 8369219, 8643443} };

            int inner, outer;//for廻圈計數器
            int[] total = new int[4];//儲存合計結果

            //foreach讀取年分並建立標頭
            foreach (int item in yr)
            {
                Write($"{item,12}年");//欄寬12
            }
            WriteLine();//換行         

            //GetLength()方法分別取得列(row)和欄(column)的值
            int row = gdp.GetLength(0);
            int column = gdp.GetLength(1);

            //雙層for廻圈，外層for先讀取row數
            for (outer = 0; outer < row; outer++)
            {
                //內層for讀取column數
                for (inner = 0; inner < column; inner++)
                {
                    //欄寬14，NO表示含有千位分號但小數位數是零
                    Write($"{gdp[outer, inner],14:N0}");
                }
                WriteLine();//換行

                total[0] += gdp[outer, 0];//101年gdp合計
                total[1] += gdp[outer, 1];//102年gdp合計
                total[2] += gdp[outer, 2];//103年gdp合計
                total[3] += gdp[outer, 3];//104年gdp合計
            }//end outer for-loop

            //輸出標頭
            String ch = new String('-', 58);
            WriteLine(ch);

            //輸出各年份合計結果，以+字元串接整行
            WriteLine($"合計:{total[0],10:N0} {total[1],12:N0}"
               + $"{total[2],14:N0} {total[3],13:N0}");

            ReadKey();   //螢幕暫停
        }
    }
}
