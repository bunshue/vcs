using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0608
{
    class Employee
    {
        //自動實作屬性
        public int Salary { get; set; }
        public string Name { get; set; }

        //預設建構函式
        public Employee() { WriteLine("員工資料..."); }

        //定義方法來輸出訊息
        public void showInfo()
        {
            WriteLine($"{Name}, 您的薪資 {Salary:C0}");
        }

        ~Employee() { WriteLine("清除資料..."); }
    }
}
