using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0910
{
    class Program
    {
        static void Main(string[] args)
        {
            //讀取陣列元素進行錯誤捕捉
            try
            {
                CatchArray();   //呼叫靜態方法
            }

            //屬性InnerException例外狀況處理
            catch (Exception ex)
            {
                Write("--Main()-- ");
                WriteLine(ex.Message);
                //當InnerException有取得例外狀況，指出錯誤所在
                if (ex.InnerException != null)
                {
                    WriteLine(
                       $"目前例外狀況：\n{ex.InnerException}");
                }
            }
            ReadKey();
        }
        //定義靜態方法-讀取陣列並超出界限
        public static void CatchArray()
        {
            //宣告陣列並初始化
            int[] number = { 11, 21, 78, 125 };
            try
            {
                //故意將陣列讀取時超出界限
                for (int k = 0; k <= 4; k++)
                {
                    Write($"{number[k]} ");
                }
            }

            //throw敘述將例外狀況擲回主程式
            catch (Exception ex)
            {
                //使用建構函式Exception(string, ex)
                throw new IndexOutOfRangeException(
                   "讀取陣列\n", ex);
            }
        }
    }
}
