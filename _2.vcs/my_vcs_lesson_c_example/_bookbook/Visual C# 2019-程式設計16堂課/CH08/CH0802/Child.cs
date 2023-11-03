using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0802
{
    class Child : Father   //繼承了Father類別
    {
        public ushort Height { get; set; }
        public string Firstname { get; set; }
        public Child(string first)
        {
            Firstname = first;
            Height = 172;
        }
        public void Display()
        {
            //屬性Surname為父類別擁有
            WriteLine($"Hi {Firstname}, {Surname}");
        }
    }
}
