using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0405
{
    class Program
    {
        static void Main(string[] args)
        {
            //取得輸入分數並以Convert類別ToUInt()方法轉成uint型別
            Write("請輸入你的成績：");
            uint score = Convert.ToUInt32(ReadLine());
            char grade = 'A';
            //第一層if/else敘述
            if (score <= 90)
            {
                //第二層if/else敘述
                if (score <= 80)
                {
                    //第三層if/else敘述
                    if (score <= 70)
                    {
                        //「? :」運算子取代第四層if/else敘述
                        grade = (score <= 60) ? 'E' : 'D';
                    }
                    else
                        grade = 'C';
                }
                else
                    grade = 'B';
            }
            else
                grade = 'A';
            //呼叫Char類別ToString()方法，轉字元為字串
            WriteLine($"你的評分 {grade.ToString()}");

            ReadKey();//螢幕暫停
        }
    }
}
