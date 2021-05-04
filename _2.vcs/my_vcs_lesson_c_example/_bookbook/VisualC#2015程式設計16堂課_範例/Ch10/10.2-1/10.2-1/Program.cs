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
        for (int i = 1; i < 15; i++)
        {
            for (int j = i; j > 0; j--)
            {
                compares++;
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

        Console.WriteLine(Environment.NewLine + "插入排序法處理後的數字順序是: ");
        for (int i = 0; i < 15; i++)
            Console.Write(array[i] + " ");
        Console.WriteLine(Environment.NewLine + "程式總共執行了 " + compares + "次元素比較");

        Console.Read();
    }
}

