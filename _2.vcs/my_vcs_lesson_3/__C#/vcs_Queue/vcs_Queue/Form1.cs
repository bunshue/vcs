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
        Queue any_queue = new Queue();

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

            //richTextBox1.Text += "從佇列尾加any\n";
            any_queue.Enqueue("aaa");

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

            //richTextBox1.Text += "從佇列尾加any\n";
            any_queue.Enqueue("bbb");

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

            //richTextBox1.Text += "從佇列尾加any\n";
            any_queue.Enqueue("ccc");

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

            //any queue取出
            if (any_queue.Count > 0)
            {
                try
                {
                    object any = any_queue.Dequeue();
                    richTextBox1.Text += "從佇列頭取出any : " + any + "\n";
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

            richTextBox1.Text += "char_queue\n";
            foreach (char c in char_queue)
            {
                richTextBox1.Text += c + " ";
            }
            richTextBox1.Text += "\n";

            richTextBox1.Text += "any_queue\n";
            PrintValues(any_queue);

            richTextBox1.Text += "any_queue 之 第1個元素\n";
            Console.WriteLine("(Peek)   \t{0}", any_queue.Peek());

            object one = any_queue.Peek();
            Console.WriteLine("我是第一個元素：{0}", one);

            // 遍歷隊列的所有內容 方法一
            foreach (Object item in any_queue)
            {
                Console.WriteLine("<1> {0}", item);
            }

            // 遍歷隊列的所有內容 方法二
            IEnumerator enumer = any_queue.GetEnumerator();
            while (enumer.MoveNext())
            {
                object o = enumer.Current;
                Console.WriteLine("<3> " + o);
            }

            // 將Queue轉換為數組
            object[] objs = any_queue.ToArray();
            for (int i = 0; i < objs.Length; i++)
            {
                object o = objs[i];
                Console.Write("<4> " + o + "\n");
            }
        }

        public static void PrintValues(IEnumerable myCollection)
        {
            foreach (Object obj in myCollection)
            {
                Console.Write("    {0}", obj);
            }
            Console.WriteLine();
        }
    }
}

