using System;

class Program
{
    public static void Main()
    {
        int[] array = new int[15];
        for (int i = 0; i < 15; i++)
        {
            Console.Write("請輸入第" + (i + 1) + "個數字: ");
            array[i] = int.Parse(Console.ReadLine());
        }

        Console.WriteLine(Environment.NewLine + "您輸入的數字排列為: ");
        for (int i = 0; i < 15; i++)
            Console.Write(array[i] + " ");


        int target;
        Console.Write(Environment.NewLine + "請輸入你想尋找的數字: ");
        target = int.Parse(Console.ReadLine());

        int index;
        for (index = 0; index < 15; index++)
            if (array[index] == target)
                break;

        if (index == 15)
            Console.WriteLine("程式在陣列中沒有找到你所指定的數字!");
        else
            Console.WriteLine("你所指定的數字在索引 " + index + "的位置!");

        Console.Read();
    }
}

