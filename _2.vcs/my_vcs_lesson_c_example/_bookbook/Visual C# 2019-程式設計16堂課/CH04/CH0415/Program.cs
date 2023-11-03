using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0415
{
    class Program
    {
        static void Main(string[] args)
        {
            //建立亂數物件rnd，呼叫Next()方法產生1~100之間的隨機數
            Random rnd = new Random();
            int guess = rnd.Next(1, 100);

            int count = 1, number = 0;

            //後測試?圈，先執行敘述，再做條件判斷
            do
            {
                Write("輸入1~100之間的數值：");
                number = Convert.ToInt32(ReadLine());

                //if/else if/else敘述判斷數字太大或太小
                if (number > guess)
                    WriteLine($"第{count}次, {number}太大了");
                else if (number < guess)
                    WriteLine($"第{count}次, {number}太小了");
                else
                {
                    WriteLine($"第{count}次, 猜中了！數字 {number}");
                }
                count++;//統計猜的次數

            } while (number != guess);

            ReadKey();//螢幕暫停
        }
    }
}
