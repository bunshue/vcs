using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH1507
{
    class Program
    {
        static void Main(string[] args)
        {
            BinaryWriter objWriter;
            FileStream objStream;
            string path = @"D:\C#Lab\Demo03.txt";
            try
            {
                objStream = new FileStream(path,
                   FileMode.Append, FileAccess.Write);
                //使用using敘詞，寫入完墓會自動釋放資源
                using (objWriter = new BinaryWriter(objStream))
                {
                    //* 寫入字串
                    objWriter.Write("空山不見人");
                    objWriter.Write("Visual C# 7.0");
                    //* 寫入數值
                    objWriter.Write(640526);
                }
            }
            catch (IndexOutOfRangeException e)
            {
                WriteLine("沒有指定檔案");
            }
            catch (Exception e)
            {
                WriteLine(e.Message);
            }
            ReadKey();
        }
    }
}
