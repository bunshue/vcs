using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _4._4_1
{
    class Program
    {
        static void Main(string[] args)
        {
            int height, weight; //宣告整數變數 height和 weight
            const string class_name= "C#程式語言必勝班"; //宣告字串常數 class_name
            height = 170;
            weight = 60;
            class_name = "VB";
            Console.Write("身高:" + height + "體重:" + weight + "班級:" + class_name);
            Console.Read();
        }
    }
}
