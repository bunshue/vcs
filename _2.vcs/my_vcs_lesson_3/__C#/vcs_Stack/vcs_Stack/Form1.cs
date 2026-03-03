using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for Stack

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
            show_item_location();
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy;

            //button
            x_st = 10;
            y_st = 10;
            dx = 200 + 10;
            dy = 60 + 10;

            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            button5.Location = new Point(x_st + dx * 0, y_st + dy * 5);
            button6.Location = new Point(x_st + dx * 0, y_st + dy * 6);
            button7.Location = new Point(x_st + dx * 0, y_st + dy * 7);
            button8.Location = new Point(x_st + dx * 0, y_st + dy * 8);
            button9.Location = new Point(x_st + dx * 0, y_st + dy * 9);

            richTextBox1.Size = new Size(800, 690);
            richTextBox1.Location = new Point(x_st + dx * 1, y_st + dy * 0);

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            this.Size = new Size(1050, 750);
            this.Text = "vcs_Stack";

            //設定執行後的表單起始位置, 正中央
            this.StartPosition = FormStartPosition.Manual;
            this.Location = new Point((Screen.PrimaryScreen.Bounds.Width - this.Size.Width) / 2, (Screen.PrimaryScreen.Bounds.Height - this.Size.Height) / 2);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button0_Click(object sender, EventArgs e)
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
            //创建一个堆栈
            Stack myStack = new Stack();
            myStack.Push("The");//入栈
            myStack.Push("quick");
            myStack.Push("brown");
            myStack.Push("fox");

            // 打印集合中的值
            Console.Write("Stack values:");
            PrintValues(myStack, '\t');

            // 打印堆栈顶部的第一个元素，并将其移除
            Console.WriteLine("(Pop)\t\t{0}", myStack.Pop());

            //打印集合中的值
            Console.Write("Stack values:");
            PrintValues(myStack, '\t');

            // 打印堆栈顶部的第一个元素，并将其移除
            Console.WriteLine("(Pop)\t\t{0}", myStack.Pop());

            //打印集合中的值
            Console.Write("Stack values:");
            PrintValues(myStack, '\t');

            // 打印堆栈顶部的第一个元素
            Console.WriteLine("(Peek)\t\t{0}", myStack.Peek());

            // 打印集合中的值
            Console.Write("Stack values:");
            PrintValues(myStack, '\t');
        }

        public static void PrintValues(IEnumerable myCollection, char mySeparator)
        {
            foreach (Object obj in myCollection)
            {
                Console.Write("{0}{1}", mySeparator, obj);
            }
            Console.WriteLine();
        }

        private class BranchInfo
        {
            public float X, Y, Theta;
            public BranchInfo(float x, float y, float theta)
            {
                X = x;
                Y = y;
                Theta = theta;
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            //Stack 使用範例3
            Stack<BranchInfo> branches = new Stack<BranchInfo>();

            int x = 10;
            int y = 10;
            float theta = 12.34f;
            branches.Push(new BranchInfo(x, y, theta));

            x = 10;
            y = 10;
            theta = 12.34f;
            branches.Push(new BranchInfo(x, y, theta));

            x = 10;
            y = 10;
            theta = 12.34f;
            branches.Push(new BranchInfo(x, y, theta));

            richTextBox1.Text += "共有 :" + branches.Count.ToString() + "\n";

            richTextBox1.Text += "pop 出來\n";
            while (branches.Count > 0)
            {
                BranchInfo branch = branches.Pop();
                richTextBox1.Text += branch.ToString() + "\n";
                richTextBox1.Text += branch.X.ToString() + "\n";
                richTextBox1.Text += branch.Y.ToString() + "\n";
                richTextBox1.Text += branch.Theta.ToString() + "\n";
            }
        }

        public static void PrintOut(IEnumerable myCollction)
        {
            int i = 0;
            foreach (Object obj in myCollction)
            {
                Console.WriteLine("   第{0}個元素 : {1} ", ++i, obj);
            }
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //Stack 使用範例4
            Stack myStack = new Stack();
            string[] ary = { "Jack", "Ford", "Bob", "David" };
            //將陣列置入堆疊
            foreach (string name in ary)
                myStack.Push(name);
            Console.WriteLine(" 1.目前堆疊內所有元素 : ");
            PrintOut(myStack);
            Console.WriteLine(" 1.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 將 Mary 置入堆疊(最上面)
            Console.WriteLine(" 2.將 Mary 置入堆疊");
            myStack.Push("Mary");
            Console.WriteLine(" 2.目前堆疊內所有元素 : ");
            PrintOut(myStack);
            Console.WriteLine(" 2.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 取得堆疊最上面的資料           
            Console.WriteLine(" 3.查詢堆疊最上面資料 : {0} ", myStack.Peek());
            Console.WriteLine(" 3.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 由堆疊最上面取出資料
            Console.WriteLine(" 4.取出堆疊最上面的資料 : {0} ", myStack.Pop());
            Console.WriteLine(" 4.目前堆疊內所有元素 : ");
            PrintOut(myStack);
            Console.WriteLine(" 4.目前堆疊內元素的總個數: {0} ", myStack.Count);
            Console.WriteLine(" ----------------------------");

            // 檢查堆疊內是否有 "David" 這個資料
            Console.WriteLine(" 5.檢查堆疊內是否有 David 這個資料 ? ");
            if (!myStack.Contains("David"))
            {
                Console.WriteLine(" 5.堆疊內無此資料!");
            }
            else
            {
                Console.WriteLine(" 5.堆疊內有此資料!");
            }
            Console.WriteLine(" ----------------------------");

            // 清除堆疊內所有元素           
            Console.WriteLine(" 6.清除堆疊內的所有資料");
            Console.WriteLine(" 6.堆疊內資料的個數: {0}", myStack.Count);
            PrintOut(myStack);
            Console.WriteLine(" ----------------------------");

            Console.Read();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            //Stack 使用範例5
            Stack m = new Stack();   // 非泛型           

            m.Push(new Member() { Name = "David", Select = true, Score = 70 });
            m.Push(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Push(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Push(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine("=== 非泛型 Stack 操作需強制轉換 .... \n");
            while (m.Count > 0)
            {
                Console.WriteLine("{0} ", (Member)m.Pop());
            }
            Console.Read();
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //Stack 使用範例6
            Stack<Member> m = new Stack<Member>();   // 泛型           

            m.Push(new Member() { Name = "David", Select = true, Score = 70 });
            m.Push(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Push(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Push(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine("=== 泛型 Stack 操作不需強制轉換 .... \n");

            while (m.Count > 0)
            {
                Console.WriteLine("{0} ", m.Pop());
            }
            Console.Read();
        }

        private void button7_Click(object sender, EventArgs e)
        {

        }

        private void button8_Click(object sender, EventArgs e)
        {

        }

        private void button9_Click(object sender, EventArgs e)
        {

        }
    }

    class Member
    {
        public string Name { get; set; }      // 姓名屬性          
        public bool Select { get; set; }      // 選課屬性
        public int Score { get; set; }        // 成績屬性

        public override string ToString()    // 覆寫覆類別 ToString()方法
        {
            return string.Format("姓名 : {0} \t 選課 :{1} \t 成績: {2} \n ", Name, Select ? "是" : "否", Score.ToString());
        }
    }
}
