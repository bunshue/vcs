using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0804
{
    class Program
    {
        static void Main(string[] args)
        {
            //初始化onePrn物件，並傳入初始值
            Person p1 = new Person("Mike Weston", 35500);
            //實體化衍生類別，加入參數值
            Worker wk = new Worker("Jennifer Mason", 23500);
            wk.hireTime();

            Console.ReadKey();
        }
    }
}
