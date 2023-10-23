using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Nested
{
    class Program
    {
        struct person
        {
            public int age;
            public float salary;
            public string skin;
        };
        struct female
        {
            public person mary;
            public string hair;
        };
        static void Main(string[] args)
        {
            female female1;
            female1.mary.age = 50;
            female1.mary.salary = 23000;
            female1.mary.skin = "黃色";
            female1.hair = "直髮";
            WriteLine("年齡：{0}", female1.mary.age);
            WriteLine("收入：{0}", female1.mary.salary);
            WriteLine("膚色：{0}", female1.mary.skin);
            WriteLine("髮型：{0}", female1.hair);
            Read();
        }
    }
}
