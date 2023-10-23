using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace StructType
{
    class Program
    {
        struct person
        {
            public int age, height;
            public float salary;
            public string skin;
        };
        static void Main(string[] args)
        {
            person person1;
            person1.age = 38;
            person1.height = 176;
            person1.salary = 46800f;
            person1.skin = "黃色";
            WriteLine("年齡：{0}", person1.age);
            WriteLine("身高：{0}", person1.height);
            WriteLine("收入：{0}", person1.salary);
            WriteLine("膚色：{0}", person1.skin);
            Read();
        }
    }
}
