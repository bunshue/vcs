using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0808
{
    /* TotalSalary()方法
       使用 new 修飾詞隱藏基底類別中的虛擬方法
       衍生類別使用override關鍵字覆寫基底虛擬方法 */
    class PartTime : Worker
    {
        private int prtSalary;//儲存薪資
        public new string Name => "Michael";

        //定義自己的方法 -- 計算月薪，隱藏父類別的虛擬方法
        public new void TotalSalary()
        {
            int hourMoney = 227;
            prtSalary = hourMoney * 5 * 20;
            Console.WriteLine(
               $"兼職員工 {Name,7} 薪水 {prtSalary:C0}");
        }
    }
}
