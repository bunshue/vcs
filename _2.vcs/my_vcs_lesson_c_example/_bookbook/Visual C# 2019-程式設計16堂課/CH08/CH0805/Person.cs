using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0805
{
    class Person   //父類別
    {
        private string FirstName { get; set; } = "Mike";
        protected string SurName { get; set; } = "Weston";
        public void Display() =>
           WriteLine($"他是 {FirstName} {SurName}...");
    }
}
