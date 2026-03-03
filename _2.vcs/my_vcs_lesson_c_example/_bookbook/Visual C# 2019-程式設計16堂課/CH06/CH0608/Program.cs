using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0608
{
    class Program
    {
        static void Main(string[] args)
        {
            //物件初始設定式
            Employee ep1 = new Employee { Name = "Mary", Salary = 28600 };
            ep1.showInfo();

            Employee ep2 = new Employee { Name = "Tomas", Salary = 29700 };
            ep2.showInfo();

            Console.ReadKey();
        }
    }

    class Employee
    {
        //自動實作屬性
        public int Salary { get; set; }
        public string Name { get; set; }

        //預設建構函式
        public Employee() { Console.WriteLine("員工資料..."); }

        //定義方法來輸出訊息
        public void showInfo()
        {
            Console.WriteLine("{Name}, 您的薪資 {Salary:C0}");
        }

        ~Employee() { Console.WriteLine("清除資料..."); }
    }
}
