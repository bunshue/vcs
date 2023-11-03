using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using static System.Console;

namespace CH1508
{
    class Program
    {
        static void Main(string[] args)
        {
            BinaryReader objReader;
            FileStream objStream;
            string path = @"D:\C#Lab\Demo03.txt";
            try
            {
                objStream = new FileStream(path,
                   FileMode.Open, FileAccess.Read);
                objReader = new BinaryReader(objStream);
                WriteLine(objReader.ReadString());
                WriteLine(objReader.ReadInt32());
                objReader.Close();
            }
            catch (IndexOutOfRangeException e)
            {
                WriteLine("沒有指定檔案");
            }

            catch (EndOfStreamException e)
            {
                WriteLine("檔案讀取完畢");
            }

            catch (Exception e)
            {
                WriteLine(e.Message);
            }
            ReadKey();
        }
    }
}
