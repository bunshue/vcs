using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0406
{
    class Program
    {
        //if/else if/else敘述做多重條件判斷
        static void Main(string[] args)
        {
            //取得輸入分數並以Convert類別ToUInt()方法轉成uint型別
            Write("請輸入你的成績：");
            uint score = Convert.ToUInt32(ReadLine());

            char grade = 'A';

            //多重條件，但只有一個結果回傳
            if (score > 90)//91~100
            {
                grade = 'A';
            }
            else if (score > 80)//81~90
            {
                grade = 'B';
            }
            else if (score > 70)//71~80
            {
                grade = 'C';
            }
            else if (score > 60)//61~70
                grade = 'D';
            else //60分以下
                grade = 'E';

            //呼叫ToString()方法，將字元變成字串
            WriteLine($"你的分數{score}, " +
               $"等級 {grade.ToString()}");

            ReadKey();//螢幕暫停
        }
    }
}