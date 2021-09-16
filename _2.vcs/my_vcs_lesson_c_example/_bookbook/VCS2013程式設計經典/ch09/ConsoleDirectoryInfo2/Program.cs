using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.IO; // 引用System.IO命名空間

namespace ConsoleDirectoryInfo2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("請輸入路徑->");
            string fpath = Console.ReadLine();
            DirectoryInfo dir = new DirectoryInfo(fpath);
            if (!dir.Exists)	//判斷路徑是否不存在
            {
                Console.WriteLine("路徑不存在");
                Console.Read();
                return;
            }
            Console.WriteLine("{0}資料夾下的子資料夾如下：", dir.FullName);
            DirectoryInfo[] subdir = dir.GetDirectories();
            foreach (DirectoryInfo r in subdir)
            {
                Console.WriteLine("完整路徑：{0}  \t建立時間{1}", r.FullName, r.CreationTime);
            }
            Console.Read();
        }
    }
}
