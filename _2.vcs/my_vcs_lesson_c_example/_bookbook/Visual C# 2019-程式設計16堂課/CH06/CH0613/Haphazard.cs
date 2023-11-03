using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CH0613
{
    class Haphazard
    {
        //私有建構函式
        private Haphazard() { }
        //建立產生亂數的物件rand
        static Random rand = new Random();
        //以byte為型別，透過陣列儲存10隨機值
        static byte[] current = new byte[10];
        //靜態類別方法-讀取隨機數
        public static void randNumber()
        {
            //呼叫NextBytes方法，產生以byte型別為主的隨機值
            rand.NextBytes(current);
            //讀取陣列元素
            foreach (byte item in current)
            {
                Console.Write($"{item} ");
            }
        }
    }
}
