using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace Stack0
{
    class Program
    {
        public static void PrintOut(IEnumerable myCollction)
        {
            int i = 0;
            foreach (Object obj in myCollction)
                Console.WriteLine("   第{0}個元素 : {1} ", ++i, obj);
        }
        static void Main(string[] args)
        {
            Stack myStack = new Stack();
            string[] ary = { "Jack", "Ford", "Bob", "David" };
            //將陣列置入堆疊
            foreach (string name in ary)
                myStack.Push(name);
            Console.WriteLine(" 1.目前堆疊內所有元素 : ");
            PrintOut(myStack);
            Console.WriteLine(" 1.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 將 Mary 置入堆疊(最上面)
            Console.WriteLine(" 2.將 Mary 置入堆疊");
            myStack.Push("Mary");
            Console.WriteLine(" 2.目前堆疊內所有元素 : ");
            PrintOut(myStack);
            Console.WriteLine(" 2.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 取得堆疊最上面的資料           
            Console.WriteLine(" 3.查詢堆疊最上面資料 : {0} ", myStack.Peek());
            Console.WriteLine(" 3.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 由堆疊最上面取出資料
            Console.WriteLine(" 4.取出堆疊最上面的資料 : {0} ", myStack.Pop());
            Console.WriteLine(" 4.目前堆疊內所有元素 : ");
            PrintOut(myStack);
            Console.WriteLine(" 4.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 檢查堆疊內是否有 "David" 這個資料
            Console.WriteLine(" 5.檢查堆疊內是否有 David 這個資料 ? ");
            if (!myStack.Contains("David"))
                Console.WriteLine(" 5.堆疊內無此資料!");
            else
                Console.WriteLine(" 5.堆疊內有此資料!");
            Console.WriteLine(" ----------------------------");

            // 清除堆疊內所有元素           
            Console.WriteLine(" 6.清除堆疊內的所有資料");
            Console.WriteLine(" 6.堆疊內資料的個數: {0}", myStack.Count);
            PrintOut(myStack);
            Console.WriteLine(" ----------------------------");

            Console.Read();
        }
    }
}
