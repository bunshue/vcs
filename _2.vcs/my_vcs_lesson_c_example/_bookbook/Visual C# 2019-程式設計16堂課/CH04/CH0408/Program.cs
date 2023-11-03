using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0408
{
    class Program
    {
        //switch/case敘述，判斷輸入數值來對應星期
        static void Main(string[] args)
        {
            Write("輸入1~7的數值：");
            //呼叫Convert類別ToByte()方法轉為byte型別
            byte number = Convert.ToByte(ReadLine());

            string display = "";//空字串

            //switch/case敘述判斷輸入數值
            switch (number)
            {
                case 1:
                    display = $"{number} -- 星期一";
                    break;

                case 2:
                    display = $"{number} -- 星期二";
                    break;

                case 3:
                    display = $"{number} -- 星期三";
                    break;

                case 4:
                    display = $"{number} -- 星期四";
                    break;

                case 5:
                    display = $"{number} -- 星期五";
                    break;

                case 6:
                    display = $"{number} -- 星期六";
                    break;

                case 7:
                    display = $"{number} -- 星期天";
                    break;

                default:
                    display = "數字不正確，無法顯示";
                    break;
            }

            WriteLine(display);//輸出訊息

            ReadKey();//螢幕暫停
        }
    }
}
