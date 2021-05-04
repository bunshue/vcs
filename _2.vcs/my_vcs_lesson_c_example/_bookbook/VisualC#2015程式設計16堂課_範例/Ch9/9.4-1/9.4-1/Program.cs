using System;

class Program
{
    public static void Main()
    {
        int[,] array = new int[,] { { 0, 11, 3, 45, 17 }, { 23, 41, 5, 8, 10 }, { 9, 21, 16, 84, 51 } };

        int Total = 0;
        foreach (int element in array)
        {
            Total += element;
        }
        Console.WriteLine("此二維陣列的各個元素總和為: " + Total);

        Console.Read();
    }
}

