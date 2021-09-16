using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Dictionary1
{
    class Program
    {
        class Member
        {
            public string Name { get; set; }      // 姓名屬性          
            public bool Select { get; set; }      // 選課屬性
            public int Score { get; set; }        // 成績屬性           
        }
        static void Main(string[] args)
        {
            Dictionary<string, Member> m = new Dictionary<string, Member>();

            m.Add("David", new Member() { Name = "David", Select = true, Score = 70 });
            m.Add("Mary", new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Add("Tom", new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Add("Jack", new Member() { Name = "Jack", Select = true, Score = 95 });

            //泛型陣列操作
            Console.WriteLine("=== 泛型 Dictionary 操作不需強制轉換 .... \n");
            foreach (KeyValuePair<string, Member> item in m)
            {
                Console.WriteLine(" 姓名:{0} \t 選課:{1}  \t  成績:{2}  \n", item.Key, item.Value.Select, item.Value.Score);
            }
            Console.Read();
        }
    }
}
