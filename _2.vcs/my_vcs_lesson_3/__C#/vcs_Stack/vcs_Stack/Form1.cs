using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for Stack

//堆棧（Stack）
//堆棧（Stack）代表了一個後進先出的對象集合。

/*
堆栈（Stack）代表了一个后进先出的对象集合。
当您需要对各项进行后进先出的访问时，则使用堆栈。
当您在列表中添加一项，称为推入元素，
当您从列表中移除一项时，称为弹出元素。


属性	描述
Count	获取 Stack 中包含的元素个数。

下表列出了 Stack 类的一些常用的 方法：
序号	方法名 & 描述
1	public virtual void Clear();
从 Stack 中移除所有的元素。
2	public virtual bool Contains( object obj );
判断某个元素是否在 Stack 中。
3	public virtual object Peek();
返回在 Stack 的顶部的对象，但不移除它。
4	public virtual object Pop();
移除并返回在 Stack 的顶部的对象。
5	public virtual void Push( object obj );
向 Stack 的顶部添加一个对象。
6	public virtual object[] ToArray();
复制 Stack 到一个新的数组中。
*/

namespace vcs_Stack
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Stack st = new Stack();

            st.Push('A');
            st.Push('M');
            st.Push('G');
            st.Push('W');

            Console.WriteLine("Current stack: ");
            foreach (char c in st)
            {
                Console.Write(c + " ");
            }
            Console.WriteLine();

            st.Push('V');
            st.Push('H');
            Console.WriteLine("The next poppable value in stack: {0}",
            st.Peek());
            Console.WriteLine("Current stack: ");
            foreach (char c in st)
            {
                Console.Write(c + " ");
            }
            Console.WriteLine();

            Console.WriteLine("Removing values ");
            st.Pop();
            st.Pop();
            st.Pop();

            Console.WriteLine("Current stack: ");
            foreach (char c in st)
            {
                Console.Write(c + " ");
            }


        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {

        }

        private void button4_Click(object sender, EventArgs e)
        {

        }
    }
}
