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
            Employee ep1 = new Employee
            { Name = "Mary", Salary = 28_600 };
            ep1.showInfo();

            Employee ep2 = new Employee
            { Name = "Tomas", Salary = 29_700 };
            ep2.showInfo();

            Console.ReadKey();
        }
    }
}
