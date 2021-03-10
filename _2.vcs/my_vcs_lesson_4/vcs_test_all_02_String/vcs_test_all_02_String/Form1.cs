using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace vcs_test_all_02_String
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n\n";
            bt_clear.Location = new Point(richTextBox1.Location.X + richTextBox1.Size.Width - bt_clear.Size.Width, richTextBox1.Location.Y + richTextBox1.Size.Height - bt_clear.Size.Height);
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string str = "Alice is a good student!!";
            richTextBox1.Text += "\n原字串:\t" + str + "\n";
            richTextBox1.Text += "轉成大寫:\t︰" + str.ToUpper() + "\n";
            richTextBox1.Text += "轉成小寫:\t" + str.ToLower() + "\n";
            richTextBox1.Text += "插入字串寫:\t" + str.Insert(6, "Wang ") + "\n";
            richTextBox1.Text += "原字串依空白拆開:\n";

            string[] strArray = str.Split(' ');
            for (int i = 0; i < strArray.Length; i++)
            {
                richTextBox1.Text += strArray[i] + "\n";
                //Console.WriteLine(strArray[i]);
            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            string str = "Welcome to the United States and have a nice day.";
            string[] split_str = new string[5];
            split_str = str.Split(' '); //以空白當分隔符號
            richTextBox1.Text += "\n原字串:\t" + str + "\n";
            richTextBox1.Text += "原字串依空白拆開:\n";
            foreach (string tmp in split_str)
            {
                richTextBox1.Text += tmp + "\n";
            }
        }

        string my_string = "   歡迎來到Myson Century!   ";
        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n";
            richTextBox1.Text += "字串:\t" + my_string + " 長度:\t" + my_string.Length.ToString() + "\n";

            string new_string = "";
            for (int i = 0; i < my_string.Length; i++)
            {
                new_string += my_string[i];
            }
            richTextBox1.Text += "原字串:\t" + my_string + " 長度:\t" + my_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串:\t" + new_string + " 長度:\t" + new_string.Length.ToString() + "\n";
        }

        private void button5_Click(object sender, EventArgs e)
        {
            int result;
            richTextBox1.Text += "\n原字串:\t" + my_string + "\n";
            result = my_string.IndexOf("n", 0);
            richTextBox1.Text += "找到n在 " + result.ToString() + "\n";

            result = my_string.IndexOf("n", result + 1);
            richTextBox1.Text += "找到n在 " + result.ToString() + "\n";

            result = my_string.IndexOf("n", result + 1);
            richTextBox1.Text += "找到n在 " + result.ToString() + "\n";
        }

        private void button6_Click(object sender, EventArgs e)
        {
            string new_string = "";
            richTextBox1.Text += "\n原字串:\t" + my_string + "\n";
            new_string = my_string.Substring(7, 5);
            richTextBox1.Text += "從第7字開始抓5字:\t" + new_string + "\n";
        }

        private void button7_Click(object sender, EventArgs e)
        {
            string new_string = "";
            new_string = my_string.Trim();

            richTextBox1.Text += "\n";
            richTextBox1.Text += "原字串:\t|" + my_string + "|\t長度:\t" + my_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串:\t|" + new_string + "|\t長度:\t" + new_string.Length.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //字串處理
            string str1 = "群曜醫電股份有限公司 Insight Medical Solutions Inc.";
            string str2 = string.Empty;
            richTextBox1.Text += "\n原字串:\t" + str1 + "\n";
            str2 = str1.Substring(0, 4);    //從0取4
            richTextBox1.Text += "原字串從0取4字:\t" + str2 + "\n";
            str2 = str1.Substring(4, 6);    //從4取6
            richTextBox1.Text += "原字串從4取6字:\t" + str2 + "\n";
            str2 = str1.Substring(8, 10);   //從8取10
            richTextBox1.Text += "原字串從8取10字:\t" + str2 + "\n";
        }

        private void button9_Click(object sender, EventArgs e)
        {
            //分割字串範例
            string[] word_S = { };
            char[] split = { '-', ' ', ',', ':', '/' };     //依各種符號來切割字串

            string compile_time = "3/3/2021 01:35 下午";
            richTextBox1.Text += "原字串\t" + compile_time + "\n";
            richTextBox1.Text += "切割字串 :\n";

            word_S = compile_time.Split(split);     //切割字串

            foreach (string str in word_S)
            {
                richTextBox1.Text += str + "\n";
            }
        }

        //字串的 Split & Join
        private void button10_Click(object sender, EventArgs e)
        {
            string ols_string = "This is a book.";

            // Split the values at spaces, removing duplicates.
            string[] values = ols_string.Split(new char[] { ' ' }, StringSplitOptions.RemoveEmptyEntries);

            int len = values.Length;
            richTextBox1.Text += "原字串 : " + ols_string + "\t依空白可拆分為 " + len.ToString() + " 個, 分別是：\n";
            int i;
            for (i = 0; i < len; i++)
            {
                richTextBox1.Text += "第 " + i.ToString() + " 項 : " + values[i] + "\n";
            }

            // Rejoin them.
            string result = String.Join("*", values);
            richTextBox1.Text += "用星號連結組合起來 : " + result + "\n";
        }

        private void bt_clear_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }



    }
}
