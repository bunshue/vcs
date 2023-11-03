using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0806
{
    class Person   //父類別
    {
        private string FirstName { get; set; } = "Mike";
        protected string SurName { get; set; } = "Weston";
        public ushort Height { get; set; }
        //父、子類別方法多載，有一個參數
        public void Display(ushort ht)
        {
            Height = ht;
            WriteLine($"他是 {FirstName} {SurName}," +
               $" 身高 {Height}cm");
        }
    }
}
