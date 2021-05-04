using System;

class Program
{
    public static void Main()
    {
        Console.WriteLine("目前的工作目錄:");
        Console.WriteLine(System.IO.Directory.GetCurrentDirectory());

        System.IO.Directory.SetCurrentDirectory("D:\\");
        Console.WriteLine("更改後的工作目錄:");
        Console.WriteLine(System.IO.Directory.GetCurrentDirectory());

        Console.Read();
    }
}

