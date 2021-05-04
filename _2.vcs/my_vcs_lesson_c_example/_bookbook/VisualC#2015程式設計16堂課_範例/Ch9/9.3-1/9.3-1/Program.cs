using System;

class Program
{
    public static void Main()
    {
        Console.Write("請輸入學生人數: ");
        int num = int.Parse(Console.ReadLine());
        int[,] array = new int[num, 5];

        for (int i = 0; i < num; i++)
        {
            Console.Write("請輸入第" + (i + 1) + "個學生的國文成績: ");
            array[i, 0] = int.Parse(Console.ReadLine());
            Console.Write("請輸入第" + (i + 1) + "個學生的英文成績: ");
            array[i, 1] = int.Parse(Console.ReadLine());
            Console.Write("請輸入第" + (i + 1) + "個學生的數學成績: ");
            array[i, 2] = int.Parse(Console.ReadLine());

            //計算各科總分與平均
            array[i, 3] = array[i, 0] + array[i, 1] + array[i, 2];
            array[i, 4] = array[i, 3] / 3;
        }

        Console.WriteLine();
        for (int i = 0; i < num; i++)
            Console.WriteLine("學生" + (i + 1) + "的總分為:" + array[i, 3] + " 平均為:" + array[i, 4]);

        Console.Read();
    }
}

