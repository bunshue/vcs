using System;
using System.IO;

class Program
{
    public static void Main()
    {
        Console.Write("請輸入學生人數: ");
        int num = int.Parse(Console.ReadLine());
        int[,] array = new int[num, 3];

        for (int i = 0; i < num; i++)
        {
            Console.WriteLine("請依序輸入第" + (i + 1) + "個學生的國文、英文、數學成績: ");
            array[i, 0] = int.Parse(Console.ReadLine());
            array[i, 1] = int.Parse(Console.ReadLine());
            array[i, 2] = int.Parse(Console.ReadLine());
        }


        Directory.SetCurrentDirectory("D:\\");
        StreamWriter sw = new StreamWriter("11.3_scores.txt");

        sw.WriteLine("        國文  英文  數學  |  總分  平均");
        for (int i = 0; i < num; i++)
        {
            sw.Write("學生" + (i + 1).ToString().PadRight(2));
            sw.Write(array[i, 0].ToString().PadLeft(6));
            sw.Write(array[i, 1].ToString().PadLeft(6));
            sw.Write(array[i, 2].ToString().PadLeft(6));
            int stu_total = array[i, 0] + array[i, 1] + array[i, 2];
            sw.Write(stu_total.ToString().PadLeft(9));
            sw.WriteLine((stu_total / 3).ToString().PadLeft(6));
        }

        sw.WriteLine("---------------------------------------");
        sw.Write("平均  ");
        int all_total = 0;
        for (int i = 0; i < 3; i++)
        {
            int class_total = 0;
            for (int j = 0; j < num; j++)
                class_total += array[j, i];
            sw.Write((class_total / num).ToString().PadLeft(6));
            all_total += class_total;
        }
        sw.Write((all_total / num).ToString().PadLeft(9));
        sw.Write((all_total / (num * 3)).ToString().PadLeft(6));

        sw.Flush();
        sw.Close();

    }
}

