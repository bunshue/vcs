using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.Collections;

namespace SortedList0
{
    class Program
    {
        static void Main(string[] args)
        {
            SortedList mySL = new SortedList(); //建立myHT為屬於Hashtable實體

            Console.WriteLine("\n1.置入四筆Key&Value鍵值到SortedList串列內.");
            mySL["iPhone5S"] = 22000;  //添加 key&value鍵值對
            mySL["iPhone5C"] = 18000;  //添加 key&value鍵值對
            mySL["iPad2"] = 12500;     //添加 key&value鍵值對
            mySL["iPad Mini"] = 15900;  //添加 key&value鍵值對

            PrintOut1(mySL);
            Console.WriteLine(" 1.目前 SortedList串列內元素總個數 : {0}",
   mySL.Count);
            Console.WriteLine(" ---------------------------------------");

            // 查詢產品單價
            Console.Write(" 2.請輸入Apple產品名稱 : ");
            string item = Console.ReadLine();
            if (!mySL.ContainsKey(item))//判斷SortedList是否含特定鍵
                Console.WriteLine(" 2. {0} 不存在 !!", item);
            else
                Console.WriteLine(" 2.{0}單價 : {1}", item, mySL[item]);
            Console.WriteLine(" --------------------------------------");

            // 移除剛查詢的 Key & Value 鍵值對
            Console.WriteLine(" 3.移除剛查詢鍵值 {0}", item);
            mySL.Remove(item);
            PrintOut2(mySL);
            Console.WriteLine(" 3.目前 SortedList串列內元素總個數 : {0}",
  mySL.Count);
            Console.WriteLine(" ---------------------------------------");

            //移除所有元素
            Console.WriteLine(" 4.移除 SortedList串列內所有元素");
            mySL.Clear();
            Console.WriteLine(" 4.目前 SortedList串列內元素總個數 : {0}",
 mySL.Count);
            Console.WriteLine(" --------------------------------------");
            Console.Read();
        }

        public static void PrintOut1(IEnumerable tempmySL)
        {
            Console.WriteLine("\t對應鍵(Key) \t   對應值(Value)");
            foreach (DictionaryEntry de in tempmySL)
                Console.WriteLine("\t {0}  \t\t{1}", de.Key, de.Value);
        }

        public static void PrintOut2(SortedList myList)
        {
            Console.WriteLine("\t對應鍵(Key) \t   對應值(Value)");
            for (int i = 0; i < myList.Count; i++)
            {
                Console.WriteLine("\t {0}  \t\t{1}", myList.GetKey(i),
 myList.GetByIndex(i));
                // GetKey(i):取得 SortedList 物件中指定之索引處的索引鍵。
                // GetByIndex(i):取得 SortedList 物件中指定之索引處的值。
            }
        }
    }
}
