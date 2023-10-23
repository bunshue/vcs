using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;  //滙入靜態類別

namespace Determinant
{
    class Program
    {
        static void Main(string[] args)
        { 
            int [,] arr= new int[2,2];
            int sum;
            Write("|a1 b1|\n");
            Write("|a2 b2|\n");
            Write("請輸入a1:");
            arr[0,0] = int.Parse(ReadLine());
            Write("請輸入b1:");
            arr[0,1] = int.Parse(ReadLine());
            Write("請輸入a2:");
            arr[1,0] = int.Parse(ReadLine());
            Write("請輸入b2:");
            arr[1,1] = int.Parse(ReadLine());
            sum = arr[0,0]*arr[1,1]-arr[0,1]*arr[1,0];//求二階行列式的值 
            Write("|" +arr[0,0] + " " + arr[0,1] + "|\n");
            Write("|" + arr[1,0] + " " + arr[1,1] + "|\n");
            WriteLine(sum);
            Read();
        }
    }
}
