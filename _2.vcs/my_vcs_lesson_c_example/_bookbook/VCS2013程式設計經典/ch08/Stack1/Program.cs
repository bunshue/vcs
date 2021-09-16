using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections;

namespace Stack1
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
            Stack m = new Stack();   // 非泛型           

            m.Push(new Member() { Name = "David", Select = true, Score = 70 });
            m.Push(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Push(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Push(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine("=== 非泛型 Stack 操作需強制轉換 .... \n");
            while(m.Count >0)
            {
                Console.WriteLine ("{0} ", (Member )m.Pop ());
            }
            Console.Read();
        }
    }
}
