using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace vcs_Class6XXX     //預設namespace同Form1.cs之namespace
{
    class Class1
    {
        //預設class同檔名
    }

    class MyStack
    {
        private int top;
        private int[] stack_list;

        public MyStack(int x)
        {
            this.top = 0;
            this.stack_list = new int[x];
        }

        public void Push(int x)
        {
            if (top == stack_list.Length)
                throw new StackOverflowException();
            else
            {
                stack_list[top] = x;
                ++top;
            }
        }

        public int Pop()
        {
            if (top == 0)
                throw new NullReferenceException();
            else
            {
                --top;
                return stack_list[top];
            }
        }
    }
}
