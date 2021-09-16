using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsolePolymorphism2
{
    class Employee // 定義Employee員工類別
    {
        //_salary宣告為Protected保護層級,此欄位可以在子類別中使用
        protected int _salary;
        public virtual int Salary
        {
            get
            {
                return _salary;
            }
            set
            {
                if ((value >= 20000) & (value <= 40000))
                {
                    _salary = value;
                }
                else
                {
                    _salary = 20000;
                }
            }
        }
        public virtual void ShowTotal()	//ShowTotal方法允許被覆寫
        {
            Console.WriteLine("\n 底薪：{0}元", Salary.ToString ("0,0"));
        }
    }
    // 定義Manager經理子類別繼承自Employee員工父類別
    class Manager : Employee 
    {

        public int Bonus { get; set; }
        public override int Salary
        {
            get
            {
                return _salary; //使用父類別的_salary
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
        public override void ShowTotal()//覆寫Employee的ShowTotal方法
        {
            base.ShowTotal();	//呼叫父類別Employee的ShowTotal方法
            Console.WriteLine("\n 薪水 + 獎金共：{0}元", (Bonus+Salary).ToString ("0,0"));
        }
    }
    class Program
    {
        static void Main(string[] args)
        {
            Employee tom = new Employee();
            tom.Salary = 40000;
            Console.WriteLine("\n Tom 員工薪資 : {0}元", tom.Salary.ToString ("0,0"));
            tom.ShowTotal();
            Console.WriteLine("======================");
            //Console.WriteLine();
            Manager peter = new Manager();
            peter.Salary = 70000;
            Console.WriteLine("\n Peter 經理薪資 : {0}元", peter.Salary.ToString("0,0"));
            peter.Bonus = 30000;
            Console.WriteLine("\n Peter 經理獎金 : {0}元", peter.Bonus.ToString("0,0"));
            peter.ShowTotal();
            Console.Read();
        }
    }
}
