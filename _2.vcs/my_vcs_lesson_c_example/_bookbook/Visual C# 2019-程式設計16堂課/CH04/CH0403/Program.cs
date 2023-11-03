using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0403
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("請輸入分數：");
            ushort score = UInt16.Parse(Console.ReadLine());
            string answer = "";   //空字串
                                  //if/else敘述
            if (score >= 60)
            {
                answer = "考試及格";
            }
            else
            {
                answer = "多努力. . .";
            }
            //條件運算子「?:」
            string answer2 = (score >= 60) ? "通過！" : "多努力...";
            Console.WriteLine(answer + answer2);
            Console.ReadKey();   //螢幕暫停
        }
    }
}
