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

        private void button1_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
            string str = "Alice is a good student!!";
            richTextBox1.Text += str + "\n";
            richTextBox1.Text += "ToUpper︰" + str.ToUpper() + "\n";
            richTextBox1.Text += "ToLower︰" + str.ToLower() + "\n";
            richTextBox1.Text += "Insert︰" + str.Insert(6, "Wang ") + "\n";
            richTextBox1.Text += "\n";

            string[] strArray = str.Split(' ');
            for (int i = 0; i < strArray.Length; i++)
            {
                richTextBox1.Text += strArray[i] + "\n";
                //Console.WriteLine(strArray[i]);
            }


        }

        private void button3_Click(object sender, EventArgs e)
        {
            string str = "Welcome to the United States of America and have a nice day.";
            string[] split_str = new string[5];
            split_str = str.Split(' '); //以空白當分隔符號
            richTextBox1.Text += "\n";
            foreach (string tmp in split_str)
            {
                richTextBox1.Text += tmp + "\n";
            }

        }

        string my_string = "   歡迎來到Myson Century!   ";
        private void button4_Click(object sender, EventArgs e)
        {
            richTextBox1.Text += "\n";
            richTextBox1.Text += "字串：" + my_string + " 長度：" + my_string.Length.ToString() + "\n";

            string new_string = "";
            for (int i = 0; i < my_string.Length; i++)
            {
                new_string += my_string[i];
            }
            richTextBox1.Text += "原字串：" + my_string + " 長度：" + my_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串：" + new_string + " 長度：" + new_string.Length.ToString() + "\n";


        }

        private void button5_Click(object sender, EventArgs e)
        {
            int result;
            result = my_string.IndexOf("n", 0);
            MessageBox.Show("Got result = " + result);

            result = my_string.IndexOf("n", result + 1);
            MessageBox.Show("Got result = " + result);

            result = my_string.IndexOf("n", result + 1);
            MessageBox.Show("Got result = " + result);

        }

        private void button6_Click(object sender, EventArgs e)
        {
            string new_string = "";
            new_string = my_string.Substring(7, 5);
            richTextBox1.Text += "\n";
            richTextBox1.Text += "取得字串：" + new_string + "\n";

        }

        private void button7_Click(object sender, EventArgs e)
        {
            string new_string = "";
            new_string = my_string.Trim();

            richTextBox1.Text += "\n";

            richTextBox1.Text += "原字串：" + my_string + " 長度：" + my_string.Length.ToString() + "\n";
            richTextBox1.Text += "新字串：" + new_string + " 長度：" + new_string.Length.ToString() + "\n";
        }

        private void button2_Click(object sender, EventArgs e)
        {
            richTextBox1.Clear();
        }

        private void button8_Click(object sender, EventArgs e)
        {
            //字串處理
            string str1 = "群曜醫電股份有限公司 Insight Medical Solutions Inc.";
            string str2 = string.Empty;
            str2 = str1.Substring(0, 4);    //從0取4
            richTextBox1.Text += "str2 = " + str2 + "\n";
            str2 = str1.Substring(4, 6);    //從4取6
            richTextBox1.Text += "str2 = " + str2 + "\n";
            str2 = str1.Substring(8, 10);   //從8取10
            richTextBox1.Text += "str2 = " + str2 + "\n";

            //char[] cChar = new char[5] { 'a', 'b', 'c', 'd', 'e' };
            str1 = "中間路線";
            byte[] byteData = Encoding.Default.GetBytes(str1);
            foreach (byte b in byteData)
            {
                richTextBox1.Text += b.ToString("X2") + " ";


            }
            richTextBox1.Text += "\n";

            string nn = string.Empty;
            nn = Encoding.Default.GetString(byteData);
            richTextBox1.Text += "new string : " + nn + "\n";


            byteData[1] = (byte)(byteData[1] + 2);
            nn = Encoding.Default.GetString(byteData);
            richTextBox1.Text += "new string : " + nn + "\n";

            str1 = "专业知识中";
            byte[] byteData2 = Encoding.Default.GetBytes(str1);
            foreach (byte b in byteData2)
            {
                richTextBox1.Text += b.ToString("X2") + " ";


            }
            richTextBox1.Text += "\n";

        }


    }
}
