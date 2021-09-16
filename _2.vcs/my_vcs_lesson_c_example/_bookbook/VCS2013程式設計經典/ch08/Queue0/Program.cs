using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace Queue0
{
    class Program
    {
        public static void PrintOut(IEnumerable myCollction)
        {
            int i = 0;
            foreach (Object obj in myCollction)
                Console.WriteLine("     第{0}個元素 : {1} ", ++i, obj);
        }
        static void Main(string[] args)
        {
            Queue myQueue = new Queue();
            string[] ary = { "Jack", "Ford", "David" };
            //將陣列置入佇列
            foreach (string name in ary)
                myQueue.Enqueue(name);
            Console.WriteLine(" 1.目前佇列的資料 : ");
            PrintOut(myQueue);
            Console.WriteLine(" 1.目前堆疊佇列內資料的個數: {0} ", myQueue.Count);
            Console.WriteLine(" --------------------------------------------");

            // 將 Mary 置入堆疊佇列(最上面)
            myQueue.Enqueue("Mary");
            Console.WriteLine(" 2.目前佇列內的資料 : ");
            PrintOut(myQueue);

            // 取得堆疊最上面的資料
            //myQueue.Peek();
            Console.WriteLine(" 3.查詢佇列最上面資料 : {0} ", myQueue.Peek());
            Console.WriteLine(" 3.目前佇列內的資料 :");
            PrintOut(myQueue);
            Console.WriteLine(" --------------------------------------------");

            // 由堆疊最上面取出資料
            Console.WriteLine(" 4.取出佇列最上面的資料 : {0} ", myQueue.Dequeue());
            Console.WriteLine(" 4.目前佇列內的資料 : ");
            PrintOut(myQueue);
            Console.WriteLine(" --------------------------------------------");

            // 檢查 "David" 是否在佇列中
            if (!myQueue.Contains("David"))
                Console.WriteLine(" 5.佇列內無 David 資料!");
            else
                Console.WriteLine(" 5.佇列內有 David 資料!");

            // 清除佇列
            myQueue.Clear();
            Console.WriteLine("\n 6.清除佇列後資料的個數: {0}", myQueue.Count);
            PrintOut(myQueue);
            Console.WriteLine(" --------------------------------------------");

            Console.Read();
        }
    }
}
