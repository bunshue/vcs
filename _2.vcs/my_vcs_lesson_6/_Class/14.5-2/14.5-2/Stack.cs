using System;

namespace myStack
{
    class Stack
    {
        private int top;
        private int[] stack_list;

        public Stack(int x)
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
