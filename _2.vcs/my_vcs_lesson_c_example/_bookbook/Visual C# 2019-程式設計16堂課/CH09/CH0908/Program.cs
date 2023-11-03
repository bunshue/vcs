using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0908
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                ArrayRead();   //呼叫靜態方法
            }
            catch (Exception e)
            {
                WriteLine("Main()-catch區塊--");
                WriteLine(e.Message);
            }
            ReadKey();
        }
        //定義靜態方法
        public static void ArrayRead()
        {
            //宣告陣列並初始化
            int[] number = { 11, 21, 78, 125 };
            //讀取陣列元素進行錯誤捕捉
            try
            {
                //故意將陣列讀取時超出界限
                for (int k = 0; k <= 4; k++)
                {
                    Write($"{number[k]} ");
                }
            }
            //讀取陣列超出界限時則做例外狀況處理
            catch (IndexOutOfRangeException ex)
            {
                WriteLine("-----");
                WriteLine(ex.Message);
                throw;   //將例外狀況擲回給呼叫端-主程式
            }
        }
    }
}
