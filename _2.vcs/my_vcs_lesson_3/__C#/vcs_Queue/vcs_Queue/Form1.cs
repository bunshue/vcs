using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for IEnumerable

namespace vcs_Queue
{
    public partial class Form1 : Form
    {
        string filename1 = @"C:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename2 = @"C:\_git\vcs\_1.data\______test_files1\bear.jpg";
        string filename3 = @"C:\_git\vcs\_1.data\______test_files1\elephant.jpg";

        Queue<Bitmap> bitmap_queue = new Queue<Bitmap>();
        Queue<string> string_queue = new Queue<string>();
        Queue<char> char_queue = new Queue<char>();

        Bitmap bitmap1 = null;
        Bitmap bitmap2 = null;
        Bitmap bitmap3 = null;

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            bitmap2 = (Bitmap)Bitmap.FromFile(filename2);	//Bitmap.FromFile出來的是Image格式
            bitmap3 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式

            update_queue_count();//更新佇列狀態
        }

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "從佇列尾加圖片1\n";
            bitmap_queue.Enqueue(bitmap1);

            //richTextBox1.Text += "從佇列尾加時間訊息\n";
            string now = DateTime.Now.ToString();
            string_queue.Enqueue(now);

            //richTextBox1.Text += "從佇列尾加字元\n";
            char_queue.Enqueue('A');

            update_queue_count();//更新佇列狀態
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "從佇列尾加圖片2\n";
            bitmap_queue.Enqueue(bitmap2);

            //richTextBox1.Text += "從佇列尾加時間訊息\n";
            string now = DateTime.Now.ToString();
            string_queue.Enqueue(now);

            //richTextBox1.Text += "從佇列尾加字元\n";
            char_queue.Enqueue('B');

            update_queue_count();//更新佇列狀態
        }

        private void button3_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "從佇列尾加圖片2\n";
            bitmap_queue.Enqueue(bitmap3);

            //richTextBox1.Text += "從佇列尾加時間訊息\n";
            string now = DateTime.Now.ToString();
            string_queue.Enqueue(now);

            //richTextBox1.Text += "從佇列尾加字元\n";
            char_queue.Enqueue('C');

            update_queue_count();//更新佇列狀態
        }

        private void button4_Click(object sender, EventArgs e)
        {
            //bitmap queue取出
            if (bitmap_queue.Count > 0)
            {
                try
                {
                    Bitmap bitmap1 = bitmap_queue.Dequeue();
                    pictureBox_show.Image = bitmap1;
                    richTextBox1.Text += "從佇列頭取出1張圖\n";
                }
                catch (Exception ex)
                {
                    Console.WriteLine("xxx錯誤訊息e03 : " + ex.Message);
                }
            }
            else
            {
                richTextBox1.Text += "無圖可讀\n";
            }

            //string queue取出
            if (string_queue.Count > 0)
            {
                try
                {
                    string str = string_queue.Dequeue();
                    richTextBox1.Text += "從佇列頭取出訊息 : " + str + "\n";
                }
                catch (Exception ex)
                {
                    Console.WriteLine("xxx錯誤訊息e03 : " + ex.Message);
                }
            }

            //char queue取出
            if (char_queue.Count > 0)
            {
                try
                {
                    char ch = (char)char_queue.Dequeue();
                    richTextBox1.Text += "從佇列頭取出字元 : " + ch + "\n";
                }
                catch (Exception ex)
                {
                    Console.WriteLine("xxx錯誤訊息e03 : " + ex.Message);
                }
            }


            update_queue_count();//更新佇列狀態
        }

        void update_queue_count()
        {
            label1.Text = "目前Queue中的張數 : " + bitmap_queue.Count.ToString();
        }

        private void button5_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "清除Queue\n";
            bitmap_queue.Clear();
            string_queue.Clear();
            char_queue.Clear();
            update_queue_count();//更新佇列狀態
        }

        private void button6_Click(object sender, EventArgs e)
        {
            //Queue訊息
            int len = string_queue.Count;
            richTextBox1.Text += "目前Queue內共有 : " + len.ToString() + " 筆資料\n";

            richTextBox1.Text += "Current queue: " + "\n";
            foreach (char c in char_queue)
            {
                richTextBox1.Text += c + " ";
            }
            richTextBox1.Text += "\n";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            //创建一个队列
            Queue myQ = new Queue();
            myQ.Enqueue("The");//入队
            myQ.Enqueue("quick");
            myQ.Enqueue("brown");
            myQ.Enqueue("fox");
            myQ.Enqueue(null);//添加null
            myQ.Enqueue("fox");//添加重复的元素

            // 打印队列的数量和值
            Console.WriteLine("myQ");
            Console.WriteLine("\tCount:    {0}", myQ.Count);

            // 打印队列中的所有值
            Console.Write("Queue values:");
            PrintValues(myQ);

            // 打印队列中的第一个元素，并移除
            Console.WriteLine("(Dequeue)\t{0}", myQ.Dequeue());

            // 打印队列中的所有值
            Console.Write("Queue values:");
            PrintValues(myQ);

            // 打印队列中的第一个元素，并移除
            Console.WriteLine("(Dequeue)\t{0}", myQ.Dequeue());

            // 打印队列中的所有值
            Console.Write("Queue values:");
            PrintValues(myQ);

            // 打印队列中的第一个元素
            Console.WriteLine("(Peek)   \t{0}", myQ.Peek());

            // 打印队列中的所有值
            Console.Write("Queue values:");
            PrintValues(myQ);
        }

        public static void PrintValues(IEnumerable myCollection)
        {
            foreach (Object obj in myCollection)
            {
                Console.Write("    {0}", obj);
            }
            Console.WriteLine();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //创建一个队列对象Queue
            Queue queue = new Queue();

            // 队列的插入操作 入队 
            queue.Enqueue("what21");
            // 队列中添加数值
            queue.Enqueue(21);
            // 队列中添加null 
            queue.Enqueue(null);
            // 队列中
            queue.Enqueue(new object());
            // 队列中重复插入
            queue.Enqueue("what21");
            // 标识一下最好一个
            queue.Enqueue("我是最后一个了");

            // 遍历队列的所有内容
            foreach (Object item in queue)
            {
                Console.WriteLine("<1> {0}", item);
            }

            // 队列的数量
            Console.WriteLine("这个队列的数量为：{0}", queue.Count);
            // 取列中的第一个元素
            object one = queue.Peek();
            Console.WriteLine("我是第一个元素：{0}", one);
            // 取列中的第一个元素，并移除 
            object rone = queue.Dequeue();
            Console.WriteLine("我是第一个元素：{0}", rone);


            // 遍历队列的所有内容
            foreach (Object item in queue)
            {
                Console.WriteLine("<2> {0}", item);
            }

            //  遍历方法二
            IEnumerator enumer = queue.GetEnumerator();
            while (enumer.MoveNext())
            {
                object o = enumer.Current;
                Console.WriteLine("<3> " + o);
            }

            // 将Queue转换为数组
            object[] objs = queue.ToArray();
            for (int i = 0; i < objs.Length; i++)
            {
                object o = objs[i];
                Console.Write("<4> " + o + "\n");
            }
        }
    }
}