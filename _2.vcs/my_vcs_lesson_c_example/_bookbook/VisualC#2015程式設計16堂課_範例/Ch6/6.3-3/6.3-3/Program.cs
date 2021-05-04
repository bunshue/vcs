using System;

class Program
{
    public static void Main()
    {
        Console.Write("請按enter計數，輸入任意文字即可停止計數: ");
        int counter = 0;

        while (true)
        {
            if (Console.ReadLine() == "")
                ++counter;
            else
                break;
        }

        Console.WriteLine("你總共按了: " + counter + "次enter!");
        Console.Read();
    }
}

