using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;


namespace aryList1
{
    class Program
    {
        static void Main(string[] args)
        {

            ArrayList myAryLst = new ArrayList { "Jack", 20, true }; // 元素為不同資料型別  
            Console.WriteLine("1.設定 AryLst串列內初值 :");
            PrintOut(myAryLst);
            Console.WriteLine("---------------------------------------");

            //插入串列的最後面
            Console.WriteLine("2.插入 \"大學\" 到串列的最後面 :");
            myAryLst.Add("大學");
            PrintOut(myAryLst);
            Console.WriteLine("---------------------------------------");

            //多筆資料採陣列方式插入到串列最後面
            Console.WriteLine("3.插入\"台北\" , \"101\" 兩個元素到串列的最後面 :");
            myAryLst.AddRange(new string[] { "台北", "101" });
            PrintOut(myAryLst);
            Console.WriteLine("---------------------------------------");

            //插入到串列的第2個元素後面
            Console.WriteLine("4.插入\"Wu\" 到串列的第2個元素後面");
            myAryLst.Insert(1, "Wu");
            PrintOut(myAryLst);
            Console.WriteLine("---------------------------------------");

            //刪除串列中 "Wu" 佇個元素
            Console.WriteLine("5.移除串列中元素為 Wu");
            myAryLst.Remove("Wu");
            PrintOut(myAryLst);
            Console.WriteLine("---------------------------------------");

            //移除串列中第3個元素
            Console.WriteLine("6.移除串列中第3個元素");
            myAryLst.RemoveAt(2);
            PrintOut(myAryLst);
            Console.WriteLine("---------------------------------------");

            // 移除串列中從第3個元素開始共兩個元素
            Console.WriteLine("7.移除串列中從第3個元素開始共兩個元素");
            myAryLst.RemoveRange(2, 2);
            PrintOut(myAryLst);
            Console.WriteLine("---------------------------------------");

            // 移除串列中所有元素
            Console.WriteLine("8.移除串列中所有元素");
            myAryLst.Clear();
            Console.WriteLine("  目前 AryList 串列元素總個數 : ", myAryLst.Count);
            Console.WriteLine("---------------------------------------");

            Console.Read();
        }

        // "走訪串列所有元素
        public static void PrintOut(IEnumerable tAryLst)
        { // 公開能逐一查看非泛型集合內容的一次的列舉直
            int i = 0;
            Console.WriteLine("  目前 AryLst串列內所有元素 : ");
            foreach (Object obj in tAryLst)
                Console.WriteLine("    第{0}個元素 : {1} ", ++i, obj);
        }
    }
}
