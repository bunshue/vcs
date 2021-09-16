using System;
using System.Collections.Generic;  // List類別置於此命名空間中
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleGenerics1
{
    //定義Member類別有Id和Name屬性
    class Member
    {
        public string Id { get; set; }
        public string Name { get; set; }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //建立listInt串列物件可存放整數資料
            List<int> listInt = new List<int>();
            listInt.Add(123);       // 存放123
            listInt.Add(789);       // 存放789
            listInt.Insert( 1,456);// 在索引1放入456
            Console.WriteLine("=int整數串列=");
            // 將listInt串列中的元素印出
            for (int i=0; i <listInt.Count; i++)
            {
                Console.WriteLine("  listInt[{0}]={1}" ,  i, listInt[i]);
            }
            Console.WriteLine();

            // 建立listMember串列物件可存放Member物件資料
            List<Member> listMember =new List<Member>();
            // 存放三筆Member物件
            listMember.Add(new Member() { Id = "M01", Name = "小明" });
            listMember.Add(new Member() { Id = "M02", Name = "小華" });
            listMember.Add(new Member() { Id = "M03", Name = "阿龍" });
            // 刪除索引1位置的Member物件
            listMember.RemoveAt (1);
            Console.WriteLine("=Member會員串列=");
            // 將listMember串列中的元素印出
            for (int i = 0; i < listMember.Count; i++)
            {
                Console.WriteLine("  listMember[{0}]=>帳號：{1}, 姓名：{2}", i, listMember[i].Id, listMember[i].Name);
            }
            Console.Read();
        }
    }
}
