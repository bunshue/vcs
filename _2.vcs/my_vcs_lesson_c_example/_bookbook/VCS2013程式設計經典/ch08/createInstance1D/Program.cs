using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;  // 若此行有寫入，第21行System.Collectios.可省略 

namespace createInstance1D
{
    class Program
    {
        static void Main(string[] args)
        {
            // 產生一個含有五個陣列元素的整數陣列
            Array ary1D = Array.CreateInstance(typeof(Int32), 5);
            // 設定陣列初值依序為:1,2,3,4,5
            for (int i = ary1D.GetLowerBound(0); i <= ary1D.GetUpperBound(0); i++)
                ary1D.SetValue(i + 1, i);

            // 顯示陣列初值            
            System.Collections.IEnumerator myEnumerator = ary1D.GetEnumerator();
            int k = 0;
            int cols = ary1D.GetLength(ary1D.Rank - 1);
            while (myEnumerator.MoveNext())
            {
                if (k < cols)
                {
                    k++;
                }
                else
                {
                    Console.WriteLine();
                    k = 1;
                }
                Console.Write(" {0}. ary1D[{1}] = {2} \n", k, k, myEnumerator.Current);
            }
            Console.Read();
        }
    }
}
