using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;    //滙入靜態類別

namespace CH0402
{
    class Program
    {
        /* 單一條件做雙向判斷
         * 攝氏 = (華氏-32)*5/9
         * 華氏 = 攝氏*(9/5)+32
         */
        static void Main(string[] args)
        {
            Write("請輸入攝氏溫度：");
            //以Convert類別ToSingle將輸入金額轉成float型別
            float cel = float.Parse(ReadLine());

            //將攝氏換為華氏溫度
            float fah = cel * (9 / (float)5) + 32;

            //當華氏溫度大於85度時，顯示天氣炎熱的訊息
            if (fah > 85)
            {
                WriteLine($"天氣炎熱，目前華氏溫度 {fah}");
            }
            //如果沒有大於華氏85度，直接顯示二者溫度
            else
            {
                WriteLine($"攝氏 {cel}, 華氏 = {fah}");
            }

            ReadKey();   //螢幕暫停
        }
    }
}
