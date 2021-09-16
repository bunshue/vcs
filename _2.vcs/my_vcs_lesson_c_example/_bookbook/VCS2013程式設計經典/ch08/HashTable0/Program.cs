using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
namespace HashTable0
{
    class Program
    {
        static void Main(string[] args)
        {
             Hashtable myHT = new Hashtable(); // 建立myHT為一個屬於Hashtable的實體

            Console.WriteLine("\n 1.置入四筆 Key & Value 鍵值到 HashTable 內.");
            myHT.Add("iPhone5S", 22000);  //添加 key&value鍵值對
            myHT.Add("iPhone5C", 18000);  //添加 key&value鍵值對
            myHT.Add("iPad2", 12500);     //添加 key&value鍵值對
            myHT.Add("iPadMini", 15900);  //添加 key&value鍵值對

            //PrintKeysAndValues(mySL);
            PrintOut(myHT);
            Console.WriteLine(" 1.目前 HashTable 內元素總個數 : {0}", myHT.Count);
            Console.WriteLine(" ------------------------------------------");

            // 查詢產品單價
            Console.Write(" 2.請輸入 Apple 產品名稱 : ");
            string item = Console.ReadLine();
            if (!myHT.ContainsKey(item))      // 判斷HashTable是否含特定鍵,傳回值true或false
                Console.WriteLine(" 2. {0} 不存在 !!", item);
            else
                Console.WriteLine(" 2.{0}單價 : {1}", item, myHT[item]);
            Console.WriteLine(" ------------------------------------------");

            // 移除剛查詢的 Key & Value 鍵值對
            Console.WriteLine(" 3.移除剛查詢鍵值 {0}", item);
            myHT.Remove(item);
            PrintOut(myHT);
            Console.WriteLine(" 3.目前 HashTable 內元素總個數 : {0}", myHT.Count);
            Console.WriteLine(" ------------------------------------------");

            //移除所有元素
            Console.WriteLine(" 4.移除 HashTable 內所有元素");
            myHT.Clear();
            Console.WriteLine(" 4.目前 HashTable 內元素總個數 : {0}", myHT.Count);
            Console.WriteLine(" ------------------------------------------");
            Console.Read();
        }
        public static void PrintOut(IEnumerable tmyHT)
        {
            Console.WriteLine("   品名 (Key)  價格 (Value)");
            foreach (DictionaryEntry de in tmyHT)
                Console.WriteLine("    {0}\t {1}", de.Key, de.Value);
       }
    }
}
        
