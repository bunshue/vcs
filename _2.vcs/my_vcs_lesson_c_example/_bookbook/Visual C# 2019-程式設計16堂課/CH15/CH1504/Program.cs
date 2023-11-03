using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH1504
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                string path = @"D:\C#Lab\Sample\Icon\";
                //取得資料夾最後一次被存取的時間
                DateTime dt = Directory.GetLastWriteTime(path);
                //如果資料夾不存在就建立資料夾
                if (!Directory.Exists(path))
                {
                    Directory.CreateDirectory(path);
                }
                else
                {
                    WriteLine($"資料夾建立的時間：\n{dt}");
                }
                //更新時間
                Directory.SetLastWriteTime(path, DateTime.Now);
                dt = Directory.GetLastWriteTime(path);
                WriteLine($"\n最後存取時間：\n{dt}");
            }
            catch (Exception e)
            {
                WriteLine($"無法建立:{e.ToString()}");
            }
            ReadKey();
        }
    }
}
