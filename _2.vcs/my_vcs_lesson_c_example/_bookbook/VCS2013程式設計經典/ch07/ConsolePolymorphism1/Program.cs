using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsolePolymorphism1
{
    class Employee  // 定義Employee員工類別
    {
        // _salary宣告為保護層級,此欄位可以在子類別中使用
        protected int _salary;
        // 宣告Salary薪水屬性為virtual，因此該屬性在子類別可被覆寫
        public virtual int Salary
        {
            get
            {
                return _salary;
            }
            set
            {
                if ((value >= 20000) && (value <= 40000))
                {
                    _salary = value;
                }
                else
                {
                    _salary = 20000;
                }
            }
        }
    }
    class Manager : Employee  // Manager經理類別繼承自Employee員工類別
    {
        // 增加Bounds獎金屬性
        public int Bonus { get; set; }
        // Manager經理子類別覆寫Employee員工父類別Salary屬性
        public override int Salary
        {
            get
            {
                return _salary;   // 使用父類別的_salary
            }
            set
            {
                if ((value >= 30000) && (value <= 60000))
                {
                    _salary = value;
                }
                else
                {
                    _salary = 30000;
                }
            }
        }
        public void ShowTotal()
        {
            Console.WriteLine("\n 實領的薪資：{0}元", (Bonus + Salary).ToString("0,0"));
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
           Manager peter = new Manager();
           peter.Salary = 70000;
           Console.WriteLine("\n Peter 經理的薪資 : {0}元", peter.Salary.ToString("0,0"));
           peter.Bonus = 30000;
           Console.WriteLine("\n Peter 經理的獎金 : {0}元", peter.Bonus.ToString("0,0"));
           peter.ShowTotal();
           Console.Read();
        }
    }
}
