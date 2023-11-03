using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0417
{
    class Program
    {
        static void Main(string[] args)
        {
            int number, div = 2, count = 0;
            bool flag = true;

            Write("輸人數字，找出區間不含1的質數？");
            number = Convert.ToInt32(ReadLine());
            WriteLine($"質數有：");
            //提供輸入數值
            while (div <= number)
            {
                //依序讀取每個數值，找出由2開始的質數
                for (int index = 2; index <= div; index++)
                {
                    //被2整除者非質數，將被排除，break敘述中斷廻圈
                    int mod = div % index;
                    if (mod == 0 && div > index)
                    {
                        flag = false;
                        break;
                    }
                    else
                        flag = true;
                }//end of for loop

                if (flag == false)
                {
                    div++;
                    //回到下一層while廻圈繼續執行
                    continue;
                } //end of if

                //輸出質數，欄寬為2，不止者前方補0
                Write($"{div:00} ");
                count++;
                div++;
            } //end of while

            ReadKey();//螢幕暫停
        }
    }
}
