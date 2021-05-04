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

        Console.WriteLine(Environment.NewLine + "您輸入的數字順序是: ");
        for (int i = 0; i < 15; i++)
            Console.Write(array[i] + " ");

        int tmp;
        for (int i = 0; i < 14; i++)
        {
            for (int j = i + 1; j < 15; j++)
            {
                if (array[j] < array[i])
                {
                    tmp = array[j];
                    array[j] = array[i];
                    array[i] = tmp;
                }
            }
        }

        Console.WriteLine(Environment.NewLine + "選擇排序法處理後的數字順序是: ");
        for (int i = 0; i < 15; i++)
            Console.Write(array[i] + " ");

        Console.Read();
    }
}

