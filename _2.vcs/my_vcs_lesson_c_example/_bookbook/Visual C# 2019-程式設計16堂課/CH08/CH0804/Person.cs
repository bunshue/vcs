using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0804
{
    class Person   //父類別
    {
        //Name, baseSalary 自動實做屬性
        protected int baseSalary { get; set; }
        protected string Name { get; set; }

        //定義基底建構函式：傳入名字和薪資
        public Person(string title, int wage)
        {
            Name = title;
            baseSalary = wage;
            WriteLine($"{Name}，薪水 {baseSalary:C0}");
        }
    }
}
