using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using System.IO;   // 引用System.IO命名空間

namespace ConsoleDirectoryInfo1
{
    class Program
    {
        static void Main(string[] args)      
        {  
            // 建立DirectoryInfo類別的dir物件，可用來操作資料夾目錄
            DirectoryInfo dir = new DirectoryInfo("d:\\CSharp");
            if (dir.Exists)
            {	// 判斷目錄是否存在
                Console.WriteLine("d:\\CSharp路徑存在, 不建立目錄");
            }
            else
            {
                Console.WriteLine("d:\\CSharp路徑不存在，建立目錄");
                dir.Create();	// 建立目錄
                dir.Refresh();	// 重新整理目錄
            }
            Console.WriteLine("{0}檔案資訊如下：", dir.FullName);
            Console.WriteLine("建立時間：{0}", dir.CreationTime);
            Console.WriteLine("存取時間：{0}", dir.LastAccessTime);
            Console.WriteLine("資料夾名稱：{0}", dir.Name);
            Console.WriteLine("根目錄：{0}", dir.Parent);
            Console.WriteLine();
            Console.Write("是否刪除d:\\CSharp資料夾   1.刪除  2.不刪除->");
            if (Console.ReadLine() == "1")
            {
                try
                {
                    dir.Delete();	       // 刪除檔案
                    Console.WriteLine("刪除成功");
                }
                catch (Exception ex)   // 刪除檔案失敗會產生例外
                {
                    Console.WriteLine("刪除失敗");
                    Console.WriteLine(ex.Message);  // 顯示例外訊息
                }
            }
            Console.Read();
        }
    }
}
