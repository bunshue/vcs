using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH1505
{
    class Program
    {
        static void Main(string[] args)
        {
            //儲存要回傳的檔案路徑和檔案類型
            string path2 = @"D:\C#Lab\Sample";
            string fnShow = "檔案清單---<*.jpg>\n\n";

            //判斷資料夾是否存在，若是不存在會擲出例外情形
            try
            {    //取得檔案路徑訊息
                DirectoryInfo currentDir =
                   new DirectoryInfo(path2);
                //從指定路徑傳回指定的檔案類型
                FileInfo[] listFile = currentDir.GetFiles("*.jpg");
                //設定檔案的標題
                string sign = new string('-', 37);
                string fnName = "檔名", fnLength = "檔案長度";
                string fnDate = "修改日期";
                string header = fnShow +
                   $"{fnName,-12}{fnLength,-8}{fnDate,-11}";

                WriteLine(header);
                WriteLine(sign);
                foreach (FileInfo getInfo in listFile)
                {
                    string dt =
                       getInfo.LastWriteTime.ToShortDateString();
                    WriteLine($"{getInfo.Name,-15}" +
                       $"{getInfo.Length.ToString(),-10} {dt}");
                }
            }
            catch (Exception ex)
            {
                WriteLine($"無此資料夾: {ex.Message}");
            }

            ReadKey();
        }
    }
}
