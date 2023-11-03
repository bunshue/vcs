using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0806
{
    class Program
    {
        static void Main(string[] args)
        {
            //產生物件呼叫自己的成員方法
            Person p1 = new Person();
            p1.Display(173);
            Human worker = new Human();
            worker.Display();
            Console.ReadKey();
        }
    }
}
