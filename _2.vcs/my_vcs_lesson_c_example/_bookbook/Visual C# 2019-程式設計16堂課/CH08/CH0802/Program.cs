using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0802
{
    class Program
    {
        static void Main(string[] args)
        {
            //實體化子類別
            Child son = new Child("Kevin");
            son.Display();
            Console.ReadKey();
        }
    }
}
