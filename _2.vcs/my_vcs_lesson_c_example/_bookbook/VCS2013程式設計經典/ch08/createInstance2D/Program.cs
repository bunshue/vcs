using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Collections; // 若此行有寫入，System.Collectios.可省略 

namespace createInstance2D
{
    class Program
    {
        static void Main(string[] args)
        {
            // 產生 2x3 字串陣列並設定初值
            Array ary2D = Array.CreateInstance(typeof(String), 2, 3);

            for (int i = ary2D.GetLowerBound(0); i <= ary2D.GetUpperBound(0); i++)
                for (int j = ary2D.GetLowerBound(1); j <= ary2D.GetUpperBound(1); j++)
                    ary2D.SetValue("註標 " + i + "," + j, i, j);

            // 顯示陣列的資料
            Console.WriteLine(" 二維陣列包含下列資料 :");

            System.Collections.IEnumerator myEnumerator = ary2D.GetEnumerator();

            int r = 0;  // row 列
            int c = 0;  // col 欄

            int cols = ary2D.GetLength(ary2D.Rank - 1);

            while (myEnumerator.MoveNext() && (myEnumerator.Current != null))
            {
                if (r > cols || c >= 3)
                {
                    Console.WriteLine();
                    r++; c = 0;
                }
                Console.Write(" ary2D[{0},{1}]={2} , ", r, c++, myEnumerator.Current);
            }
            Console.Read();
        }
    }
}
