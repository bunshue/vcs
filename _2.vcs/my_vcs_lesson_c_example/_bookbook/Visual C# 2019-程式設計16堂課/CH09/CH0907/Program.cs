using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0907
{
    class Program
    {
        static void Main(string[] args)
        {
            byte mn;
            //判斷輸入是否為數值，若超出範圍或非數值，繼續廻圈
            while (true)
            {
                try
                {
                    TestMonth(out mn);//呼叫靜態方法

                    //多重條件-依數值顯示月分
                    switch (mn)
                    {
                        case 2:
                            WriteLine($"{mn}月有28或29天");
                            break;
                        case 4:
                        case 6:
                        case 9:
                        case 11:
                            WriteLine($"{mn}月有30天");
                            break;
                        default:
                            WriteLine($"{mn}月有31天");
                            break;
                    }

                    break;   //輸入正確的數值則中斷廻圈
                }
                //處理範圍較小-資料型別不對
                catch (InvalidCastException ex1)
                {
                    WriteLine(ex1.Message);
                }
                //處理所有範圍
                catch (Exception ex2)
                {
                    WriteLine("Main()-catch區塊");
                    WriteLine(ex2.Message);
                }
            }
            Read();
        }

        //定義靜態方法-out關鍵字做傳址 
        public static void TestMonth(out byte number)
        {
            Write("請輸入1~12的數字：");
            number = Convert.ToByte(ReadLine());

            //輸入數字須在1~12之間，若不是throw敘述擲出例外訊息
            if (number <= 0 || number > 12)
            {
                //數值超出允許範圍-ArgumentOutOfRangeException()
                throw new ArgumentOutOfRangeException();
            }
            else
                Write("輸入正確...");
        }
    }
}
