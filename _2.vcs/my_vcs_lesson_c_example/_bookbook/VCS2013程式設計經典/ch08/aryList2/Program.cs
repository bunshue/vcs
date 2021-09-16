using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace aryList2
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayList myAryLst = new ArrayList { "Jack", "Ford", "Bob", "David" };

            // 顯示ArrayList串列的初值內容(排序前）：
            Console.WriteLine(" 1. 顯示串列初值設定內容(排序前）:");
            PrintOut(myAryLst);
            Console.WriteLine(" ---------------------------------");

            // 顯示ArrayList串列排序後內容
            myAryLst.Sort();

            Console.WriteLine(" 2.  myAryLst.Sort()由小而大做遞增排序 :");
            PrintOut(myAryLst);
            Console.WriteLine(" ----------------------------------");

            // 顯示ArrayList串列排序後內容
            myAryLst.Reverse();
            Console.WriteLine(" 3. myAryLst.Reverse()由大而小做遞減排序 :");
            PrintOut(myAryLst);
            Console.WriteLine(" ----------------------------------");

            Console.Read();
        }
        public static void PrintOut(IEnumerable myAryLst)
        {
            int i = 0;
            foreach (Object obj in myAryLst)
                Console.WriteLine("\t第{0}個元素 : {1} ", ++i, obj);         
        }

    }
}
