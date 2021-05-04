using System;

class Program
{
    public static void Main()
    {
        Console.Write("請輸入學生人數: ");
        int num = int.Parse(Console.ReadLine());
        int[] array = new int[num];

        for (int i = 0; i < num; i++)
        {
            Console.Write("請輸入第" + (i + 1) + "個學生的成績: ");
            array[i] = int.Parse(Console.ReadLine());
        }

        int sum = 0;
        for (int i = 0; i < num; i++)
            sum += array[i];
        Console.WriteLine("本班學生平均分數為: " + (sum / num));

        Console.Read();
    }
}

