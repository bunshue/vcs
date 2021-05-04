using System;

class Program
{
    public static void Main()
    {
        int[] array = new int[50];
        int m = 0, carry = 0;
        array[0] = 1;

        for (int i = 2; i <= 30; i++)
        {
            for (int j = 0; j <= m; j++)
            {
                array[j] *= i;
                array[j] += carry;
                carry = array[j] / 10;
                if (carry != 0 && j == m)
                    m++;
                array[j] = array[j] % 10;
            }
        }

        Console.Write("30! = ");
        for (int k = m; k >= 0; k--)
            Console.Write(array[k]);

        Console.Read();
    }
}

