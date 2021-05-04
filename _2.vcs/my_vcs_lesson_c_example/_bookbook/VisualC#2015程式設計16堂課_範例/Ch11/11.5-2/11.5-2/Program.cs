using System;
using System.IO;

class Program
{
    public static void Main()
    {
        Console.Write("請輸入欲加密檔案的位置: ");
        string filename = Console.ReadLine();
        StreamReader sr = new StreamReader(filename);
        StreamWriter sw = new StreamWriter(filename + "output.txt");

        Console.Write("請輸入字元欲位移的數量: ");
        int shift = int.Parse(Console.ReadLine());

        for (int ascii; !sr.EndOfStream; )
        {
            ascii = sr.Read();
            if (ascii >= 32 && ascii <= 126)
            {
                ascii += shift;
                if (ascii > 126)
                    ascii = (ascii % 126) + 31;
                else if (ascii < 32)
                    ascii += 95;
            }
            sw.Write(Convert.ToChar(ascii));
        }

        sw.Flush();
        sr.Close();
        sw.Close();

    }
}

