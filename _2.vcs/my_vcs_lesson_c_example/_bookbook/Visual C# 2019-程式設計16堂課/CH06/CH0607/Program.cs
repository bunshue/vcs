using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0607
{
    class Program
    {
        static void Main(string[] args)
        {
            string na = "david";
            float payment = 12345f;

            //建立一個含有參數的Student物件
            Employee ep1 = new Employee(na, payment);
            ep1.Taxmoney();//呼叫方法成員
            Console.ReadKey();
        }
    }

    class Employee
    {
        //自動實做屬性
        public float Salary { get; set; }
        public string Name { get; set; }

        //以建構函式來初始化屬性值
        public Employee(string title, float pay)
        {
            Console.WriteLine("計算員工薪資！");
            //將接收的值指定給屬性
            Salary = pay;
            Name = title;
        }

        //定義成員方法--判別扣除的稅額
        public void Taxmoney()
        {
            float tax = 0.0F;//稅率

            Console.Write("{Name}, ");

            //多重條件-依據稅率
            if (Salary >= 28000)
            {
                tax = Salary * 0.05F;
                Salary -= tax;
            }
            else if (Salary >= 30000)
            {
                tax *= Salary * 0.08F;
                Salary -= tax;
            }
            else if (Salary >= 35000)
            {
                tax *= Salary * 0.10F;
                Salary -= tax;
            }
            else
            {
                tax *= 0.12F;
                Salary -= tax;
            }
            Console.WriteLine("扣除稅額 {tax:N0}，月薪 {Salary:N0}");
        }
    }
}

