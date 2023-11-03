using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0808
{
    /* TotalSalary()方法      
       不指定 override、new 關鍵字，編譯器會發出警告
       且衍生類別中的方法會隱藏基底類別中的方法
    */
    class Hireling : Worker
    {
        private int Salary; //欄位--取得計算的月薪
                            //隱藏父類別的屬性，以子類別的屬性值為主
        protected new string Name => "Claire";

        //覆寫基底類別TotalSalary()方法，計算時薪
        public override void TotalSalary()
        {
            //基本薪 money, 津貼 subsidy
            int money = 22_500, subsidy = 7_500;
            Salary = money + subsidy;
            WriteLine($"正式員工{Name,8} 薪水 {Salary:C0}");
        }
    }
}
