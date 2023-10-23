using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Console;//滙入靜態類別

namespace Shuffle
{
    class Program
    {
        static int top = -1;

        static void Main(string[] args)
        {
            int[] card = new int[52];
            int[] stack = new int[52];
            int i, j, k = 0, test;
            char ascVal = 'H';
            int style;
            Random intRnd = new Random();
            for (i = 0; i < 52; i++)
                card[i] = i;
            WriteLine("[洗牌中...請稍後!]");
            while (k < 30)
            {
                for (i = 0; i < 51; i++)
                {
                    for (j = i + 1; j < 52; j++)
                    {
                        if ((intRnd.Next(10000) % 52) == 2)
                        {
                            test = card[i];//洗牌
                            card[i] = card[j];
                            card[j] = test;
                        }
                    }

                }
                k++;
            }
            i = 0;
            while (i != 52)
            {
                Push(stack, 52, card[i]);  //將52張牌推入堆疊
                i++;
            }
            WriteLine("[逆時針發牌]");
            WriteLine("[顯示各家牌子]\n 東家\t  北家\t   西家\t    南家");
            WriteLine("=================================");
            while (top >= 0)
            {
                style = stack[top] / 13;   //計算牌子花色
                switch (style)          //牌子花色圖示對應
                {
                    case 0:             //梅花
                        ascVal = 'C';
                        break;
                    case 1:             //方塊
                        ascVal = 'D';
                        break;
                    case 2:             //紅心
                        ascVal = 'H';
                        break;
                    case 3:             //黑桃
                        ascVal = 'S';
                        break;
                }
                Write("[" + ascVal + (stack[top] % 13 + 1) + "]");
                Write('\t');
                if (top % 4 == 0)
                    WriteLine();
                top--;
            }
            ReadKey();
        }
        public static void Push(int[] stack, int MAX, int val)
        {
            if (top >= MAX - 1)
                WriteLine("[堆疊已經滿了]");
            else
            {
                top++;
                stack[top] = val;
            }
        }

        public static int Pop(int[] stack)
        {
            if (top < 0)
                WriteLine("[堆疊已經空了]");
            else
                top--;
            return stack[top];
        }
    }
}
