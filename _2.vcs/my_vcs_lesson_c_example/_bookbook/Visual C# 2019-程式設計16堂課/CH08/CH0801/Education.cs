using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0801
{
    class Education
    {
        static void Main(string[] args)
        {
            //實體化子類別物件並呼叫父類別的方法
            Subjects son = new Subjects();
            son.ShowMsg();
            son.Display(20);   //子類別的成員方法

            Console.ReadKey();
        }
    }
}
