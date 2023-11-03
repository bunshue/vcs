using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;

namespace CH0803
{
    class Mother
    {
        private string Firstname { get; set; }
        protected string Surname
        { get { return "Purefoy"; } }
        public ushort Height { get; set; }
        public string Hair { get; set; } = "棕色髮";

        //建構函式
        public Mother()
        {
            Firstname = "Claire";
            Height = 165;
        }

        //成員方法-運算式主體定義
        public void Display() => WriteLine(
           $"{Firstname} {Surname}\n" +
           $"{Hair}, 身高 {Height}cm");
    }
}
