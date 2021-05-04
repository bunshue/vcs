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

        int tmp, compares = 0;
        for (int i = 14; i > 0; i--)
        {
            for (int j = 0; j < i; j++)
            {
                compares++;
                if (array[j] > array[j + 1])
                {
                    tmp = array[j + 1];
                    array[j + 1] = array[j];
                    array[j] = tmp;
                }
            }
        }

        Console.WriteLine(Environment.NewLine + "氣泡排序法處理後的數字順序是: ");
        for (int i = 0; i < 15; i++)
            Console.Write(array[i] + " ");
        Console.WriteLine(Environment.NewLine + "程式總共執行了 " + compares + "次元素比較");

        Console.Read();
    }
}

