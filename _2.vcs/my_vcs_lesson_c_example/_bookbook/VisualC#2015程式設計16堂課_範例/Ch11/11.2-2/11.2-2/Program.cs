using System;
using System.IO;

class Program
{
    public static void Main()
    {
        Directory.SetCurrentDirectory("D:\\");
        StreamReader sr = new StreamReader("11.2_list2.txt");

        Console.WriteLine("一次印出所有檔案內容");
        Console.WriteLine(sr.ReadToEnd());
        Console.WriteLine();

        sr = new StreamReader("11.2_list2.txt");
        Console.WriteLine("逐行印出檔案內容");
        int line = 1;

        for (; !sr.EndOfStream; line++)
        {
            Console.Write("第" + line + "行: ");
            Console.WriteLine(sr.ReadLine());
        }
        sr.Close();

        Console.Read();
    }
}

