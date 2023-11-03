using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0805
{
    class Human : Person   //子類別
    {
        public string Title { get; set; } = "lawyer";
        public string FirstName { get; set; } = "Joson";
        //與父類別同名稱，修飾詞new會隱藏父類別所宣告的方法
        new public void Display() =>
           WriteLine($"{FirstName}，是一位{Title}!");
    }
}
