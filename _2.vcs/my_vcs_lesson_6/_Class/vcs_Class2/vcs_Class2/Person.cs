using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class2
{
    class Person3
    {
        public Person3()
        {
            Console.WriteLine("建立一個Person3的物件");
        }

        ~Person3()
        {
            Console.WriteLine("銷毀一個Person3的物件");
        }
    }
}
