using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0607
{
    class Employee
    {
        //自動實做屬性
        public float Salary { get; set; }
        public string Name { get; set; }

        //以建構函式來初始化屬性值
        public Employee(string title, float pay)
        {
            WriteLine("計算員工薪資！");
            //將接收的值指定給屬性
            Salary = pay;
            Name = title;
        }

        //定義成員方法--判別扣除的稅額
        public void Taxmoney()
        {
            float tax = 0.0F;//稅率

            Write($"{Name}, ");

            //多重條件-依據稅率
            if (Salary >= 28_000)
            {
                tax = Salary * 0.05F;
                Salary -= tax;
            }
            else if (Salary >= 30_000)
            {
                tax *= Salary * 0.08F;
                Salary -= tax;
            }
            else if (Salary >= 35_000)
            {
                tax *= Salary * 0.10F;
                Salary -= tax;
            }
            else
            {
                tax *= 0.12F;
                Salary -= tax;
            }
            WriteLine($"扣除稅額 {tax:N0}，月薪 {Salary:N0}");
        }
    }
}