using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0504
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告陣列並初始化
            ushort[] score = new ushort[] { 78, 65, 92, 55, 83 };
            ushort index = 0;//陣列的索引

            Write("排序前");
            //foreach廻圈讀取元素
            foreach (ushort item in score)
            {
                Write($"{item,3}");//設欄寬為3
            }

            Array.Sort(score);//遞增排序

            WriteLine();//換行
            Write("遞增排序");

            //for廻圈讀取陣列排序後元素
            for (index = 0; index < score.Length; index++)
            {
                Write($"{score[index],3}");
            }

            Array.Reverse(score);//遞減排序

            WriteLine();//換行
            Write("遞減排序");

            index = 0;
            //while廻圈，取得的陣列長度讀取陣列元素
            while (index < score.Length)
            {
                Write($"{score[index],3}");
                index++;   //遞增索引值
            }
            ReadKey();//螢幕暫停
        }
    }
}
