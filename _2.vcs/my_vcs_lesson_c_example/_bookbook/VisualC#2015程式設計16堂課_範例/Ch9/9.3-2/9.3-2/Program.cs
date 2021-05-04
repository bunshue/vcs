using System;

class Program
{
    public static void Main()
    {
        Console.Write("請輸入部門數量: ");
        int numDep = int.Parse(Console.ReadLine());
        int[][] array = new int[numDep][];
        int[] arrTotal = new int[numDep];

        int tmpNum;
        for (int i = 0; i < numDep; i++)
        {
            Console.Write("請輸入第" + (i + 1) + "個部門的員工數量: ");
            tmpNum = int.Parse(Console.ReadLine());
            array[i] = new int[tmpNum];

            for (int j = 0; j < tmpNum; j++)
            {
                Console.Write("請輸入該部門第" + (j + 1) + "個員工的薪資: ");
                array[i][j] = int.Parse(Console.ReadLine());
                arrTotal[i] += array[i][j];
            }
        }

        Console.WriteLine();

        int Total = 0;
        for (int i = 0; i < numDep; i++)
        {
            Console.WriteLine("第" + (i + 1) + "個部門的員工薪資總和為: " + arrTotal[i]);
            Total += arrTotal[i];
        }
        Console.WriteLine("公司全部員工薪資總和為: " + Total);

        Console.Read();
    }
}

