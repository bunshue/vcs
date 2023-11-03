using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console; //匯入靜態類別

namespace CH0312
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告常數
            const double Pound = 2.20462;
            Write("輸入公斤數：");

            //將輸入的字串呼叫Parse()方法轉成整數
            int weight = int.Parse(ReadLine());

            //單位換算時自動轉成double型別
            WriteLine($"{weight}公斤 = {weight * Pound:f2}磅");

            ReadKey();//螢幕暫停
        }
    }
}
