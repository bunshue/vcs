using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

using System.Collections;   //for ArrayList

namespace vcs_ArrayList
{
    public partial class Form1 : Form
    {
        ArrayList ArrayListData = new ArrayList();

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            show_item_location();

            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        void show_item_location()
        {
            int x_st;
            int y_st;
            int dx;
            int dy; ;

            //button
            x_st = 20;
            y_st = 30;
            dx = 130;
            dy = 80;

            /*
            button0.Location = new Point(x_st + dx * 0, y_st + dy * 0);
            button1.Location = new Point(x_st + dx * 0, y_st + dy * 1);
            button2.Location = new Point(x_st + dx * 0, y_st + dy * 2);
            button3.Location = new Point(x_st + dx * 0, y_st + dy * 3);
            button4.Location = new Point(x_st + dx * 0, y_st + dy * 4);
            */

            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            ArrayListData.Add(textBox1.Text);
            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int i;
            /*
            for (i = 0; i < ArrayListData.Count; i++)
            {
                richTextBox1.Text += (i+1).ToString() + " : " + ArrayListData[i] + "\n";
            }
            */
            i = 0;
            foreach (string str_name in ArrayListData)
            {
                i++;
                richTextBox1.Text += i.ToString() + " : " + str_name + "\n";
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
        }

        private void button4_Click(object sender, EventArgs e)
        {
            ArrayListData.Remove(textBox1.Text);
            label1.Text = "共有 " + ArrayListData.Count.ToString() + " 個項目";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int item = int.Parse(textBox2.Text);
            if ((item > 0) && (item <= ArrayListData.Count))
            {
                ArrayListData.RemoveAt(item - 1);      //刪除特定項目
            }
        }

        private void button6_Click(object sender, EventArgs e)
        {
            ArrayListData.Sort();
        }

        private void button7_Click(object sender, EventArgs e)
        {
            ArrayListData.Reverse();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            Object tmp;
            if (textBox3.Text == "")
                return;
            tmp = textBox3.Text;  //取得所輸入的資料
            if (ArrayListData.IndexOf(tmp) < 0)
            {
                //若超過陣列索引值則表示找不到符合的資料
                richTextBox1.Text += "找不到您所輸入的資料\n";
            }
            else
            {
                richTextBox1.Text += "您所尋找的資料在第 " + (ArrayListData.IndexOf(tmp) + 1).ToString() + " 筆\n";
            }
        }

        private void button9_Click(object sender, EventArgs e)
        {
            ArrayListData.Insert(3, "David"); //插入一個元素
        }

        private void button10_Click(object sender, EventArgs e)
        {
            //建立一個ArrayList

            ArrayList list = new ArrayList();

            list.Add("alive");

            list.Add("silver");

            list.Add("dog");

            list.Add("Ftp");

            //d.SetData("para", list);

            //將制定的值賦值給應用程序域的屬性

            //foreach (string s in (ArrayList)d.GetData("para"))
            {// 獲取存在當前應用程序域中的值

                //Console.WriteLine("you will see" + s);
            }
        }

        private void button11_Click(object sender, EventArgs e)
        {
            //建立和初始化 ArrayList ，以及顯示其值

            // Creates and initializes a new ArrayList.
            ArrayList myAL = new ArrayList();
            myAL.Add("Hello");
            myAL.Add("World");
            myAL.Add("!");

            // Displays the properties and values of the ArrayList.
            Console.WriteLine("myAL");
            Console.WriteLine("    Count:    {0}", myAL.Count);
            Console.WriteLine("    Capacity: {0}", myAL.Capacity);
            Console.Write("    Values:");
            PrintValues(myAL);

            richTextBox1.Text += "顯示ArrayList的內容:\n";
            richTextBox1.Text += "myAL\n";
            richTextBox1.Text += "    Count:    " + myAL.Count.ToString() + "\n";
            richTextBox1.Text += "    Capacity: " + myAL.Capacity.ToString() + "\n";
            richTextBox1.Text += "    Values: ";

            foreach (Object obj in myAL)
                richTextBox1.Text += "   " + obj.ToString() + " ";

            richTextBox1.Text += "\n";
        }

        public static void PrintValues(IEnumerable myList)
        {
            foreach (Object obj in myList)
                Console.Write("   {0}", obj);
            Console.WriteLine();
        }

    }
}
