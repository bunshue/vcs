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

        Queue<Bitmap> frames = new Queue<Bitmap>(); // Queue that stores frames to be written by the recorder thread

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            update_queue_count();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            frames.Enqueue((Bitmap)bitmap1.Clone());
            richTextBox1.Text += "將第1張圖放入Queue, 從尾加\n";
            update_queue_count();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename2);	//Bitmap.FromFile出來的是Image格式
            frames.Enqueue((Bitmap)bitmap1.Clone());
            richTextBox1.Text += "將第2張圖放入Queue, 從尾加\n";
            update_queue_count();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bitmap bitmap1 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式
            frames.Enqueue((Bitmap)bitmap1.Clone());
            richTextBox1.Text += "將第3張圖放入Queue, 從尾加\n";
            update_queue_count();
        }

        private void button4_Click(object sender, EventArgs e)
        {
            if (frames.Count > 0)
            {
                try
                {
                    Bitmap bitmap1 = frames.Dequeue();
                    pictureBox_show.Image = bitmap1;
                    richTextBox1.Text += "從Queue中讀出第1張圖, 從頭取\n";
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
            update_queue_count();
        }

        void update_queue_count()
        {
            label1.Text = "目前Queue中的張數 : " + frames.Count.ToString();
            //richTextBox1.Text += "目前Queue中的張數 : " + frames.Count.ToString() + "\n";
            pictureBox_count.Invalidate();
        }

        private void pictureBox_count_Paint(object sender, PaintEventArgs e)
        {
            int border = 10;    //10 percent
            int W = pictureBox_count.ClientSize.Width;
            int H = pictureBox_count.ClientSize.Height;
            int x_st = W * border / 100;
            int y_st = H * border / 100;
            int w = W * (100 - border * 2) / 100;
            int h = H * (100 - border * 2) / 100;

            int cnt = frames.Count;
            int i = 0;
            int width = 0;

            e.Graphics.Clear(Color.Pink);
            if (cnt == 0)
            {
            }
            else if (cnt <= 10)
            {
                width = w / 10;
                for (i = 0; i < cnt; i++)
                {
                    e.Graphics.FillRectangle(Brushes.Red, x_st + width * i, y_st, width, h);
                    e.Graphics.DrawRectangle(Pens.DarkRed, x_st + width * i, y_st, width, h);
                }



            }
        }

        private void button5_Click(object sender, EventArgs e)
        {
            frames.Clear();
            richTextBox1.Text += "清除Queue\n";
            update_queue_count();

        }

        private void button6_Click(object sender, EventArgs e)
        {
            Queue<char> q = new Queue<char>();

            q.Enqueue('A');
            q.Enqueue('B');
            q.Enqueue('C');
            q.Enqueue('D');

            richTextBox1.Text += "Current queue: " + "\n";
            foreach (char c in q)
            {
                richTextBox1.Text += c + " ";
            }
            richTextBox1.Text += "\n";

            q.Enqueue('E');
            q.Enqueue('F');
            richTextBox1.Text += "Current queue: " + "\n";
            foreach (char c in q)
            {
                richTextBox1.Text += c + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "Removing some values " + "\n";
            char ch = (char)q.Dequeue();
            richTextBox1.Text += "The removed value: " + ch + "\n";
            ch = (char)q.Dequeue();
            richTextBox1.Text += "The removed value: " + ch + "\n";

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
                Console.Write("    {0}", obj);
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

        Queue<string> string_queue = new Queue<string>(); // Queue that stores frames to be written by the recorder thread

        private void button9_Click(object sender, EventArgs e)
        {
            //Queue訊息
            int len = string_queue.Count;
            richTextBox1.Text += "目前Queue內共有 : " + len.ToString() + " 筆資料\n";
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //Queue加入
            richTextBox1.Text += "加入Queue";
            string str = "加入Queue";
            string_queue.Enqueue(str);
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //Queue取出
            if (string_queue.Count > 0)
            {
                try
                {
                    string str = string_queue.Dequeue();
                    richTextBox1.Text += "取得 : " + str + "\n";
                }
                catch (Exception ex)
                {
                    Console.WriteLine("xxx錯誤訊息e03 : " + ex.Message);
                }
            }
        }
    }
}

