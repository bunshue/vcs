using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleInheritException
{
    class Program
    {
    // 定義 SalaryException 例外繼承自 Exception 例外類別
    class SalaryException : Exception
    {
        public override String ToString()  // 覆寫ToString()方法
        {
            return "發生Salary例外類別";
        }
        // 覆寫 Message 屬性, 該屬性是唯讀屬性
        public override String Message  
        {
            get
            {
                return "薪水不能設定負數或零";
            }
        }
        public void ShowMsg()	 // 新增  ShowMsg() 方法
        {
            Console.WriteLine("沒良心的老闆，設定員工薪水請小心...^_|||");
        }
    }

    class Empolyee			// 定義  Empolyee 員工類別
    {
        private string _name;	// 私有  _name 欄位
        private int _salary;	// 私有  _salary 欄位
        //  Empolyee 員工類別的建構式，用來設定員工姓名
        public Empolyee(string name)  
        {
            _name = name;
        }
        public int Salary      	// 薪水屬性
        {
            get
            {
                return _salary;
            }
            set
            {
                // 如果薪水小於等於0，則產生 SalaryException 例外類別物件
                if (value <= 0)
                {
                    Console.WriteLine("員工 {0} 設定薪水 {1} 失敗",
 						_name, value);
                    // 產生 SalaryException 例外類別物件
                    throw new SalaryException(); 
                }
                else
                {
                    _salary = value;
                }
            }
        }
        public void ShowSalary()
        {
            Console.WriteLine("員工 {0} 的薪水 {1}", _name, Salary);
        }
    }

        static void Main(string[] args)
        {
            try
            {
                Empolyee tom = new Empolyee("湯姆");
                tom.Salary = 50000;
                tom.ShowSalary();
                Console.WriteLine("=================================");
                Empolyee peter = new Empolyee("彼得");
              // 設定Peter物件的薪水為負數，因此會產生SalaryException例外類別
                peter.Salary = -10000;
                peter.ShowSalary();
            }
            catch (SalaryException ex)  // 補捉 SalaryException 例外
            {
                // 呼叫 SalaryException 的 ToString() 方法
                Console.WriteLine(ex.ToString());
                // 呼叫 SalaryException 的 Message 屬性
                Console.WriteLine(ex.Message);
                // 呼叫 SalaryException 的ShowMsg()方法
                ex.ShowMsg();	  
            }
            Console.Read();
        }
    }
}
