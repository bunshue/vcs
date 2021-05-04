using System;

class Program
{
    public static void Main()
    {
        string age, name;

        Console.WriteLine("請輸入您的姓名:");
        name = Console.ReadLine();
        Console.WriteLine("請輸入您的年齡:");
        age = Console.ReadLine();

        Console.Write(name + " 您好, 您今年是 " + age + " 歲");
        Console.Read();
    }
}

