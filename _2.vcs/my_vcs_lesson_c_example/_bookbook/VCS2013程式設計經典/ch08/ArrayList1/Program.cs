using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace ArrayList1
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
                return string.Format ("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n " , Name,Select? "是":"否",Score.ToString ());
            }
        }

        static void Main(string[] args)
        {
            ArrayList m = new ArrayList();   // 非泛型

            //SortedList<string, Member> m = new SortedList<string, Member>();

            m.Add(new Member() { Name = "David", Select = true, Score = 70 });
            m.Add(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Add(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Add(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine("=== 非泛型陣列操作需強制轉換 .... \n");
            foreach (var item in m)
            {
                if (item is Member)
                    Console.WriteLine("{0} ", item.ToString());
                else
                    Console.WriteLine("{0} ", (string)item);          
            }
            Console.Read();
        }
    }
}
