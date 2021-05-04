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

        int tmp;
        for (int i = 1; i < 15; i++)
        {
            for (int j = i; j > 0; j--)
            {
                if (array[j - 1] > array[j])
                {
                    tmp = array[j - 1];
                    array[j - 1] = array[j];
                    array[j] = tmp;
                }
                else
                    break;
            }
        }

        Console.WriteLine(Environment.NewLine + "插入排序法處理後的數字排列是: ");
        for (int i = 0; i < 15; i++)
            Console.Write(array[i] + " ");


        int target;
        Console.Write(Environment.NewLine + "請輸入你想尋找的數字: ");
        target = int.Parse(Console.ReadLine());

        int highIndex = 14, lowIndex = 0;
        int midIndex = (highIndex + lowIndex) / 2;
        for (; lowIndex < highIndex; midIndex = (highIndex + lowIndex) / 2)
        {
            if (array[midIndex] == target)
                break;
            else if (array[midIndex] > target)
                highIndex = midIndex - 1;
            else if (array[midIndex] < target)
                lowIndex = midIndex + 1;
        }

        if (lowIndex > highIndex)
            Console.WriteLine("程式在陣列中沒有找到你所指定的數字!");
        else
            Console.WriteLine("你所指定的數字在索引 " + midIndex + "的位置!");

        Console.Read();
    }
}

