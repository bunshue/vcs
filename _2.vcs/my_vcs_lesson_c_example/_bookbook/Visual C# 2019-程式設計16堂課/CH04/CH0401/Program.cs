using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;    //滙入靜態類別

namespace CH0401
{
    class Program
    {
        /* 單一條件做單向判斷
         * if敘述判斷輸入的值是否大於1500
         */
        static void Main(string[] args)
        {
            Write("請輸入購物金額：");
            //以Convert類別ToSingle將輸入金額轉成float型別
            float money = Convert.ToSingle(ReadLine());

            //當購物金額大於1500時享有95折優待
            if (money >= 1500)
            {
                money *= 0.95F;
                WriteLine("享有95折優待，");
            }

            //輸出金額含有NT$
            WriteLine($"您的購物金額 {money:c}");
            ReadKey();   //螢幕暫停
        }
    }
}
