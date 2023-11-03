using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0502
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告陣列並初始化
            int[] number = { 78, 129, 314, 117 };
            int index = 0;//陣列的索引
                          //foreach廻圈讀取陣列元素
            foreach (int item in number)
            {
                WriteLine($"number[{index}] = {item,3}");
                index++;   //遞增索引值
            }
            ReadKey();//螢幕暫停
        }
    }
}