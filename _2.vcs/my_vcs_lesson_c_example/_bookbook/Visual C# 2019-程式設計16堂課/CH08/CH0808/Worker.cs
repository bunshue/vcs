using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0808
{
    /* 方法以virtual宣告為虛擬，
       繼承的子類別可以實作自己的版本      
    */
    class Worker //父類別
    {
        protected string Name => "員工";

        public void Display()//成員方法
        {
            Write($"{Name} ");
            TotalSalary();
        }

        //定義虛擬方法：採運算式主體定義，子類別可覆寫
        public virtual void TotalSalary() =>
           WriteLine("基本薪 NT$ 22,500");
    }
}
