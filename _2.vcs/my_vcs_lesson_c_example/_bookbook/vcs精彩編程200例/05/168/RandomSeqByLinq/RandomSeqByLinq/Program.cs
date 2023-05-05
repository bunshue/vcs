using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace RandomSeqByLinq
{
    class Program
    {
        static void Main(string[] args)
        {
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo.mdf";
            //string filename = @"C:\_git\vcs\_1.data\______test_files1\_vcs200_db\db_TomeTwo_log.ldf";   another
            //像是沒有用到資料庫

            Random rand = new Random();//创建一个随机数生成器
            Console.WriteLine("請輸入一個整數");
            try
            {
                int intCount = Convert.ToInt32(Console.ReadLine());//输入要生成随机数的组数
                //生成一个包含指定个数的重复元素值的序列，
                //由于Linq的延迟性，所以此时并不产生随机数，而是在枚举randomSeq的时候生成随机数
                IEnumerable<int> randomSeq = Enumerable.Repeat<int>(1, intCount).Select(i => rand.Next());
                Console.WriteLine("將產生" + intCount.ToString() + "個隨機數:");
                foreach (int item in randomSeq)//通过枚举序列来生成随机数，
                {
                    Console.WriteLine(item.ToString());//输出若干组随机数
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
            }
            Console.Read();
        }
    }
}
