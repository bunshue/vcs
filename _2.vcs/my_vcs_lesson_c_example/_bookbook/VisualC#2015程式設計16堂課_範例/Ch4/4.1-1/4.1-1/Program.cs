using System;

class Program
{
    public static void Main()
    {
        int height, weight; //宣告整數變數 height和 weight
        string class_name; //宣告字串變數 class_name
        height = 170;
        weight = 60;
        class_name = "C#程式語言必勝班";
        Console.Write("身高:" + height + "體重:" + weight + "班級:" + class_name);
        Console.Read();
    }
}