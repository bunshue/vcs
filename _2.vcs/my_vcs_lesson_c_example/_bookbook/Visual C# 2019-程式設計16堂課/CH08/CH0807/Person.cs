using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0807
{
    class Person   //父類別
    {
        public string Name { get; set; }
        protected int Salary { get; set; }
        protected int Level { get; set; }

        //建構函式-傳入名稱
        public Person(string title)
        {
            Name = title;
        }

        //成員方法-定義薪資額度
        public virtual int Display(int grade)
        {
            if (grade == 1)
                Salary = 28_500;
            else if (grade == 2)
                Salary = 32_500;
            else if (grade == 3)
                Salary = 35_200;

            return Salary;
        }
    }
}
