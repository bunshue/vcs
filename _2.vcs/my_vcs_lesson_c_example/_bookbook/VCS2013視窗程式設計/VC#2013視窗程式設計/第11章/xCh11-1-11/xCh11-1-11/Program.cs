using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace xCh11_1_11
{
    class Program
    {
        static void Main(string[] args)
        {
            // Step 01. 取得資料來源
            int[] numbers = new int[7] { 0, 1, 2, 3, 4, 5, 6 };

            // Step 02. 建立查詢，
            // 其中nbrQuery是「查詢變數」，具有IEnumerable<int>資料型別
            var nbrQuery =
                from nbr in numbers
                where (nbr % 2) == 0
                select nbr;

            // Step 03. 執行查詢
            foreach (int x in nbrQuery)
            {
                Console.Write("{0,1} ", x);
            }
        }
    }
}


