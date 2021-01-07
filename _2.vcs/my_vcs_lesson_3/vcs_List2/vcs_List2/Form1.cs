using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_List2
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num = 20;
            Random rr = new Random();

            List<int> myList = new List<int>();   //宣告int型態的List

            /*  不均勻分配
            myList.Add('A');
            myList.Add('A');
            myList.Add('A');
            myList.Add('B');
            myList.Add('C');
            */

            for (int i = 0; i < num; i++)
            {
                myList.Add(rr.Next(10));
            }


            /*
            //特定分配
            for (int i = 50; i <= 57; i++)
                //ASCII碼，找出數字
                myList.Add((char)i); //從2開始，排除了0，1，放入列表
            */

            richTextBox1.Text += "建立長度為 " + num.ToString() + " 的List\t內容:\n";
            show_list(myList);

            myList.Sort();

            richTextBox1.Text += "排序後:\n";
            show_list(myList);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            int num = 10;
            List<string> myList = new List<string>();   //宣告string型態的List

            myList.Add("john");
            myList.Add("mary");
            myList.Add("david");
            myList.Add("bill");
            myList.Add("tom");
            myList.Add("sue");
            myList.Add("larry");
            myList.Add("michael");
            myList.Add("pepa");
            myList.Add("eric");

            richTextBox1.Text += "建立長度為 " + num.ToString() + " 的List\t內容:\n";
            show_list(myList);
            myList.Sort();

            richTextBox1.Text += "排序後:\n";
            show_list(myList);


            richTextBox1.Text += "移除一些:\n";
            myList.Remove("sue");
            myList.Remove("john");
            myList.RemoveAt(2); //上述已經移除後, 再移除第2個

            show_list(myList);

            richTextBox1.Text += "新增一些:\n";
            myList.Insert(2, "rebecca");
            myList.Insert(6, "sharon");
            myList.Insert(1, "emily");
            show_list(myList);

        }

        void show_list(List<int> l)
        {
            for (int i = 0; i < l.Count; i++)
            {
                richTextBox1.Text += l[i] + " ";

            }
            richTextBox1.Text += "\n";
        }

        void show_list(List<string> l)
        {
            for (int i = 0; i < l.Count; i++)
            {
                richTextBox1.Text += l[i] + " ";

            }
            richTextBox1.Text += "\n";
        }

        private void button3_Click(object sender, EventArgs e)
        {
            List<List<string>> myList = new List<List<string>>();
            myList.Add(new List<string>() { "A001", "David" });
            myList.Add(new List<string>() { "A002", "John" });
            myList.Add(new List<string>() { "A003", "Tom" });
            richTextBox1.Text += "學號\t->\t姓名\n";
            foreach (var showlist in myList)
            {
                richTextBox1.Text += showlist[0] + "\t->\t" + showlist[1] + "\n";
            }
        }


        private class myList
        {
            public string ID { get; set; }
            public string Name { get; set; }
            public string Level { get; set; }

        }

        private void button4_Click(object sender, EventArgs e)
        {
            List<myList> myList = new List<myList>();
            myList.Add(new myList { ID = "A001", Name = "David", Level = "A" });
            myList.Add(new myList { ID = "A002", Name = "John", Level = "B" });
            myList.Add(new myList { ID = "A003", Name = "Tom", Level = "A" });
            richTextBox1.Text += "學號\t->\t姓名\t->\t等級\n";
            foreach (var showlist in myList)
            {
                richTextBox1.Text += showlist.ID + "\t->\t" + showlist.Name + "\t->\t" + showlist.Level + "\n";
            }



        }

    }
}
