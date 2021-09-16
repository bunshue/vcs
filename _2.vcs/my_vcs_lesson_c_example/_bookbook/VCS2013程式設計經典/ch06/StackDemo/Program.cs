using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StackDemo
{
    class Stack
    {
        private int[] _aryData;
        private int _top;
        // 建構式
        public Stack(int n)
        {
            _aryData = new int[n];
            _top = 0;
        }
        // 將資料放入堆疊
        public void Push(int n)
        {
            if (_top == _aryData.Length)
            {
                Console.WriteLine("    堆疊滿了");
                return;
            }
            _aryData[_top] = n;
            _top += 1;
            Console.WriteLine("    壓入{0}到堆疊內", n);
        }
        //將堆疊的資料拿出
        public void Pop()
        {
            if (_top == 0)
            {
                Console.WriteLine("    堆疊空了");
                return;
            }
            _top -= 1;
            Console.WriteLine("    由堆疊彈出資料：{0}", _aryData[_top]);
        }
        //印出堆疊的所有資料
        public void PrintStack()
        {
            if (_top == 0)
            {
                Console.WriteLine("    堆疊內沒有資料");
                return;
            }
            Console.Write("    印出堆疊內容：");
            for (int i = 0; i < _top; i++)
            {
                Console.Write("{0} ", _aryData[i]);
            }
            Console.WriteLine();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("請輸入堆疊可存放的數量：");
            int num = int.Parse(Console.ReadLine());
            Stack s = new Stack(num);
            int sel, input;
            do
            {
                Console.WriteLine();
                Console.WriteLine("=== Stack Operation ===");
                Console.WriteLine("    1. Push Operation ");
                Console.WriteLine("    2. Pop Operation ");
                Console.WriteLine("    3. Printout Stack");
                Console.WriteLine("    4. Quit");
                Console.WriteLine("=======================");
                Console.Write("    請選擇 [0-3]：");
                sel = int.Parse(Console.ReadLine());
                if (sel == 1)
                {
                    Console.Write("    請輸入要放入堆疊的資料：");
                    input = int.Parse(Console.ReadLine());
                    s.Push(input);
                }
                else if (sel == 2)
                {
                    s.Pop();
                }
                else if (sel == 3)
                {
                    s.PrintStack();
                }
                else if (sel == 4)
                {
                    Console.WriteLine("    離開系統");
                    return;
                }
                else
                {
                    Console.WriteLine("    === Error input(0-3)!!");
                }
            } while (true);
            Console.ReadLine();
        }
    }
}


