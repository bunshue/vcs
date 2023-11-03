using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//匯入靜態類別

namespace CH0407
{
    class Program
    {
        //修改範例CH0404 -- 巢狀if判斷月分天數
        static void Main(string[] args)
        {
            Write("輸入數值1~12，顯示當月天數：");
            //呼叫Parse()方法轉換ushort型別
            ushort month = UInt16.Parse(ReadLine());

            string display = "";//空字串

            //switch/case判斷月分天數
            switch (month)
            {
                case 2:
                    display = $"{month}月 28或29天";
                    break;
                case 4:
                case 6:
                case 9:
                case 11:
                    display = $"{month}月 30天";
                    break;
                default:
                    display = $"{month}月 31天";
                    break;
            }
            WriteLine(display);//輸出訊息         

            ReadKey();//螢幕暫停
        }
    }
}
