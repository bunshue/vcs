using System;
using System.IO;

class Program
{
    public static void Main()
    {
        Directory.SetCurrentDirectory("D:\\");
        StreamReader sr = new StreamReader("11.2_list1.txt");

        Console.WriteLine("檔案中第一個字元的字元(ascii)碼");
        Console.WriteLine(sr.Read());
        Console.WriteLine("檔案中的第二個字元");
        Console.WriteLine(Convert.ToChar(sr.Read()));

        Console.WriteLine("逐個字元讀入直到遇到換行為止");
        char ch = Convert.ToChar(sr.Read());
        while (ch != '\n')
        {
            Console.Write(ch);
            ch = Convert.ToChar(sr.Read());
        }
        Console.WriteLine();

        Console.WriteLine("逐行字串讀入直到達到檔案尾端為止");
        while (!sr.EndOfStream)
        {
            Console.WriteLine(sr.ReadLine());
        }
        sr.Close();

        Console.Read();
    }
}

