using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

 namespace IBM
 {
    namespace Taiwan            // 子命名空間 Taiwan
    {
        class Notebook
        {
        }
    }
    namespace Japan             // 子命名空間 Japan
    {
        class Notebook
        {
        }
    }
}

 namespace Apple
 {
     class Notebook
     {
     }
 }

namespace SubNamespace
{
    class Program
    {
        static void Main(string[] args)
        {
            // 使用IBM的Taiwan子命名空間下的Notebook類別建立A物件
             IBM.Taiwan.Notebook A = new IBM.Taiwan.Notebook();
             // 使用IBM的Japan子命名空間下的Notebook類別建立A物件
             IBM.Japan.Notebook B = new IBM.Japan.Notebook();
             // 使用Apple命名空間下的Notebook類別建立C物件
             Apple.Notebook C = new Apple.Notebook();
         }
    }
}
