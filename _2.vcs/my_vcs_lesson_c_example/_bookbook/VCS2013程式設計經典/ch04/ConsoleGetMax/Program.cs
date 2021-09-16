using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleGetMax
{
    class Program
    {
        static int GetMax(ref int[] ary)	//以陣列當引數傳遞為參考呼叫
        {
            int i, max;
            max = ary[0];       		// 先假設陣列第一個元素為最大值
            // 使用 迴圈逐一尋找陣列元素中的最大值
            for (i = 1; i <= ary.GetUpperBound(0); i++)
            {
                if (max < ary[i])
                {
                    max = ary[i];
                }
            }
            return max;  // 傳回陣列元素中的最大值
        }

        static void Main(string[] args)
        {
            int[] tAry = new int[] { 12, 15, 38, 21, 25 };
            Console.WriteLine("=陣列元素如下=");
            int i;
            for (i = 0; i <= tAry.GetUpperBound(0); i++)
            {
                Console.Write("{0} ", tAry[i]);
            }
            Console.WriteLine("\n");
            Console.WriteLine("陣列最大值：{0}", GetMax(ref tAry));
            Console.Read();
        }
    }
}
