using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace Bubble
{
    class Program
    {
        static void Main(string[] args)
        {
            int i, j, tmp;
            int[] data = { 80, 15, 93, 76, 29, 88,46 };  //原始資料

            WriteLine("氣泡排序法：");
            Write("原始資料：");
            for (i = 0; i < data.Length; i++)
            {
                Write(data[i] + " ");
            }
            WriteLine();

            for (i = data.Length - 1; i > 0; i--)  //掃瞄次數
            {
                for (j = 0; j < i; j++)     //比較、交換次數
                {
                    // 比較相鄰兩數，如第一數較大則交換
                    if (data[j] > data[j + 1])
                    {
                        tmp = data[j];
                        data[j] = data[j + 1];
                        data[j + 1] = tmp;
                    }
                }

                //把各次掃描後的結果印出
                Write("第" + (data.Length - i) + "次排序結果：");
                for (j = 0; j < data.Length; j++)
                {
                    Write(data[j] + " ");
                }
                WriteLine();
            }

            Write("排序後結果為：");
            for (i = 0; i < data.Length; i++)
            {
                Write(data[i] + " ");
            }
            WriteLine();
            ReadKey();
        }
    }
}
