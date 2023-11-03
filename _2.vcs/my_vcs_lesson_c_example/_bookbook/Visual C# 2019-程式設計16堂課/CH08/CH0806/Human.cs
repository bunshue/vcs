using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0806
{
    class Human : Person   //子類別
    {
        public string Title { get; set; } = "lawyer";
        public string FirstName { get; set; } = "Joson";
        //父、子類別方法多載
        public void Display() =>
           WriteLine($"{FirstName} {SurName}，是一位{Title}!");
    }
}
