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
        string filename1 = @"D:\_git\vcs\_1.data\______test_files1\picture1.jpg";
        string filename2 = @"D:\_git\vcs\_1.data\______test_files1\bear.jpg";
        string filename3 = @"D:\_git\vcs\_1.data\______test_files1\elephant.jpg";

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
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);

            bitmap1 = (Bitmap)Bitmap.FromFile(filename1);	//Bitmap.FromFile出來的是Image格式
            bitmap2 = (Bitmap)Bitmap.FromFile(filename2);	//Bitmap.FromFile出來的是Image格式
            bitmap3 = (Bitmap)Bitmap.FromFile(filename3);	//Bitmap.FromFile出來的是Image格式

            update_queue_count();//更新佇列狀態
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
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

        public static void PrintOut(IEnumerable myCollction)
        {
            int i = 0;
            foreach (Object obj in myCollction)
            {
                Console.WriteLine("     第{0}個元素 : {1} ", ++i, obj);
            }
        }

        private void button7_Click(object sender, EventArgs e)
        {
            //Queue測試1
            Queue myQueue = new Queue();
            string[] ary = { "Jack", "Ford", "David" };
            //將陣列置入佇列
            foreach (string name in ary)
            {
                myQueue.Enqueue(name);
            }
            Console.WriteLine(" 1.目前佇列的資料 : ");
            PrintOut(myQueue);
            Console.WriteLine(" 1.目前堆疊佇列內資料的個數: {0} ", myQueue.Count);
            Console.WriteLine(" --------------------------------------------");

            // 將 Mary 置入堆疊佇列(最上面)
            myQueue.Enqueue("Mary");
            Console.WriteLine(" 2.目前佇列內的資料 : ");
            PrintOut(myQueue);

            // 取得堆疊最上面的資料
            //myQueue.Peek();
            Console.WriteLine(" 3.查詢佇列最上面資料 : {0} ", myQueue.Peek());
            Console.WriteLine(" 3.目前佇列內的資料 :");
            PrintOut(myQueue);
            Console.WriteLine(" --------------------------------------------");

            // 由堆疊最上面取出資料
            Console.WriteLine(" 4.取出佇列最上面的資料 : {0} ", myQueue.Dequeue());
            Console.WriteLine(" 4.目前佇列內的資料 : ");
            PrintOut(myQueue);
            Console.WriteLine(" --------------------------------------------");

            // 檢查 "David" 是否在佇列中
            if (!myQueue.Contains("David"))
            {
                Console.WriteLine(" 5.佇列內無 David 資料!");
            }
            else
            {
                Console.WriteLine(" 5.佇列內有 David 資料!");
            }

            // 清除佇列
            myQueue.Clear();
            Console.WriteLine("\n 6.清除佇列後資料的個數: {0}", myQueue.Count);
            PrintOut(myQueue);
            Console.WriteLine(" --------------------------------------------");
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //Queue測試2
            Queue m = new Queue();   // 非泛型           

            m.Enqueue(new Member() { Name = "David", Select = true, Score = 70 });
            m.Enqueue(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Enqueue(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Enqueue(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine("=== 非泛型 Queue 操作 需強制轉換 .... \n");
            while (m.Count > 0)
            {
                Console.WriteLine("{0} ", ((Member)m.Dequeue()).ToString());
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //Queue測試3

            Queue<Member> m = new Queue<Member>();   // 泛型           

            m.Enqueue(new Member() { Name = "David", Select = true, Score = 70 });
            m.Enqueue(new Member() { Name = "Mary", Select = false, Score = 65 });
            m.Enqueue(new Member() { Name = "Tom", Select = true, Score = 85 });
            m.Enqueue(new Member() { Name = "Jack", Select = true, Score = 95 });

            Console.WriteLine("=== 泛型 Queue 操作不需強制轉換 .... \n");

            while (m.Count > 0)
            {
                Console.WriteLine("{0} ", (m.Dequeue().ToString()));
            }
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
