using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace CH0511
{
    class Program
    {
        static void Main(string[] args)
        {
            //宣告鋸齒陣列為隱含型別
            var subject = new[]
            {
            new[] {"Tomas", "國文", "英文", "計算機概論" },
            new[] {"Mary", "數學", "資料庫"},
            new[] {"Peter", "數學","應用文", "多媒體", "程式設計"}
         };

            //外層for廻圈，取屬性subject.Length為列數
            for (var outer = 0; outer < subject.Length; outer++)
            {
                //內層for廻圈，取屬性subject[outer].Length為欄數
                for (var inner = 0;
                      inner < subject[outer].Length; inner++)
                {
                    //-6表示欄寬為6，負號為靠左對齊
                    Write($"{subject[outer][inner],-6}");
                }
                WriteLine();//
            }

            ReadKey();//螢幕暫停
        }
    }
}
