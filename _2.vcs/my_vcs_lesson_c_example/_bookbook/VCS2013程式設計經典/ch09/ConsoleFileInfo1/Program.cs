using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.IO; // 引用System.IO命名空間

namespace ConsoleFileInfo1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("請輸入路徑->");
            string fpath = Console.ReadLine();
            DirectoryInfo dir = new DirectoryInfo(fpath);
            if (!dir.Exists)  //判斷資料夾路徑是否不存在
            {
                Console.WriteLine("路徑不存在");
                Console.Read();
                return;
            }
            Console.WriteLine("{0}資料夾下的檔案資訊如下：", dir.FullName);
            //傳回FileInfo物件陣列，並指定給f陣列
            FileInfo[] f = dir.GetFiles();
            foreach (FileInfo r in f)
            {
                Console.WriteLine("完整路徑：{0})", r.FullName);
                Console.WriteLine("寫入時間：{0}", r.LastWriteTime);
                Console.WriteLine("檔案大小：{0} Bytes", r.Length);
                Console.WriteLine();
            }
            Console.Read();
        }
    }
}
