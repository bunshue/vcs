using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;
//using System.Collections;  泛型不用引入

namespace SortedList2
{
    class Program
    {
        class Member
        {
            public string Name { get; set; }      // 姓名屬性          
            public bool Select { get; set; }      // 選課屬性
            public int Score { get; set; }        // 成績屬性

            public override string ToString()    // 覆寫覆類別 ToString()方法
            {
                return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
            }
        }

        static void Main(string[] args)
        {
            SortedList<string, Member> m = new SortedList<string, Member>();

            m.Add("David", new Member() { Name = "David", Select = true, Score = 70 });
            m.Add("Mary", new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Add("Tom", new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Add("Jack", new Member() { Name = "Jack", Select = true, Score = 95 });

            //泛型陣列操作
            Console.WriteLine("=== 泛型 SortedList 操作不需強制轉換 .... \n");
            foreach (KeyValuePair<string, Member> item in m)
            {
                // Console.WriteLine (" 姓名:{0} \t 選課:{1}  \t  成績:{2}  \n" ,item.Key, item.Value.Select, item.Value.Score );
                Console.WriteLine(item.Value.ToString());
            }
            Console.Read();
        }
    }
}